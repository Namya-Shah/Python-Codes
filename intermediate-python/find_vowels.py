a_string = input("Enter String: ")
lowercase = a_string.lower()

vowel_counts = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count

counts = vowel_counts.values()
total_vowels = sum(counts)
print("total vowels in string ", total_vowels)