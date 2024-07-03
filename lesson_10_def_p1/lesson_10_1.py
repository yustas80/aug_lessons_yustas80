# Task_1_taxes

def taxes(sal: int | float, tax: int | float) -> int | float:
    """
    Calculate salary without a tax.

    :param sal: The amount of salary
    :param tax: The amount of tax rate
    :return: The salary after tax deduction.
    """
    if not isinstance(sal, int | float):
        raise TypeError('amount must be an int or float')
    if not isinstance(tax, int | float):
        raise TypeError('tax must be an int or float')
    if sal <= 0:
        raise ValueError('sal must be a positive number')
    if 1 < tax < 0:
        raise ValueError('tax must be between 0 and 1')

    return sal - sal * tax


a, b = (float(input('Input your salary: ')), float(input('Input taxes: ')))

print(f'You salary - {taxes(a, b)}')


