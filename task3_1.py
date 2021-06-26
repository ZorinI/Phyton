def first(var_1, var_2):
    try:
        var_1 = int(var_1)
        var_2 = int(var_2)
        res = var_1 / var_2
        print(f"res:{res}")
    except (ValueError, ZeroDivisionError) as err:
        print(err)
        return

first(var_1=(input("введите первое число: ")), var_2=(input("введите второе число:")))