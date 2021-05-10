#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    pr = input("Введите предложение: ")
    s = ''
    for i in range(len(pr)):
        if i % 3 == 0 and i != 0:
            s += 'a'
        else:
            s += pr[i]
    print("Замена произведена:", s)



