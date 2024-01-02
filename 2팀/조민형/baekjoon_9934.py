k = int(input(""))
inorder = input("").split(" ")

node_count = len(inorder)
tree = [None] * node_count

def make_tree(trees,index):
    if len(trees) == 1 :
        tree[index] = inorder[index]
        return
    center = len(trees)//2 + 1
    tree[center] = inorder[center]
    
    left = center * 2
    right = left + 1

    tree[left] = make_tree(tree[1:left], left)
    tree[right] = make_tree(tree[right:], right)

tree_maked = make_tree(inorder,len(inorder))



# 중위순회 결과로 트리 만들기

