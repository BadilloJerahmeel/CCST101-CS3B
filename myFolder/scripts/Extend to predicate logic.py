def forall(predicate, domain):
    """
    Evaluate whether the predicate holds for all elements in the domain.
    :param predicate: A function that takes one argument and returns a boolean.
    :param domain: An iterable representing the domain of discourse.
    :return: True if the predicate is true for all elements, False otherwise.
    """
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """
    Evaluate whether the predicate holds for at least one element in the domain.
    :param predicate: A function that takes one argument and returns a boolean.
    :param domain: An iterable representing the domain of discourse.
    :return: True if the predicate is true for at least one element, False otherwise.
    """
    return any(predicate(x) for x in domain)


# Define a predicate function
def is_even(x):
    return x % 2 == 0

# Define a domain
numbers = [2, 4, 6, 8]

# Evaluate using the forall function
all_even = forall(is_even, numbers)
print(f"All numbers are even: {all_even}")  # Output: True

# Define another domain with at least one odd number
mixed_numbers = [1, 2, 3, 4]

# Evaluate using the exists function
any_even = exists(is_even, mixed_numbers)
print(f"At least one number is even: {any_even}")  # Output: True

# Check with a domain that has no even numbers
odd_numbers = [1, 3, 5, 7]
all_even_odd = forall(is_even, odd_numbers)
print(f"All numbers are even: {all_even_odd}")  # Output: False