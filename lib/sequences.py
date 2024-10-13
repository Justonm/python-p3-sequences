def print_fibonacci(length):
    if length <= 0:
        print([])  
        return
    
    fib_sequence = [0, 1]
    
    for i in range(2, length):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    if length == 1:
        fib_sequence = [0]
    
    print(fib_sequence)

print_fibonacci(8)
