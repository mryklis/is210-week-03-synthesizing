#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition

FLEMISH = inquisition.SPANISH

word = 'Spanish'
length= len(word)
found=inquisition.SPANISH.index('Spanish')

part1 = FLEMISH[:found]
part2 = FLEMISH[(found + length):]

FLEMISH = part1 + 'Flemish' + part2

print FLEMISH
