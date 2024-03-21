def fizzbuzz(n):
    nums = []
    for num in range(1, n + 1):
        if num % 15 == 0:
            nums.append("FizzBuzz")

        elif num % 5 == 0:
            nums.append("Buzz")

        elif num % 3 == 0:
            nums.append("Fizz")

        else:
            nums.append(num)
    return nums


print(fizzbuzz(20))
