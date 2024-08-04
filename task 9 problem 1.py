from collections import Counter
s = input("Enter string   ")
def min_removals_to_equal_frequency(s: str) -> int:
    char_count = Counter(s)
    frequencies = list(char_count.values())
    frequencies.sort()
    min_removals = float('inf')
    for i in range(len(frequencies)):
        target_freq = frequencies[i]
        removals = sum(f - target_freq for f in frequencies if f > target_freq)
        min_removals = min(min_removals, removals)    
    return min_removals
print(min_removals_to_equal_frequency(s))
