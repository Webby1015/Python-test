n = int(input())
ch = input().split()
k = int(input())


from itertools import combinations

contain = 0
total = 0

for i in combinations(ch, k):
    if "a" in i:
        contain += 1
    total += 1
print(contain/total)
