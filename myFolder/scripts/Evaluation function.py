def evaluate(statement, values):
    # Define custom replacements for logical operators
    replacements = {
        'and': ' and ',
        'or': ' or ',
        'not': ' not ',
        'implies': ' <= ',  # Custom operator handling for implies
    }
    
    # Replace the propositions in the statement with their corresponding truth values
    for prop, val in values.items():
        statement = statement.replace(prop, str(val))
    
    # Replace logical operations with Python equivalents
    for key, value in replacements.items():
        statement = statement.replace(key, value)
    
    # Evaluate the modified statement using eval
    return eval(statement)


# Test statements and values
statements = [
    ("A and B", {"A": True, "B": False}),
    ("A or B", {"A": True, "B": False}),
    ("not A", {"A": True}),
    ("A implies B", {"A": True, "B": False})
]

# Demonstrate evaluation
results = {stmt: evaluate(stmt, vals) for stmt, vals in statements}
print(results)