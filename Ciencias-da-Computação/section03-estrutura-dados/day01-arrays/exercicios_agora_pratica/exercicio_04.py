def interval_frequency(enter, out, interval):
    interval_count = 0
    for i in range(len(enter)):
        if enter[i] <= interval <= out[i]:
            interval_count += 1
    return interval_count


# another way to solve the problem

def interval_frequency_01(enter, out, interval):
    return sum(
        enter <= interval <= out
        for enter, out in zip(enter, out)
    )

enter = [1, 2, 3]
out = [3, 2, 7]
interval = 4
interval_01 = 3

print(interval_frequency(enter, out, interval))
print(interval_frequency_01(enter, out, interval_01))
resultado: 1

# O estudante 1 entrou no instante 1 e saiu no 3, já o segundo entrou
# e saiu no 2 e o último foi único a estar presente no instante 4.