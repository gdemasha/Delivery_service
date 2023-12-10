# ID успешной посылки: 102485552
import sys

from typing import List


def platform_counter(weights: List[int], limit: int) -> int:
    """
    Функция, подсчитывающая необходимое количество
    платформ для перевозки грузов.
    """

    left_pointer: int = 0
    right_pointer: int = len(weights)
    count: int = 0

    weights.sort()

    while left_pointer < right_pointer:
        right_pointer -= 1
        if right_pointer == left_pointer:
            break
        if weights[left_pointer] + weights[right_pointer] <= limit:
            count += 1
            left_pointer += 1

    return len(weights) - count


if __name__ == '__main__':
    data = sys.stdin.readline().rstrip()
    weights = [int(weight) for weight in data.split()]
    limit = sys.stdin.readline().rstrip()
    limit = int(limit)

    print(platform_counter(weights, limit))
