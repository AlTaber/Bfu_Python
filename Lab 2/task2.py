s = input()
scores = {c : s.count(c) for c in set(s)}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for i in range(3): print(f"{sorted_scores[i][0]}: {sorted_scores[i][1]}")