"""
Cette question s'accompagne d'un dossier `exercise/handmade_research` qui contient toutes les traces de recherche que j'ai pu faire sur le sujet dans la partie mathématique du problème.
Ce PDF indique mes schémas et quelques pensées/écrits mathématiques qui essayent de répondre à la problématique via différentes approches.

Concernant le code ci-dessous, je considère l'utilisation de la dernière solution visible dans le pdf `exercise/handmade_research/maths_by_hand.pdf` qui me semble être la plus pertinente.

"""

from exercise.utils.utils import compute_intermediate_factor_for_monthly_rate_and_duration


def ratio(taux1: float, duree1: float, taux2: float, duree2: float) -> float:
    """Computes the maximal ratio for given taux1, duree1, taux2, duree2

    Args:
        taux1 (float): The rate of the short line loan
        duree1 (float): The duration of the short line loan
        taux2 (float): The rate of the long line loan
        duree2 (float): The duration of the long line loan

    Returns:
        float: A value in %, that is the maximum ratio found between short line loan and total loan
    """
    ratio_max = 0

    for y_axis_index in range(1, 100):
        short_line_monthly_part = y_axis_index / 100.0
        long_line_monthly_part = 1 - short_line_monthly_part
        amount_long_line = (
            long_line_monthly_part / compute_intermediate_factor_for_monthly_rate_and_duration(taux2, duree2) - short_line_monthly_part / compute_intermediate_factor_for_monthly_rate_and_duration(taux2, duree1)
        )
        amount_short_line = (
            short_line_monthly_part / compute_intermediate_factor_for_monthly_rate_and_duration(taux1, duree1)
        )

        computed_ratio = amount_short_line / (amount_short_line + amount_long_line)

        if computed_ratio > ratio_max:
            ratio_max = computed_ratio

    return ratio_max
