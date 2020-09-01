import sys

sys.path.insert(0, 'WANNRelease\prettyNeatWann')
from matplotlib import pyplot as plt
from vis.viewInd import viewInd
import networkx as nx
import numpy as np

if __name__ == '__main__':
    # stats = np.loadtxt('log/test_stats.out', delimiter=',')
    # fig, ax = plt.subplots()
    # x = stats[:, 0]
    # y = stats[:, [1, 2, 3]]
    # plt.plot(y)
    # plt.legend(['Median Fitness', 'Max Fitness', 'Best Fitness'])
    # plt.xlabel('Evaluations')
    # plt.ylabel('Fitness')
    # plt.show()
    # fig, ax, G, in_and_out_dict = viewInd('WANNRelease/WANNTool/champions/swing.out',
    #                        'swingup')
    fig, ax, G, in_and_out_dict = viewInd('log/test_best.out',
                                          'swingup')
    # plt.savefig('laptop_swinger_best')
    # plt.show()
    # print(in_and_out_dict)
    x = nx.all_simple_paths(G, 0, 1)
    hist_dict = {}

    npArr = np.empty((0,))
    for i in range(15):
        hist_dict[i] = 0
    for inNode in range(in_and_out_dict['nIn']):  # in
        for outNode in range(in_and_out_dict['nNode'] - in_and_out_dict[
            'nOut'], in_and_out_dict['nNode']):  # out
            for path in nx.all_simple_paths(G, inNode, outNode):
                npArr = np.append(npArr, len(path))
                hist_dict[len(path)] += 1
    print('mean: ', np.mean(npArr))
    print('std: ', np.std(npArr))
    print('number of pathes: ', len(npArr))
    print('even path perc: ', np.sum(npArr % 2 == 0) / len(npArr))
    # print(hist_dict)
    plt.bar(list(hist_dict.keys()), hist_dict.values(), color='g')

    plt.xlabel('path length')
    plt.ylabel('number of paths')
    plt.title('Histogram of path length - activation function swing')
    # plt.savefig('histogram_path_length_activation_function_swing')
