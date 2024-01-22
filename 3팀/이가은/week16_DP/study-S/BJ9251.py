word1 = list(input())
word2 = list(input())

length1 = len(word1)
length2 = len(word2)
grid = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(length1):
    for j in range(length2):
        if word1[i] == word2[j]:
            grid[i+1][j+1] = grid[i][j] + 1
        else:
            grid[i+1][j+1] = max(grid[i][j+1], grid[i+1][j])

print(grid[-1][-1])
        