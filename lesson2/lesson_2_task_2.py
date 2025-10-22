def is_year_leap(year):
    return True if year % 4 == 0 else False

prnt_year = int(input("Введите год: "))
result = is_year_leap(prnt_year)
print(f"Високосный ли год {prnt_year}? - {result}")