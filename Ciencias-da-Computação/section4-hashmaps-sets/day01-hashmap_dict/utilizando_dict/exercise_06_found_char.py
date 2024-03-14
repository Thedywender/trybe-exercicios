# string = "bbbbaaaacccaaaaaaddddddddccccccc"
string = "coxinha"


def count_char(string):
    char_count = dict()

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


print(count_char(string))
