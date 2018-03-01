# Working with random and other iterator things

import random

ceiling = 50
index   = range(0, ceiling, 1) # 0, 1, 2, 3, 4... etc. up to 49

#print(index)

#iterator = {'index':index} # {'index': [1,2,3,4... etc.]}

iterator = {}

#print(iterator)

categories = ['Node0', 'Node1', 'Node3']

for category in categories:
    iterator[category] = [random.randint(1,100) for x in index] 
    #{'Node1': [87, 44, ... ], 'Node0': [23, 4, ... ]}
    
#print(iterator) 

