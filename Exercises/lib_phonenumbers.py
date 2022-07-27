import phonenumbers

salesforce_phonenumbers = ["+442083661177"]
for number in salesforce_phonenumbers:
    print(phonenumbers.parse(number, None))
