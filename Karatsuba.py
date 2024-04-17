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