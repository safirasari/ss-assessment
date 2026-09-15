# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    # TODO: Write your logic here

    count_categories = {}

    for category in categories:
        count_categories[category] = count_categories.get(category, 0) + 1

    return count_categories


    pass

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))