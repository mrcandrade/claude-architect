# Claude como Suporte Tecnico de TI
## Aula Pratica — Do Chamado ao Fechamento
## Duracao: 2 horas (com intervalo de 10 min)

---

## Objetivo

Ao final da aula, o profissional de suporte vai saber:
- Usar o Claude como copiloto no dia a dia do suporte
- Escrever prompts que resolvem problemas reais de TI
- Diagnosticar erros, redigir chamados e criar documentacao
- Conhecer os limites e cuidados com IA no ambiente corporativo

---

## Cronograma

| Tempo | Bloco | Conteudo |
|-------|-------|----------|
| 0-10 min | Contexto | Por que IA no suporte de TI? |
| 10-25 min | Fundamento | A formula do prompt tecnico |
| 25-50 min | Pratica 1 | Diagnostico e troubleshooting |
| 50-60 min | Intervalo | — |
| 60-80 min | Pratica 2 | Comunicacao e documentacao |
| 80-100 min | Pratica 3 | Automacao e scripts |
| 100-115 min | Seguranca | O que NUNCA fazer |
| 115-120 min | Fechamento | Kit de prompts prontos |

---

# BLOCO 1 — Por que IA no Suporte de TI? (10 min)

---

## O problema que todo tecnico conhece

```
Segunda-feira, 8h da manha.

15 chamados abertos.
3 impressoras com problema.
1 servidor que "parou do nada".
O diretor quer saber "por que a internet ta lenta".
E voce? Sozinho.
```

O Claude nao vai resolver esses problemas por voce — ele nao acessa sua rede,
nao ve sua tela e nao sabe a senha do roteador. Mas ele pode:

- Sugerir passos de diagnostico que voce esqueceu
- Redigir respostas de chamado em 10 segundos
- Criar tutoriais para o usuario parar de te ligar
- Explicar erros que voce nunca viu
- Gerar scripts que automatizam tarefas repetitivas
- Traduzir "tecniquês" para linguagem humana

**Analogia:** O Claude e como um estagiario que leu toda a documentacao da Microsoft,
Cisco, HP e todos os foruns de TI que existem. Ele nao coloca a mao na massa,
mas te da o mapa.

---

# BLOCO 2 — A Formula do Prompt Tecnico (15 min)

---

## Prompt generico vs. prompt de suporte

O segredo para tirar o maximo do Claude em TI e dar contexto tecnico.

### A formula:

```
CARGO + AMBIENTE + PROBLEMA + RESTRICAO + FORMATO
```

| Ingrediente | O que e | Por que importa |
|-------------|---------|-----------------|
| Cargo | Seu papel no suporte | Define o nivel tecnico da resposta |
| Ambiente | SO, rede, equipamento | Evita sugestoes que nao se aplicam |
| Problema | Erro exato ou sintoma | Quanto mais especifico, melhor |
| Restricao | O que voce NAO pode fazer | Evita sugestoes impossiveis |
| Formato | Como quer a resposta | Passo a passo, tabela, script |

### Comparacao ao vivo

Prompt fraco:
```
impressora nao imprime
```

Prompt forte:
```
Sou tecnico de suporte de uma escola com 200 computadores Windows 11.
Uma impressora HP LaserJet Pro M404 conectada via rede (IP fixo 192.168.1.50)
parou de imprimir. Os computadores mostram o status "Erro - Imprimindo".
O ping para o IP da impressora funciona. O spooler ja foi reiniciado.
Quais os proximos passos de diagnostico? Lista em ordem do mais simples
ao mais complexo.
```

**Atividade (5 min):** Cada participante pega um chamado recente que resolveu
e reescreve como prompt usando a formula. Testa no Claude. A resposta e util?

---

# BLOCO 3 — Pratica 1: Diagnostico e Troubleshooting (25 min)

---

## Caso 1 — Erro desconhecido do Windows

**Cenario:** Um usuario liga dizendo que apareceu uma tela azul e o computador reiniciou.

Prompt:
```
Sou do suporte tecnico. Um usuario com Windows 11 teve uma tela azul
com o codigo KERNEL_DATA_INPAGE_ERROR. O computador reiniciou sozinho.
E um desktop Dell OptiPlex com SSD de 256GB e 8GB de RAM, tem 2 anos de uso.
Quais sao as causas mais provaveis e como diagnosticar cada uma?
Formato: tabela com causa, como testar e como resolver.
```

**Exercicio:** Teste no Claude. Depois, mude o codigo de erro para
IRQL_NOT_LESS_OR_EQUAL e compare as respostas.

---

## Caso 2 — Rede lenta e todo mundo reclamando

**Cenario:** 14h, todas as salas reclamam que a internet esta lenta.

Prompt:
```
Sou administrador de rede de uma escola. A rede tem um link de 200Mbps,
roteador MikroTik, 3 switches gerenciaveis e 150 dispositivos conectados.
A internet ficou lenta para todos ao mesmo tempo, comecou as 14h.
O speedtest no servidor mostra 180Mbps, mas nos computadores da ~5Mbps.
Me da um roteiro de diagnostico em ordem logica, do mais rapido ao mais demorado.
```

**Exercicio:** Teste e depois adicione ao prompt: "O problema some quando
desligo o switch do bloco B." Veja como a resposta muda.

---

## Caso 3 — Software que nao instala

**Cenario:** Precisam instalar um sistema novo em 30 maquinas e da erro.

Prompt:
```
Preciso instalar o software [nome] em 30 computadores Windows 11 Pro
em dominio Active Directory. Na instalacao manual, aparece o erro
"Erro 1603: falha fatal durante a instalacao". Os computadores tem
permissao de admin local. O software precisa do .NET Framework 4.8.
Como resolver e como automatizar a instalacao nas 30 maquinas?
```

---

## Caso 4 — Email nao chega / nao envia

**Cenario:** Um departamento inteiro parou de receber emails.

Prompt:
```
Sou do suporte de uma empresa com 50 usuarios. Usamos Microsoft 365.
O departamento financeiro (5 usuarios) parou de receber emails externos
desde ontem. Emails internos funcionam normalmente. Nenhuma regra
de fluxo de email foi alterada recentemente. Os outros departamentos
estao funcionando. O que pode ser e como verificar passo a passo?
```

---

## Caso 5 — Usar o Claude como "par" de diagnostico

Tecnica avancada: conversa interativa em vez de prompt unico.

```
Mensagem 1:
"Vou te descrever um problema de TI e quero que voce me faca perguntas
de diagnostico, uma por vez, como se fosse um tecnico senior me orientando.
O problema: um servidor de arquivos Windows Server 2019 esta com disco
em 95% e esta travando."

Mensagem 2 (responda as perguntas do Claude):
"O servidor tem 2TB de disco, o maior consumo e a pasta compartilhada
do departamento de marketing que tem 800GB."

(continue a conversa ate chegar na solucao)
```

**Exercicio:** Em duplas, um descreve o problema e o outro usa o Claude
como copiloto. Depois trocam.

---

# BLOCO 4 — Pratica 2: Comunicacao e Documentacao (20 min)

---

## 6 tipos de texto que o Claude escreve melhor que voce (e mais rapido)

### 1. Resposta de chamado

Prompt:
```
Escreve a resposta de encerramento de um chamado de suporte.
Dados:
- Solicitante: Maria da Silva, secretaria
- Problema: nao conseguia acessar o sistema de matriculas
- Causa: senha expirada no Active Directory
- Solucao: senha resetada, usuario orientado a trocar no proximo login
- Tempo de atendimento: 15 minutos
Tom: profissional mas acessivel. Maximo 5 linhas.
```

### 2. Tutorial para usuario

Prompt:
```
Cria um tutorial passo a passo de como conectar uma impressora de rede
no Windows 11. O publico sao funcionarios sem experiencia com TI.
Linguagem simples, passos numerados, inclui onde clicar exatamente.
Nao use termos tecnicos sem explicar entre parenteses.
```

### 3. Comunicado de manutencao

Prompt:
```
Escreve um comunicado informando que o sistema [nome] ficara fora do ar
no sabado das 6h as 12h para manutencao programada. O tom deve ser
profissional e tranquilizador. Sugira que os usuarios salvem seus
trabalhos antes de sexta as 18h. Maximo 8 linhas.
```

### 4. Relatorio de incidente

Prompt:
```
Escreve um relatorio tecnico de incidente com base nesses dados:
- Data: 15/03/2026, 09:15 - 11:30
- Impacto: sistema de ponto eletronico ficou fora por 2h15
- Causa raiz: certificado SSL expirado no servidor de aplicacao
- Acao corretiva: certificado renovado e configurado alerta de vencimento
- Usuarios afetados: 120
Formato: relatorio com secoes (resumo, cronologia, causa raiz,
acoes tomadas, prevencao futura).
```

### 5. Justificativa de compra para a chefia

Prompt:
```
Preciso justificar a compra de um nobreak de 3kVA para o rack de
servidores da empresa. O ultimo apagao causou corrupcao no banco
de dados e 4h de downtime. Escreve uma justificativa tecnica
e financeira que um diretor sem conhecimento de TI entenda.
Maximo 15 linhas.
```

### 6. Base de conhecimento interna

Prompt:
```
Cria um artigo de base de conhecimento sobre o problema:
"Computador nao liga apos queda de energia".
Formato:
- Sintoma
- Causas possiveis (lista)
- Passo a passo de solucao (do mais simples ao mais complexo)
- Quando escalar para o nivel 2
Linguagem tecnica mas clara. Publico: tecnicos de suporte nivel 1.
```

**Exercicio (10 min):** Cada participante escolhe 2 tipos de texto da lista acima,
adapta o prompt para um caso real do seu trabalho e testa no Claude.

---

# BLOCO 5 — Pratica 3: Automacao e Scripts (20 min)

---

## Claude como gerador de scripts

O Claude e excelente para gerar scripts que voce usaria no dia a dia.
Mesmo que voce nao saiba programar, pode pedir e adaptar.

### Script 1 — Limpeza de disco automatizada (PowerShell)

Prompt:
```
Cria um script PowerShell que faz limpeza automatica em computadores
Windows 10/11:
- Limpa a pasta Temp do usuario e do sistema
- Limpa a lixeira
- Limpa o cache do Windows Update
- Mostra quanto espaco foi liberado no final
- Inclui comentarios explicando cada parte
O script deve ser seguro para rodar em maquinas de producao.
```

### Script 2 — Verificacao de saude da maquina

Prompt:
```
Cria um script PowerShell que gera um relatorio basico de saude
de um computador Windows:
- Nome do PC e usuario logado
- Espaco em disco (% livre)
- Uso de RAM
- Uptime (tempo desde ultimo boot)
- Ultimos 5 erros do Event Viewer
- Status do antivirus
Formato de saida: texto simples que posso colar num chamado.
```

### Script 3 — Criacao de usuarios em lote

Prompt:
```
Cria um script PowerShell para Active Directory que cria usuarios
em lote a partir de um arquivo CSV. O CSV tem as colunas:
Nome, Sobrenome, Usuario, Departamento, Cargo.
O script deve:
- Criar o usuario na OU correta baseado no departamento
- Definir senha padrao e forcar troca no primeiro login
- Adicionar ao grupo do departamento
- Gerar log de quem foi criado e quem deu erro
Inclui comentarios e tratamento de erros.
```

### Script 4 — Monitoramento simples

Prompt:
```
Cria um script PowerShell que roda a cada 5 minutos (via Task Scheduler)
e verifica se um servico do Windows (ex: Spooler) esta rodando.
Se o servico estiver parado, reinicia automaticamente e envia um email
de alerta para suporte@empresa.com. Inclui log em arquivo texto.
```

**CUIDADO:** Sempre leia e entenda o script antes de rodar.
Teste primeiro em uma maquina de testes, nunca direto em producao.

**Exercicio (10 min):** Escolha um script acima, gere no Claude, e leia
linha por linha. Identifique: voce entende tudo? Tem algo que mudaria?

---

# BLOCO 6 — Seguranca e Limites (15 min)

---

## O que o Claude NAO faz

| Limitacao | Explicacao |
|-----------|-----------|
| Nao acessa sua rede | Ele nao faz ping, nao acessa switches, nao ve logs |
| Nao acessa a internet em tempo real | Nao sabe se o site X esta fora agora |
| Nao garante que a solucao funciona | E uma sugestao, nao um diagnostico definitivo |
| Nao conhece seu ambiente | Ele nao sabe sua topologia, seus servidores, suas regras |
| Pode inventar coisas | "Alucinacao" — ele pode sugerir um comando que nao existe |

---

## O que NUNCA colocar no Claude

```
REGRA DE OURO: se voce nao colaria num post-it na sua mesa,
nao cole no Claude.
```

| NUNCA envie | Por que |
|-------------|---------|
| Senhas de sistemas | Dados enviados podem ser usados para treinamento |
| Chaves de API / tokens | Risco de vazamento de credenciais |
| Dados pessoais (CPF, RG, dados de alunos) | Viola LGPD e politicas de privacidade |
| IPs publicos e topologia detalhada | Informacao sensivel de seguranca |
| Logs com dados de usuarios | Podem conter informacoes pessoais |
| Configs com credenciais | Senhas em texto plano nunca devem sair da rede |

### Como anonimizar

Em vez de:
```
O usuario joao.silva (CPF 123.456.789-00) nao consegue acessar
o servidor 200.150.30.10 com a senha TI@2026
```

Use:
```
Um usuario nao consegue acessar um servidor Windows via RDP.
A conexao expira com timeout. O servidor esta pingando normalmente.
```

---

## Quando confiar e quando duvidar

### Confiavel (usar direto):
- Explicacoes de conceitos (o que e DHCP, como funciona DNS)
- Estrutura de comandos conhecidos (netstat, ipconfig, Get-ADUser)
- Templates de texto (chamados, comunicados, tutorials)
- Roteiros de diagnostico genericos

### Verificar antes de usar:
- Scripts com mais de 10 linhas (leia tudo e teste em sandbox)
- Passos que alteram configuracoes de servidor ou rede
- Comandos do PowerShell com -Force ou Remove-
- Informacoes sobre compatibilidade de hardware/software especificos
- Qualquer numero, versao ou link que ele mencionar

### Nunca confiar cegamente:
- "Esse comando resolve" em servidor de producao
- Links ou URLs que ele gerar (podem nao existir)
- Informacoes sobre vulnerabilidades de seguranca recentes

---

# BLOCO 7 — Kit de Prompts Prontos (5 min)

---

## Copie e adapte para o seu dia a dia

### Diagnostico rapido
```
Sou tecnico de suporte [nivel 1/2/3]. Um usuario com [SO]
esta com o erro "[mensagem de erro exata]" ao tentar [acao].
O equipamento e [marca/modelo]. Ja tentei [o que voce fez].
Quais os proximos passos? Lista do mais simples ao mais complexo.
```

### Interpretar log/erro
```
Me explica o que significa esse log/erro de forma simples:
[cola o log aqui]
Quais as causas possiveis e o que devo verificar primeiro?
```

### Resposta de chamado
```
Escreve a resposta de encerramento de um chamado:
- Solicitante: [nome, cargo]
- Problema: [descricao]
- Causa: [o que encontrou]
- Solucao: [o que fez]
- Tempo: [quanto levou]
Tom profissional, maximo 5 linhas.
```

### Tutorial para usuario
```
Cria um tutorial passo a passo de [tarefa] para [publico].
Linguagem simples, passos numerados, sem termos tecnicos.
Inclui prints imaginarios entre colchetes [Clique em "Arquivo"].
```

### Comunicado de TI
```
Escreve um comunicado de TI informando que [evento].
Data/hora: [quando]. Impacto: [o que sera afetado].
Tom: profissional e tranquilizador. Maximo 8 linhas.
```

### Gerar script
```
Cria um script [PowerShell/Bash/Python] que [objetivo].
Requisitos:
- [requisito 1]
- [requisito 2]
Inclui comentarios explicando cada parte.
Deve ser seguro para rodar em maquinas de producao.
```

### Comparar solucoes
```
Preciso escolher entre [opcao A] e [opcao B] para [objetivo].
Meu cenario: [ambiente, orcamento, quantidade de usuarios].
Cria uma tabela comparativa com: custo, facilidade, seguranca e escalabilidade.
```

### Estudar para certificacao
```
Estou estudando para a certificacao [nome]. Me explica o conceito
de [topico] como se eu nunca tivesse ouvido falar. Depois, me da
3 perguntas de prova sobre esse assunto com as respostas.
```

---

## Tarefa final

Escolha 3 chamados que voce resolveu na ultima semana.
Para cada um, escreva o prompt que teria usado para pedir
ajuda ao Claude. Teste os 3 e avalie:

| Chamado | O Claude ajudaria? | Nota (1-5) | Economizaria tempo? |
|---------|--------------------|------------|---------------------|
| 1.      |                    |            |                     |
| 2.      |                    |            |                     |
| 3.      |                    |            |                     |

---

## Recursos extras

- Claude: https://claude.ai (conta gratuita disponivel)
- Anthropic Docs: https://docs.anthropic.com
- Prompt Engineering Guide: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview

---

Aula preparada para profissionais de suporte tecnico de TI.
Feita com Claude (Anthropic) — https://claude.ai
