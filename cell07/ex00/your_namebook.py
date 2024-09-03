#!/usr/bin/env python3

def array_of_names(per):
    res = [f"{key.capitalize()} {value.capitalize()}" for key, value in per.items()]
    return res
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))