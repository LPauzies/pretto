"""
Chercher les intérêts les plus faibles parmi toutes les combinaisons possible pour une durée du prêt total fixée.

De ma compréhension, on assume ici que `ratio` est une fonction existante qui renvoie un flottant compris entre 0 et 100 (en %),
qui est le ratio maximal pour deux couples (duree, taux) short line vs long line.
Plus il est grand, plus cela signifie que les intérêts sont faibles pour la combinaison taux1, durée1 et taux2, durée2 choisie.

"""

from dataclasses import dataclass
from typing import List, Tuple
from itertools import combinations

from exercise.question_2 import ratio


@dataclass
class DurationRate:
    """The DurationRate DAO"""
    duration_year: int
    rate: float

    @property
    def duration_months(self) -> int:
        """Computes duration in months on the fly

        Returns:
            int: The duration in months for current duration rate object
        """
        return self.duration_year * 12


GIVEN_RATE_GRID = [
    DurationRate(10, 2.9),
    DurationRate(12, 3.2),
    DurationRate(15, 3.5),
    DurationRate(20, 3.8),
    DurationRate(22, 3.8),
    DurationRate(25, 4.4),
]


def find_best_combinations_for_the_smaller_interests(
    rate_grid: List[DurationRate],
) -> List[Tuple[DurationRate, DurationRate]]:
    """Find the best combinations of duration rate objects that provide the smaller interests

    NB: This method is using itertools.combinations which is a built-in function that creates combinations of k among n values.
    In our case we use it with k = 2 and n the rate grid.

    Args:
        rate_grid (List[DurationRate]): The list of DurationRate objects sorted by duration ascending

    Returns:
        List[Tuple[DurationRate, DurationRate]]: The list containing the couples of DurationRate objects that have the smaller interests.
    """
    # Check if the rate_grid is sorted ascending using duration_year key as a prerequisite
    assert sorted(rate_grid, key=lambda duration_rate: duration_rate.duration_year) == rate_grid

    combinations_with_smaller_interests = []
    ratio_with_smaller_interests = 0
    for short_line_duration_rate, long_line_duration_rate in combinations(rate_grid, 2):
        computed_ratio = ratio(
            short_line_duration_rate.rate,
            short_line_duration_rate.duration_months,
            long_line_duration_rate.rate,
            long_line_duration_rate.duration_months,
        )
        if computed_ratio > ratio_with_smaller_interests:
            combinations_with_smaller_interests = [
                (short_line_duration_rate, long_line_duration_rate)
            ]
            ratio_with_smaller_interests = computed_ratio
        elif computed_ratio == ratio_with_smaller_interests:
            combinations_with_smaller_interests.append(
                (short_line_duration_rate, long_line_duration_rate)
            )
    return combinations_with_smaller_interests

print(find_best_combinations_for_the_smaller_interests(GIVEN_RATE_GRID))
