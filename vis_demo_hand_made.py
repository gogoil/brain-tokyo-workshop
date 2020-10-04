import sys

# sys.path.insert(0, 'WANNRelease\prettyNeatWann')
from matplotlib import pyplot as plt
from WANNRelease.prettyNeatWann.vis.viewInd import viewInd
import networkx as nx
import numpy as np
import os

def graph_layers_BFS_dict(G, in_and_out_dict):
    seen = {}
    layer = 0
    for i in range(in_and_out_dict['nIn']):
        seen[i] = layer
    while len(seen) != in_and_out_dict['nNode']:
        for node in list(seen):
            if seen[node] == layer:
                for n in G.neighbors(node):
                    if n not in seen:
                        seen[n] = layer + 1
        layer += 1
    return seen


def plot_BFS_dict(bfs_dict, nNode):
    arr = np.zeros(10)
    for key in bfs_dict:
        arr[bfs_dict[key]] += 1
    print(arr)
    plt.bar(np.arange(10), arr)

    plt.xlabel('layer number')
    plt.ylabel('number of nodes')
    plt.title('Histogram of layers')
    plt.text(6,9, 'number of nodes is {}'.format(nNode))
    print(os.path.dirname(os.path.abspath(__file__)))
    plt.savefig('swing_pos_weights_and_act_histo_of_layers.png')
    plt.show()


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
    # fig, ax, G, in_and_out_dict = viewInd('swing_act_function/test_best.out',
    #                        'swingup')
    fig, ax, G, in_and_out_dict = viewInd(
        '../../WANNRelease/WANN/log/test_best.out',
        'swingup')
    # plt.savefig('laptop_swinger_best')
    plt.show()

    bfs_dict = graph_layers_BFS_dict(G, in_and_out_dict)
    plot_BFS_dict(bfs_dict, in_and_out_dict['nNode'])

    # print(in_and_out_dict)
    x = nx.all_simple_paths(G, 0, 1)
    hist_dict = {}

    npArr = np.empty((0,))
    for i in range(35):
        hist_dict[i] = 0

    # for node in G.nodes:
    #     hist_dict[G.degree(node)] += 1

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
    print(hist_dict)

    plt.bar(list(hist_dict.keys()), hist_dict.values(), color='g')

    plt.xlabel('path length')
    plt.ylabel('number of paths')
    plt.title('Histogram of path length - activation function swing')
    # plt.xlabel('node degree')
    # plt.ylabel('number of nodes')
    # plt.title('Histogram of node degree - biped pos\' weights')
    # plt.savefig('histogram_path_length_activation_function_swing')
    plt.show()
