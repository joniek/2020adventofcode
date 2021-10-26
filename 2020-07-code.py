import os

# folderpath = '/Users/joankhoo/Documents/GitHub/2020adventofcode'
folderpath = '/Users/socialgen/Documents/GitHub/2020adventofcode'
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


# Part 2: Find the number of bags a shiny gold bag can hold.
# Wrong answers: 138 too low.

target = ['shiny gold']
newTarget = []
parent_child_qty = []
parents = set(['shiny gold'])


def getChildren(parent):
    return bags_dict.get(parent)


print(getChildren(target[0]))




# while len(target) > 0:

#     for t in target:
#         new_dict = bags_dict.get(t)
#         print(t)
#         print(new_dict)

#         for n in new_dict:
#             if new_dict[n] != 'no':
#                 parent_child_qty.append([t,n,int(new_dict[n])])
#                 newTarget.append(n)
#                 parents.add(n)
#             else:
#                 parent_child_qty.append([t,n,1])

#     target = newTarget
#     newTarget = []
#     print(len(target))

    

