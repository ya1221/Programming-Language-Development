#Part B
from functools import reduce

#Question 1
# Lambda function to generate Fibonacci sequence
fibonacci = lambda n: reduce(lambda seq, _: seq + [seq[-1] + seq[-2]], range(n - 2), [0, 1])[:n]

#Question 2
concat_strings = lambda strings: reduce(lambda x, y: f'{x} {y}', strings)

#Question 3
def cumulative_sum_of_squares(lists):
    return list(map(
        lambda sublist: reduce(
            lambda acc, x: acc + (lambda y: y ** 2)(x),
            filter(lambda x: (lambda z: z % 2 == 0)(x),sublist),0),lists))

#Question 4
def reduce_operation(binary_op):
    """
    Returns a function that applies the binary operation cumulatively
    to a sequence.

    :param binary_op: A lambda function representing a binary operation.
    :return: A function that applies binary_op cumulatively to a sequence.
    """
    return lambda sequence: reduce(binary_op, sequence)

def factorial(n):
    """
    Computes the factorial of a number using reduce_operation.

    :param n: The number to compute the factorial of.
    :return: The factorial of the number n.
    """
    # Define the binary operation for factorial: multiplication
    factorial_op = reduce_operation(lambda x, y: x * y)

    # Apply the operation cumulatively to the sequence 1 to n
    return factorial_op(range(1, n + 1))

def exponentiation(base, exp):
    """
    Computes base raised to the power of exp using reduce_operation.

    :param base: The base number.
    :param exp: The exponent.
    :return: base raised to the power of exp.
    """
    # Define the binary operation for exponentiation: repeated multiplication
    exponentiation_op = reduce_operation(lambda x, y: x * y)

    # Apply the operation cumulatively to the sequence [base] repeated exp times
    return exponentiation_op([base] * exp)

# Question 6
palindrome_counts = lambda lst: list(map(lambda sublist: len(list(filter(lambda s: s == s[::-1], sublist))), lst))

# Question 7
'''Lazy evaluation refers to the technique of delaying the evaluation of an expression until its value is actually
 needed. This can be particularly useful for optimizing performance and memory usage, especially when dealing with 
 large datasets or computationally expensive operations.

Eager Evaluation:
    Process -
        generate_values() is called, and the values are generated all at once and stored in the list values.
        The list comprehension [square(x) for x in values] squares each value in values immediately.
    Output -
        When list(generate_values()) is executed, you see "Generating values..." printed once, and then the values 1, 2, and 3 are generated.
        Then, for each value, the message "Squaring X" is printed, followed by the squared result.

Lazy Evaluation:
    Process -
        The list comprehension [square(x) for x in generate_values()] is applied directly on the generator returned by generate_values().
        Instead of generating all values upfront, generate_values() yields one value at a time as it is needed for squaring.
    Output -
        "Generating values..." is printed, but the values are not generated all at once.
        As each value is needed for squaring, it's generated and squared one by one. So, for each value, you see "Squaring X" immediately after it's generated.

Key Differences:
    Eager Evaluation - All values are generated first, stored in memory, and then processed (squared). This can be more memory-intensive because the entire list is kept in memory.
    Lazy Evaluation - Values are generated and processed one by one, as they are needed. This approach is more memory-efficient, especially when dealing with large or infinite sequences, as it doesn't store all values in memory at once.

Benefits of Lazy Evaluation:
    Memory Efficiency - Only the values that are actually needed are computed and stored, reducing memory usage.
    Performance Optimization - Computations are deferred until necessary, potentially avoiding unnecessary calculations if some values are never used.
    Handling Infinite Sequences - Lazy evaluation allows working with infinite sequences, as only the needed portion of the sequence is generated.

In this program, the difference in behavior between eager and lazy evaluation is highlighted by when the 
"Generating values..." and "Squaring X" messages are printed, demonstrating how lazy evaluation defers computations 
until absolutely necessary.'''

# Question 8
def primes_descending(lst):
    return sorted([x for x in lst if (lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)))(x)], reverse=True)

def print_menu():
    print("Menu:\n0 - Exit\n1 - Question 1\n2 - Question 2\n3 - Question 3\n4 - Question 4\n5 - Question 5\n6 - "
          "Question 6\n8 - Question 8")



def handle_choice(choice):
    if choice == '0':
        print("Exiting the program. Goodbye!")
    elif choice == '1':
        print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    elif choice == '2':
        print(concat_strings(["Hello", "world,", "this", "is", "sentence"])) # Output: "Hello world this is sentence"
    elif choice == '3':
        print(cumulative_sum_of_squares([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [4, 52, 64]
    elif choice == '4':
        print(factorial(5)),  # Test factorial function - Output: 120 (5! = 120)
        print(exponentiation(2, 3))  # Test exponentiation function - Output: 8 (2^3 = 8)
    elif choice == '5':
        print(reduce(lambda acc, x: acc + x, map(lambda x: x ** 2, filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6]))))
    elif choice == '6':
        print(palindrome_counts(
            [["madam", "apple", "racecar"], ["hello", "level"], ["not", "a", "palindrome"]])),  # Output: [2, 1, 1]
    elif choice == '8':
        print(primes_descending([1, 10, 23, 5, 8, 7, 11, 4])),  # Output: [23, 11, 7, 5]
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    choice = None
    while choice != '0':
        print_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)


if __name__ == "__main__":
    main()