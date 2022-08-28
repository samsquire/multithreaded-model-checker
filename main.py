import re
from itertools import product, zip_longest
a = ["c1", "ci", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"]
b = ["c1", "ci", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"]
position = 0
skips = [0, 0, 0]

interleavings_len = len(a) * len(b) + 240
print(interleavings_len)
print(len(a))
a_start = 0

middle = len(a) + 1
b_start = 0
interleavings_a = [None] * interleavings_len
interleavings_b = [None] * interleavings_len

# for index in range(middle, middle + len(b)):
#   interleavings_b[middle + (b_start * 2)]  = b[b_start]
#   b_start = b_start + 1
                                                                                                                                                                                             
# print(interleavings_b)                                                                                                                                                                     

def execute_interleavings(a, b):
  state = [False] * 6
  fail = [0, 0]
  safe = [True] * 5
  did = [False, False]
  index = 0
  skip = 0
  threads = [0] * 2
  for row_a, row_b in zip_longest(a, b):
    output_a = ""
    output_b = ""
    if row_a:
      output_a = row_a
    if row_b:
      output_b = row_b
    if not row_a and not row_b:
      
      skip = skip + 1
      if skip > 3 and not row_a and not row_b:
        index = index + 1
        continue
    if (not row_a and row_b) or (row_a and not row_b) or (row_a and row_b):
      skip = 0
    
    if row_a and "ci" in row_a:
      thread = int(re.findall("(\d+)", row_a)[0])
      threads[0] = thread
 
      if safe[0]:
        state[thread] = thread
        safe[1] = False
      else:
        output_a = "{}{}".format("fci", thread)

    elif row_b and "ci" in row_b:
      thread = int(re.findall("(\d+)", row_b)[0])
      threads[1] = thread
      if safe[1]:
        state[thread] = thread
        safe[0] = False
      else:
        output_b = "{}{}".format("fci", thread)
 
      
    if row_a and "ctf" in row_a:
      thread = int(re.findall("(\d+)", row_a)[0])
      if not fail[0]: 
          if state[thread] and state[thread] != threads[0]:
            fail[0] = True
            output_a = "{}{}".format("fctf", thread)
      else:
        output_a = "{}{}".format("fsctf", thread)
        fail[0] = True

    if row_b and "ctf" in row_b:
      thread = int(re.findall("(\d+)", row_b)[0])
      if not fail[1]: 
          if state[thread] and state[thread] != threads[1]:
            fail[1] = True
            output_b = "{}{}".format("fctf", thread)
      else:
        output_b = "{}{}".format("fsctf", thread)
        fail[1] = True

    if row_a and "ctb" in row_a:
      thread = int(re.findall("(\d+)", row_a)[0])
      if not fail[0]: 
          if state[thread] and state[thread] != threads[0]:
            fail[0] = True
            output_a = "{}{}".format("fctb", thread)
      else:
        output_a = "{}{}".format("fsctb", thread)
        fail[0] = True

    if row_b and "ctb" in row_b:
      thread = int(re.findall("(\d+)", row_b)[0])
      if not fail[1]: 
          if state[thread] and state[thread] != threads[1]:
            fail[1] = True
            output_b = "{}{}".format("fctb", thread)
      else:
          output_b = "{}{}".format("fsctb", thread)
          fail[1] = True
        
    if row_a == "cs":
      if not fail[0]:
        did[0] = True
      else:
        output_a = "fscs" # fail skip critical section
    if row_b == "cs":
      if not fail[1]:
        did[1] = True
      else:
        output_b = "fscs"

    if row_a == "ce":
      safe[1] = True
      state[0] = False
      fail[0] = False
    if row_b == "ce":
      safe[0] = True
      state[1] = False
      fail[1] = False
      
    
    print("{}:  {:<6}\t{:<6}".format(index, output_a, output_b))
    assert (not did[0] and not did[1] or (did[0] and not did[1] or not did[0] and did[1]) or did[0] and did[1] and not fail[0] and not fail[1])
    index = index + 1

def print_interleavings(a, b):
  print("###### CASE")
  index = 0 
  for row_a, row_b in zip(a, b):
    output_a = " "
    output_b = " "
    if row_a:
      output_a = row_a
    if row_b:
      output_b = row_b
    print("{}:  {}  {}".format(index, output_a, output_b))
    index = index + 1

def simulate():
    inters = [interleavings_a, interleavings_b]
    items = [a, b]
    rotate = 0

    generated = [False, False]
    priority = 0
    for i in range(0, 4):
      for leaving in range(0, len(inters)):
        for thread in range(0, 5): 
          differences = [0] * len(items[leaving])
      
          for difference_sums in product(range(0, 2, 1), repeat=len(items[leaving])):
            if rotate == 0:
                difference_sums = list(reversed(difference_sums))
            rotate = (rotate + 1) % 2
            inters[leaving] = [None] * interleavings_len
            
            last_index = 0
            difference_sum = 0
            
            for item in range(len(items[leaving])):
              difference_sum = difference_sum + difference_sums[item] + 1
              
              
              next_index = difference_sum
              
              
              # print(next_index)
          
              candidate = items[leaving][item] 
              if candidate == "ci":
                candidate = "{}{}".format(candidate, thread)
              inters[leaving][next_index] = candidate
      
        
        
        
            if not generated[0] or not generated[1]:
                generated[leaving] = True
                break
          
        
            if generated[0] and generated[1]:
                if priority == 0:    
                  execute_interleavings(inters[0], inters[1])
                if priority == 1:
                  execute_interleavings(inters[1], inters[0])
            priority = (priority + 1) % 2

execute_interleavings(
["c1", "ci2", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"],
["c1", None, None,  None,   None,    None,   None,   None,  None,   None,   None,   None,   None,   None, "ci1", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"])
execute_interleavings(
["c1", "ci2", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"],
["c1", None, None,  None,   None,    None,   None,   None,  "ci1", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"])
execute_interleavings(
["c1", "ci2", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"],
["c1", None, None,  None,   None,    None,   None,   None,    None,  None,   None,   None,   None,   None,  None,  None, "ci1", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"])
execute_interleavings(
["c1", "ci2", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"],
["c1", None, None,  None,   None,    None,   None,   None,    None,  None,   None,   None,   None,   None,  None, "ci1", "c2f", "ctf0", "ctf1", "ctf2", "ctf3", "ctf4", "c2b", "ctb4", "ctb3", "ctb2", "ctb1", "ctb0", "cs", "ce"])
simulate()
