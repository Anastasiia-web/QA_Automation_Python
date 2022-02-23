def buble_sort(l):
    t = l.copy()
    for n in range(0, len(t)):
        for i in range(len(t) - n):
            if t[i] <= t[n]:
                t[i], t[n] = t[n], t[i]
    return t

nums = [4, 1, 6, 3, 2, 7, 8]
sorted = buble_sort(nums)
print(sorted)  #  [1, 2, 3, 8, 4, 6, 7]
