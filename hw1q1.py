print('A:')
# a_q has to be less than 50
a_p = (float(input()))
a_p_val = (a_p < 50) and (a_p > 0)
# a_q has to be positive and of int type
a_q = int(input())
a_q_val = a_q > 0

print('B:')
# b_p has to be less than 30
b_p = float(input())
b_p_val = (b_p < 30) and (b_p > 0)
# b_q has to be positive and of int type
b_q = int(input())
b_q_val = b_q > 0

print('C:')
c_p = float(input())
c_p_val = c_p > 0
# c_q has to be positive and of int type
c_q = int(input())
c_q_val = c_q > 0

print('D:')
d_p = float(input())
d_p_val = d_p > 0
# d_q has to be of type int and bigger than 1
d_q = int(input())
d_q_val = d_q >= 1

# a_q + c_quantity has to be less than 5
a_and_c_quantity = a_q * a_q_val + c_q * c_q_val
a_and_c_quantity_val = a_and_c_quantity <= 5

total_purchase = round(a_p * a_p_val * a_q * a_q_val + b_p * b_p_val * b_q * b_q_val + c_p * c_p_val * c_q * c_q_val + d_p * d_p_val * d_q * d_q_val, 2)
total_items = a_q * a_q_val + b_q * b_q_val + c_q * c_q_val + d_q * d_q_val
average_item_price = round(total_purchase/total_items, 2)

# in case one of the conditions isn't respected this error message should be displayed:
total_validity = (a_p_val and a_q_val and b_p_val and b_q_val and c_p_val and c_q_val and d_p_val and d_q_val and a_and_c_quantity_val)
result = '{} {} {}'.format(total_purchase, total_items, average_item_price)
print(result * total_validity or (total_validity or "Invalid Purchase"))