def fatorial(num_ref):
    fat_result = 1
    for num in range(1, num_ref + 1):
        fat_result *= num
    return fat_result


# print(fatorial(3))


def mult_notes(ratings: list):
    result_notes = list()
    for note in ratings:
        if note % 3 == 0:
            result_notes.append(note * 10)
    return result_notes


ratings = [6, 8, 5, 9, 10]
# print(mult_notes(ratings))


def concat_like_tuple(*args):
    final_string = ""
    for index, name in enumerate(args, 1):
        final_string += f"O nome da pessoa {index} é {name}.\n"
    return final_string


def concat_like_dict(**kwargs):
    final_string = (
        f'{kwargs["nome"]} {kwargs["sobrenome"]} tem {kwargs["idade"]} anos.\n'
    )
    return final_string


# print(concat_like_tuple("Cris", "Wallace", "Carol"))
# saída:
# O nome da pessoa 1 é Cris.
# O nome da pessoa 2 é Wallace.
# O nome da pessoa 3 é Carol.

print(concat_like_dict(nome="Felipe", sobrenome="Silva", idade=25))
# saída:
# Felipe Silva tem 25 anos.
