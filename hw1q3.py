import math


def first_card(letter: str):
    return ord(letter.lower()) - ord('a')


def second_card(num: int):
    temp = num
    power = temp % 10
    temp = int(temp / 10)
    base = temp % 10
    temp = int(temp / 10)
    return int(math.pow(base, power) / temp)


def third_card(letter):
    if ord(letter) % 7 == 0:
        return 17
    elif ord(letter) % 4 == 0:
        return 6
    return 0

print('Player A,')
print('Insert 1st card:')
a_first = str(input())
print('Insert 2nd card:')
a_sec = int(input())
print('Insert 3rd card:')
a_third = str(input())

a_result = first_card(a_first) + second_card(a_sec) + third_card(a_third)

print('Player B,')
print('Insert 1st card:')
b_first = str(input())
print('Insert 2nd card:')
b_sec = int(input())
print('Insert 3rd card:')
b_third = str(input())

b_result = first_card(b_first) + second_card(b_sec) + third_card(b_third)

print('Score A - total:{}, card2:{}'.format(a_result, second_card(a_sec)))
print('Score B - total:{}, card2:{}'.format(b_result, second_card(b_sec)))

if a_result > b_result:
    print('The winner in Player {}!'.format('A'))
elif a_result < b_result:
    print('The winner in Player {}!'.format('B'))
elif second_card(a_sec) > second_card(b_sec):
    print('The winner in Player {}!'.format('A'))
elif second_card(a_sec) < second_card(b_sec):
    print('The winner in Player {}!'.format('B'))
else:
    print("It's a tie.")