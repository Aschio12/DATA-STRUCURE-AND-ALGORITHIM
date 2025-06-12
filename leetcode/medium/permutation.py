from itertools import permutations
n=[1,2,3]
a=list(permutations(n))
a=[list(i) for i in a]
print(a)


"""
def generate_permutations(nums):
    # Base case: empty list has only one permutation - itself
    if len(nums) == 0:
        return [[]]
    
    result = []
    for i in range(len(nums)):
        # Select current element
        current = nums[i]
        
        # Create new list without current element
        remaining = nums[:i] + nums[i+1:]
        
        # Recursively generate permutations of remaining elements
        for perm in generate_permutations(remaining):
            # Prepend current element to each permutation
            result.append([current] + perm)
            
    return result

# Example usage
numbers = [1, 2, 3]
print(generate_permutations(numbers))
"""