def validate_phonenumber(number):
    if not number.startswith('+1'):
        number = "{}{}".format('+1', number)
    elif len(number) != 12:
        raise Exception('Please enter a valid phone number')
    return number
