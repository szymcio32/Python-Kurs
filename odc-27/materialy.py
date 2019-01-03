def potegowanie(podstawa_potegi, wykladnik):
    if wykladnik == 0:
        return 1
    else:
        return podstawa_potegi * potegowanie(podstawa_potegi, wykladnik - 1)

print(potegowanie(3,3))


# potegowanie(3, 3) --> 27
# potegowanie(3, 2) --> 9
# potegowanie(3, 1) --> 3
# potegowanie(3, 0) --> 1

# potegowanie(3, 1) --> 3 * 1 = 3
# potegowanie(3, 2) --> 3 * 3 = 9
# potegowanie(3, 3) --> 3 * 9 = 27
