from pydantic import BaseModel, validator
from typing import List

from validation.validate_name import name_doesnt_contain_special_characters
from validation.validate_price import price_is_bigger_then_zero


class PizzaItem(BaseModel):
    name: str
    price: float

    @validator("name")
    def name_validation(cls, name: str):
        name_doesnt_contain_special_characters(name=name)

    @validator("price")
    def validate_price(cls, price: float):
        price_is_bigger_then_zero(price=price)


class OrderRequest(BaseModel):
    customer_name: str
    pizzas: List[PizzaItem]

    @validator("name")
    def name_validation(cls, customer_name: str):
        name_doesnt_contain_special_characters(name=customer_name)
