#!/usr/bin/env python3

def red_filter(find):
    key, value = find
    if value == 'red':
        return True
    else:
        return False

def find_the_redheads(fam):
    res = dict(filter(red_filter,fam.items()))
    return list(res)

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))