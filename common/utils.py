def validate_phone_number_and_otp(phone_number, otp):
    """
    Validate the phone number and OTP (One-Time Password) inputs.
    Args:
        phone_number (str): The phone number to validate.
        otp (int): The OTP to validate.
    Returns:
        bool: True if the phone number and OTP are valid, False otherwise.
    """
    if phone_number is None or len(phone_number) != 10:
        return False
    if otp is None or len(str(otp)) != 6:
        return False
    return True