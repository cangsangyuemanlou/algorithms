def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p , r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


if __name__ == '__main__':
    a = [4,3,5,2,1]
    quick_sort(a, 0 , len(a) - 1)
    print(a)
