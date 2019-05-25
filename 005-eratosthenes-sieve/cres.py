def eratosthenes(n):
    lst = [False, False] + [True] * (n-1)

    for i in range(int((n+1)**0.5) + 1):
        if lst[i]:
            for x in range(i, n//2+1):
                y = i * x
                if y <= n:               # len(lst) == n+1
                    lst[y] = False
    return [i for i in range(n+1) if lst[i]]

        
print(eratosthenes(1000))
