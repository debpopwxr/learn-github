def generate_random_code(n):
    import random
    
    # Generate a random string of length n
    rand_str = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(n))
    
    # Return the generated code
    return rand_str
