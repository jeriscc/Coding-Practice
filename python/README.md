# Python Solutions

This directory contains python solutions for coding challenges I've solved. Below are some general python insights I've learned from doing so.

## References/Pointers in Python

All variables in Python are pointers to objects in memory locations. So when you pass an array variable to a function, it creates a copy of that **pointer** and works with it. Depending on what you do with the pointer, this will or will not modify the original. The follow are examples for both.

### Modifies

```python
nums = [1,2,3]

def assignNums(n):
    n[2] = 4

assignNums(nums)
print(nums)
# 1,2,4
```

In this case, we are using the pointer to access and modify the object it points to. Thus, the original object has not changed.

### Doesn't Modify

```python
nums = [1,2,3]

def assignNums(n):
    n = [4,5,6]

assignNums(nums)
print(nums)
# 1,2,3
```

In this case, we are assigning the list a new value. This instantiates a new array object and updates the pointer in the scope of the function to point to the new object. Thus, the original array does not change.

### Copying

To prevent modifying orignal objects, we can create copies of the original object. There are two types of copying: **shallow** and **deep**. Some definitions from the [Official Docs](https://docs.python.org/3/library/copy.html).

"A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original." It creates copies of the pointers. Array example:

Note: The function `id()` returns the memory location that a pointer points to.

```python
arr = [[1,2],[3,4]]

# Three different shallow copy methods
arr_copy = arr[:]
arr_copy = copy.copy(arr)
arr_copy = arr.copy()

print(id(arr[0]) == id(arr_copy[0]))
# True
```

"A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original." Array examples:

```python
arr = [[1,2],[3,4]]

arr_copy = copy.deepcopy(arr)

print(id(arr[0]) == id(arr_copy[0]))
# False
```

There is a special case where shallow and deep copies are effectively the same. For instance, when the original object is an array of integers.

```python
nums = [1,2,3]
nums_copy = copy.copy(nums) # Shallow copy
print(id(nums[0]) == id(nums_copy[0]))
# True

nums_deep_copy = copy.deepcopy(nums)
print(id(nums[0]) == id(nums_deep_copy[0]))
# True (but why???)
```

The reason for this behavior has to do with the difference between immutable and mutable objects. Let's look into that.

## Mutable vs Immutable Objects

There are two types of objects in python. Mutable and immutable. For a mutable object, you can change its data members without making a new copy. For an immutable object, any "changes" in value must result in a new copy of it.

Immutable objects: bool, int, float, tuple, str, frozenset
Mutable objects: list, set, dict

When python makes a deep copy of a immutable data member of an object it doesn't bother creating a duplicate of that data member in memory because its value won't change. The only way to "change" the value of that data member is very assignment, which doesn't affect the original memory location. Thus, it just points to the same data member.

For a mutable data member, because its value can change, deep copies will duplicate the object in memory and point the new data member to that object.

```python
arr = [[1,2],3]
arr_deep_copy = copy.deepcopy(arr)
print(id(arr[0]) == id(arr_deep_copy[0]))
# False
print(id(arr[1]) == id(arr_deep_copy[1]))
# True
```

This is the same for objects in general. Copies (deep and shallow alike) of immutable objects share the same memory address with its original. Shallow copies of mutable data objects will create a new copy of the object in memory, but not duplicate mutable data members. If you want to duplicate the mutable data members, use a deep copy.

```python
tup = (1,2)
print(id(tup) == id(copy.copy(tup)) == id(copy.deepcopy(tup)))
# True

arr = [1,2,dict()]
arr_copy =  copy.copy(arr);
print(id(arr) == id(arr_copy))
# False
print(id(arr[2]) == id(arr_copy[2]))
# True
arr_deep_copy = copy.deepcopy(arr);
print(id(arr) == id(arr_deep_copy))
# False
print(id(arr[2]) == id(arr_deep_copy[2]))
# False
```

## Python Tips

- `len()` is O(1) time for list, tuple, string, dictionary, set, array.array, etc.
- `thing in x` is O(n) time when `x` is a
- [This website](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt) is a good list for complexity of common python operations.
- Adding a duplicate item into a set doesn't change the set contents
- `all(condition(i) for i in arr)` returns true if all `i` in `arr` returns true for `condition()`
- `any(condition(i) for i in arr)` returns true if any `i` in `arr` returns true for `condition()`
- if you have an array of two element arrays, you can access the two via `for x,y in arr_pairs`.
- `list = [set() for _ in range(size)]` creates a list of empty sets with length `size`
- `result // 10` integer divides `result` by 10. `result ** 2` returns `result` to the 2nd power.
- `sum(map(int,str(n)))` sums the digits of a number `n`.
- `for c in str` iterates through characters in `str`. Though each character will be str itself.
- String methods `.islower()` and `isupper()` check for all lower or all uppercase. `.lower()` and `.upper()` converts to lower and uppercase.
- `for i, c in enumerate("hello")` extracts in the index `i` and character `c` from "hello"
- `function(i) for i in iterable` is a generator expression, which can be taken as input into functions like `str.join(...)`, `all(...)`, `any(...)`, and `list(...)`. Generator expressions don't fully evaluate the entire iterable in memory out right and instead does so one by one in the calling fucntion. Thus, it is good for short-circuiting functions like `all(...)` and `any(...)`.
- `import this` is a gem.
- Use `for i, n in enumerate(nums)` to loop through both the indeces and values of an List.
- `range(start, end, step)` loops from `start` to before `end` by `step` increments.
- To access key, value of dictionary use `for key,val in dict.items()`
- To just access key of dictionary use `for key in dict`.