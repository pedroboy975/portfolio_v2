# -*- coding: utf-8 -*-
"""
Gera docs/en/index.html a partir de docs/index.html.

Por que um script e nao um arquivo escrito a mao: duas edicoes escritas em
paralelo divergem em silencio. Aqui o motor, o CSS e a estrutura sao os mesmos
bytes do PT por construcao, e so o texto muda. Quando o PT mudar, roda de novo.

Cada substituicao declara quantas vezes deve acontecer. Se o PT mudar e uma
string sumir, o script para e diz qual: silencio nao e opcao.

    python ferramentas/build-en.py
"""
import io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = os.path.join(RAIZ, "docs", "index.html")
DESTINO = os.path.join(RAIZ, "docs", "en", "index.html")
BASE = "https://pedroboy975.github.io/portfolio_v2/"

# (pt, en, vezes esperadas)
T = [
# ---------- cabecalho do documento ----------
('<html lang="pt-BR">', '<html lang="en">', 1),
('<title>Pedro Maia | Tesouraria, dados e agentes de IA</title>',
 '<title>Pedro Maia | Treasury, data and AI agents</title>', 1),
('content="Pedro Maia | Tesouraria, dados e agentes de IA"',
 'content="Pedro Maia | Treasury, data and AI agents"', 1),
('Especialista de Tesouraria na Kinross Gold Corp. Caixa, câmbio, hedge, investimentos, seguros e capital de giro para Brasil e Chile. Dados e agentes de IA constru&#237;dos de dentro do problema.'.replace('&#231;','ç').replace('&#227;','ã').replace('&#237;','í'),
 'Treasury Specialist at Kinross Gold Corp. Cash, FX, hedging, investments, insurance and working capital for Brazil and Chile. Data and AI agents built from inside the problem.', 2),
('<meta property="og:locale" content="pt_BR">',
 '<meta property="og:locale" content="en_US">', 1),
('<link rel="alternate" hreflang="pt-BR" href="./">',
 '<link rel="alternate" hreflang="pt-BR" href="../">', 1),
('<link rel="alternate" hreflang="en" href="./en/">',
 '<link rel="alternate" hreflang="en" href="./">', 1),
('<meta property="og:url" content="' + BASE + '">',
 '<meta property="og:url" content="' + BASE + 'en/">', 1),
('<link rel="canonical" href="' + BASE + '">',
 '<link rel="canonical" href="' + BASE + 'en/">', 1),
('<meta property="og:image" content="' + BASE + 'assets/social.jpg">',
 '<meta property="og:image" content="' + BASE + 'assets/social-en.jpg">', 1),
('content="Pedro Maia, Especialista de Tesouraria na Kinross Gold Corp. Ao fundo, uma poca de ouro derretido no piso de uma camara de aco."',
 'content="Pedro Maia, Treasury Specialist at Kinross Gold Corp. Behind him, a pool of molten gold in the floor of a steel chamber."', 1),

# ---------- navegacao ----------
('>Pular para o conteúdo<', '>Skip to content<', 1),
('<a href="#entregue">Entregas</a>', '<a href="#entregue">Delivered</a>', 1),
('<a href="#registros">Registros</a>', '<a href="#registros">Records</a>', 1),
('<a href="#contato">Contato</a>', '<a href="#contato">Contact</a>', 1),
('<a href="./en/" hreflang="en">EN</a>', '<a href="../" hreflang="pt-BR">PT</a>', 1),

# ---------- faixas do hero ----------
('<p class="kicker">A MESA</p>\n        <p class="line">Centenas de milhões de dólares passam pela minha mesa.</p>',
 '<p class="kicker">THE DESK</p>\n        <p class="line">Hundreds of millions of dollars cross my desk.</p>', 1),
('<p class="kicker">O ESCOPO ATUAL</p>', '<p class="kicker">THE CURRENT SCOPE</p>', 1),
('<p class="line">Brasil e Chile. Caixa, câmbio, hedge, investimentos, seguros e capital de giro.</p>',
 '<p class="line">Brazil and Chile. Cash, FX, hedging, investments, insurance and working capital.</p>', 1),
('<p class="kicker">O QUE MUDOU</p>', '<p class="kicker">WHAT CHANGED</p>', 1),
('<p class="line">Eu apaguei <span class="num">cinco horas semanais</span> de trabalho manual do calendário da equipe.</p>',
 '<p class="line">I wiped <span class="num">five hours a week</span> of manual work off my team\'s calendar.</p>', 1),
('<p class="role">Especialista de Tesouraria na <b>Kinross Gold Corp.</b></p>',
 '<p class="role">Treasury Specialist at <b>Kinross Gold Corp.</b></p>', 1),
('<p class="sub">Tesouraria, dados e agentes de IA.</p>',
 '<p class="sub">Treasury, data and AI agents.</p>', 1),
('>Abrir conversa no LinkedIn <span class="arw">', '>Start a conversation on LinkedIn <span class="arw">', 1),
('>Abrir conversa <span class="arw">', '>Start a conversation <span class="arw">', 2),
('>Role<span></span>', '>Scroll<span></span>', 1),
('>Voltar ao modo parado<', '>Back to the still version<', 1),
('</span>Ver a abertura em movimento<', '</span>See the opening in motion<', 1),
('Seu sistema pede menos movimento e o site obedece.\n      O resto da página continua parado de qualquer forma.',
 'Your system asks for less motion and the site obeys.\n      The rest of the page stays still either way.', 1),

# ---------- hero estatico ----------
('<h1>Centenas de milhões de dólares passam pela minha mesa. E eu construo o sistema que faz o trabalho.</h1>',
 '<h1>Hundreds of millions of dollars cross my desk. And I build the system that does the work.</h1>', 1),
('<p>Especialista de Tesouraria na Kinross Gold Corp. Caixa, câmbio, hedge, investimentos, seguros e capital de giro para Brasil e Chile. Uma década em finanças, agora com dados e agentes de IA em cima.</p>',
 '<p>Treasury Specialist at Kinross Gold Corp. Cash, FX, hedging, investments, insurance and working capital for Brazil and Chile. A decade in finance, now with data and AI agents on top.</p>', 1),

# ---------- 1. a ponte ----------
('<p class="eyebrow">POR QUE ESSA COMBINAÇÃO</p>', '<p class="eyebrow">WHY THIS COMBINATION</p>', 1),
('<h2>Quase ninguém está dos dois lados</h2>', '<h2>Almost nobody sits on both sides</h2>', 1),
('<p class="tag">LADO TÉCNICO</p>', '<p class="tag">THE TECHNICAL SIDE</p>', 1),
('<p>Constrói rápido e não sabe o que o negócio precisa.</p>',
 '<p>Builds fast and does not know what the business needs.</p>', 1),
('<p class="tag">LADO FINANCEIRO</p>', '<p class="tag">THE FINANCE SIDE</p>', 1),
('<p>Sabe exatamente o que precisa e não constrói.</p>',
 '<p>Knows exactly what it needs and does not build.</p>', 1),
('<p class="tag">ONDE EU FICO</p>', '<p class="tag">WHERE I SIT</p>', 1),
('<p>Eu passo o dia numa mesa de tesouraria de verdade, com fechamento, banco e dinheiro no meio, e construo do outro lado com o problema ainda fresco. Não escolho o que automatizar por curiosidade. Escolho pelo que já me atrasou.</p>',
 '<p>I spend my day at a real treasury desk, with closing, banks and money in the middle of it, and I build on the other side with the problem still fresh. I do not pick what to automate out of curiosity. I pick what has already cost me time.</p>', 1),
('<p class="verdict">O valor não está em saber programar. Está em saber <em>o que construir</em>.</p>',
 '<p class="verdict">The value is not in knowing how to code. It is in knowing <em>what to build</em>.</p>', 1),

# ---------- 2. trajetoria ----------
('<p class="eyebrow">TRAJETÓRIA</p>', '<p class="eyebrow">TRACK RECORD</p>', 1),
('<h2>Onde o ofício foi aprendido</h2>', '<h2>Where the craft was learned</h2>', 1),
('<p class="lede">Em três das quatro, o reporte foi para fora do Brasil, em inglês, no calendário de fechamento da matriz.</p>',
 '<p class="lede">In three of the four, reporting went outside Brazil, in English, on the parent company\'s closing calendar.</p>', 1),
('alt="Escadaria de aço em vários lances, em ziguezague, subindo a parede de uma câmara alta."',
 'alt="A steel staircase of many switchback flights climbing the wall of a tall chamber."', 1),
('<p class="when">2023 ATÉ HOJE</p>', '<p class="when">2023 TO TODAY</p>', 1),
('<span class="hq">Matriz: Canadá</span>', '<span class="hq">Head office: Canada</span>', 1),
('<p class="role">Especialista de Tesouraria (Analista Sênior até 2026)</p>',
 '<p class="role">Treasury Specialist (Senior Analyst until 2026)</p>', 1),
('<p class="desc">Gestão de caixa, fluxo, relacionamento bancário e operações financeiras para Brasil e Chile. Programa corporativo de hedge cambial com NDF e Zero Cost Collar. Capital de giro, seguros e garantias. Orçamento e forecast de caixa.</p>',
 '<p class="desc">Cash management, forecasting, banking relationships and financial operations for Brazil and Chile. Corporate FX hedging programme with NDF and Zero Cost Collar. Working capital, insurance and guarantees. Budget and cash forecast.</p>', 1),
('<p class="when">2020 A 2023</p>', '<p class="when">2020 TO 2023</p>', 1),
('<span class="hq">Matriz: Malásia</span>', '<span class="hq">Head office: Malaysia</span>', 1),
('<p class="role">Analista Sênior de Tesouraria</p>', '<p class="role">Senior Treasury Analyst</p>', 1),
('<p class="desc">Caixa e operações bancárias das Américas: Argentina, Brasil, México e Estados Unidos. Negociação e gestão de dívida, hedge, capital de giro e análise do Ciclo de Conversão de Caixa.</p>',
 '<p class="desc">Cash and banking operations across the Americas: Argentina, Brazil, Mexico and the United States. Debt negotiation and management, hedging, working capital and Cash Conversion Cycle analysis.</p>', 1),
('<p class="when">2017 A 2020</p>', '<p class="when">2017 TO 2020</p>', 1),
('<span class="hq">Matriz: Brasil</span>', '<span class="hq">Head office: Brazil</span>', 1),
('<p class="role">Analista Financeiro de Tesouraria</p>', '<p class="role">Treasury Financial Analyst</p>', 1),
('<p class="desc">Operação de câmbio ponta a ponta: análise, classificação, registro e execução junto ao Banco Central do Brasil. Apuração de tributo sobre operação financeira e cambial. Gestão da exposição cambial da instituição.</p>',
 '<p class="desc">End-to-end FX operations: analysis, classification, registration and execution with the Central Bank of Brazil. Assessment of tax on financial and FX transactions. Management of the institution\'s FX exposure.</p>', 1),
('<p class="when">2015 A 2017</p>', '<p class="when">2015 TO 2017</p>', 1),
('<span class="hq">Matriz: Itália</span>', '<span class="hq">Head office: Italy</span>', 1),
('<p class="role">Estágio, Finanças Estruturadas e Câmbio</p>',
 '<p class="role">Internship, Structured Finance and FX</p>', 1),
('<p class="desc">Cotação de câmbio, NDF e swap com bancos. Registro em BM&amp;F, SELIC e CETIP. Operações overnight, garantias bancárias e projetos com linha subsidiada.</p>',
 '<p class="desc">FX, NDF and swap quoting with banks. Registration with BM&amp;F, SELIC and CETIP. Overnight operations, bank guarantees and subsidised credit line projects.</p>', 1),

# ---------- 3. a mesa ----------
('<p class="eyebrow">A MESA</p>', '<p class="eyebrow">THE DESK</p>', 1),
('<h2>O tamanho da operação</h2>', '<h2>The size of the operation</h2>', 1),
('alt="Fila de portas de aço maciças recuando por uma parede de câmara, com uma fresta de luz quente acesa sob cada uma."',
 'alt="A row of massive steel doors receding along a chamber wall, a slot of warm light lit under each one."', 1),
('<dt>OPERAÇÃO</dt><dd>Mineração de ouro; maior mina de ouro a céu aberto do Brasil</dd>',
 '<dt>OPERATION</dt><dd>Gold mining; the largest open-pit gold mine in Brazil</dd>', 1),
('<dt>PAÍSES HOJE</dt><dd>Brasil, Chile</dd>', '<dt>COUNTRIES TODAY</dt><dd>Brazil, Chile</dd>', 1),
('<dt>JÁ OPEROU</dt><dd>Argentina, México, Estados Unidos</dd>',
 '<dt>PREVIOUSLY COVERED</dt><dd>Argentina, Mexico, United States</dd>', 1),
('<dt>REPORTE</dt><dd>Canadá, Malásia e Itália, em inglês, no calendário da matriz</dd>',
 '<dt>REPORTING</dt><dd>Canada, Malaysia and Italy, in English, on the parent company\'s calendar</dd>', 1),
('<dt>HEDGE</dt><dd>Programa corporativo com NDF e Zero Cost Collar</dd>',
 '<dt>HEDGING</dt><dd>Corporate programme with NDF and Zero Cost Collar</dd>', 1),
('<dt>INSTRUMENTOS</dt><dd>Câmbio, derivativo de hedge, dívida, capital de giro, seguros e garantias</dd>',
 '<dt>INSTRUMENTS</dt><dd>FX, hedging derivatives, debt, working capital, insurance and guarantees</dd>', 1),
('<dt>ÓRGÃOS E SISTEMAS</dt><dd>Bancos privados, Banco Central do Brasil, BM&amp;F, SELIC, CETIP e corretoras de seguros</dd>',
 '<dt>BODIES AND SYSTEMS</dt><dd>Private banks, the Central Bank of Brazil, BM&amp;F, SELIC, CETIP and insurance brokers</dd>', 1),
('<dt>CADÊNCIA</dt><dd>Rotinas diárias, semanais, mensais e trimestrais</dd>',
 '<dt>CADENCE</dt><dd>Daily, weekly, monthly and quarterly routines</dd>', 1),
('<p class="note">Escopo real de responsabilidade, sem número que não seja meu de dizer.</p>',
 '<p class="note">Real scope of responsibility, with no number that is not mine to state.</p>', 1),

# ---------- 4. entregue na mesa ----------
('<p class="eyebrow">ENTREGUE NA MESA</p>', '<p class="eyebrow">DELIVERED AT THE DESK</p>', 1),
('<h2>Automação que já está rodando no trabalho</h2>', '<h2>Automation already running at work</h2>', 1),
('<span class="what">Trabalho manual eliminado</span>', '<span class="what">Manual work eliminated</span>', 1),
('<span class="how">Por semana, do calendário da equipe, com Power Automate, Power BI e DAX</span>',
 '<span class="how">Per week, off my team\'s calendar, with Power Automate, Power BI and DAX</span>', 1),
('<span class="what">Dashboards em uso</span>', '<span class="what">Dashboards in use</span>', 1),
('<span class="how">Tesouraria, Financeiro e Tax, para decisão de caixa, hedge e tributo</span>',
 '<span class="how">Treasury, Finance and Tax, for cash, hedging and tax decisions</span>', 1),
('<span class="what">Caixa sob gestão</span>', '<span class="what">Cash under management</span>', 1),
('<span class="how">Em dólares, Brasil e Chile</span>', '<span class="how">In dollars, Brazil and Chile</span>', 1),
('<dd class="words">Centenas de milhões</dd>', '<dd class="words">Hundreds of millions</dd>', 1),
('<p class="closing">Isso não é projeto de fim de semana. É processo redesenhado dentro de uma operação que não pode parar.</p>',
 '<p class="closing">This is not a weekend project. It is process redesigned inside an operation that cannot stop.</p>', 1),

# ---------- 5. cadeia de execucao ----------
('<p class="eyebrow">CADEIA DE EXECUÇÃO</p>', '<p class="eyebrow">EXECUTION CHAIN</p>', 1),
('<h2>Como uma instrução atravessa a câmara</h2>', '<h2>How an instruction crosses the chamber</h2>', 1),
('alt="Canal aberto no piso de aço com ouro derretido correndo por baixo de uma comporta, recuando ao fundo da câmara."',
 'alt="An open channel in the steel floor with molten gold running under a gate, receding into the chamber."', 1),
('<p class="n">01 / INSTRUÇÃO</p>', '<p class="n">01 / INSTRUCTION</p>', 1),
('<h3>A pergunta vira contrato</h3>', '<h3>The question becomes a contract</h3>', 1),
('<p class="desc">Escopo, fonte, periodicidade e formato ficam escritos antes de qualquer código. É o que impede o relatório de virar pedido avulso toda semana.</p>',
 '<p class="desc">Scope, source, frequency and format are written down before any code. That is what stops the report from becoming a fresh request every week.</p>', 1),
('<p class="n">02 / EXECUÇÃO</p>', '<p class="n">02 / EXECUTION</p>', 1),
('<h3>O relógio opera, não a pessoa</h3>', '<h3>The clock runs it, not a person</h3>', 1),
('<p class="desc">Coleta, modelo e cálculo rodam agendados. Agentes fazem o repetitivo: buscar série, consolidar, comparar com o ciclo anterior, escrever.</p>',
 '<p class="desc">Collection, model and calculation run on a schedule. Agents do the repetitive part: pull the series, consolidate, compare against the previous cycle, write.</p>', 1),
('<p class="n">03 / ASSINATURA</p>', '<p class="n">03 / SIGNATURE</p>', 1),
('<h3>Toda saída tem procedência</h3>', '<h3>Every output carries its provenance</h3>', 1),
('<p class="desc">Fonte, ciclo e transformação ficam gravados junto do resultado. Quem recebe rastreia de onde veio cada número.</p>',
 '<p class="desc">Source, cycle and transformation are recorded alongside the result. Whoever receives it can trace where each number came from.</p>', 1),
('<p class="n">04 / ENTREGA</p>', '<p class="n">04 / DELIVERY</p>', 1),
('<h3>No formato de quem usa</h3>', '<h3>In the format the reader uses</h3>', 1),
('<p class="desc">Relatório, painel ou base. O artefato chega pronto pra decisão, não como tarefa pendente.</p>',
 '<p class="desc">Report, dashboard or dataset. The artefact arrives ready for a decision, not as a pending task.</p>', 1),
('>Segure para ver uma instrução atravessar<', '>Hold to watch an instruction cross<', 1),
('>ARTEFATO ENTREGUE<', '>ARTEFACT DELIVERED<', 1),

# ---------- 6. registros ----------
('<p class="eyebrow">REGISTROS</p>', '<p class="eyebrow">RECORDS</p>', 1),
('<h2>O que está em comissionamento agora</h2>', '<h2>What is in commissioning right now</h2>', 1),
('<p class="lede">Projetos meus, fora do trabalho. Cada um mostra o estado real: projetado, em comissionamento ou no ar. Nada aqui é apresentado como pronto antes de estar.</p>',
 '<p class="lede">My own projects, outside work. Each one shows its real state: designed, in commissioning or live. Nothing here is presented as finished before it is.</p>', 1),
('<span class="state comiss">Em comissionamento</span>', '<span class="state comiss">In commissioning</span>', 2),
('<span class="state">Projetado</span>', '<span class="state">Designed</span>', 1),
('<span class="state no-ar">No ar</span>', '<span class="state no-ar">Live</span>', 1),
('<h3>Crew macroeconômico</h3>', '<h3>Macroeconomic crew</h3>', 1),
('<p>Conjunto de agentes que escreve sozinho: levanta o panorama, organiza por tema e entrega o texto pronto. A mesma arquitetura serve relatório macro periódico, newsletter e artigo. A operação ainda não fecha um ciclo sem supervisão.</p>',
 '<p>A set of agents that writes on its own: it gathers the picture, organises it by theme and delivers finished text. The same architecture serves a periodic macro report, a newsletter and an article. The operation still cannot close a cycle without supervision.</p>', 1),
('<h3>Organização financeira</h3>', '<h3>Financial organisation</h3>', 1),
('<p>Base de conhecimento que dá nome e categoria à movimentação, com mapeamento de contas e diário das decisões de modelagem. É a espinha de um controle financeiro pessoal. A modelagem está escrita, a aplicação ainda não foi construída.</p>',
 '<p>A knowledge base that gives transactions a name and a category, with account mapping and a journal of modelling decisions. It is the spine of a personal finance control. The modelling is written, the application has not been built yet.</p>', 1),
('<h3>Auditor de perfil</h3>', '<h3>Profile auditor</h3>', 1),
('<p>Lê um currículo em PDF e monta um dossiê estruturado. O que é conta sai calculado, e os dados pessoais são retirados antes de qualquer coisa sair da máquina. Fecha ponta a ponta na máquina local.</p>',
 '<p>It reads a CV in PDF and assembles a structured dossier. What is arithmetic comes out calculated, and personal data is stripped before anything leaves the machine. It closes end to end on the local machine.</p>', 1),
('<h3>IA local</h3>', '<h3>Local AI</h3>', 1),
('<p>Assistente rodando em Ollama, na própria máquina, com memória em grafo de conhecimento. Orquestra tarefas, monta relatório, revisa código e responde no dia a dia. Não esquece o que já foi dito e nada do que ele lê sai do computador. Único registro no ar, e o mais usado de todos: está ligado agora.</p>',
 '<p>An assistant running on Ollama, on the machine itself, with memory in a knowledge graph. It orchestrates tasks, assembles reports, reviews code and answers day to day. It does not forget what has been said and nothing it reads leaves the computer. The only record that is live, and the most used of them all: it is running right now.</p>', 1),
('<p class="closing">Dois deles processam sem mandar nada pra fora da máquina. Quem trabalha com número de empresa sabe por que isso importa.</p>',
 '<p class="closing">Two of them process without sending anything off the machine. Anyone who works with company numbers knows why that matters.</p>', 1),

# ---------- 7. construcao ----------
('<p class="eyebrow">CONSTRUÇÃO</p>', '<p class="eyebrow">TOOLING</p>', 1),
('<h2>Com o que eu construo</h2>', '<h2>What I build with</h2>', 1),
('<span class="part">MODELO</span><p>Modelo semântico, DAX, TMDL e automação do ciclo de relatório.</p>',
 '<span class="part">MODEL</span><p>Semantic model, DAX, TMDL and automation of the reporting cycle.</p>', 1),
('<span class="part">ROTINA</span><p>Fluxo que tira o passo manual do meio do processo financeiro.</p>',
 '<span class="part">ROUTINE</span><p>Flows that take the manual step out of the middle of a finance process.</p>', 1),
('<span class="part">BASE</span><p>Modelagem, consulta e a camada onde o dado ganha categoria estável.</p>',
 '<span class="part">DATABASE</span><p>Modelling, querying and the layer where data gets a stable category.</p>', 1),
('<span class="part">COLETA</span><p>Coleta, tratamento e o que precisa rodar fora da ferramenta de BI.</p>',
 '<span class="part">COLLECTION</span><p>Collection, treatment and whatever has to run outside the BI tool.</p>', 1),
('<span class="tool">Agentes de IA</span><span class="part">OPERAÇÃO</span><p>MCP e Claude Code operando a parte repetitiva do trabalho de dados.</p>',
 '<span class="tool">AI agents</span><span class="part">OPERATION</span><p>MCP and Claude Code running the repetitive part of data work.</p>', 1),
('<span class="part">LOCAL</span><p>Modelo rodando na própria máquina, para o que não pode sair dela.</p>',
 '<span class="part">LOCAL</span><p>A model running on the machine itself, for what cannot leave it.</p>', 1),
('<span class="tool">Grafo de conhecimento</span><span class="part">MEMÓRIA</span><p>Onde o assistente local guarda contexto e ligação entre as coisas, em vez de recomeçar do zero a cada conversa.</p>',
 '<span class="tool">Knowledge graph</span><span class="part">MEMORY</span><p>Where the local assistant keeps context and the links between things, instead of starting from zero in every conversation.</p>', 1),
('<span class="tool">Orquestração</span><span class="part">RELÓGIO</span><p>Execução agendada, estado por etapa e registro do que foi feito.</p>',
 '<span class="tool">Orchestration</span><span class="part">CLOCK</span><p>Scheduled execution, state per step and a record of what was done.</p>', 1),

# ---------- 8. formacao ----------
('<p class="eyebrow">FORMAÇÃO</p>', '<p class="eyebrow">EDUCATION</p>', 1),
('<h2>A base</h2>', '<h2>The groundwork</h2>', 1),
('alt="Pórtico de aço maciço visto à distância, apoiado sobre um monte de rocha em camadas com veios de ouro acesos."',
 'alt="A monumental bare steel frame seen at a distance, standing on a mound of layered rock with lit seams of gold."', 1),
('<p class="k">PÓS-GRADUAÇÃO</p><p>Ciência de Dados para o Mercado Financeiro com Inteligência Artificial, XP Educação, concluída em 2026</p>',
 '<p class="k">POSTGRADUATE</p><p>Data Science for Financial Markets with Artificial Intelligence, XP Educação, completed in 2026</p>', 1),
('<p class="k">MBA</p><p>Finanças, IBMEC</p>', '<p class="k">MBA</p><p>Finance, IBMEC</p>', 1),
('<p class="k">GRADUAÇÃO</p><p>Negócios Internacionais e Comércio Exterior, FUMEC</p>',
 '<p class="k">BACHELOR&rsquo;S</p><p>International Business and Foreign Trade, FUMEC</p>', 1),
('<p class="k">CERTIFICAÇÕES</p><p>Engenharia de Prompts, Formação em Liderança</p>',
 '<p class="k">CERTIFICATIONS</p><p>Prompt Engineering, Leadership Programme</p>', 1),
('<p class="k">IDIOMAS</p><p>Português, inglês e espanhol, todos fluentes</p>',
 '<p class="k">LANGUAGES</p><p>Portuguese, English and Spanish, all fluent</p>', 1),

# ---------- 9. perguntas ----------
('<p class="eyebrow">PERGUNTAS</p>', '<p class="eyebrow">QUESTIONS</p>', 1),
('<h2>As que sempre vêm</h2>', '<h2>The ones that always come up</h2>', 1),
('<summary>Você ainda trabalha com tesouraria?</summary>', '<summary>Do you still work in treasury?</summary>', 1),
('<p>Trabalho, e é justamente o ponto. Não larguei finanças pra virar programador. Continuo na mesa da Kinross e construo as ferramentas de dentro do problema.</p>',
 '<p>I do, and that is exactly the point. I did not leave finance to become a programmer. I am still at the Kinross desk and I build the tools from inside the problem.</p>', 1),
('<summary>Você programa ou só usa ferramenta de IA?</summary>', '<summary>Do you code, or do you just use AI tools?</summary>', 1),
('<p>Os dois, e a divisão é proposital. O que regex e aritmética resolvem não passa por modelo. Fiz pós-graduação em ciência de dados para o mercado financeiro com IA pra não depender de intuição nessa divisão.</p>',
 '<p>Both, and the split is deliberate. What regex and arithmetic can solve does not go through a model. I took a postgraduate degree in data science for financial markets with AI so that I would not have to rely on intuition for that split.</p>', 1),
('<summary>Esses projetos são de trabalho ou pessoais?</summary>', '<summary>Are these projects from work or personal?</summary>', 1),
('<p>As duas coisas, e a página separa. A automação com mais de cinco horas semanais eliminadas e os dashboards são trabalho, em produção. Os registros no fim da página são meus, fora do expediente, com o estado real de cada um escrito.</p>',
 '<p>Both, and the page keeps them apart. The automation with more than five hours a week eliminated and the dashboards are work, in production. The records at the end of the page are mine, outside working hours, with the real state of each one written down.</p>', 1),
('<summary>Dá pra ver o código?</summary>', '<summary>Can I see the code?</summary>', 1),
('<p>O que está público está no GitHub, com link em cada registro. O que ainda é privado está marcado como tal, não escondido.</p>',
 '<p>What is public is on GitHub, linked from each record. What is still private is marked as such, not hidden.</p>', 1),
('<summary>Você quer vaga ou consultoria?</summary>', '<summary>Are you after a role or consulting work?</summary>', 1),
('<p>As duas conversas me interessam. Papel de liderança onde automação e IA façam parte do modelo de operação da área financeira, ou projeto pontual de automação de processo financeiro. É a mesma habilidade nas duas.</p>',
 '<p>Both conversations interest me. A leadership role where automation and AI are part of how the finance function operates, or a one-off financial process automation project. It is the same skill in both.</p>', 1),

# ---------- 10. o que eu procuro ----------
('<p class="eyebrow">O QUE EU PROCURO</p>', '<p class="eyebrow">WHAT I AM LOOKING FOR</p>', 1),
('<p class="want">Um papel de liderança em que automação e IA deixem de ser iniciativa isolada e virem parte do modelo de operação da área financeira. Também converso sobre projeto pontual de automação de processo financeiro.</p>',
 '<p class="want">A leadership role where automation and AI stop being an isolated initiative and become part of how the finance function operates. I am also open to a one-off financial process automation project.</p>', 1),

# ---------- 11. contato ----------
('<p class="eyebrow">CONTATO</p>', '<p class="eyebrow">CONTACT</p>', 1),
('<h2>A linha está aberta</h2>', '<h2>The line is open</h2>', 1),
('<p>Se você precisa de alguém que entende o processo financeiro e constrói o sistema, e não só um dos dois, a próxima instrução é sua.</p>',
 '<p>If you need someone who understands the finance process and builds the system, not just one of the two, the next instruction is yours.</p>', 1),

# ---------- rodape ----------
('<p>As imagens de fundo deste site foram geradas por IA. A trajetória, os números e os estados dos projetos são reais.</p>',
 '<p>The background images on this site were generated by AI. The track record, the numbers and the project states are real.</p>', 1),
('<p>Nenhum dado de mercado, cotação ou informação confidencial de empregador aparece nesta página.</p>',
 '<p>No market data, quotes or confidential employer information appear on this page.</p>', 1),
('<p class="mono">EMITIDO EM 2026</p>', '<p class="mono">ISSUED IN 2026</p>', 1),
]


def main():
    s = io.open(ORIGEM, encoding="utf-8").read()
    faltando = []
    for pt, en, n in T:
        achou = s.count(pt)
        if achou != n:
            faltando.append((achou, n, pt[:78]))
            continue
        s = s.replace(pt, en)
    if faltando:
        print("PAROU. O PT mudou e estas substituicoes nao batem mais:\n")
        for achou, n, trecho in faltando:
            print("  achou %d, esperava %d  ->  %s" % (achou, n, trecho))
        sys.exit(1)

    # Caminhos: a pagina EN mora um nivel abaixo. As URLs absolutas do cartao
    # social e do canonical nao podem virar ../ , entao saem de cena primeiro.
    guarda = "\x00URLABS\x00"
    s = s.replace(BASE + "assets/", guarda)
    s = s.replace('"assets/', '"../assets/')
    s = s.replace("'assets/", "'../assets/")
    s = s.replace(guarda, BASE + "assets/")

    restou = [ln for ln in s.split("\n")
              if "assets/" in ln and "../assets/" not in ln and BASE not in ln]
    if restou:
        print("PAROU. Sobraram caminhos relativos nao corrigidos:")
        for ln in restou:
            print("  " + ln.strip()[:100])
        sys.exit(1)

    aviso = ("<!-- GERADO. Nao edite este arquivo a mao: ele e reconstruido a partir de\n"
             "     docs/index.html por ferramentas/build-en.py. Editar aqui faz as duas\n"
             "     edicoes divergirem em silencio, que e exatamente o que o script evita. -->\n")
    s = s.replace("<!doctype html>\n", "<!doctype html>\n" + aviso, 1)

    os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
    io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(s)
    print("escrito %s  (%d substituicoes, %d bytes)"
          % (os.path.relpath(DESTINO, RAIZ), len(T), len(s.encode("utf-8"))))
    # Rede de seguranca. So o texto visivel: comentarios ficam em portugues de
    # proposito, e "conversation" contem "conversa", entao ambos dao falso alarme.
    corpo = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    corpo = re.sub(r"<(script|style)\b.*?</\1>", " ", corpo, flags=re.S | re.I)
    corpo = re.sub(r"<[^>]+>", " ", corpo)
    marcas = ["tesouraria", "trabalho", "registros", "câmara", "ouro", "você",
              "não", "está", "código", "número", "máquina"]
    sobrou = sorted({m for m in marcas
                     if re.search(r"(?<![a-zà-ú])" + m + r"(?![a-zà-ú])", corpo, re.I)})
    print("restos de portugues no texto visivel: %s"
          % (", ".join(sobrou) if sobrou else "nenhum"))


if __name__ == "__main__":
    main()
