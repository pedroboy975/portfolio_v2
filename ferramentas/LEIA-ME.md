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
