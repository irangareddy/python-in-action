"""Phonenumbers library example"""

import phonenumbers

temp_phonenumbers = [
    '+1 0033 60-7731861',
    "+1 0041 445 551 000",
    "+27 87 362 6902",
    "+49 89 380066592",
    "+1442035679858",
    "+(415) 833-00009",
    "+32 47-9760962",
    "+91 80 61790110",
    "+1 06 65 16 16 32"
]
for number in temp_phonenumbers:
    result = phonenumbers.parse(number)
    print(f'national_number: {result.national_number}')
    print(f'number_of_leading_zeros:'
          f' {result.number_of_leading_zeros}')
    print(f'extension: {result.extension}')
    print(f'raw_input: {result.raw_input}')
    print(f'country_code: {result.country_code}')
    print(f'preferred_domestic_carrier_code: '
          f'{result.preferred_domestic_carrier_code}')
    print(f'italian_leading_zero: {result.italian_leading_zero}')
    print(f'{result} and type: {type(result)}')
    print("******************")
