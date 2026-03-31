"""
tests/run_evals_ci.py
Evals automaticos para CI/CD.
Feito com Claude (Anthropic) - https://claude.ai
"""
import os, sys, json, time, datetime
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
HAIKU = "claude-haiku-4-5-20251001"
THRESHOLD = 0.80

DATASET = [
    {"id":"s1","input":"Produto excelente!","label":"positivo"},
    {"id":"s2","input":"Horrivel, nao recomendo.","label":"negativo"},
    {"id":"s3","input":"Entrega no prazo.","label":"neutro"},
    {"id":"s4","input":"Superou expectativas!","label":"positivo"},
    {"id":"s5","input":"Dinheiro jogado fora.","label":"negativo"},
    {"id":"i1","input":"Hello, how are you?","label":"ingles"},
    {"id":"i2","input":"Ola, tudo bem?","label":"portugues"},
]

SYS = {
    "s": "Classifique como positivo, negativo ou neutro. Responda uma palavra.",
    "i": "Identifique o idioma em portugues. Responda uma palavra.",
}

def rodar(caso):
    t0 = time.time()
    sys_ = SYS.get(caso["id"][0], "")
    saida = client.messages.create(
        model=HAIKU, max_tokens=32, system=sys_,
        messages=[{"role":"user","content":caso["input"]}]
    ).content[0].text.strip().lower()
    return {**caso, "saida": saida, "passou": caso["label"] in saida,
            "dt": round(time.time()-t0, 2)}

def main():
    print(f"Rodando {len(DATASET)} evals (threshold: {THRESHOLD:.0%})")
    with ThreadPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(rodar, DATASET))

    passou = sum(r["passou"] for r in res)
    acuracia = passou / len(res)

    for r in res:
        print(f"  {'OK' if r['passou'] else 'FALHOU'} [{r['id']}] {r['input'][:30]:30} -> {r['saida']}")

    print(f"\nAcuracia: {acuracia:.0%} ({passou}/{len(res)})")
    json.dump({"timestamp":datetime.datetime.now().isoformat(),
               "acuracia":round(acuracia,4),"total":len(res),"passou":passou,"casos":res},
              open("eval_result.json","w", encoding="utf-8"), indent=2)

    if acuracia >= THRESHOLD:
        print("PASSED"); sys.exit(0)
    else:
        print(f"FAILED - acuracia {acuracia:.0%} < {THRESHOLD:.0%}"); sys.exit(1)

if __name__ == "__main__":
    main()
