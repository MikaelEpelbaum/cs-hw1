print('A:')
# a_p has to be less than 50
a_p = float(input())
# a_q has to be positive and of int type
a_q = int(input())

print('B:')
# b_p has to be less than 30
b_p = float(input())
# b_q has to be positive and of int type
b_q = int(input())

print('C:')
c_p = float(input())
# c_q has to be positive and of int type
c_q = int(input())

print('D:')
d_p = float(input())
# d_q has to be positive, of int type and bigger than 1
d_q = int(input())

# a_q + c_quantity has to be less than 5

totlat_purchase = round(a_p * a_q + b_p * b_q + c_p * c_q + d_p * d_q, 2)
total_items = a_q + b_q + c_q
average_item_price = round(totlat_purchase/total_items, 2)

# in case one of the conditions isn't respected this error message should be displayed:
# print("Invalid Purchase")