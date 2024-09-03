def Karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)),len(str(y)))
        half_n = n // 2
        a = x // 10 ** half_n
        b = x % 10 ** half_n
        c = y // 10 ** half_n
        d = y % 10 ** half_n
        ac = Karatsuba(a, c)
        bd = Karatsuba(b, d)
        ad_bc = Karatsuba(a + b, c + d) - ac - bd
        result = 10 ** (2*half_n) * ac + 10 ** half_n * ad_bc + bd
        return result
    
"""
    Karatsuba algorithm is a fast multiplication algorithm that multiplies two large integers efficiently using divide and conquer.

    Steps:
    1. If the numbers are small (e.g., less than a certain threshold), use the standard multiplication method.
    2. Otherwise, split each number into two halves and recursively compute three products:
        - A = high bits of x * high bits of y
        - B = low bits of x * low bits of y
        - C = (high bits of x + low bits of x) * (high bits of y + low bits of y)
    3. Combine the results using the Karatsuba formula:
        - result = A * 10^(2*m) + (C - A - B) * 10^m + B

    Time Complexity:
    - O(n^log2(3)), where n is the number of digits in the input integers.

    Space Complexity:
    - O(n), due to the recursive calls and intermediate arrays.

    The algorithm is particularly efficient for very large numbers.
    """