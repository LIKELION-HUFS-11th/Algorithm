import sys
input = sys.stdin.readline

trees = dict()
total = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    
    total += 1
    if trees.get(tree):
        trees[tree] += 1
    else:
        trees[tree] = 1

trees = sorted(trees.items())

for tr, amount in trees:
    print("{} {:.4f}".format(tr, round(amount/total*100, 4)))