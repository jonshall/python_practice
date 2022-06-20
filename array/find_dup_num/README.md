# Find Duplicate Number

### Problem

Given an array of integers ```nums``` containing ```n + 1``` integers where each integer is in the range ```[1, n]``` inclusive.

There is only one repeated number in ```nums```, return the repeated number.

Solve the problem without modifying the array ```nums``` and uses only constant extra space.

### Example Input

nums = [1,3,4,2,2]

### Example Output

2

### Algorithm

Floyd’s algorithm consists of two phases and uses two pointers, usually called tortoise and hare.

### Time Complexity

- O(n)

### Space Complexity

- O(1)
