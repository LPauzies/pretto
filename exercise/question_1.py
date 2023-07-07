"""
Pour un prêt donné, un taux annuel donné et une durée de prêt (en mois) donné, on calcule la totalité des intérêts dûs.
NB1: On connait le montant fixe du loyer mensuel
NB2: On sait calculer les interêts pour un résiduel donné (Valeur du prêt - capital remboursé)

"""

from utils.utils import compute_classic_monthly_payment, compute_monthly_interest


def calculate_total_interests_over_loan(
    amount: float, annual_rate: float, duration: int
) -> float:
    """Calculate the total of interests over given loan, with given annual rate and duration (in months)

    >>> int(calculate_total_interests_over_loan(300000, 0.0158, 300))
    63335

    >>> int(calculate_total_interests_over_loan(300000, 0.04, 300))
    175053

    >>> int(calculate_total_interests_over_loan(200000, 0.03, 240))
    66206

    >>> int(calculate_total_interests_over_loan(160000, 0.018, 300))
    38808

    >>> int(calculate_total_interests_over_loan(140000, 0.0115, 180))
    12488

    Args:
        amount (float): The amount of the loan
        annual_rate (float): The annual rate for the loan
        duration (int): The duration of the loan (in months)

    Returns:
        float: Interests paid for the given loan
    """
    monthly_rate = annual_rate / 12
    fixed_monthly_payment = compute_classic_monthly_payment(
        amount, monthly_rate, duration
    )
    sum_of_interests = 0
    for _ in range(duration):
        monthly_interest = compute_monthly_interest(amount, monthly_rate)
        amount -= fixed_monthly_payment - monthly_interest
        sum_of_interests += monthly_interest
    return sum_of_interests
