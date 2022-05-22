s = input()

print(''.join(map(lambda cycle: cycle[-1], sorted([s[i:] + s[:i] for i in range(len(s))]))))