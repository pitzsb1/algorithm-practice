def search(l, n):
    result = []
    for i in range(len(l)):
        if l[i] == n:
            result.append(i)
    return result

d = [1, 3, 5, 6, 6, 8]
print(search(d, 6))
