from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Johnson_algorithm import Johnson_algorithm
from Johnson_algorithm3 import Johnson_algorithm3
from NEH_Algorithm import NEH_Algorithm 

seed = 752
tasks = 5
machines = 3

str1 = "===================================================================\n"
print (str1 + "NATURAL PERMUTATION")
natural_permutation = Natural_permutation(seed, tasks, machines)
print(natural_permutation)

#print (str1 + "JOHNSON ALGORITHM")
#johnson3 = Johnson_algorithm3(seed, tasks, machines)
#print(johnson3)

print (str1 + "NEH ALGORITHM")
neh = NEH_Algorithm(seed, tasks, machines)
neh.DoNEH()
print(neh)

print (str1 + "NEH PLUS 4 ALGORITHM")
neh = NEH_Algorithm(seed, tasks, machines)
neh.DoNEHPlus4()
print(neh)

print (str1 + "NEH PLUS 1 ALGORITHM")
neh = NEH_Algorithm(seed, tasks, machines)
neh.DoNEHPlus1()
print(neh)







