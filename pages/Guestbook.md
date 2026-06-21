---
title: Guestbook
slug: guestbook
published_date: 2025-12-02T21:39:00+00:00
publish: true
make_discoverable: false
is_page: true
meta_description: Deixe sua mensagem e ajude a manter este blog ainda mais vivo. Eu leio e respondo todas as mensagens com atenção e carinho.
meta_image: https://bear-images.sfo2.cdn.digitaloceanspaces.com/rcapitao/guestbook.webp
---

# Guestbook  
<nav class="breadcrumb" aria-label="Breadcrumb">  
  <ol>  
    <li><a href="/">Home</a></li>  
    <li>Guestbook  
  </ol>  
</nav>  

Deixe sua mensagem e ajude a deixar esse blog ainda mais vivo. Eu leio e respondo todas as mensagens.  

_Observe que sua mensagem não aparecerá na página imediatamente, pois tenho que revisar cada entrada para manter meu livro de visitas livre de spam._  

<!-- Guestbook Script -->  
<script async src="https://guestbooks.meadow.cafe/resources/js/embed_script/5961/script.js"></script>  
<!-- Guestbook Form -->  
<div id="guestbooks___guestbook-form-container">  
  <form id="guestbooks___guestbook-form"  
        action="https://guestbooks.meadow.cafe/guestbook/5961/submit"  
        method="post">  
    <div class="guestbooks___input-container">  
      <input type="text"  
             id="name"  
             name="name"  
             placeholder="Nome"  
             required>  
    </div>  
    <div class="guestbooks___input-container">  
      <input type="url"  
             id="website"  
             name="website"  
             placeholder="Website (opcional) - incluir com https://">  
    </div>  
    <div id="guestbooks___challenge-answer-container"></div>  
    <div class="guestbooks___input-container">  
      <textarea id="text"  
                name="text"  
                placeholder="Deixe a sua mensagem aqui..."  
                rows="4"  
                style="width: 100%; box-sizing: border-box; resize: vertical;"  
                required></textarea>  
    </div>  
    <button type="submit">Assine o Guestbook</button>  
    <div id="guestbooks___error-message"></div>  
  </form>  
</div>  
<!-- Attribution (optional but appreciated!) -->  
<div id="guestbooks___guestbook-made-with" style="text-align: right; margin-top: 10px;">  
  <small>Powered by <a href="https://guestbooks.meadow.cafe" target="_blank">Guestbooks</a></small>  
</div>  
<!-- Messages Section -->  
<hr style="margin: 2em 0;"/>  
<h3 id="guestbooks___guestbook-messages-header">Mensagens</h3>  
<div id="guestbooks___guestbook-messages-container"></div>