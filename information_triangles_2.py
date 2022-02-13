try:
    list_ab = list(map(int, input(
        "Введите числовой список длин катетов а и b: "
        ).split()))
    list_a = list_ab[0:len(list_ab):2]
    list_b = list_ab[1:len(list_ab):2]
    if len(list_a) != len(list_b):
        raise IndexError(
            "InconsistentDataError - выделенные списки с длинами катетов "
            f"a и b имеют разную длину ({len(list_a)} != {len(list_b)})"
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
