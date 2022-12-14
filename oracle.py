#!/usr/bin/python3

import re
import os
import sys

lines = sys.stdin.readlines()

l1 = []
l2 = []

lemma = sys.argv[1]
print(lemma)
if (lemma == 'ForwardSecrecyInitMaster'):

  for line in lines:
    num = line.split(':')[0]
    if re.match('.*OwnKeyUpdate\(.*\#i.*', line) or re.match('.*AppDataKey\(.*\#i.*', line):
      l1.append(num)
    else :
      l2.append(num)

elif (lemma == 'ForwardSecrecyRespMaster'):
  for line in lines:
    num = line.split(':')[0]
    if re.match('.*OwnKeyUpdateR\(.*\#i.*', line) or re.match('.*AppDataKey\(.*\#i.*', line):
      l1.append(num)
    else :
      l2.append(num)
else:
  pass

ranked = l1 + l2 