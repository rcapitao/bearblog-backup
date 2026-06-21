---
title: Identificar cookies nos sites
slug: identificar-cookies-nos-sites
published_date: 2025-07-22T10:49:00+00:00
tags: dicas, privacidade
publish: true
make_discoverable: true
is_page: false
meta_description: Sites sem cookies existem? Descubra por que essa afirmação quase sempre está errada e como verificar cookies manualmente no navegador.
---

Durante uma reunião sobre a adequação dos sites organizacionais à LGPD, ouvi a seguinte frase de um representante da área:  

> O nosso site não possui cookies.  

Na hora, soou estranho. Afinal, é raríssimo um site, mesmo os mais simples, não ter ao menos cookies proprietários ou de terceiros.  

Esse episódio me trouxe um ponto importante que quero dividir com quem trabalha com privacidade e proteção de dados: Conhecimentos técnicos são essenciais, não basta conhecer apenas a legislação.  

Na mesma hora, compartilhei a tela, acessei o site, abri o módulo do desenvolvedor do navegador e... lá estavam os cookies de terceiros, visíveis sem o uso de nenhuma ferramenta automatizada.  

**Dica prática**: Sempre que alguém afirmar que um site não utiliza cookies, faça a checagem técnica.  

## Como eu faço para identificar cookies diretamente no navegador?  

### 💻 Chrome  

_O caminho é o praticamente o mesmo para outros navegadores que usam o Chromium, como Edge e Brave._  

1. Acesse o site.  
2. Pressione `F12` ou clique com o botão direito e selecione **“Inspecionar”**.  
3. Vá até a aba **“Application”**.  
4. No menu lateral esquerdo, clique em **“Cookies”** (dentro de “Storage”).  
5. Você verá os cookies separados por domínio. Cookies de domínios diferentes do site visitado são de terceiros.  

### 🦊 Firefox  

1. Acesse o site.  
2. Pressione `F12` ou clique com o botão direito e selecione **“Inspecionar”**.  
3. Vá até a aba **“Armazenamento”** (Storage).  
4. Em “Cookies”, clique no domínio e veja os detalhes.  
5. Compare com o domínio do site visitado para identificar terceiros.  

### 🍏 Safari (macOS)  

1. Acesse o site.  
2. Vá em **Safari > Preferências > Privacidade > Gerenciar Dados do Site...**  
3. Aparecerá a lista de domínios com cookies ou dados armazenados.  
4. Para mais detalhes, ative o **Modo Desenvolvedor** (Safari > Ajustes > Avançado > Mostrar menu de Desenvolvimento na barra de menus)  
5. Com o site aberto, vá em **Desenvolvedor > Mostrar Ferramentas da Web > Armazenamento > Cookies**  

<div class="reply-email">  
<a href="https://letterbird.co/rcapitao?subject=Re:%20{{ post_title }}" target="_blank">Comente por e-mail</a>  
</div>   

<meta name="fediverse:creator" content="@rcapitao@mastodon.social">