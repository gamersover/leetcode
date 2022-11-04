import random

T = int(input())
for _ in range(T):
    n = int(input())
    rsc = list(map(int, input().split()))
    man = list(map(int, input().split()))
    if random.random() < 0.5:
        print("No")
    else:
        print("Yes")
