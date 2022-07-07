# 2.1 Covering Your A** With Assertions

# Python's assert statement is debugging aid that tests a condition either TRUE or FALSE

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