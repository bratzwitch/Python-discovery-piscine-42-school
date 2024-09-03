#!/usr/bin/env python3

def greetings(text=None):
    if not text:
        print("Hello, noble stranger.")
    elif isinstance(text,str):
        print(f"{'Hello,'} {text}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)