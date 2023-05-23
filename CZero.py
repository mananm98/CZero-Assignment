from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

# Data Store (Python Dictionary)
inventory = {
    "CZPR": {
        "product_name": "CZero Pen Brand",
        "variant": "Red Pen",
        "price": 1.00,
        "qty": 5,
        "description": "High quality pens that are carbon-neutral"
    },
    "CZPB": {
        "product_name": "CZero Pen Brand",
        "variant": "Blue Pen",
        "price": 1.00,
        "qty": 5,
        "description": "High quality pens that are carbon-neutral"
    },
    "CZPG": {
        "product_name": "CZero Pen Brand",
        "variant": "Green Pen",
        "price": 1.00,
        "qty": 5,
        "description": "High quality pens that are carbon-neutral"
    },
    "RPG": {
        "product_name": "Red’s Pens",
        "variant": "Black Fountain Pen",
        "price": 5.00,
        "qty": 100,
        "description": "Fountain pens designed by Paul Red"
    },
    "PRG": {
        "product_name": "Red’s Pens",
        "variant": "Purple Fountain Pen",
        "price": 5.00,
        "qty": 100,
        "description": "Fountain pens designed by Paul Red"
    },
    "BYP": {
        "product_name": "Good Quality Pencil",
        "variant": "",
        "price": 0.50,
        "qty": 1000,
        "description": "Handmade Pencils"
    }
}

# Get whole inventory
@app.get("/products")
def get_products():
    """
    Shows the full inventory database
    """
    return inventory


@app.get("/products/{sku}")
def get_product_by_sku(sku: str):
    """
    Retrieve product details by SKU.

    - **sku**: The SKU of the product to retrieve.
    """
    if sku in inventory:
        return inventory[sku]
    
    return {"message": "Product not found"}

# Add new product
@app.post("/products")
def add_product(product_name: str, sku: str, price: float, qty: int, variant: Optional[str] = None, description: Optional[str] = None,):
    """
    Add a new product to the inventory.

    - **product_name**: The name of the product.
    - **variant**: (Optional) The variant of the product.
    - **sku**: The SKU of the product.
    - **price**: The price of the product.
    - **qty**: The quantity of the product.
    - **description**: (Optional) The description of the product.
    """
    if sku in inventory:
        return {"message": "Product already exists"}
    
    inventory[sku] = {
        "product_name": product_name,
        "variant": variant,
        "price": price,
        "qty": qty,
        "description": description
    }

    return {"message": "Product added successfully"}



# Update product quantity
@app.put("/products/{operation}/{sku}/")
def update_inventory(operation : str, sku: str, qty: int):
    """
    Add a new product to the inventory.

    - **operation**: enter **add** or **delete** depending on the usage.
    - **sku**: The SKU of the product.
    - **qty**: The quantity of the product to add/delete.

    """
    if sku not in inventory:
        return {"message": "Product not found"}
    else:
        if operation == "add":
            inventory[sku]["qty"] += qty
        else:
            inventory[sku]["qty"] -= qty
        
        return {"message": "Inventory updated successfully"}

# Update product
@app.put("/products/{sku}")
def update_product(sku: str, product_name: Optional[str] = None, variant: Optional[str] = None,
                   price: Optional[float] = None, qty: Optional[int] = None, description: Optional[str] = None):
    
    """
    Update a product in the inventory.

    - **sku**: The SKU of the product to update.
    - **product_name**: (Optional) The updated name of the product.
    - **variant**: (Optional) The updated variant of the product.
    - **price**: (Optional) The updated price of the product.
    - **qty**: (Optional) The updated quantity of the product.
    - **description**: (Optional) The updated description of the product.
    """
      
    if sku not in inventory:
        return {"message": "Product not found"}
    
    if product_name:
        inventory[sku]["product_name"] = product_name
    if variant:
        inventory[sku]["variant"] = variant
    if price:
        inventory[sku]["price"] = price
    if qty:
        inventory[sku]["qty"] = qty
    if description:
        inventory[sku]["description"] = description

    return {"message": "Product updated successfully"}

# Remove product
@app.delete("/products/{sku}")
def remove_product(sku: str):
    """
    Remove a product from the inventory.

    - **sku**: The SKU of the product to remove.
    """
    if sku not in inventory:
        return {"message": "Product not found"}
    del inventory[sku]
    return {"message": "Product removed successfully"}


# Buy product (Shopping Cart)
@app.post("/cart/total")
def calculate_total(products: dict):
    """
    Shows total amount of products in cart

    - **products**: A dictionary of {product_sku:quantity}

    """
    total = 0.0
    for product_id, qty in products.items():
        if product_id in inventory:
            price = inventory[product_id]["price"]
            total += price * qty
    return {"The total amount of shopping cart is = ": total}


# Global Search
@app.get("/search/{query}")
def search_products(query: str):
    """
    Search across all product features

    - **query**: query word to search products on

    **Returns** — All products that match the query

    """
    results = []
    for sku, product in inventory.items():
        for field, value in product.items():
            if query.lower() in str(value).lower():
                results.append(product)
                break
    return results
