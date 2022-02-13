try:
    list_a = list(map(int, input(
        "Введите числовой список длин катетов а: "
        ).split()))
    list_b = list(map(int, input(
        "Введите числовой список длин катетов b: "
        ).split()))
    if len(list_a) != len(list_b):
        raise IndexError(
            "InconsistentDataError - списки с длинами катетов a и b "
            f"имеют разную длину ({len(list_a)} != {len(list_b)})"
            )
    for i, (a, b) in enumerate(zip(list_a, list_b), 1):
        c = (a ** 2 + b ** 2) ** 0.5
        S = a * b / 2
        print(
            f"Треугольник {i} с катетами {a} и {b} "
            f"имеет площадь {S} и гипотенузу {c}"
            )
except ValueError:
    print("NonNumericError - в списке катетов присутствуют не числа")
