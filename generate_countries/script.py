import os


def template(en_country: str, ru_country: str):
    return f"""---
title: "Как иммигрировать в {ru_country}"
layout: page
permalink: /country/{en_country}
sidebar:
nav: "docs"
---

# Как иммигрировать в {ru_country}

Страница находится в разработке. Если вы хотите помочь заполнить её по [шаблону](/template), пишите в нашу [группу волонтёров](https://t.me/+FHi3FnJaoWJkMDAx).
"""


line = ""
with open('countres_list.txt') as f:
    line = f.readline()

countres_list = [country.strip() for country in line.split("\t")]
print(len(countres_list))
with open('russia_country_list.txt', encoding="utf8") as f:
    line = f.readline()
russia_countres_list = [country.strip() for country in line.split("\t")]

for ru_country, en_country in zip(russia_countres_list, countres_list):
    with open(os.path.join('generate', en_country.replace(" ", "").lower() + '.md'), 'w', encoding="utf8") as f:
        f.write(template(en_country.replace(" ", "").lower(), ru_country))
