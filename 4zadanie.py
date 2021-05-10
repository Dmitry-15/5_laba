#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    s = input('Введите предложение: ')
    s1 = s.split(' ')
    for i in range(len(s1) - 1):
        for j in range(len(s1) - i - 1):
            if len(s1[j]) < len(s1[j + 1]):
                s1[j], s1[j + 1] = s1[j + 1], s1[j]
    s = ''
    for i in range(0, len(s1)):
        s += s1[i] + ' '
    print(s)



