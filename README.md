# multithreaded-model-checker
a model checker for my multithreaded algorithm

This model checker checks for correctness of my multithreaded virtual critical section algorithm found in the code of my [Main.java multiversion-concurrency-control repository](https://github.com/samsquire/multiversion-concurrency-control).

Run `python3 main.py` to run the simulation. The simulator shall execute variations of the interleavings of two random threads out of 5 threads and see if the critical section is upheld.

# example

Two threads both run at exact same time in perfect synchronization. Thread 2 detects that the critical section is not free. (`fsctf4`)

```
1:  c1      c1                                                                                                                                                                               
2:  ci4     ci1                                                                                                                                                                              
3:  c2f     c2f                                                                                                                                                                              
4:  ctf0    ctf0                                                                                                                                                                             
5:  ctf1    ctf1                                                                                                                                                                             
6:  ctf2    ctf2                                                                                                                                                                             
7:  ctf3    ctf3                                                                                                                                                                             
8:  ctf4    fctf4                                                                                                                                                                            
9:  c2b     c2b                                                                                                                                                                              
10:  ctb4   fsctb4                                                                                                                                                                           
11:  ctb3   fsctb3                                                                                                                                                                           
12:  ctb2   fsctb2                                                                                                                                                                           
13:  ctb1   fsctb1                                                                                                                                                                           
14:  ctb0   fsctb0                                                                                                                                                                           
15:  cs     fscs                                                                                                                                                                             
16:  ce     ce    
```

Thread 2 runs while the critical section of Thread 1 is running. The critical section is not available, so Thread 2 fails to indicate it wants the critical section.
```
0:  c1      c1                                                                                                                                                                               
1:  ci2                                                                                                                                                                                      
2:  c2f                                                                                                                                                                                      
3:  ctf0                                                                                                                                                                                     
4:  ctf1                                                                                                                                                                                     
5:  ctf2                                                                                                                                                                                     
6:  ctf3                                                                                                                                                                                     
7:  ctf4                                                                                                                                                                                     
8:  c2b                                                                                                                                                                                      
9:  ctb4                                                                                                                                                                                     
10:  ctb3                                                                                                                                                                                    
11:  ctb2                                                                                                                                                                                    
12:  ctb1                                                                                                                                                                                    
13:  ctb0                                                                                                                                                                                    
14:  cs     fci1                                                                                                                                                                             
15:  ce     c2f                                                                                                                                                                              
16:         ctf0                                                                                                                                                                             
17:         ctf1                                                                                                                                                                             
18:         fctf2                                                                                                                                                                            
19:         fsctf3                                                                                                                                                                           
20:         fsctf4                                                                                                                                                                           
21:         c2b                                                                                                                                                                              
22:         fsctb4                                                                                                                                                                           
23:         fsctb3                                                                                                                                                                           
24:         fsctb2                                                                                                                                                                           
25:         fsctb1                                                                                                                                                                           
26:         fsctb0                                                                                                                                                                           
27:         fscs                                                                                                                                                                             
28:         ce   
```

# keywords





