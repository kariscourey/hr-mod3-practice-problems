// Here is the Python implementation of quicksort from the exploration on sorting:

// def partition(values, left, right):
//     # get the pivot value (the last item)
//     pivot = values[right]

//     # star keeps track of the end of the "smaller than the pivot" list
//     star = left - 1

//     # move all of  the items that are less than pivot to the beginning of the list
//     for i in range(left, right):
//         if values[i] <= pivot:
//             star += 1
//             values[star], values[i] = values[i], values[star]

//     # move the pivot value into the "middle" of the list
//     star += 1
//     values[star], values[right] = values[right], values[star]

//     # return the position of the pivot value
//     return star

// def quicksort(values, left=None, right=None):
//     # handle the default calling case where only values is provided
//     if left is None and right is None:
//         left = 0
//         right = len(values) - 1

//     # if there is nothing left to sort return
//     if left >= right or left < 0:
//         return

//     # partition values and get the position (index) of the pivot item
//     p = partition(values, left, right)

//     # recursively sort the left half
//     quicksort(values, left, p - 1)

//     # recursively sort the right half
//     quicksort(values, p + 1, right)
// Now implement quicksort in JavaScript 🛠️


function partition(values, left, right) {
    const pivot = values[right];
    let star = left - 1;
    let temp;

    for (let i=left; i < right; i++) {
        if (values[i] <= pivot) {
            star++;
            temp = values[star];
            values[star] = values[i];
            values[i] = temp;
        }
    }

    star++;
    temp = values[star];
    values[star] = values[right];
    values[right] = temp;

    return star;
}

function quicksort(values, left=null, right=null) {
    if (left == null && right == null) {
        left = 0;
        right = values.length - 1;
    }
    if (left >= right || left < 0) {
        return null;
    }

    let p = partition(values, left, right);
    quicksort(values, left, p - 1);
    quicksort(values, p + 1, right);

}
