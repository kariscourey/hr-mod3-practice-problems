// Below is a Python implementation of selection-sort.

// Selection-sort is kind of like bubble-sort in that the next most-extreme value makes its way to the correct end of the list on each iteration of the outer loop.

// However, instead of continually swapping adjacent items like bubble-sort, selection-sort finds the next most-extreme value and then does a single swap to place that value in the correct place.

// def selection_sort(items):
//     length = len(items)
//     for start in range(length-1):
//         min_idx = start
//         min_val = items[start]
//         for i in range(start+1, length):
//             if items[i] < min_val:
//                 min_idx = i
//                 min_val = items[i]
//         if min_idx > start:
//             items[start], items[min_idx] = items[min_idx], items[start]
//     return items
// Now, please implement selection-sort in JavaScript below:

function selectionSort(items) {
    let length = items.length;
    for (let start = 0; start < length - 1; start++) {
        let min_idx = start;
        let min_val = items[start];
        for (let i = start + 1; i < length; i++) {
            if (items[i] < min_val) {
                min_idx = i;
                min_val = items[i];
            }
        }
        if (min_idx > start) {
            temp = items[start];
            items[start] = items[min_idx];
            items[min_idx] = temp;
        }
    }
    return items;
}

items = [3, 1, 4, 6, 2];
console.log(selectionSort(items));
