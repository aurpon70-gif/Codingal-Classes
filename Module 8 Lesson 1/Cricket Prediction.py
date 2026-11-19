import numpy as np

print("=" * 55)
print("       India vs Australia Cricket Match Prediction")
print("=" * 55)

india_score = np.array([287, 312, 198, 345, 267, 389, 223, 301, 278, 334])
australia_score = np.array([265, 334, 201, 298, 289, 367, 245, 278, 301, 312])
match_labels = [f"Match {i + 1}" for i in range(1, 11)]

print("\nScores")
print(f"{'Match':<10}{'India':>8}{'Australia':>12} {'Winner':>12}")
for i in range(10):
    winner = "India" if india_score[i] > australia_score[i] else "Australia" if australia_score[i] > india_score[i] else "Tie"
    print(f"{match_labels[i]:<10}{india_score[i]:>8}{australia_score[i]:>12} {winner:>12}")

print("\n India Statistics")
print("-" * 35)
print(f"  Average Score: {np.mean(india_score):.1f}")
print(f"  Highest Score: {np.max(india_score)}")
print(f"  Lowest Score: {np.min(india_score)}")

india_top3_scores = np.sort(india_score)[::-1][:3]
india_top3_idx = np.argsort(india_score)[::-1][:3]
print(f"  Top 3 Scores: {india_top3_scores}")

print("\n Australia Statistics")
print("-" * 35)
print(f" Average Score: {np.mean(australia_score):.1f}")
print(f" Highest Score: {np.max(australia_score)}")
print(f" Lowest Score: {np.min(australia_score)}")
print(f" std deviation: {np.std(australia_score):.2f}")
print(f" total runs: {np.sum(australia_score)}")

print("\n Head to Head Statistics")
print("-" * 35)
diff = india_score - australia_score
india_wins = np.sum(diff > 0)
australia_wins = np.sum(diff < 0)
ties = np.sum(diff == 0)
print(f" India Wins: {india_wins}")
print(f" Australia Wins: {australia_wins}")
print(f" Ties: {ties}")

threshold = 300
print(f"\n Matches where India scored above {threshold}: {np.sum(india_score > threshold)}")
print(f" Matches where Australia scored above {threshold}: {np.sum(australia_score > threshold)}")
print("-" * 35)

print("\n + ""=" * 50)
if india_wins > australia_wins:
    print(" Overall Winner: India")
elif australia_wins > india_wins:
    print(" Overall Winner: Australia")
else:
    print(" Overall Result: Tie")
print("=" * 55)

print("\n challenge")
print("Can you find the average winning margin for india wins, how many matches had scores within 20 runs, and india score in the top 50th percentile? ")