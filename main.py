def optimize_script():
    """
    This is a basic Python script example
    """
    # Import the necessary libraries
    import time

    # Define a function to calculate the Fibonacci sequence
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_seq = [0, 1]
            for i in range(2, n):
                next_num = fib_seq[i-1] + fib_seq[i-2]
                fib_seq.append(next_num)
            return fib_seq

    # Get user input for the number of Fibonacci numbers
    count = int(input("Enter the number of Fibonacci numbers to generate: "))

    # Start the timer
    start_time = time.time()

    # Generate the Fibonacci sequence
    fib_numbers = fibonacci(count)
    print(fib_numbers)

    # Calculate and print the elapsed time
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time} seconds")


# Call the optimize_script() function to run the code
optimize_script()
