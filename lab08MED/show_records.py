from snake import get_scores

scores = get_scores()
print("\n=== TOP RECORDS ===")
if not scores:
    print("No records yet")
else:
    for i, s in enumerate(scores[:10], 1):
        print(f"{i}. Score: {s[0]}  |  {str(s[1])[:19]}")
print("===================\n")