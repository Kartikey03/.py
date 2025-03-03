from collections import Counter

my_set = {"apple", "banana", "orange", "banana", "apple", "grape"}

# Count occurrences of each element (string)
element_count = Counter(my_set)

distinct_count = len(element_count)
same_elements = [element for element, count in element_count.items() if count > 1]

print("Number of distinct elements:", distinct_count)
print("Same elements:", same_elements)
