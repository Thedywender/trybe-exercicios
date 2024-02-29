# def recursive_count_pair_numbers(n):
#     if n == 0:
#         return 0, []
#     else:
#         count, numbers = recursive_count_pair_numbers(n - 1)
#         if n % 2 == 0:
#             return count + 1, numbers + [n]
#         else:
#             return count, numbers

# count, numbers = recursive_count_pair_numbers(10)

# print(count)
# print(numbers)

def conta_pares(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + conta_pares(n - 1)
    else:
        return conta_pares(n - 1)
    
print(conta_pares(10))