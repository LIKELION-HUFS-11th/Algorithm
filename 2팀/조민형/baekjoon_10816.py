card = int(input())
card_list = sorted(list(map(int,input().split())))

card_count_plus = [0] * (card_list[-1]+1)
card_count_minus = [0] * (-(card_list[0])+1)

for i in range(card):
    if card_list[i] >= 0:
        card_count_plus[card_list[i]] +=1
    else:
        card_count_minus[-(card_list[i])] +=1

sg_card = int(input())
sg_cardList = list(map(int,input().split()))

result=[]
for j in range(sg_card):
    if sg_cardList[j] >= 0 and sg_cardList[j] <= card_list[-1]:    
        result.append(card_count_plus[sg_cardList[j]])
    elif sg_cardList[j] >= card_list[0] and sg_cardList[j] < 0:
        result.append(card_count_minus[-(sg_cardList[j])])
    else: result.append(0)

print(" ".join(map(str,result)))







    
    




# def binary_search(list, target):
#     end = -1
#     if len(list) == 1:
#         return
#     elif card_list[end] > target:
#         return binary_search(list[:len(list)//2], target)
#     elif card_list[end] < target: 
#         return binary_search(list[len(list)//2:], target)
#     elif card_list[end] == target:
#         count+=1
#         if card_list[end-1] == target:
#             return binary_search(end-1, target)
#         elif card_list[end+1] == target:
#             return binary_search(end+1, target)
#         else:
# #             return

# result=[]

# for card in sg_cardList:
#     count = 0
#     binary_search(sg_cardList,card)
#     result.append(count)

# print(result)


    



