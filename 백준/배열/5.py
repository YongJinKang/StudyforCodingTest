import sys

input = sys.stdin.readline

n = int(input())

scores = list(map(int,input().split()))

max_score = max(scores)

new_scores = []
for i in scores:
    i = (i/max_score)*100
    new_scores.append(i)

print(sum(new_scores)/len(new_scores))
