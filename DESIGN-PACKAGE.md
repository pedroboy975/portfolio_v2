# Design Package — A Câmara

Documento único de decisões criativas. Escrito antes de qualquer geração.
Todo texto marcado como copy é final e vai para a página literalmente.
Os números de faixa são pontos de partida, validados depois pelo teste de flick.

Tier: 1 (uma tomada contínua de 6 segundos).
Idiomas: PT e EN, paridade completa.
Revisão 6, depois da segunda auditoria de frontend sobre a página construída.
Nenhum crédito gasto. Nada gerado até o aval do usuário.

**Decisões travadas em revisões anteriores:**
- LinkedIn correto: `linkedin.com/in/pedrovmaia`
- 100X Partners fica fora do site.
- Os números do resumo profissional entram todos.
- Sem formulário, sem e-mail visível. Canal único: LinkedIn.

**Decisões travadas na revisão 5, depois da auditoria de direção de arte:**
- O ciano de sistema saiu. O ouro passa a ser a única cor saturada da página.
- Trio tipográfico trocado: sai IBM Plex, entra Spline Sans com Spline Sans Mono.
  Marcado como provisório pelo usuário, sujeito a nova prova.
- A seção Entregue na mesa deixa de ser três blocos de número e vira leitura de
  posição, no formato de relatório de caixa.
- A camada de animação foi cortada de treze para sete peças.

**Decisões travadas na revisão 6, depois da auditoria de frontend:**
- A página não tinha nenhum estado `:active`. Todo retorno tátil vivia em
  `:hover`, que não existe em toque. Botões, cards e o disparo da cadeia agora
  respondem ao dedo.
- `overflow-x` saiu do `body` e virou `overflow-x:clip` no `html`. `hidden` no
  body cria contêiner de rolagem e é o assassino clássico de `position:sticky`,
  que é o que segura o hero inteiro. `clip` recorta sem criar contêiner.
- Hero em `100svh` e hero estático em `100dvh`, com `100vh` de reserva antes.
  `dvh` no hero grudado seria errado: a unidade muda durante o scroll e o
  cálculo de progresso trepida.
- Registros passa de três colunas com um card órfão para duas colunas largas.
  Coluna de 300px não comporta print de dashboard legível, e print é o que
  está pendente.
- Duas fugas de ouro fora da lista fechada do parágrafo 2 voltaram para o aço:
  o número da faixa 3 do hero e o destaque do veredito da ponte. A lavagem
  radial de ouro a 8% no fundo do hero fica, por ser ambiente e não acento.
- `.step.lit` perde o empurrão lateral de 4px. Sinalizava o mesmo estado que a
  borda e o texto já sinalizavam, e não codificava nada.

---

## 1. A premissa da marca

**Comissionamento.** Em engenharia, comissionar é a fase em que um sistema
construído é testado, assinado e entregue para operar. Não é o projeto e não é
a rotina: é a passagem entre os dois.

Pedro é Especialista de Tesouraria na Kinross Gold, uma das maiores operações
de ouro do Brasil. Gerencia caixa na escala de centenas de milhões de dólares
para Brasil e Chile, e estrutura o programa corporativo de hedge cambial. Não
automatiza como hobby: já apagou mais de cinco horas semanais de trabalho
manual do calendário da própria equipe.

O site inteiro ensina uma ideia só: **o valor não está em saber programar, está
em saber o que construir.** Qualquer um aprende Python. Quase ninguém que
constrói agente sabe o que uma tesouraria realmente precisa.

Toda seção serve essa ideia. Seção que não serve, não entra.

---

## 2. A paleta como tokens CSS

Direção tirada do mundo real do assunto: espaço escuro instrumentado, aço frio
como estrutura, e **ouro** como a única cor. O ouro não é escolha decorativa. É
o material da operação onde Pedro trabalha. Valores exatos finalizados depois
que a filmagem passar no portão.

```css
:root{
  --canvas:#0A0E13;         /* fundo, quase preto puxado pro azul frio, nunca #000 */
  --panel:#111823;          /* superfícies elevadas, painéis de instrumento */
  --panel-line:#1E2A38;     /* fio de contorno dos painéis */
  --accent:#9DB2C4;         /* aço frio. Estrutura: linha, etiqueta, contorno, foco. */
  --accent-hover:#C9D8E4;
  --accent-muted:#33434F;   /* nível sussurro: bordas, brilho, grade */
  --gold:#E9B45A;           /* ouro. A ÚNICA cor saturada da página. */
  --gold-hover:#F5C978;
  --text-primary:#E6EDF3;
  --text-secondary:#8B9AA8;
}
```

**Regra dura do ouro:** aparece em no máximo dois lugares por tela. É o estado
"em operação", é o número que prova, e é o chamado. Ouro espalhado mata o efeito.

**Onde o ouro pode aparecer, lista fechada:** nome da Kinross no hero, o nó do
emprego atual na trajetória, os valores da leitura de posição, o estado NO AR,
a etapa acesa da cadeia de execução, e o botão de chamado. Em nenhum outro
lugar. Etiqueta de matriz, ponto do cabeçalho e ícone de estado ficam em aço.

**Nota de direção, corrigida na revisão 5.** A versão anterior desta paleta
tinha um ciano de sistema como acento. Isso caía direto em um dos looks que a
direção marca como padrão de página gerada: fundo quase preto com um acento
brilhante único. O ouro tem defesa, porque é o material literal do assunto. O
ciano não tinha nenhuma. A correção não foi trocar o ciano por outro tom
brilhante, foi **rebaixar o acento a estrutura**: o aço não é cor, é o
instrumento em volta. Com isso a página inteira fica dessaturada e o ouro passa
a ser a única coisa quente na tela, o que resolve a hierarquia sozinho, sem
precisar de tamanho ou peso. O olho vai para o chamado porque nada compete.

Isso é gastar a ousadia em um lugar só, que é a regra. Desvio dito em voz alta.

---

## 3. O trio tipográfico

| Papel | Fonte | Pesos |
|---|---|---|
| Display | Saira Condensed | 600, 800 |
| Corpo | Spline Sans | 400, 500 |
| Etiqueta | Spline Sans Mono | 400, 600 |

Display em caixa alta, entrelinha apertada, tracking levemente aberto.
Mono só em etiqueta pequena: REGISTRO, ESTADO, CICLO, INSTRUÇÃO.
Nada de Inter. Nada de Roboto.

**Por que Spline, e não Plex.** O critério original continua valendo: sans e
mono desenhadas juntas, então combinam sem esforço. O que mudou foi a família.
A Plex é a tipografia de engenharia da IBM e, exatamente por isso, virou a
escolha automática de todo site que quer parecer técnico. Legibilidade
excelente, personalidade nenhuma. A Spline sustenta o mesmo argumento de
parentesco e não carrega o vício.

Três razões concretas, em ordem de peso:

1. **Parentesco preservado.** Corpo e etiqueta saem da mesma família. É uma
   decisão, não duas escolhas soltas para defender separadamente.
2. **Contraste com a display, em vez de imitação.** Saira Condensed é uma
   grotesca condensada. Um corpo também estreito faria título e parágrafo
   virarem a mesma espécie, e pareamento existe para criar diferença. A Spline
   é mais larga e de aberturas mais soltas, então a display volta a ter voz
   própria.
3. **Aguenta o tamanho pequeno.** Legenda da leitura de posição, corpo dos
   cards e rodapé rodam em 14 e 15px. A contraforma aberta da Spline segura
   melhor nesse tamanho.

A Spline é levemente mais quente que a Plex. Isso não briga com a direção de
aço frio, alivia: a página já é quase preta, com filete de 1px e caixa alta em
quase tudo. Frio demais não vira preciso, vira ilegível.

**Estado desta decisão: provisória.** O usuário escolheu "por enquanto". A
prova de tipografia fica em `review/tipografia.html`, com quatro trios sobre o
texto real, para nova comparação a qualquer momento. A opção que continua na
mesa é Newsreader no corpo, que é serifa e empurraria a página da prateleira de
portfólio de tecnologia para a de documento financeiro.

---

## 4. O mapa de faixas do hero

Vídeo: descida vertical por um espaço escuro instrumentado. A ação vive na
faixa central. O texto vive nas laterais e no terço inferior.

### PT

| Faixa | Alcance | Momento da filmagem | Copy (literal) | Entrada |
|---|---|---|---|---|
| 1 | 0.00 a 0.16 | Início da descida, maquinário passando ao longe | "Centenas de milhões de dólares passam pela minha mesa." | Painel de arquitetura se desenha à esquerda, linha por linha |
| 2 | 0.20 a 0.40 | Atravessa um plano de luz, respingo na lente | "Brasil e Chile. Caixa, hedge cambial, capital de giro." | Chamada lateral com linha de guia apontando pro maquinário |
| 3 | 0.46 a 0.68 | Descida acelera, instrumentos densos dos dois lados | "Eu apaguei cinco horas semanais de trabalho manual do calendário da equipe." | Fluxo vertical de quatro etapas acendendo uma a uma, o número em ouro |
| 4 | 0.76 a 1.00 | Chegada, superfície larga e calma | "PEDRO MAIA" / "Especialista de Tesouraria na Kinross Gold." / "Tesouraria, dados e agentes de IA." / [Abrir conversa] | Painel final monta em volta do nome, cantos em colchete fecham por último |

### EN

| Faixa | Copy (literal) |
|---|---|
| 1 | "Hundreds of millions of dollars cross my desk." |
| 2 | "Brazil and Chile. Cash, FX hedging, working capital." |
| 3 | "I wiped five hours of manual work a week off my team's calendar." |
| 4 | "PEDRO MAIA" / "Treasury Specialist at Kinross Gold." / "Treasury, data and AI agents." / [Start a conversation] |

Faixa 4 é o repouso: a página para aqui e a instrumentação fica montada.

---

## 5. Bloco do hero estático (celular e movimento reduzido)

Sobre o frame final ou o poster, sem jornada atrás.

**PT**
- **Título:** Centenas de milhões de dólares passam pela minha mesa. E eu construo o sistema que faz o trabalho.
- **Subtítulo:** Especialista de Tesouraria na Kinross Gold. Caixa, hedge cambial e capital de giro para Brasil e Chile. Uma década em finanças, agora com dados e agentes de IA em cima.
- **CTA:** Abrir conversa

**EN**
- **Título:** Hundreds of millions of dollars cross my desk. And I build the system that does the work.
- **Subtítulo:** Treasury Specialist at Kinross Gold. Cash, FX hedging and working capital for Brazil and Chile. A decade in finance, now with data and AI agents on top.
- **CTA:** Start a conversation

A camada de instrumentação aparece montada, em estado final, sem animação.

---

## 6. O plano abaixo da dobra

Toda seção afunila para UM chamado: **Abrir conversa**.
Nenhuma seção repete o esqueleto da vizinha.

| # | Seção | Esqueleto |
|---|---|---|
| 1 | A ponte | Duas colunas em contraste, mais um bloco largo de resposta |
| 2 | Trajetória | Linha do tempo com trilho à esquerda |
| 3 | A mesa | Lista de campos etiquetados, leitura de instrumento |
| 4 | Entregue na mesa | Leitura de posição, rótulo à esquerda e valor à direita |
| 5 | Cadeia de execução | Diagrama vertical, é a assinatura |
| 6 | Registros | Cards com estado |
| 7 | Construção | Tabela de linhas alinhada na base |
| 8 | Formação e idiomas | Fila compacta em linha |
| 9 | Perguntas | Acordeão |
| 10 | O que eu procuro | Bloco estreito e centrado, sem painel |
| 11 | Contato | Painel largo, chamado único |

### 6.1 A ponte

- **Etiqueta:** POR QUE ESSA COMBINAÇÃO
- **Título:** Quase ninguém está dos dois lados
- **Corpo:** Tem gente técnica que constrói rápido e não sabe o que o negócio precisa. Tem gente de finanças que sabe exatamente o que precisa e não constrói. Eu passo o dia numa mesa de tesouraria de verdade, com fechamento, banco e dinheiro no meio, e construo do outro lado com o problema ainda fresco. Não escolho o que automatizar por curiosidade. Escolho pelo que já me atrasou.

### 6.2 Trajetória

- **Etiqueta:** TRAJETÓRIA
- **Título:** Onde o ofício foi aprendido

Cada linha carrega o país da matriz. Em três das quatro, o reporte foi para
fora do Brasil, em inglês, no calendário de fechamento da matriz.

| Período | Empresa | Matriz | Cargo | Linha (literal) |
|---|---|---|---|---|
| 2023 até hoje | Kinross Gold Corporation | Canadá | Especialista de Tesouraria (Analista Sênior até 2026) | Gestão de caixa, fluxo, relacionamento bancário e operações financeiras para Brasil e Chile. Programa corporativo de hedge cambial com NDF e Zero Cost Collar. Capital de giro, seguros e garantias. Orçamento e forecast de caixa. |
| 2020 a 2023 | PETRONAS Lubricants International | Malásia | Analista Sênior de Tesouraria | Caixa e operações bancárias das Américas: Argentina, Brasil, México e Estados Unidos. Negociação e gestão de dívida, hedge, capital de giro e análise do Ciclo de Conversão de Caixa. |
| 2017 a 2020 | Banco Inter | Brasil | Analista Financeiro de Tesouraria | Operação de câmbio ponta a ponta: análise, classificação, registro e execução junto ao Banco Central do Brasil. Apuração de tributo sobre operação financeira e cambial. Gestão da exposição cambial da instituição. |
| 2015 a 2017 | Fiat Finanças Brasil | Itália | Estágio, Finanças Estruturadas e Câmbio | Cotação de câmbio, NDF e swap com bancos. Registro em BM&F, SELIC e CETIP. Operações overnight, garantias bancárias e projetos com linha subsidiada. |

### 6.3 A mesa

- **Etiqueta:** A MESA
- **Título:** O tamanho da operação
- **Nota:** Escopo real de responsabilidade, sem número que não seja meu de dizer.

| Campo | Valor (literal) |
|---|---|
| OPERAÇÃO | Mineração de ouro, uma das maiores do Brasil |
| PAÍSES HOJE | Brasil, Chile |
| JÁ OPEROU | Argentina, México, Estados Unidos |
| REPORTE | Canadá, Malásia e Itália, em inglês, no calendário da matriz |
| HEDGE | Programa corporativo com NDF e Zero Cost Collar |
| INSTRUMENTOS | Câmbio, derivativo de hedge, dívida, capital de giro, garantias |
| ÓRGÃOS E SISTEMAS | Banco Central do Brasil, BM&F, SELIC, CETIP |
| CICLO | Diário, semanal, mensal, trimestral |

### 6.4 Entregue na mesa

Esta é a seção que separa Pedro de quem só tem projeto pessoal. Automação
entregue dentro de uma multinacional, em produção, com gente usando.

- **Etiqueta:** ENTREGUE NA MESA
- **Título:** Automação que já está rodando no trabalho
- **Esqueleto:** leitura de posição. Rótulo à esquerda em display, valor
  alinhado à direita em ouro com `tabular-nums`, filete entre as linhas.

| Rótulo (literal) | Detalhe (literal) | Valor |
|---|---|---|
| Trabalho manual eliminado | Por semana, do calendário da equipe, com Power Automate, Power BI e DAX | +5h |
| Dashboards em uso | Tesouraria, Financeiro e Tax, para decisão de caixa, hedge e tributo | +10 |
| Caixa sob gestão | Em dólares, Brasil e Chile | Centenas de milhões |

**Por que não são três blocos de número.** Era assim na revisão 4: três colunas
iguais, número grande em cima, legenda curta embaixo. Esse é o formato mais
comum em página gerada por IA, e o conteúdo aqui é bom demais para entregar no
formato genérico. A leitura de posição vem do mundo real do assunto: é como um
relatório de caixa é composto. O ganho não é só de forma. "Trabalho manual
eliminado" com `+5h` à direita lê como linha de relatório. `+5h` com um
parágrafo embaixo lê como card de landing page.

Os valores continuam subindo do zero uma vez só, quando a seção entra.

- **Fechamento da seção:** Isso não é projeto de fim de semana. É processo redesenhado dentro de uma operação que não pode parar.

### 6.5 A cadeia de execução (a assinatura)

- **Etiqueta:** CADEIA DE EXECUÇÃO
- **Título:** Como uma instrução atravessa a câmara
- **Momento interativo:** pressione e segure para rodar um ciclo. A instrução desce pelas quatro etapas, cada uma acende em ouro na vez dela, e o artefato sai no fim. Soltar antes do fim para o ciclo onde está.
- **Microcopy do interativo:** Segure para rodar um ciclo
- **Etapas:**
  1. **INSTRUÇÃO — A pergunta vira contrato.** Escopo, fonte, periodicidade e formato ficam escritos antes de qualquer código. É o que impede o relatório de virar pedido avulso toda semana.
  2. **EXECUÇÃO — O relógio opera, não a pessoa.** Coleta, modelo e cálculo rodam agendados. Agentes fazem o repetitivo: buscar série, consolidar, comparar com o ciclo anterior, escrever.
  3. **ASSINATURA — Toda saída tem procedência.** Fonte, ciclo e transformação ficam gravados junto do resultado. Quem recebe rastreia de onde veio cada número.
  4. **ENTREGA — No formato de quem usa.** Relatório, painel ou base. O artefato chega pronto pra decisão, não como tarefa pendente.

### 6.6 Registros

- **Etiqueta:** REGISTROS
- **Título:** O que está em comissionamento agora
- **Legenda:** Projetos meus, fora do trabalho. Cada um mostra o estado real: projetado, em comissionamento ou no ar. Nada aqui é apresentado como pronto antes de estar.
- **Linha de fecho da seção:** Dois deles processam sem mandar nada pra fora da máquina. Quem trabalha com número de empresa sabe por que isso importa.

| Id | Nome | Estado | Resumo (literal) |
|---|---|---|---|
| 0002 | Crew macroeconômico | EM COMISSIONAMENTO | Conjunto de agentes que escreve sozinho: levanta o panorama, organiza por tema e entrega o texto pronto. A mesma arquitetura serve relatório macro periódico, newsletter e artigo. A operação ainda não fecha um ciclo sem supervisão. |
| 0003 | Organização financeira | PROJETADO | Base de conhecimento que dá nome e categoria à movimentação, com mapeamento de contas e diário das decisões de modelagem. É a espinha de um controle financeiro pessoal. A modelagem está escrita, a aplicação ainda não foi construída. |
| 0004 | Auditor de perfil | EM COMISSIONAMENTO | Lê um currículo em PDF e monta um dossiê estruturado. O que é conta sai calculado, e os dados pessoais são retirados antes de qualquer coisa sair da máquina. Fecha ponta a ponta na máquina local. |
| 0005 | IA local | NO AR | Assistente rodando em Ollama, na própria máquina, com memória em grafo de conhecimento. Orquestra tarefas, monta relatório, revisa código e responde no dia a dia. Não esquece o que já foi dito e nada do que ele lê sai do computador. Único registro no ar, e o mais usado de todos: está ligado agora. |

**Regra:** todo card recebe tratamento igual. Se um tiver print, todos têm.
Print pendente de envio do usuário.

### 6.7 Construção

- **Etiqueta:** CONSTRUÇÃO
- **Título:** Com o que eu construo

| Ferramenta | Papel | Linha (literal) |
|---|---|---|
| Power BI | MODELO | Modelo semântico, DAX, TMDL e automação do ciclo de relatório. |
| Power Automate | ROTINA | Fluxo que tira o passo manual do meio do processo financeiro. |
| SQL | BASE | Modelagem, consulta e a camada onde o dado ganha categoria estável. |
| Python | COLETA | Coleta, tratamento e o que precisa rodar fora da ferramenta de BI. |
| Agentes de IA | OPERAÇÃO | MCP e Claude Code operando a parte repetitiva do trabalho de dados. |
| Ollama | LOCAL | Modelo rodando na própria máquina, para o que não pode sair dela. |
| Grafo de conhecimento | MEMÓRIA | Onde o assistente local guarda contexto e ligação entre as coisas, em vez de recomeçar do zero a cada conversa. |
| Orquestração | RELÓGIO | Execução agendada, estado por etapa e registro do que foi feito. |

### 6.8 Formação e idiomas

- **Etiqueta:** FORMAÇÃO
- **Título:** A base

| Campo | Valor (literal) |
|---|---|
| PÓS-GRADUAÇÃO | Ciência de Dados para o Mercado Financeiro com Inteligência Artificial, XP Educação, concluída em 2026 |
| MBA | Finanças, IBMEC |
| GRADUAÇÃO | Negócios Internacionais e Comércio Exterior, FUMEC |
| CERTIFICAÇÕES | Engenharia de Prompts, Formação em Liderança |
| IDIOMAS | Português, inglês e espanhol, todos fluentes |

### 6.9 As perguntas que sempre vêm

Objeções tiradas da pesquisa com recrutadores e gestores técnicos.

- **Você ainda trabalha com tesouraria?**
  Trabalho, e é justamente o ponto. Não larguei finanças pra virar programador. Continuo na mesa da Kinross e construo as ferramentas de dentro do problema.

- **Você programa ou só usa ferramenta de IA?**
  Os dois, e a divisão é proposital. O que regex e aritmética resolvem não passa por modelo. Fiz pós-graduação em ciência de dados para o mercado financeiro com IA pra não depender de intuição nessa divisão.

- **Esses projetos são de trabalho ou pessoais?**
  As duas coisas, e a página separa. A automação com mais de cinco horas semanais eliminadas e os dashboards são trabalho, em produção. Os registros no fim da página são meus, fora do expediente, com o estado real de cada um escrito.

- **Dá pra ver o código?**
  O que está público está no GitHub, com link em cada registro. O que ainda é privado está marcado como tal, não escondido.

- **Você quer vaga ou consultoria?**
  As duas conversas me interessam. Papel de liderança onde automação e IA façam parte do modelo de operação da área financeira, ou projeto pontual de automação de processo financeiro. É a mesma habilidade nas duas.

### 6.10 O que eu procuro

Esqueleto: bloco estreito e centrado, tipografia grande, sem painel em volta.
É o único momento de silêncio da página, logo antes do chamado.

- **Etiqueta:** O QUE EU PROCURO
- **Título:** Onde eu quero estar
- **Corpo:** Um papel de liderança em que automação e IA deixem de ser iniciativa isolada e virem parte do modelo de operação da área financeira. Também converso sobre projeto pontual de automação de processo financeiro.

### 6.11 Contato

- **Etiqueta:** CONTATO
- **Título:** A linha está aberta
- **Corpo:** Se você precisa de alguém que entende o processo financeiro e constrói o sistema, e não só um dos dois, a próxima instrução é sua.
- **CTA primário:** Abrir conversa no LinkedIn
- **Destino:** https://www.linkedin.com/in/pedrovmaia/
- **Secundário:** GitHub, https://github.com/pedroboy975

**Decisão de formulário:** sem formulário. O site é estático e não tem servidor.
Formulário que finge enviar é pior que link honesto. E-mail e telefone não
aparecem, por escolha do usuário.

### 6.12 Rodapé

- Linha de honestidade: **As imagens de fundo deste site foram geradas por IA. A trajetória, os números e os estados dos projetos são reais.**
- Nota herdada: Nenhum dado de mercado, cotação ou informação confidencial de empregador aparece nesta página.
- Emitido em [data]

---

## 6.13 Nota sobre a versão em inglês

Títulos de seção, etiquetas, chamadas e as perguntas do FAQ são escritos aqui
nas duas línguas quando aparecem acima. Os parágrafos de corpo em inglês são
escritos na passagem de build, no mesmo registro seco e curto, e passam pelo
mesmo portão de copy da Fase 9.

Desvio consciente da regra de "todo texto literal no documento", feito para o
documento caber em uma leitura. Registrado em voz alta.

Paridade é requisito: a edição em inglês entrega a mesma prova, nunca um resumo.

---

## 7. O plano da camada vetorial

Esta é a assinatura do site. Se sumir, a página vira um portfólio escuro comum.

- **Painéis de instrumento:** retângulos de fio fino com cantos em colchete
  (quatro cantos desenhados, lados abertos). Desenham-se de canto a canto no
  scroll.
- **Linhas de guia:** filete de 1px saindo de uma chamada de texto até um ponto
  do vídeo, terminando num círculo pequeno. Cresce da etiqueta pro alvo.
- **Fluxo de etapas:** quatro caixas empilhadas ligadas por seta vertical.
  Acendem em sequência. Um dos dois lugares onde o ouro entra.
- **Contador dos números:** os três números da seção Entregue na mesa sobem do
  zero ao valor quando a seção entra, uma vez só. O outro lugar do ouro.
- **Trilho da trajetória:** linha vertical à esquerda da linha do tempo, com um
  nó por empresa. Desenha-se de cima pra baixo conforme a seção entra.
- **Medidor de telemetria:** barra de picos irregulares no canto inferior,
  pulsando devagar, nível sussurro. Puramente ambiente.
- **Grade de fundo fixa:** malha em aço, opacidade muito baixa, com deriva
  lenta de 90 segundos, atrás de tudo. É o que faz a página ser um lugar só.
  Anda mais devagar que o conteúdo, o que dá o plano de profundidade.

**Movimento reduzido:** todo elemento acima aparece no estado final, imóvel.
Números já no valor final. Nenhum drive roda. Nenhum vídeo é requisitado.

### 7.1 A camada de animação, depois do corte da revisão 5

Abaixo da dobra o movimento usa a API nativa de scroll (`animation-timeline`),
dentro de `@supports` e de uma classe ligada só quando `CSS.supports` confirma.
Sem suporte, cai no IntersectionObserver: a página fica correta, só menos viva.
Roda no compositor, então não custa quadro.

**O que ficou, e o que cada peça codifica:**

| Peça | O que ela diz |
|---|---|
| Parallax da grade | Profundidade. A página é um lugar, não uma lista. |
| Revelação por seção | Ritmo de leitura. |
| Trilho da trajetória desenhando com o scroll | Tempo passando. Você controla o traço. |
| Cards dos registros entrando pela própria posição | Cada projeto é separado, e não um lote. |
| Cadeia de execução, segurar para rodar | A assinatura. É o pico da página. |

**O que foi cortado, e por quê.** A revisão 4 tinha treze peças de animação.
Efeito espalhado é exatamente o que denuncia página gerada: muita coisa se
mexendo, nada dizendo. Saíram: camada de poeira, barra de progresso, cabeçalho
encolhendo, colchetes do contato abrindo, linhas da construção deslizando,
colunas de número respirando. As quatro últimas ainda animavam `padding`,
`background`, `width` e `height`, que forçam layout e pintura a cada quadro, ao
contrário de `transform` e `opacity`.

Um caso separado: a seção "O que eu procuro" desbotava para 35% ao sair da
tela. Texto que some enquanto a pessoa lê é problema de legibilidade, não
efeito. Agora entra e fica.

**Armadilha registrada:** animação de linha do tempo de scroll não tem duração,
então o truque de `animation-duration: .001ms` do bloco de movimento reduzido
não a alcança. É preciso matar `animation-timeline` e `animation-name`
explicitamente.

---

## 8. A lista de engenharia

O build segue o padrão inteiro de `scrub-pipeline.md`, sem meia memória:

- Vídeo buscado como Blob, com anel de carregamento honesto se passar de 8 MB.
- Lerp do tempo exibido normalizado por dt, em laço rAF que descansa.
- Seeks com portão, nunca sobrepostos.
- Escrita no DOM só quando muda.
- Faixas paginadas em distância de scroll, validadas pelo teste de flick.
- Sistema de legibilidade de quatro camadas, auditado contra o pior frame.
- Cinco portões do hero estático, em CSS e JS, com listener de mudança.
- Página completa e bonita mesmo se o vídeo nunca carregar.
- Piso de qualidade inteiro: contraste calculado, landmarks semânticos, skip
  link, vídeo decorativo fora da ordem de tabulação, foco visível no aço,
  alvo de toque de 44px, favicon SVG da marca.
- Padrão do site inteiro animado: nada snapa, tudo tem easing, cada seção tem
  um elemento vivo em nível sussurro.
- Nenhum estado só de `:hover`. Todo alvo interativo tem `:active`.
- Sem `overflow` recortado em ancestral de elemento grudado.
- Unidades de viewport escolhidas por papel: `svh` para o que gruda, `dvh` para
  o que só precisa encher a tela uma vez.
- Duas edições, PT em `/` e EN em `/en/`, com troca de idioma no cabeçalho e
  `hreflang` cruzado.

---

## 9. Dados que NÃO entram no site

- Telefone e e-mail pessoal, presentes no currículo. Canal único: LinkedIn.
- 100X Partners, por escolha do usuário.
- Qualquer informação confidencial da Kinross. Os números usados são os que o
  próprio Pedro publica no resumo do LinkedIn dele.

---

## 10. O portão de copy

Todo texto acima vai para a página literalmente. A página construída passa pelo
grep da Fase 9 antes de qualquer pessoa ver: zero travessão, zero palavra de
catálogo, mais a varredura de vícios de IA no corpo do texto.

Dispositivos de marca escritos aqui de propósito são ofício e ficam: as
etiquetas em caixa alta, os estados em mono, a frase curta e seca. A varredura
caça o que entrou sem convite.

---

## 11. Estado da construção

| Item | Estado |
|---|---|
| Página PT em `site/index.html` | CONSTRUÍDA, arquivo único, sem build e sem npm |
| Página EN em `/en/` | NÃO CONSTRUÍDA |
| Fundo do hero | PLACEHOLDER. Gradiente CSS no lugar do vídeo. |
| Prints dos registros | PENDENTES de envio do usuário |
| Créditos Higgsfield gastos | ZERO. Teste de três dias ainda não ativado. |

O elemento `<video id="heroVideo">` já está no DOM e o seek com portão já está
escrito dentro do laço de pintura. Quando a filmagem existir, é plugar o Blob e
tirar o `display:none`. O parallax do hero já separa fundo e instrumentação, e
continua valendo sem mudança quando o vídeo entrar.

**A regra do teste de três dias não mudou:** ativar só depois do aval do
documento e com a página pronta. Planejar é de graça.

**Ferramenta de apoio:** `review/tipografia.html` compara quatro trios
tipográficos sobre o texto real do site. A pasta `review/` nunca é publicada.
