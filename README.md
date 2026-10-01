# A Câmara

Site de portfólio de Pedro Maia. Tesouraria, dados e agentes de IA.

No ar: https://pedroboy975.github.io/portfolio_v2/ (edição em inglês em `/en/`).

HTML, CSS e JavaScript puro. Sem framework, sem build, sem npm. Um `index.html`
mais uma pasta `assets/`, que é o que faz o deploy caber num commit e o preview
caber num duplo clique.

## O que tem aqui

| Caminho | O que é |
|---|---|
| `docs/` | A página publicada pelo GitHub Pages. PT em `docs/index.html`, EN em `docs/en/index.html`. |
| `ferramentas/` | Fontes do que é gerado por fora: o `build-en.py` e os cartões sociais. Ver `ferramentas/LEIA-ME.md`. |
| `DESIGN-PACKAGE.md` | Todas as decisões criativas: paleta, tipografia, faixas do hero, copy de cada seção. |
| `PLANO-DE-CONSTRUCAO.md` | A ordem de serviço original em dez blocos. Registro histórico. |

`review/` não é versionado. É onde o vídeo cru e os frames de inspeção ficam.

## Editar o texto

1. Edite `docs/index.html` (PT).
2. Rode `python ferramentas/build-en.py`. Ele regenera `docs/en/index.html` e
   para com erro se algum trecho do PT mudou sem a tradução correspondente.
3. Faça o commit dos dois arquivos juntos.

As imagens de fundo do site são geradas por IA. A trajetória, os números e os
estados dos projetos são reais.
