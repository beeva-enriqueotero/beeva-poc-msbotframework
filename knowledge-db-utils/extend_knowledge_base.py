#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import json
import io

import argparse
from collections import OrderedDict


parser = argparse.ArgumentParser(description='Extend input file using synonyms from json.')
parser.add_argument('file_in', help='input file')
parser.add_argument('file_out', help='output file')
parser.add_argument('synonyms', help='synonyms file in json format')

args = parser.parse_args()
print len(vars(args))
if len(vars(args)) < 3:
    print parser.print_help()
    exit(1)

F_SYNONYMS = vars(args)['synonyms']
F_IN = vars(args)['file_in']
F_OUT = vars(args)['file_out']

dict_synonyms = json.load(io.open(F_SYNONYMS, encoding='utf-8'))

keys = dict_synonyms.keys()
print keys

# To augment sentences_list with synonyms
sentences_list = []
with io.open(F_IN, encoding='utf-8') as f:
   for line in f:
       sentences_list.append(line)
       line1 = line.split('\t')
       words = re.split(r'[^\w]', line1[0])

       for key in keys:
          if (key in words):
              #print line
              index = words.index(key)
              extensions = [line1[0].replace(key, replacement)+"\t"+line1[1] for replacement in dict_synonyms[key]]

              sentences_list.extend(extensions)

# To remove duplicates
sentences_list = (OrderedDict.fromkeys(sentences_list))

# To store output
outfile = open(F_OUT, 'w')
outfile.write("".join(sentences_list).encode('utf-8'))
