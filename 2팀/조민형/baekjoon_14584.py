import sys

def change_letter(letter, change):
    letter_listed = list(letter)
    for i in range(len(letter_listed)) :
        if ord(letter_listed[i]) + change > 122:
            letter_listed[i] = chr((ord(letter_listed[i]) + change) % 122 + 96)
        else: letter_listed[i] = chr(ord(letter_listed[i])+ change)
    return ''.join(letter_listed)

cryptogram = sys.stdin.readline().rstrip('\n')
dict_count = int(sys.stdin.readline())


word_list =[]
for n in range(dict_count):
    word = sys.stdin.readline().rstrip("\n")
    word_list.append(word)

rotate_number = 0
success = False
while rotate_number<27:
    changed = change_letter(cryptogram,rotate_number)
    for m in word_list:
        if m in changed:
            print(change_letter(cryptogram, rotate_number))
            success=True
            break
    if success == True: break
    rotate_number+=1

    
    



