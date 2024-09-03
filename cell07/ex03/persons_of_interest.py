#!/usr/bin/env python3

def famous_births(sci):
    values = sci
    sor = sorted(sci.values(), key=lambda x: int(x['date_of_birth']))
    for science in sor:
        print(f"{science['name']} is a great scientist born in {science['date_of_birth']}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

men_scientists = {
"einstein": {"name": "Albert Einstein","date_of_birth": "1879"},
"newton": {"name": "Isaac Newton","date_of_birth": "1643"},
"tesla": {"name": "Nikola Tesla","date_of_birth": "1856"},
"darwin": {"name": "Charles Darwin","date_of_birth": "1809"}
}
famous_births(women_scientists)
print("")
famous_births(men_scientists)