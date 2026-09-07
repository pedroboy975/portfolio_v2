# Plano de construção do site A Câmara

Escrito com a skill 10k-websites, contra o DESIGN-PACKAGE.md revisão 6 e a
página já rascunhada em `site/index.html`.

Este documento é a ordem de serviço. Cada bloco tem entrada, saída e portão.
Portão marcado com ⛔ nunca é pulado.

**Regra de dinheiro, herdada da decisão do usuário:** o teste gratuito de 3 dias
da Higgsfield só é ativado no bloco 4, depois que o roteiro do plano estiver
aprovado. Zero créditos gastos até lá.

---

## Bloco 0. Estado do sistema (verificado hoje)

| Item | Estado |
|---|---|
| ffmpeg | ✓ versão 9.0.1 full build |
| Node.js | ✓ v24.19.0 |
| npx | ✓ 11.17.0 (serve o preview local) |
| Conector Higgsfield | ✓ ferramentas respondem |
| Créditos Higgsfield | ✗ teste não ativado, zero gastos |
| Conector Hostinger | ✗ não conectado, e por decisão do plano isso fica para o bloco 8 |

Nada a instalar. O ambiente está pronto.

### O que já existe

- `DESIGN-PACKAGE.md`, revisão 6. Premissa, paleta, trio tipográfico, mapa de
  quatro faixas em PT e EN, hero estático, plano completo abaixo da dobra em
  treze seções, camada vetorial, lista de engenharia, portão de copy.
- `site/index.html`, 957 linhas, sem build. Página PT inteira montada, camada
  vetorial, animação de scroll nativa com reserva por IntersectionObserver,
  parallax, momento interativo da cadeia de execução, hero estático.
- `site/assets/`, vazia. É aqui que o vídeo processado e as imagens entram.
- `review/tipografia.html`, prova de quatro trios tipográficos. Nunca é publicada.

### O que não existe

- Vídeo do hero. O `<video id="heroVideo">` está no HTML e o seek está escrito,
  mas não há arquivo, não há poster, não há carregamento.
- Edição EN em `/en/`.
- Prints dos projetos nos cards de Registros.
- Metatags `og:` e `theme-color`.

---

## Bloco 1. Fechar as decisões que travam o resto

Nada aqui custa dinheiro. Tudo aqui trava ou destrava os blocos seguintes.

**1.1 O aval do design package.** É o portão mais barato do processo inteiro.
Um sim antes de qualquer geração vale mais que três re-rolagens depois.

**1.2 Os prints dos projetos.** Regra de paridade: ou os quatro cards de
Registros têm imagem, ou nenhum tem. Um card sem print ao lado de três com print
lê como buraco, não como escolha. Se algum projeto não tem tela que possa ser
mostrada, a decisão certa é nenhum card ter print e as quatro imagens de apoio
irem para outras seções.

**1.3 Onde o site vai morar.** Duas rotas, e elas não se somam:

- **Hostinger direto**, que é o caminho da skill. Subdomínio temporário gratuito
  para testar hoje, domínio próprio depois, zip e deploy em um comando, e o
  redeploy custa um minuto.
- **GitHub Pages primeiro**, que foi a ideia inicial. Funciona, mas é um segundo
  pipeline para manter, e o subdomínio temporário da Hostinger já entrega
  exatamente o que o GitHub Pages entregaria aqui: um endereço público para
  testar antes de apontar o domínio.

Recomendação: ir direto para Hostinger e pular o GitHub Pages. Decisão do usuário.

**1.4 A revisão da tipografia.** A Spline Sans está marcada como provisória no
§3. `review/tipografia.html` continua de pé, com a Newsreader ainda na mesa.
A hora de reabrir isso é agora, antes do vídeo, porque o trio entra no clima da
filmagem. Depois do vídeo aprovado, mexer em tipografia é retrabalho.

---

## Bloco 2. Fechar o roteiro do vídeo (⛔ portão, sem custo)

O §4 do design package já define a filmagem: descida vertical por um espaço
escuro instrumentado, ação na faixa central, texto nas laterais e no terço
inferior, quatro faixas, repouso em superfície larga e calma.

Falta escrever os prompts literais. Estão escritos abaixo, prontos para colar.
Este bloco é ler os dois prompts, olhar para eles contra o §4, e aprovar ou
ajustar. Aprovação aqui é o que autoriza o bloco 4.

### 2.1 Prompt do frame inicial (imagem, 16:9, 2k, cerca de 2 créditos)

Escrito contra as doze leis. A lei 1 pede que descer na página leia como descer
na imagem, e a descida vertical atende. A lei 5 pede assunto perdoador, e luz,
névoa e maquinário distante não têm anatomia para quebrar. A lei 7 pede
composição para o layout, e a faixa central fica livre para o texto flanquear.
A armadilha do espaço negativo está tratada: o mundo é descrito de borda a
borda, nunca como vazio ou escuridão nas laterais.

```
Looking straight down the length of a tall dark industrial shaft, composed as
the first moment of a slow continuous vertical descent. Cold steel-blue light
falls from above and rakes across brushed metal surfaces that recede into
depth on the left and on the right, the two sides carrying the same quiet
treatment so the centre of the frame stays open. A single warm gold filament
of light runs down the far centre of the shaft, small and distant. Thin haze
drifts through the beams. Deep blue-black atmosphere, cold steel highlights,
one warm gold accent, nothing else saturated. Cinematic, photorealistic,
high detail, 16:9. No text, no logos, no lettering anywhere.
```

**O que inspecionar antes de animar:** marcas registradas escondidas, que a IA
adora inventar. Se a faixa central ficou entulhada, o texto não tem onde morar
e o frame vale uma re-rolagem de 2 créditos, não um vídeo perdido.

### 2.2 Prompt do vídeo (imagem para vídeo, 1080p, 6 segundos, modo padrão, sem áudio)

A lei 8 pede que a travessia de superfície tenha o momento físico da lente. A
lei 4 pede o final escrito explicitamente, com margem generosa em cima e
embaixo, porque o cabeçalho do site senta em cima do frame e o corte de tela
larga come as bordas.

```
One continuous shot, no cuts. The camera descends straight down the centre of
the shaft at a steady unbroken speed, passing brushed metal instrumentation on
both sides. Haze drifts and shifts through the light throughout, and the beams
flicker faintly as the camera passes them, so the space stays alive. Partway
down the camera passes through a horizontal plane of pale light: a brief wash
of glare, fine droplets catching on the lens, one beat of soft blur, then the
descent continues. The gold filament at the centre grows steadily nearer. The
shot ends at rest on a wide calm horizontal metal surface lit from above, the
gold light pooling softly at its centre, generous open space above and below
the surface, the camera settled and still. No text or lettering anywhere.
```

**Por que este final:** superfície larga sem nada recortável é seguro para
texto em qualquer tela, que é a alternativa que a lei 4 recomenda explicitamente
contra o final de produto, onde o corte come as bordas.

### 2.3 As quatro imagens de apoio (cerca de 2 créditos cada)

Geradas só depois do vídeo passar no portão, e todas descritas no MESMO mundo:
mesma paleta, mesma luz, mesma gradação. Vão para as seções que não têm print
real. Se a decisão 1.2 for "sem prints", elas cobrem Trajetória, A mesa, Cadeia
de execução e Formação.

---

## Bloco 3. Preencher os buracos de engenharia (sem custo, pode rodar hoje)

A página está bonita e o motor do hero não está construído. Estes são os itens
do padrão de `scrub-pipeline.md` que faltam. Todos independem do vídeo, então
dá para escrever tudo antes de gastar um crédito.

**3.1 O carregador Blob com anel de progresso.** Muitos hosts não suportam
download parcial, e sem isso o seek trava em zero no site publicado enquanto
funciona perfeitamente no local. O vídeo é baixado inteiro como Blob. Acima de
8 MB vai transmitido, com anel de progresso honesto, cão de guarda de 20
segundos sem chunk, e queda para o hero estático se travar. O poster é pintado
primeiro e ganha a corrida de banda de propósito.

**3.2 Os cinco portões do hero estático, e eles devem bater caractere por
caractere entre CSS e JS.** Hoje existem dois, e o handler de mudança faz
`location.reload()`, que é grosseiro e perde a posição do usuário. Os cinco:

```
(max-width: 720px)
(orientation: portrait) and (max-width: 1024px)
(orientation: portrait) and (pointer: coarse)
(orientation: landscape) and (pointer: coarse) and (max-height: 560px)
(prefers-reduced-motion: reduce)
```

O quarto é o que a página não tem e mais dói: um celular deitado passa em toda
checagem de largura e não tem altura nenhuma para a jornada. O reload sai e
entram `enableScrub` e `disableScrub`, armados pelo evento de mudança das cinco
consultas.

**3.3 O portão de seek com escape de travamento.** O código atual usa
`!video.seeking`, que evita sobreposição mas não coalesce nem se recupera de
erro. O padrão do skill guarda o alvo mais novo, dispara exatamente um seek de
acompanhamento no evento `seeked`, e zera a trava no evento `error`, senão um
seek que falha congela o scrub para sempre.

**3.4 `overflow-x` nos dois.** Hoje só o `html` tem `clip`. O padrão pede
`hidden` primeiro como reserva e `clip` depois, em `html` E `body`.

**3.5 Divisão do texto das faixas e uma entrada por faixa.** O §4 já nomeia as
quatro entradas. Falta a máquina: divisão em spans de palavra e de caractere
feita uma vez no carregamento, com gerador pseudo-aleatório semeado para que o
"aleatório" seja idêntico em toda visita, cópia visualmente escondida com a
frase inteira para leitor de tela, e `--k` por faixa escrito pelo laço com
portão de delta. A faixa 1 abre montada, com rampa de carregamento única que
passa o bastão para o scroll.

**3.6 O sistema de legibilidade de quatro camadas.** Scrim base global, scrim
por faixa que acompanha o `--k`, token de sombra de texto em três camadas
desligado nos botões, e chip com desfoque para as etiquetas pequenas. A
auditoria de pior frame vem no bloco 6, com o vídeo na mão.

**3.7 Pausa em aba escondida.** `body.paused *, body.paused *::before,
body.paused *::after { animation-play-state: paused !important }`, ligado no
`visibilitychange`. O seletor precisa alcançar pseudo-elementos porque
`animation-play-state` não é herdado.

**3.8 As metatags que faltam.** `theme-color`, e `og:image` com `og:url` com um
comentário `<!-- DEPLOY STEP -->` bem marcado, para serem preenchidas com a URL
real no bloco 8.

**3.9 O sistema de movimento da página, não só o do hero.** Já aplicado hoje:
tokens de curva `--ease-out` e `--ease-in-out`, os sete `:hover` atrás de
`@media (hover:hover) and (pointer:fine)`, pressão em 140ms com escala de 0.97,
captura de ponteiro no botão da cadeia, soltura que desfaz de trás para frente
em vez de saltar pra zero, e movimento reduzido deixando cor e opacidade
passarem. Falta usar o `--ease-in-out`, que hoje está declarado e sem uso: ele é
a curva das faixas do hero, que se movem na tela em vez de entrar e sair.

**3.10 A edição EN em `/en/`.** Paridade completa, não resumo. Os títulos e as
perguntas já estão escritos nas duas línguas no design package; falta escrever
os parágrafos de corpo e montar o arquivo. Troca de idioma no cabeçalho e
`hreflang` cruzado nos dois lados.

---

## Bloco 4. Gerar o hero (⛔ aqui o dinheiro se move)

Ativar o teste de 3 dias da Higgsfield só neste momento.

1. **Preflight de custo com `get_cost: true`**, que é gratuito, no frame exato
   planejado. Dizer o preço antes de gerar.
2. **Gerar o frame inicial.** Cerca de 2 créditos.
3. **Inspecionar o frame eu mesmo** antes de mostrar: marcas registradas,
   composição, se a faixa central ficou livre. Depois mostrar para o usuário.
4. **⛔ Escolha do modelo de vídeo, com números reais.** Preflight do MESMO
   plano nos dois ou três modelos do catálogo. A diferença de preço entre o
   topo e o meio já foi medida em cinco para um, e os dois lados são de
   primeira linha. Num saldo de teste, o modelo do meio transforma uma tomada
   em várias, o que muda o portão do vídeo de assustador para decisão criativa
   normal. A escolha é do usuário, com os preços na mão.
5. **Gerar o vídeo**, 1080p, 6 segundos. Leva minutos. Enquanto roda, o bloco 3
   continua sendo escrito.
6. **Inspecionar o vídeo eu mesmo:** extrair frames de início, meio e fim, e
   medir se o final realmente repousa, com a curva de movimento:
   ```
   ffmpeg -i raw.mp4 -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -
   ```
   Uma chegada sobe e volta para perto do nível inicial. Uma deriva fica alta
   até o fim, e aí o conserto barato é aparar o cru no último frame estável,
   não re-rolar.
7. **⛔ O PORTÃO DO VÍDEO.** O arquivo vai para `review/`, fora da pasta que é
   publicada, para o usuário abrir com dois cliques e assistir. Junto vai
   minha crítica honesta, o preço de uma re-rolagem e o saldo restante. Se
   reprovar, ajusto o prompt ou o frame inicial e re-rolo. Se um conceito
   falhar três vídeos, o problema é o conceito, não o prompt, e aí ele muda.
8. **As quatro imagens de apoio**, só depois do portão passar.

---

## Bloco 5. Processar os arquivos (sem custo)

Nada gerado entra em `assets/` sem passar por aqui. Os crus e as cópias de
revisão ficam FORA da pasta publicada, sempre.

**A codificação de scrub**, que é a que mais importa. Sem intervalo curto de
quadro-chave o scrub engasga, porque o navegador só busca com precisão até um
quadro-chave:

```
ffmpeg -i raw.mp4 -c:v libx264 -crf 18 -preset slow -g 8 -keyint_min 8 \
  -pix_fmt yuv420p -movflags +faststart -an site/assets/hero-scrub.mp4
```

Alvo de 4 a 8 MB para 6 segundos em 1080p. Atenção à bifurcação de compressão:
a filmagem planejada é escura, com névoa e gradientes suaves, e gradiente é
justamente o tipo que faz banda em vez de esconder artefato. Então empurrar o
crf para cima quebra os frames calmos primeiro. Conferir os frames calmos
especificamente, e mexer em uma variável por vez.

**Poster e frame final:**

```
ffmpeg -i site/assets/hero-scrub.mp4 -frames:v 1 -q:v 2 site/assets/hero-poster.jpg
ffmpeg -sseof -0.1 -i site/assets/hero-scrub.mp4 -update 1 -frames:v 1 -q:v 2 site/assets/hero-ending.jpg
```

O frame final é um ativo de design gratuito e perfeitamente na marca. Reaproveitar
numa seção de baixo.

**Imagens de apoio**, uma passada limpa de compressão, cerca de 1920px de largura:

```
ffmpeg -i raw-still.png -vf scale=1920:-2 -q:v 2 site/assets/nome-da-secao.jpg
```

Prints de dashboard ficam em PNG. A passada JPEG é para imagem fotográfica, e
borda dura de interface é exatamente o que ela estraga.

---

## Bloco 6. Casar a página com a filmagem entregue

A inspeção corre nos dois sentidos. O modelo às vezes melhora o roteiro, e
quando a filmagem melhora o plano, o plano cede. Se o elemento-chave do frame
final cair fora do centro, o texto do repouso se move para honrar isso.

1. **Amostrar a paleta da filmagem aprovada** e finalizar os tokens do §2. Hoje
   eles são direção; depois do vídeo passam a ser medidos. O ouro e o aço já
   estão escolhidos, mas os valores exatos saem do frame.
2. **Ajustar os alcances das faixas** contra o vídeo real, com o teste de flick:
   passos de roda de 120px, 240px e 360px. Toda faixa precisa ficar legível por
   5 a 6 flicks normais, e nenhuma pode ser pulável a 360px. Arrastar devagar
   não prova nada; visitante real dá flick. Faixa que reprova é fundida com a
   vizinha, nunca espremida encurtando as rampas.
3. **A auditoria de pior frame.** Extrair os frames de cada faixa, aplicar o
   scrim no pico da faixa, e medir o pixel mais claro sob a zona do texto.
   Piso de 3.5 para 1, medido contra o PIOR frame, não contra a média. A média
   mente; o pior frame é onde o visitante vai estar no meio da leitura.
4. **Verificar o final com o cabeçalho simulado por cima**, numa janela larga e
   numa janela baixa, antes de aprovar de vez.

---

## Bloco 7. Autoteste antes de mostrar (⛔ portão de copy incluído)

Auditoria adversária. Provar, não presumir.

- Capturas em 1280x800, 1440x900, 375x812, 375x667.
- Exercitar todo botão e link.
- Scrub no topo, no meio, no fim, e depois scrub rápido. Chrome mostra engasgo
  primeiro.
- Teste de flick no mapa de faixas.
- Auditoria de legibilidade de pior frame.
- Provar que cada entrada realmente toca, porque ordem de cascata mata entrada
  em silêncio.
- Tentar empurrar a página para o lado: âncoras, decorações largas, larguras
  estreitas.
- Rodar com movimento reduzido, e virar movimento reduzido COM a página aberta,
  não só antes de carregar. Nos dois sentidos.
- Carregar com o vídeo ausente. A página tem que ficar completa sobre o poster.
- Console limpo em tamanho de desktop e de celular.
- Rabos de letra, g, y, p, em todo texto mascarado, a 100 por cento de zoom.

**⛔ O portão de copy.** Buscar no arquivo inteiro, PT e EN, os dois lados:

- travessão: zero ocorrências.
- as palavras de catálogo: leverage, seamless, empower, unlock, robust,
  actionable, data-driven, solutions, e os equivalentes em português.
- os tiques mais silenciosos: construções do tipo "não é só X, é Y", falsas
  amplitudes, atribuição vaga do tipo "muitos especialistas dizem", conclusão
  genérica de arremate, e as palavras testament, landscape, delve, elevate.

Ressalva que importa: recurso de marca escrito de propósito no design package é
ofício, não tique. O trio deliberado e a batida curta planejada ficam. A
varredura caça o que entrou sem ser convidado.

**Depois, a passada de olhos frescos.** Largar a lista e olhar a página como
visitante de primeira viagem, sem contexto. Algo flutua sem explicação? Algum
elemento paralelo está desigual, um card diferente dos irmãos, uma etapa sem
imagem? Isto é um ato diferente de auditar, e pega o que auditoria não pega.

**Então o preview.** Dois caminhos, e é preciso dizer qual está sendo visto:

- Dois cliques no `index.html` mostra o hero estático desenhado, porque o
  navegador bloqueia `fetch` em endereço de arquivo e o carregador Blob cai na
  reserva de propósito. É uma chance gratuita de conferir esse estado.
- O scrub completo precisa de um servidor local: `npx http-server` na pasta, e
  abrir o link do localhost NO NAVEGADOR, não no painel lateral do aplicativo,
  que tranca em página de vídeo com scroll.

---

## Bloco 8. Publicar

Só quando as rodadas de ajuste assentarem, e quem decide a hora é o usuário.

1. **Conectar a Hostinger.** No Windows:
   `claude mcp add hostinger -- npx.cmd -y hostinger-api-mcp`. Logo depois,
   disparar o login com uma leitura inofensiva, listar os sites. O navegador
   abre para autorizar uma vez, e pode ser um navegador diferente do usual.
   Se nada abrir, um reinício resolve, e é o único reinício previsto.
2. **Resolver o endereço primeiro.** Listar os domínios da conta. Se o domínio
   próprio já estiver lá, ele é a proposta. Se não, subdomínio temporário
   gratuito, que é opção real e não versão menor: põe o site no ar hoje e o
   domínio entra depois.
3. **Preencher as og tags** com a URL viva, no comentário `<!-- DEPLOY STEP -->`.
   Com editor, nunca com substituição por linha de comando, porque script de
   shell lê o arquivo UTF-8 na codificação errada e transforma todo acento em
   lixo. Isto vale duplo aqui: a página é em português e está cheia de acento.
4. **Zipar o CONTEÚDO, não a pasta.** `index.html` no topo do zip, `assets` ao
   lado. Zipar a pasta aninha tudo um nível e o site vive mostra listagem de
   diretório ou 404. `review/` e os crus ficam fora.
   ```
   Compress-Archive -Path .\index.html, .\assets, .\en -DestinationPath ..\site.zip -Force
   ```
5. **Criar o site na hospedagem e publicar o zip.**
6. **Verificar eu mesmo, antes de dizer que está pronto:** 200 em HTTPS, a URL
   do vídeo servindo sozinha, console limpo na URL viva, e o scrub funcionando
   no site publicado. Domínio novo em folha demora alguns minutos para o
   cadeado do HTTPS sair, e aviso de segurança logo depois do primeiro deploy é
   certificado sendo emitido, não site quebrado.
7. **Os recibos de velocidade**, medidos, nunca estimados:
   ```
   curl.exe -s -o NUL -w "TTFB %{time_starttransfer}s, total %{time_total}s, %{size_download} bytes\n" https://URL-VIVA/
   ```
   Rodar contra a página e contra o vídeo. Peso da página sem o vídeo deve cair
   nas dezenas de KB, e o carregamento bem abaixo de um segundo. Estes números
   respondem a única objeção séria a site cinematográfico, que é "bonito, mas
   deve ser lento": são arquivos estáticos, sem framework, sem build, sem
   servidor, então não existe backend para ser ruim.
8. **O teste do usuário no aparelho real.** Desktop e o celular dele, na rede de
   verdade, não no localhost. Conferir o scroll no topo e no fim do hero, no
   Chrome, que é onde engasgo aparece primeiro.

---

## Bloco 9. A volta de polimento

Mudar, rezipar, republicar. Um comando, um minuto. Feedback em rodadas:
estrutura primeiro, as seções certas; depois acabamento, alinhamento, corte,
imagem; depois movimento. Cada rodada aplicada numa passada só e reverificada
no ar.

---

## Ordem sugerida para amanhã

**Manhã, sem gastar nada:** bloco 1 inteiro, as quatro decisões. Depois bloco 2,
ler os dois prompts e aprovar. Depois bloco 3, que é a maior massa de trabalho
do plano e não depende de crédito nenhum.

**Tarde:** bloco 4, ativar o teste e gerar. Os minutos de renderização são
gastos escrevendo o que sobrou do bloco 3.

**Depois:** blocos 5, 6 e 7 correm juntos, e o 8 quando você mandar.

O caminho crítico é o bloco 1. Enquanto o aval do design package e a decisão
dos prints não saírem, tudo abaixo do bloco 3 fica parado.

---

## Os números, ditos antes de qualquer gasto

| Item | Custo |
|---|---|
| Preflight de qualquer geração | grátis, sempre |
| Frame inicial do hero | cerca de 2 créditos |
| Vídeo do hero, 1080p, 6 segundos | entre cerca de 10 e 55 créditos, conforme o modelo |
| Quatro imagens de apoio | cerca de 2 créditos cada, cerca de 8 no total |
| Uma re-rolagem de vídeo, se precisar | o mesmo preço do vídeo |
| Hospedagem | separado, e só entra na conversa no bloco 8 |
| Publicar e republicar | zero |

Um caminho completo com um retrato fica entre cerca de 20 e 70 créditos,
dependendo do modelo escolhido no passo 4.4. O teste gratuito cobre um hero
inteiro com uma re-rolagem, e cobre mais que isso com o modelo do meio.
