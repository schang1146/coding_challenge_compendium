# Dynamic Programming

Dynamic Programming (DP) can be thought of as an optimization over plain recursion. The idea is to store the results of subproblems so that we do not have to recompute them later.

**Example:** Calculate the n<sup>th</sup> Fibonacci Number.

```python
def fib_recursive(n):
    """
    Time Complexity: O(n^2)
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
```

```python
def fib_dp(n):
    """
    Time Complexity: O(n)
    """
    if n == 1:
        return 1

    f = [0, 1]
    for _ in range(n - 1):
        f[1], f[0] = f[0] + f[1], f[1]
    return f[1]
```
