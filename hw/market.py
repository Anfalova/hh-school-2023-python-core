from hw.logging_decorator import logging_decorator


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {wine.title: wine for wine in wines if wine.title} if wines else {}
        self.beers = {beer.title: beer for beer in beers if beer.title} if beers else {}

    @logging_decorator
    def has_drink_with_title(self, title=None) -> bool:
        return title in self.wines or title in self.beers

    @logging_decorator
    def get_drinks_sorted_by_title(self) -> list:
        list_of_drinks = list(self.wines.values()) + list(self.beers.values())
        return sorted(list_of_drinks, key=lambda drink: drink.title)

    @logging_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        list_of_drinks = list(self.wines.values()) + list(self.beers.values())
        drinks_by_date = filter(lambda drink: drink.production_date is not None, list_of_drinks)
        if from_date:
            drinks_by_date = filter(lambda drink: from_date <= drink.production_date, drinks_by_date)
        if to_date:
            drinks_by_date = filter(lambda drink: drink.production_date <= to_date, drinks_by_date)
        return list(drinks_by_date)
