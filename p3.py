# Problem 3: Comprehensions
words = ["ai", "python", "data"]

print([n ** 2 for n in range(1, 11) if n % 2 == 0])
print({w: len(w) for w in words})
print(sorted({letter for letter in "banana"}))
