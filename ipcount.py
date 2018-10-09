#!/usr/bin/env python
# encoding: utf-8
import collections
data = open('ipfile.txt')
d=data.read()
d = d.strip()
alpha = len(d.split(' '))
print 'number of data %s' % alpha
d = d.split(' ')
print collections.Counter(d)
