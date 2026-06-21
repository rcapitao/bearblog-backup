# bearblog-backup

Automação que faz o backup diário dos posts do [Bear Blog](https://bearblog.dev) publicados em [rcapitao.com](https://rcapitao.com), lendo o feed Atom do blog (`https://rcapitao.com/feed/`).

## O que a automação faz

- Roda automaticamente todos os dias à 00:00 (UTC) via GitHub Actions.
- O feed do Bear Blog traz sempre os 10 posts mais recentes, então a cada execução são salvos/atualizados os 10 últimos posts publicados.
- Cada post é salvo em uma pasta dentro de `posts/`, nomeada apenas com a data de **publicação** do post no formato `AAAA-MM-DD`. O arquivo Markdown leva o título do post como nome:

  ```
  posts/AAAA-MM-DD/
  ├── Título do post.md
  ├── imagem-do-post.webp   (se houver imagens no corpo do post)
  └── imagem-meta.jpg       (imagem usada como meta_image)
  ```

- Se houver mais de uma publicação no mesmo dia, todas ficam na mesma pasta da data, cada uma com seu próprio arquivo Markdown (nomeado pelo título) e suas respectivas imagens.
- O arquivo Markdown contém o conteúdo do post e um frontmatter com:
  - `title`
  - `link`
  - `date` (data de publicação)
  - `tags`
  - `meta_description`
  - `meta_image`
- Imagens usadas no corpo do post e a imagem indicada em `meta_image` são baixadas e salvas junto com o markdown na pasta do post (exceto a imagem padrão do site, `og-image.png`, que não é baixada).
- A automação **nunca remove** posts antigos: ela apenas cria ou atualiza os arquivos dos 10 posts presentes no feed a cada execução. Posts que saem do feed permanecem intactos em `posts/`, então o backup vai acumulando ao longo do tempo.
- Ao final, as mudanças são commitadas e enviadas automaticamente para a branch `main` do repositório.

## Limitação e como ter o backup completo

Como o feed do Bear Blog só lista os 10 posts mais recentes, a automação não tem acesso ao histórico completo do blog — apenas aos últimos posts publicados.

Para garantir um backup completo de todo o histórico, exporte seus posts diretamente no painel do Bear Blog no formato `.md` e adicione esses arquivos neste repositório (por exemplo, na pasta `posts/`). A partir daí, a automação diária mantém o backup sempre atualizado com os posts mais recentes, enquanto o histórico exportado preserva os posts mais antigos.
