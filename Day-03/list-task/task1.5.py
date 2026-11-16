name_marks=[("Ritik,", 25), ("Aman", 30), ("Ritik", 25), ("Aman", 30)]

top_scorer_first=sorted(name_marks, key=lambda item: item[1], reverse=True)

print("Sorted list of tuples based on marks:",top_scorer_first)
print("Top scorer (first occurrence):", top_scorer_first[0])