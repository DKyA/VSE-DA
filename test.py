
def bubble_sort(array):

    arr = array[:]

    should_end = False

    for _ in range(len(arr) - 1):

        if should_end: break
        should_end = True

        for i in range(1, len(arr)):

            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                should_end = False

        print(arr)
        # sleep(2)

    return arr

source = [5, 4, 3, 2, 1]

print(source)
print(bubble_sort(source))
