def summa(a,b):
    return a + b

print(summa(10,12))

def is_even(n):
    return  n % 2 == 0

print(is_even(10))
print(is_even(13))

def power(x, exp=2):
    return x ** exp

print(power(2))
print(power(2,10))

def max_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(max_of_three(4,9,1))

numbers = [1,4,9]

def squares(numbers):
    return list(map(lambda x:x**2,numbers))

print(squares(numbers))

nums = [10,20,30,40,50]
nums = nums[:3]
print(nums)

words = ['a','b','c','d']
words = words[-2:]
print(words)


letter = ['A','B','C','D','E','F']
letter = letter[::2]
print(letter)

nums = [1,2,3,4,5]
nums= nums[:-2]
print(nums)

numbers = [0,1,2,3,4,5,6,7,8]
numbers = numbers[1::3]
print(numbers)

nums = [10,20,30,40,50,60]
nums = nums[::-2]
print(nums)

test = "Pithon"
test = test[::-1]
print(test)