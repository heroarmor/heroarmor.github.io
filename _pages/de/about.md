---
layout: about
title: über mich
permalink: /de/
lang: de
translations:
  en: /
  de: /de/
subtitle: Doktorand, <a href='https://engineering.purdue.edu/ECE'>Elmore Family School of Electrical and Computer Engineering</a>, Purdue University

profile:
  align: right
  image: prof_pic.png
  image_circular: false
  more_info: >
    <p>Purdue University</p>
    <p>West Lafayette, IN, USA</p>

# The about layout prints English headings for these sections, so they are written out below instead.
selected_papers: false
social: false

announcements:
  enabled: false

latest_posts:
  enabled: false
---

Ich bin Doktorand im ersten Jahr an der [Elmore Family School of Electrical and Computer Engineering](https://engineering.purdue.edu/ECE) der Purdue University und werde von Prof. Jinghan Sun betreut. Meine Forschung liegt an der Schnittstelle von **Rechnerarchitektur**, **EDA** und **Systemen für maschinelles Lernen**.

Zuvor habe ich meinen B.S.E. in Computer Engineering (_Summa Cum Laude_) an der [University of Michigan](https://ece.engin.umich.edu/) abgeschlossen. Dort habe ich bei [Prof. Nathaniel Bleier](https://nbleier.com/) in der [Crucible Computing Group](https://crucible.eecs.umich.edu/) an stochastischem Rechnen für DNN-Inferenz mit gemischter Präzision, an Chiplet-basierten Systemen und an agilem Hardware-Design gearbeitet. Außerdem habe ich mit [Prof. Jishen Zhao](https://cseweb.ucsd.edu/~jzhao/) und [Prof. Zhijian Liu](https://zhijianliu.com/) an effizienter LLM-Inferenz für lange Kontexte geforscht. Darüber hinaus habe ich einen B.S. in Maschinenbau der [Shanghai Jiao Tong University](https://www.ji.sjtu.edu.cn/) (UM-SJTU Joint Institute).

<div style="clear: both;"></div>

<h2>
  <a href="{{ '/de/publications/' | relative_url }}" style="color: inherit">ausgewählte publikationen</a>
</h2>

<div class="publications">

{% bibliography --group_by none --query @*[selected=true]* %}

</div>

<div class="social">
  <div class="contact-icons">{% social_links %}</div>
  <div class="contact-note">Am besten erreichen Sie mich per E-Mail.</div>
</div>
