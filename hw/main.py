from wine import Wine
from beer import Beer
from market import Market


wines = [
    Wine("Abrau-Durso", "2024/01/15"),
    Wine("Alamos Merlot", "2024/01/01"),
    Wine("Cabernet Merlot Chateau", "2023/11/10"),
    Wine("Obalo Roble", "2023/12/12"),
    Wine("Folonari Verona", "2024/01/07")
]

beers = [
    Beer("Grimbergen", "2023/10/08"),
    Beer("Corona", "2024/01/06"),
    Beer("Weissberg", "2023/10/10"),
    Beer("Heineken", "2024/01/03"),
    Beer("Kronenbourg", "2023/12/14")
]

market = Market(wines, beers)

#формирование списка напитков, отсортированных по наименованиям

sorted_drinks = market.get_drinks_sorted_by_title()

for drink in sorted_drinks:
    print(drink.title, drink.production_date)
print()

#проверка наличия напитка в магазине

print(market.has_drink_with_title("Hoegaarden"))
print(market.has_drink_with_title("Abrau-Durso"))
print()

#получение списка напитков (вина и пива) в указанном диапазоне даты производства

#Случай 1: обе даты определены

drinks_filtered_by_date1 = market.get_drinks_by_production_date("2024/01/01", "2024/01/20")
for drink in drinks_filtered_by_date1:
    print(drink.title, drink.production_date)
print()

#Случай 2: определена одна из дат

drinks_filtered_by_date2 = market.get_drinks_by_production_date("2023/12/01")
for drink in drinks_filtered_by_date2:
    print(drink.title, drink.production_date)
