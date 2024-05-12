
counts = {}
s = "BhavinBhatia"

for i in range(len(s)):
    if s[i] in counts:

        counts[s[i]] += 1
    else:
        counts[s[i]] = 1

print(counts)


