#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import json
import io
F_SYNONYMS = sys.argv[1]
F_IN = sys.argv[2]
F_OUT = sys.argv[3]

dict_synonyms = json.load(io.open(F_SYNONYMS, encoding='utf-8'))

#dict_synonyms = {'PR':['permiso retribuido'], 'SRF':['sistema de retribución flexible'], 'solicito':['pido', 'pedir']}
keys = dict_synonyms.keys()
print keys

sentences_list = []
with io.open(F_IN, encoding='utf-8') as f:
   for line in f:
       sentences_list.append(line)
       words = re.split(r'[^\w]', line)

       for key in keys:
          if (key in words):
              print line
              index = words.index(key)
              extensions = [line.replace(key, replacement) for replacement in dict_synonyms[key]]

              sentences_list.extend(extensions)

       outfile = open(F_OUT, 'w')
outfile.write("".join(sentences_list).encode('utf-8'))
