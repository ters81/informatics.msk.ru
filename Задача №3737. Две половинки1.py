n = input()
print(n[((len(n) // 2) + len(n) % 2):] + n[:((len(n) // 2) + len(n) % 2)])
