from random import randint
from time import perf_counter
import sys
import resource


def merge(arr1, arr2):
    i = 0
    j = 0

    ret = []
    count = 0

    while i < len(arr1) and j < len(arr2):
        count += 1
        if arr1[i] < arr2[j]:
            ret.append(arr1[i])
            i += 1
        else:
            ret.append(arr2[j])
            j += 1

    ret.extend(arr1[i:])
    ret.extend(arr2[j:])

    return ret, count


def mergesort(arr):
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2

    left, c1 = mergesort(arr[:mid])
    right, c2 = mergesort(arr[mid:])
    merged, c3 = merge(left, right)

    return merged, c1 + c2 + c3


def insertionsort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            count += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key

    return arr, count


def hybridsort(arr, s):
    if len(arr) <= s:
        return insertionsort(arr)
    else:
        mid = len(arr) // 2
        left, c1 = hybridsort(arr[:mid], s)
        right, c2 = hybridsort(arr[mid:], s)
        merged, c3 = merge(left, right)
        return merged, c1 + c2 + c3


f1 = open("merge.csv", "a")
f2 = open("hybrid.csv", "a")

sys.setrecursionlimit(10**7)

x = 100000

i = 1000

while i <= 10**7:
    arr = [randint(1, x) for j in range(i)]
    t_start = perf_counter()
    sorted_arr, comparisons = mergesort(arr)
    t_end = perf_counter()
    t_merge = t_end - t_start
    f1.write(f"{i}, {t_merge}, {comparisons}\n")
    print(f"Mergesort done for {i} nums")

    k = 1
    while k < 10:
        s = 2**k
        t_start = perf_counter()
        sorted_arr, comparisons = hybridsort(arr, s)
        t_end = perf_counter()
        t_hybrid = t_end - t_start
        f2.write(f"{i}, {s}, {t_hybrid}, {comparisons}\n")
        print(f"Hybridsort done for {i} nums with {s} threshold")
        k += 1

    if i < 10000:
        i += 1000
    elif i < 100000:
        i += 10000
    elif i < 1000000:
        i += 100000
    else:
        i += 1000000

f1.close()
f2.close()
