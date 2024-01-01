"""
Not a very efficient solution, and fails at large strings. An improved version is under development.
"""
import re
from itertools import product

def splitby2variation1(s):
  """
  si = []
  temp = s[0]
  
  for i in range(1, len(s)):
    if (s[i] == s[i - 1]) and (len(temp) < 2):
      temp += s[i]
    else:
      si.append(temp)
      temp = s[i]
    if (i == len(s) - 1):
      si.append(temp)
  return si
  """
  return [m.group(0) for m in re.finditer(r"(.)(?:\1)?", s)]

replaced = []
sinput = input()
for value in product([0, 1], repeat = sinput.count('?')):
    rs = sinput
    for v in value:
      rs = rs.replace('?', str(v), 1)
      replaced.append(rs)

final = []
for replacement in replaced:
  final.append(splitby2variation1(replacement).count('11') + splitby2variation1(replacement).count('00'))

print(max(final))
