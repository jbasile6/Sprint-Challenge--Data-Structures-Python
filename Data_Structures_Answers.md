Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1) - always the same, input does not affect runtime

2. What is the space complexity of your ring buffer's `append` function?
O(1) - capacity is set before we run the append method, append only hits one index at a time

3. What is the runtime complexity of your ring buffer's `get` method?
O(n) where n is the capacity, increases as capacity increases

4. What is the space complexity of your ring buffer's `get` method?
O(n) again, storage increases as capacity increases and get runs through the storage to filter out "nones"


5. What is the runtime complexity of the provided code in `names.py`?
O(n^2), the nested loops make it so each item in name1 is compared to each item in name2, exponentially grows as size of the inputs increase

6. What is the space complexity of the provided code in `names.py`?
O(n), just has to store the total of the two lists, does not grow exponentially as runtime does, also stores duplicates list

7. What is the runtime complexity of your optimized code in `names.py`?
O(n log n)
creating bstName1 is O(n), using contains to create duplicates is O(log n)

8. What is the space complexity of your optimized code in `names.py`?
O(n), stores duplicates list and bstnames1 BST, is linear
