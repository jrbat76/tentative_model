import numpy as np
import random
from collections import Counter
from itertools import permutations, combinations
import itertools
import operator
import matplotlib.pyplot as plt 

# Available resource for the Initiator
choice = [1, 2, 3, 4, 5]

# This method returns a list that contains combinations of elements from the choice
def createPermu(iterable):
	l1 = []
	for i in range(1, len(iterable) + 1):
		for j in itertools.permutations(iterable, i):
			l1.append(j)
	return l1

# The method accepts iterable and number of trials as parameter and returns a list 
def createRandomTrials(iterable, num_trials):
	# import random
	picked = []
	trials = num_trials
	for i in range(1, trials):
		a = random.choice(iterable)
		picked.append(a)
	return picked

# returns sum of the all values in dictionary
def getSum(dict):
	sum = 0
	coun = 0

	for keys, values in dict.items():
		sum += values
		coun += 1
	return sum

# returns weighted probability values
def getWeighted(dict, sum):
	weighted = {}
	for keys, values in dict.items():
	    a = round(values / sum, 4)
	    weighted[keys] = weighted.get(keys, a)

	return weighted

pool = createPermu(choice)
# for ind, i in enumerate(pool):
# 	print(ind+1, i)
afterTrial = createRandomTrials(pool, 10000)
afterTrialCountered = Counter(afterTrial)

#print(afterTrialCountered)

sum1 = getSum(afterTrialCountered)
#print(sum1)

afterWeighted = getWeighted(afterTrialCountered, sum1)

sorted_d = dict(sorted(afterWeighted.items(), key=operator.itemgetter(1), reverse=True))
#for k1, v1 in sorted_d.items():
#    print(k1, v1)

# plt.hist(list(sorted_d.values()), 50)
# plt.show()

taken = []
for i in sorted_d.values():
	taken.append(i)

print('mean:', np.mean(taken))

print('std: ', np.std(taken))

print('var: ', np.var(taken))

