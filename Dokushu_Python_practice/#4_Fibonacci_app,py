from functools import lru_cache


@lru_cache(maxsize=2)
def fibonacci_number(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)


# Example usage:
n = 40
print(f"Fibonacci number at position {n}: {fibonacci_number(n)}")