def main(arr, kth):
    sortable = SortableArray(arr)
    print(sortable.quickselect(kth, 0, len(arr) - 1))
    sortable.quicksort(0, len(arr) - 1)
    print(f'final sorted array: {sortable.arr}')