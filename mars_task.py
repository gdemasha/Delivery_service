# ID успешной посылки: 102342949
from typing import List, Tuple


def main(weights: List[int], limit: int) -> int:
    """
    Функция, подсчитывающая необходимое количество
    платформ для перевозки грузов.
    """

    UNPACKING_PAIR: int = 2

    left_pointer: int = 0
    right_pointer: int = len(weights) - 1
    pairs: List[Tuple[int, int]] = []

    weights.sort()

    while left_pointer < right_pointer:
        result = weights[left_pointer] + weights[right_pointer]
        if result <= limit:
            pairs.append((left_pointer, right_pointer))
            right_pointer -= 1
            left_pointer += 1
        else:
            right_pointer -= 1

    platforms = (len(weights) - len(pairs)*UNPACKING_PAIR) + len(pairs)
    return platforms
