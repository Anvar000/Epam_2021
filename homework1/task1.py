def check_power_of_2(a: int) -> bool:
    """Function to check is the number 'a' a power of 2 or not

    Args:
        a (int): any number

    Returns:
        bool: True - if the number 'a' is a power of 2
              False - if the number 'a' is not a power of 2
    """
    if a > 0:
        return not (bool(a & (a - 1)))
    else:
        return False


print(check_power_of_2(0))