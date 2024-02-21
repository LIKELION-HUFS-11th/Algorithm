import sys

stringsToBuy, brand = map(int, sys.stdin.readline().split());

brandList = []
for i in range(brand):
    sixString, piece = map(int, sys.stdin.readline().split())
    brandList.append((sixString, piece))
    
result = 0

while stringsToBuy>0:
    packagePrice = min(brandList, key=lambda x: x[0])[0]
    piecePrice = min(brandList, key=lambda x: x[1])[1]
    if stringsToBuy >= 6:
        result += packagePrice
        stringsToBuy -= 6
    elif packagePrice < piecePrice * stringsToBuy:
        result += packagePrice
        stringsToBuy -= 6
    else:
        result += piecePrice
        stringsToBuy -= 1

print(result)