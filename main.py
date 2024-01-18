def sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        sort(A, p, q)
        sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    left_size = q - p + 1
    right_size = r - q

    left = A[:left_size]
    right = A[:right_size]

    for i in range(0, left_size):
        left[i] = A[p - 1 + i]

    for i in range(0, right_size):
        right[i] = A[q + i]

    i, j, k = 0, 0, p - 1

    while i < left_size and j < right_size:
        if left[i] <= right[j]:
            A[k] = left[i]
            k += 1
            i += 1
        else:
            A[k] = right[j]
            k += 1
            j += 1

    while i < left_size:
        A[k] = left[i]
        k += 1
        i += 1

    while j < right_size:
        A[k] = right[j]
        k += 1
        j += 1


A = [5, 2, 4, 6, 1, 3, 2, 6]
sort(A, 1, len(A))

print(A)
