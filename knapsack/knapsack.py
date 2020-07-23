#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Greedy algorithm:
    # at each step take the item with the best value/size ratio
    # Passes small and medium tests.  Fails large test with just 1 item different

    # Precalculate ratios
    ratios = {}
    for item in items:
        ratios[item.index] = item.value / item.size
    
    # Get a list of item id's sorted by that ratio, descending
    item_order = sorted(ratios, key=ratios.get, reverse=True)
    
    taken_size = 0
    taken_value = 0
    bag = []
    for i in range(len(item_order)):
        # Get the item that has index iten_order[i]
        item = [item for item in items if item.index == item_order[i]][0]
        # If that item fits, add it to the bag
        if item.size + taken_size <= capacity:
            bag.append(item)
            taken_size += item.size
            taken_value += item.value
    
    # All items have been checked, return results
    chosen = [i.index for i in bag]
    chosen.sort()  # tests expect the chosen item id's to be sorted
    return {"Value": taken_value, 
            "Chosen": chosen}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
