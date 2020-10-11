# -- View stats of a completed run
# Rows:
# 0 - Fitness evaluations used
# 1 - Median fitness of population
# 2 - Max fitness of population
# 3 - Top fitness every achieved
# 4 - Median number of nodes of individuals in population
# 5 - Median number of connections of individuals in population
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    stats = np.loadtxt('demo_test_stats.out', delimiter=',')
    fig, ax = plt.subplots()
    x = stats[:,0]
    y = stats[:,[1,2,3]]
    plt.plot(y)
    plt.legend(['Median Fitness','Max Fitness','Best Fitness'])
    plt.xlabel('Evaluations')
    plt.ylabel('Fitness')
    plt.savefig('swing_test_stats_T20')