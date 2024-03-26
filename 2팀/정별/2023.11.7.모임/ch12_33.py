
ic = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e','f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
inp = '23'

for i in range(len(inp)):
    elem = inp[i]
    for j in range(len(ic[elem])):
        ic[elem][j] + ic[inp[i+1]]

#elem은 각 숫자들임
def comb(elem):
    ic[elem]

for i in range(len(inp)):
    comb(ic[inp[i]])

