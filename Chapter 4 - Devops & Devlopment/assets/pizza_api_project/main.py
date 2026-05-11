from fastapi import FastAPI
import uvicorn
from models.pizza import PizzaItem, OrderRequest
from routers import orders
from routers.orders import create_order

app = FastAPI(title="Pizza Delivery API")
app.include_router(orders.router)


def main():
    pizza: PizzaItem = PizzaItem(**{"name": "of#", "price": 0.1})
    print(pizza.price)
    # uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()


@app.get("/")
def root():

    return {"message": "Welcome to the Pizza API"}
