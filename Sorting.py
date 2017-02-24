
def bub_sort(arr):
    tmpArr = arr[:]  # so we don't modify the origianl list
    # http://stackoverflow.com/questions/184643/what-is-the-best-way-to-copy-a-list
    for i in range(len(tmpArr)):
        for j in range(i):
            if tmpArr[i] < tmpArr[j]:
                tmpArr[i], tmpArr[j] = tmpArr[j], tmpArr[i]
    return tmpArr


ARR = [9, 1, 7, 0, 3, 5, 4, 6, 8, 2]

print("bub_sort - ", bub_sort(ARR))
print("Original - ", ARR)
ARR.sort()
print("sort     - ", ARR)
