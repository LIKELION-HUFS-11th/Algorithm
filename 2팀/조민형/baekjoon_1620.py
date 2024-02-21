import sys

pokemonCount, question = map(int, sys.stdin.readline().split())

pokemonDictForNum = {}
pokemonDictForStr = {}

for i in range(1, pokemonCount+1):
    pokemon = sys.stdin.readline().rstrip('\n')
    pokemonDictForNum[i] = pokemon
    pokemonDictForStr[pokemon] = i

result = []
for j in range(question):
    ques = sys.stdin.readline().rstrip('\n')
    if ord(ques[0]) >= 65 and ord(ques[0]) <= 122 :
        result.append(str(pokemonDictForStr[ques]))
    else:
        result.append(pokemonDictForNum[int(ques)])

print("\n".join(result))

