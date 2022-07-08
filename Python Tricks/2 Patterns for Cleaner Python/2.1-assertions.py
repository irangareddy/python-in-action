# 2.1 Covering Your A** With Assertions

# Python's assert statement is debugging aid that tests a condition either TRUE or FALSE

from ast import Expression


def apply_discount(product, discount):
    """ apply discount for a product with specified discount """
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

ipad = {
'name': 'iPad Pro 12.9 inch',
'price': 1600
}

final_amount = apply_discount(product=ipad,discount=0.15)
print(final_amount)

# raises AssertionError
# apply_discount(product=ipad,discount=2.25)


# Python's Assert Syntax
expression1 = 10%2==1
expression2 = 10%2==0

if __debug__:
    if not expression1:
        raise AssertionError(expression2)

# bogus assertion: Heisenbug
cond = 'x'

if cond == 'x':
   print('x')
elif cond == 'y':
   print('y')
else:
    assert False, (
        'This should never happen, but it does '
        'occasionally. We are currently trying to '
        'figure out why. Email dbader if you '
        'encounter this in the wild. Thanks!')

# read more: https://dbader.org/blog/catching-bogus-python-asserts