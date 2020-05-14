# Random Sigil Grid Generator

import numpy as np

sigilValues = [1,2,3,4,5,6,7,8,9]

sigilLetters = ['A','B','C','D','E','F','G','H','I',
                'J','K','L','M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z','*']

sigilTable0 = np.random.choice(sigilValues, 9, False)
sigilTable1 = np.random.choice(sigilLetters, (3,9), False)
print('Randomized Sigil Table:\n{0}\n{1}'.format(sigilTable0,sigilTable1))

sigilGrid = np.random.choice(sigilValues, (3,3), False)
print('Randomized Sigil Grid:\n{0}'.format(sigilGrid))
