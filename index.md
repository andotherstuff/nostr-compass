---
layout: home
---

{:.logo}
![Nostr Compass Logo](/img/logos/compass-notext.svg)

Nostr Compass is a technical resource for the Nostr protocol, helping
developers, relay operators, and builders stay current on protocol evolution.

We publish [weekly newsletters][] covering NIP proposals, client updates,
relay developments, and notable code changes. Our [podcast][] features
conversations with the developers building Nostr. The [topic index][topics]
documents key concepts with links to primary sources.

[Learn more about us][about].

[weekly newsletters]: /en/newsletters/
[podcast]: /en/podcast/
[about]: /en/about
[topics]: /en/topics/

{% assign posts_en = site.posts | where:"lang","en" %}

{% if posts_en.size > 0 %}
<h2>Recent newsletters and podcasts</h2>
<ul class="post-list">
  {%- for post in posts_en limit:5 -%}
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

<p class="rss-subscribe">View more <a href="/en/newsletters/">newsletters</a>. Subscribe via <a href="{{ "/feed.xml" | relative_url }}">RSS</a>.</p>
{% else %}
<h2>Coming Soon</h2>
<p>Our first newsletter is in progress. Subscribe to be notified when we launch.</p>
{% endif %}

{% include newsletter-signup.html %}
