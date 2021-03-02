# Insertion Sort Blog 

## Pseudocode
```
  InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp

# Example Array: [8,4,23,42,16,15]
```

Create a function `InsertionSort` that takes in an array of integers. 
```
Input array:                [8,4,23,42,16,15]
Coresponding Index Values:  [0,1, 2, 3, 4, 5]
```

Create a `for` loop to look at the array length starting at index 1. 
```
Values looked at by FOR LOOP: [4,23,42,16,15]
Coresponding Index Values:    [1, 2, 3, 4, 5]
```

Assigning variable `j` to the value of `i` minus 1. 
```
i = 1
# j = 1 - 1 
j = 0
```

Assigning a `temp` variable to hold the current *value* of `i`.
```
i = 4
temp = 4
```

Create a `while` loop that only runs if the value of `j` is `0` or larger ***AND*** the `temp` value is less than the value of `arr[j]`.

If the conditions of the while loop are true, take the value of the next index and assign it to the index value before it.
```
while 0 >= 0 AND 4 < 8
    arr[0 + 1] = arr[0]
    # Value at index [1]  is now the value at index [0] 
    1 <-- 1 - 1
    # Reassign j to j - 1 to look at the previous index on the next pass
```

Now you have to assign the `temp` variable to the inxed that you removed.
```
arr[0 + 1] <-- 4
```

If the conditions of the `while` loop are false the code will continue to run until the `while` loop cinditions are true. 

Continue until the array is sorted in numerical order.

Return the sorted array


| PASS | BEFORE | AFTER |
| --- | --- | --- |
| 1 | [8,4,23,42,16,15] | [4,8,23,42,16,15] | 8 & 4
| 2 | [4,8,23,42,16,15] | [4,8,23,42,16,15] | 4 & 8
| 3 | [4,8,23,42,16,15] | [4,8,23,42,16,15] | 8 & 23
| 4 | [4,8,23,42,16,15] | AFTER |
| 5 | [4,8,23,42,16,15] | [4,8,23,16,42,15] |
| 6 | [4,8,23,16,42,15] | [4,8,23,16,42,15] |
| 7 | [4,8,23,16,42,15] | [4,8,23,16,15,42] |
| 8 | [4,8,23,16,15,42] | AFTER |