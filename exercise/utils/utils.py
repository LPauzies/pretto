"""Some utils function that will be useful during the exercise"""

import math


def compute_monthly_interest(amount: float, monthly_rate: float) -> float:
    """Compute monthly interest given a loan amount and a monthly rate

    >>> compute_monthly_interest(30000, 0.004)
    120.0

    >>> compute_monthly_interest(30000, 0.05)
    1500.0

    Args:
        amount (float): The amount of the loan
        monthly_rate (float): The monthly rate

    Returns:
        float: The interests paid for the given amount of the loan in a month
    """
    return amount * monthly_rate


def compute_classic_monthly_payment(
    amount: float, monthly_rate: float, duration: int
) -> float:
    """Compute classic monthly payment given a loan amount, a monthly rate and the duration (in months)

    >>> int(compute_classic_monthly_payment(200000, 0.003, 300))
    1012

    >>> int(compute_classic_monthly_payment(300000, 0.002, 240))
    1575

    Args:
        amount (float):The amount of the loan
        monthly_rate (float): The monthly rate
        duration (int):The duration of the loan (in months)

    Returns:
        float: The monthly payment due
    """
    return amount * compute_intermediate_factor_for_monthly_rate_and_duration(
        monthly_rate, duration
    )


def compute_intermediate_factor_for_monthly_rate_and_duration(
    monthly_rate: float, duration: int
) -> float:
    """Compute ρ function from pretto subject

    >>> compute_intermediate_factor_for_monthly_rate_and_duration(0.05, 180)
    0.05000767295786077

    >>> compute_intermediate_factor_for_monthly_rate_and_duration(0.1, 300)
    0.10000000000003822

    Args:
        monthly_rate (float): The monthly rate
        duration (int): The associated duration

    Returns:
        float: ρ result
    """
    return monthly_rate / (1 - math.pow(1 + monthly_rate, -duration))
