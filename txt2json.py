import re
import numpy as np

def has_another_line(file):
    cur_pos = file.tell()
    does_it = bool(file.readline())
    file.seek(cur_pos)
    return does_it

f = open("sample.txt", "r")
number_languages = 3

file = np.empty(number_languages, dtype=object) 

for i in range(number_languages):
    file[i] = open("language{value}.json".format(value = i), "w")
    file[i].write("{\n")

lines  = f.readlines()

pattern = r"\{(.*?)\}"

for i in range(0, len(lines)):    
  result = re.sub(r'\s+', '', lines[i]) 
  key = re.search(r'(.*?)\=', result)
  key = "\"" + key.group()[:-1] + "\""
  value = re.search(pattern, result)
  value = re.sub(pattern, r"\1", value.group())
  value = re.split(",",value)
  comma = "," if i < len(lines) - 1 else ""
  for i in range(number_languages):    
    file[i].write("    " + key + ":" + value[i] + comma +"\n")

for i in range(number_languages):    
    file[i].write("}\n")
    file[i].close()

f.close()