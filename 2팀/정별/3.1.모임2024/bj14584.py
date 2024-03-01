def main():
    cipher = input().strip()
    n = int(input().strip())
    s = [input().strip() for _ in range(n)]

    for i in range(26):
        temp = ""
        for char in cipher:
            temp += chr((ord(char) - ord('a') + i) % 26 + ord('a'))

        for word in s:
            if word in temp:
                print(temp)
                return

if __name__ == "__main__":
    main()
