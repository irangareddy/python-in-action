"""2.1 Covering Your A** With Assertions"""

"""
Python's assert statement is debugging
aid that tests a condition either TRUE or FALSE
"""


def apply_discount(product, discount):
    """ apply discount for a product with specified discount """
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


ipad = {
    'name': 'iPad Pro 12.9 inch',
    'price': 1600
}

final_amount = apply_discount(product=ipad, discount=0.15)
print(final_amount)

# raises AssertionError
# apply_discount(product=ipad,discount=2.25)


"""Python's Assert Syntax"""
expression1 = 10 % 2 == 0
expression2 = 10 % 2 == 1

if __debug__ and not expression1:
    raise AssertionError(expression2)

"""bogus assertion: Heisenbug"""
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

# TODO: https://dbader.org/blog/catching-bogus-python-asserts

"""
TOPIC: Common Pitfalls With Using Asserts in Python
DATE: 2022/08/01

Two Caveats

1. Introducing security risks and bugs into your applications,
2. Syntax quirk that makes it easy to write useless assertions.
"""

# Caveat - 1 – Don’t Use Asserts for Data Validation
"""
def delete_product(prod_id, user):
    assert user.is_admin(), 'Must be admin'
    assert store.has_product(prod_id), 'Unknown product'
    store.get_product(prod_id).delete()

Serious Problems
1. Checking for admin privileges with an assert statement is dangerous.
Reason: If assertions are disabled in the Python interpreter,
this turns into a null-op.Therefore any user can now delete products.
The privileges check does not even run. This likely introduces a security
problem and opens the door for attackers to destroy or
severely damage the data in our online store. Not good.
2. The has_product() check is skipped when assertions are disabled.
Reason:This means get_product() can now be called with invalid produc
t
IDs—which could lead to more severe bugs,depending on how our program
is written. In the worst case, this could be an avenue for someone
to launch Denial of Service attacks against our store.
For example, if the store app crashes if someone attempts to
delete an unknown product, an attacker could bombard it with
invalid delete requests and cause an outage.


Key Takeaways:
The answer is to never use assertions to do data validation.
Instead, we could do our validation with regular if-statements
and raise validation exceptions if necessary, like so:

def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(product_id):
        raise ValueError('Unknown product id')
    store.get_product(product_id).delete()
"""

# Caveat -2 - Asserts That Never Fail

"""
raises SyntaxWarning: assert(1 == 2, 'This should fail')
Reason: Because it asserts the truth value of a tuple object.
"""

try:
    assert 1 == 2, 'This should fail'
except AssertionError:
    print('1 == 2  failed with an AssertionError')

"""
Key Takeaways

* Python’s assert statement is a debugging aid that tests a condition as an internal self-check in your program. # noqa:E501
* Asserts should only be used to help developers identify bugs. They’re not a mechanism for handling run-time errors. # noqa:E501
* Asserts can be globally disabled with an interpreter setting.
"""
