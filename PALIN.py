def inc_str(value):
    count = len(value)
    inverse = value[::-1]
    count_nine = 0

    for i in inverse:
        if i == '9':
            count_nine += 1
        else:
            break

    if count_nine == count:
        return '1' + '0' * count_nine

    max_interval = count - count_nine - 1
    initial = value[0:max_interval]
    inc = str(int(value[max_interval]) + 1)

    return initial + inc + '0' * count_nine


def palin(number):
    count = len(number)

    if count == 1:
        return '11'

    left_size = index = int(count / 2)
    left = number[:index]

    if count % 2:
        left = number[:index + 1]
        left_size += 1

    right = left[index - 1::-1]

    new_number = left + right

    while len(new_number) == count and new_number <= number:
        left = inc_str(left)
        right = left[index - 1::-1]

        new_number = left + right

    return new_number

t = int(input())
numbers = []
while t != 0:
    t -= 1
    numbers.append(input())

for K in numbers:
    print(palin(K))
