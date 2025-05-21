def main(x):
    card_number = x.translate(str.maketrans({ '-' :'' , ' ' :'' , '"':'' ,'\'':''}))
    print(verification(card_number))
                                             
    if verification(card_number) % 10 == 0:
        print('VALID')
    else:
        print('INVALID')

def verification(card_number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0

    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    even_digits = card_number_reversed[1::2]

    for i in odd_digits:
        sum_of_odd_digits += int(i)

    for i in even_digits:
        number = int(i * 2)
        sum_of_even_digits += (number // 10) + (number%10)
    
    total = sum_of_even_digits + sum_of_odd_digits
    return total

x = input('Enter Card Number: ')
main(x)