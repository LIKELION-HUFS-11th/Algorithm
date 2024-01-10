num = int(input(""))
member_list = []

j = 0
while j < num:
    member = input("")
    member_inf = member.split(" ")

    if len(member_list) == 0:
        member_list.append(member)
    else:
        i=0
        while i < len(member_list):
            mem_inf = member_list[i].split(" ")
            if i == len(member_list)-1:
                member_list.insert(i, member)
                break
            if int(member_inf[0]) <= int(mem_inf[0]):
                member_list.insert(i, member)
                break
            i+=1
    j+=1

print("\n".join(member_list))
    

        