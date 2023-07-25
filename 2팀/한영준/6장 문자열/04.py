input_para = input()
para = "".join(x.lower() for x in input_para if x not in ",.")
banned = input()
banned_arr = []
banned_arr.append(banned)

para = list(para.split())
para = [para[i] for i in range(len(para)) if para[i] not in banned_arr]

cnt_arr = []
cnt_arr = [para.count(para[i]) for i in range(len(para))]
print(para[cnt_arr.index(max(cnt_arr))])
