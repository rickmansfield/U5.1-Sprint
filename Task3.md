```python
def reverseString(str):
    greeting = reversed(str)
print(reverseString("Love Lambda"))
```
The code above uses a builtin method that stores each character in an object in memory. It is a O(n) linear in both time and space complexity and the larger the given string the longer it takes to process. Each character is stored O(1). Therefore this particular method might be improved upon in some way such as using [::-1]. But for the sake of demonstration it's a valid alternative for small simple strings not larger volumes of information. 