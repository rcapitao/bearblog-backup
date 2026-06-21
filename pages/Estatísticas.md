---
title: Estatísticas
slug: estatisticas
published_date: 2026-06-04T17:35:00+00:00
publish: true
make_discoverable: true
is_page: true
meta_description: Acompanhe o ritmo do blog: posts publicados, calendário de atividade, contagem de palavras e médias que revelam a constância do blog.
meta_image: https://bear-images.sfo2.cdn.digitaloceanspaces.com/rcapitao/estatisticas.webp
---

# Estatísticas  
<nav class="breadcrumb" aria-label="Breadcrumb">  
  <ol>  
    <li><a href="/">Home</a></li>  
    <li>Estatísticas</li>  
  </ol>  
</nav>  

{{ posts }}  

<div id="cb-summary">  

Desde {{ first_post }}, publiquei {{ total_posts }} ao longo de {{ years_blogging }}, uma média de {{ average_posts }} por mês. Meu mês mais ativo foi {{ most_active_month }}.  

</div>  

<div class="bl-widget">  
  <p class="bl-label">Últimos 10 posts</p>  
  <div class="bl-grid" id="bl-grid">  
    <div class="bl-loading">Buscando estatíticas…</div>  
  </div>  
</div>  

### Calendário de Postagens  

<div id="cb-wrap">  
  <div class="cb-nav">  
    <button id="cb-prev" type="button" aria-label="Previous year">&#8592;</button>  
    <span id="cb-year"></span>  
    <button id="cb-next" type="button" aria-label="Next year">&#8594;</button>  
  </div>  
  <div id="cb-grid"></div>  
</div>  

<meta name="fediverse:creator" content="@rcapitao@mastodon.social">