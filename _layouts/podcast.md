---
type: pages
layout: default
---
<link rel="stylesheet" href="/assets/css/main.css">

<h1 class="post-title">Podcast</h1>

The Nostr Compass podcast features conversations with the developers whose
work is covered in our weekly newsletters. We discuss NIP proposals, client
implementations, relay developments, and the reasoning behind technical
decisions.

<!-- TODO: Add podcast links when episodes are available
{% include functions/podcast-links.md %}
-->

{% if content != ""%}
  <div class="post-content">
    {{ content }}
  </div>
{%- endif -%}

{% assign posts_podcast = site.posts | where:"lang", page.lang | where:"type","podcast" %}

{% if posts_podcast.size > 0 %}
<ul class="post-list">
  {%- for post in posts_podcast -%}
  <li>
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    <span class="post-meta">{{ post.date | date: date_format }}</span>
    <h3>
      <a class="post-link" href="{{ post.url | relative_url }}">
        {{ post.title | escape }}
      </a>
    </h3>
    {%- if site.show_excerpts -%}
      {{ post.excerpt }}
    {%- endif -%}
  </li>
  {%- endfor -%}
</ul>
{% else %}
<p><em>Podcast episodes coming soon. We're preparing conversations with developers building Nostr.</em></p>
{% endif %}
