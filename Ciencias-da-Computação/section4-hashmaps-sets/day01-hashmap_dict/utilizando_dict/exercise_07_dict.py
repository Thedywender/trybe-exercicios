double = {i: i * 2 for i in range(3, 21)}

for key in double:
    if key % 2 is not 0:
        double[key] = key * 3

print(double)


# dict = {"num1": 3, "num2": 20}

# for key in dict:
#     if dict[key] % 2 != 0:
#         dict[key] *= 2

# print(dict)
