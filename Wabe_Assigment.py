def smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return None

    for i in range(2, n + 1):
        if n % i == 0:
            return i

# Get user input
user_input = int(input("Enter an integer >=2: "))

# Find the smallest factor
factor = smallest_factor(user_input)

# Display the result
if factor is not None:
    print(f"The smallest factor other than 1 for {user_input} is {factor}.")
