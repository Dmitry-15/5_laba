#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input('Введите текст: ')
    a = '0'
    for i in s:
        if i.isdigit() and i > a:
            a = i
    print(s.lstrip().index(a) + 1)



