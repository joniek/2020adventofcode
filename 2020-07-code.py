import os

folderpath = '/Users/joankhoo/Documents/GitHub/2020adventofcode'
filename = '2020-07-input.txt'


with open(os.path.join(folderpath,filename), 'r') as f:
    bags = f.read().split('.\n')

    bags_dict = {}
    for bag in bags:
        if bag != '':
            bag = bag.replace(" bags","").replace(" bag","") # remove "bags"
            bag = bag.split(" contain ")
            bag[1] = bag[1].split(", ")
            temp_dict = {}
            for innerbag in bag[1]:
                temp_dict[innerbag[2:]] = innerbag[:2]
            bags_dict[bag[0]] = temp_dict.copy()



#Part 1.

target = 'shiny gold'


def parent(target):
    tempArray = []
    for bag in bags_dict:
        if target in bags_dict[bag]:
            tempArray.append(bag)
    return tempArray
        

outerbag = set()
outerbag.update(parent(target))
print(outerbag)

