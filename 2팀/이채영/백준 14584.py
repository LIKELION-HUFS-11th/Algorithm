
def encode(ord1_list, k):
    ord_list = ord1_list.copy() #문제

    for i in range(len(ord_list)):
        # ord_list[i] = ord_list[i] + k
        # if ord_list[i] > 122:
        #     ord_list[i] = 96 + (ord_list[i] - 122)
        
        ord_list[i] = ((ord_list[i] - 97 + k) % 26) + 97

        ord_list[i] = chr(ord_list[i])

    str = ''.join(ord_list) #type<str>

    return str


key = input() # srbv
ord_list = list(key) #['s','r','b','v']
for i in range(len(ord_list)):
    ord_list[i] = ord(ord_list[i]) #[65, 66, 67, 68]


n = int(input())

dict = []
for _ in range(n):
    dict.append(input())

# alphabets = "abcdefghijklmnopqrstuvwsyz"
# alphabets = list(alphabets)
    

satisfied = False
for i in range(26): #(1, 26) 말고 (0, 26)
    encoded_key = encode(ord_list, i)

    for elem in dict:
        if elem in encoded_key:
            satisfied = True
            break
    
    if satisfied:
        break

print(encoded_key)