def sort_key(a: list):
    return a.split()[1], a.split()[0]


list = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

let_log, num_log = [], []

for i in list:
    if i.split()[1].isdigit():
        num_log.append(i)
    else:
        let_log.append(i)

let_log.sort(key=sort_key)

print(let_log + num_log)
