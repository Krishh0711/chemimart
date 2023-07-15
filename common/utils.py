def validate_phone_number_and_otp(phone_number, otp):
    if phone_number is None or len(phone_number) != 10:
        return False
    if otp is None or len(str(otp)) != 6:
        return False
    return True