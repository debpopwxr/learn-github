def generate_random_python_code():
    import random
    code = []
    for _ in range(10):
        line = []
        for _ in range(5):
            token = random.choice(['+', '-', '*', '/', '(', ')'])
            if token == '(':
                token += str(random.randint(2, 10))
            elif token == ')':
                token = str(random.randint(2, 10))
            line.append(token)
        code.append(line)
    return '\n'.join([' '.join(line) for line in code])
