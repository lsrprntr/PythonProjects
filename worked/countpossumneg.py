def count_positives_sum_negatives(arr):
    if not arr: return print(arr)
    pos = list()
    neg = list()
    for i in arr:
        if i > 0:
            pos.append(i)
        if i < 0:
            neg.append(i)
    return print([len(pos),sum(neg)])

count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])
count_positives_sum_negatives([0,0,0,0,0,0,0,0,0])
count_positives_sum_negatives([])
