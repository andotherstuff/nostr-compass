---
title: Topics
permalink: /en/topics/
layout: page
---

The Nostr Compass topic index documents key protocol concepts, NIPs, client
implementations, and relay software. Each topic includes links to primary
sources (NIPs, code repositories) and our newsletter coverage.

{% capture raw_topics_list %}
{%- for topic in site.topics -%}
[{{topic.title}}]({{topic.url}})ENDTOPIC
  {%- for alias in topic.title-aliases -%}*[{{alias}}]({{topic.url}})*ENDTOPIC{%- endfor -%}
{%- endfor -%}
{% endcapture %}

{% assign topics_list = raw_topics_list | split: 'ENDTOPIC' | sort_natural %}
{% assign number_of_topics = site.topics | size %}
{% assign number_of_entries = topics_list | size %}
{% assign number_of_aliases = number_of_entries | minus: number_of_topics %}

{% if number_of_topics > 0 %}
<div class="center" markdown="1">

{{number_of_topics}} topics (and
{{number_of_aliases}} aliases in *italics* for topics with alternative
names).

{:.center}
{% assign previous_character = '' %}
{% for entry in topics_list %}
  {%- assign first_character = entry | truncate: 1, '' | downcase -%}
  {%- if first_character != previous_character -%}
    {%- if previous_character != nil -%}
      [{{first_character | upcase}}](#{{first_character}}){{' '}}
    {%- endif -%}
  {%- endif -%}
  {%- assign previous_character = first_character -%}
{% endfor %}
</div>

<div>

{% assign previous_character = '' %}
{% for entry in topics_list %}
  {% assign first_character = entry | truncate: 1, '' | downcase %}
  {% if first_character != previous_character %}
    {% if previous_character != '' %}</ul>{% endif %}
    <h3 id="{{first_character}}">{{first_character | upcase}}</h3>
    <ul>
  {% endif %}
  <li>{{entry | markdownify | remove: "<p>" | remove: "</p>" | strip }}</li>
  {% assign previous_character = first_character %}
{% endfor %}
</ul>

</div>
{% else %}
<p><em>Topic index coming soon. We're building out documentation of key Nostr concepts, NIPs, and implementations.</em></p>
{% endif %}

Want to suggest a topic? Open an issue on our [GitHub repository](https://github.com/nostrcompass/nostr-compass).
