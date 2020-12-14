#!/usr/bin/evn python3
# -*- config: utf-8 -*-

def program():
    while True:
        a = int(input("a = "))
        b = int(input("b = "))

        if a == 0 or b == 0:
            break

        s = a * b
        print("Произведение a и b равно", s)

if __name__ == '__main__':
    program()