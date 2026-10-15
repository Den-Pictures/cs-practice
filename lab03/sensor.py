threshold = float(input())
kol = int(input())
values = []
maximum = -9999999999999
kerror = 0
k = 0
for i in range(kol):
    n = str(input())
    if n == 'error':
        kerror += 1
    else:
        n = float(n)
        values.append(n)
        if n > maximum:
            maximum = n
        if n > threshold:
            k += 1


