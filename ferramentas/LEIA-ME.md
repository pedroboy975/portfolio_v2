# Ferramentas

Fontes versionadas do que é gerado por fora do site.

## card-social.html

A fonte do cartão social (`docs/assets/social.jpg`, 1200x630) que o LinkedIn
mostra quando alguém cola o link. É uma página real, com as mesmas fontes e os
mesmos tokens do site, fotografada em vez de desenhada à mão.

Para regenerar, com o quadro final ao lado do arquivo:

```
cp ../docs/assets/hero-ending.jpg .
python -m http.server 8125 --bind 127.0.0.1
# fotografar em 1200x630 com deviceScaleFactor 2, depois:
ffmpeg -i card@2x.png -vf scale=1200:630 -q:v 2 ../docs/assets/social.jpg
```

A composição não é gosto: a coluna de texto tem 470px porque o perfil de
luminância do quadro passa de 0.27 em x=500 e o contraste desaba dali para a
direita. Mexer na largura da coluna exige medir de novo.

## build-en.py

Gera `docs/en/index.html` a partir de `docs/index.html`.

```
python ferramentas/build-en.py
```

**Rode isso toda vez que mexer no texto do PT.** Duas edições escritas em
paralelo divergem em silêncio: ninguém lê as duas lado a lado, então a diferença
só aparece quando alguém de fora repara. Aqui o motor, o CSS e a estrutura são os
mesmos bytes por construção, e só o texto muda.

Cada substituição declara quantas vezes deve acontecer. Se o PT mudar e um
trecho sumir, o script para e diz exatamente qual — falhar alto é o objetivo.

Ele também corrige os caminhos relativos para `../assets/`, preservando as URLs
absolutas do cartão social e do canonical, e recusa a escrever se sobrar algum
caminho não corrigido.

## card-social-en.html

Mesmo cartão, texto em inglês, vira `docs/assets/social-en.jpg`. Gerado do mesmo
jeito que o PT. A `og:image` da página EN aponta para ele: um cartão em português
num link compartilhado em inglês é uma quebra de paridade que aparece logo no
primeiro compartilhamento.
