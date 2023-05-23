# CZero-Assignment

This is a simple REST API for managing an inventory of CZero Pens. The API allows you to retrieve, add, update, and remove products from the inventory. It also provides functionality for calculating the total amount of products in a shopping cart and performing global searches across the inventory.

## API Endpoints

### Get Whole Inventory

- Endpoint: `GET /products`
- Description: Retrieves the full inventory database.
- Response: JSON object containing all products in the inventory.

### Get Product by SKU

- Endpoint: `GET /products/{sku}`
- Description: Retrieves product details based on the SKU.
- Parameters:
  - **sku**: The SKU of the product to retrieve.
- Response: JSON object containing the product details if found, or an error message if the product is not found.

### Add New Product

- Endpoint: `POST /products`
- Description: Adds a new product to the inventory.
- Parameters:
  - **product_name**: The name of the product.
  - **variant**: (Optional) The variant of the product.
  - **sku**: The SKU of the product.
  - **price**: The price of the product.
  - **qty**: The quantity of the product.
  - **description**: (Optional) The description of the product.
- Response: JSON object with a success message if the product is added successfully, or an error message if the SKU already exists.

### Update Product Quantity

- Endpoint: `PUT /products/{operation}/{sku}`
- Description: Updates the quantity of a product in the inventory.
- Parameters:
  - **operation**: Specifies whether to add or delete the quantity. Enter 'add' or 'delete'.
  - **sku**: The SKU of the product.
  - **qty**: The quantity of the product to add or delete.
- Response: JSON object with a success message if the inventory is updated successfully, or an error message if the product is not found.

### Update Product

- Endpoint: `PUT /products/{sku}`
- Description: Updates a product in the inventory.
- Parameters:
  - **sku**: The SKU of the product to update.
  - **product_name**: (Optional) The updated name of the product.
  - **variant**: (Optional) The updated variant of the product.
  - **price**: (Optional) The updated price of the product.
  - **qty**: (Optional) The updated quantity of the product.
  - **description**: (Optional) The updated description of the product.
- Response: JSON object with a success message if the product is updated successfully, or an error message if the product is not found.

### Remove Product

- Endpoint: `DELETE /products/{sku}`
- Description: Removes a product from the inventory.
- Parameters:
  - **sku**: The SKU of the product to remove.
- Response: JSON object with a success message if the product is removed successfully, or an error message if the product is not found.

### Buy Product (Shopping Cart)

- Endpoint: `POST /cart/total`
- Description: Calculates the total amount of products in a shopping cart.
- Parameters:
  - **products**: A dictionary of {product_sku:quantity}.
- Response: JSON object containing the total amount of the shopping cart.

### Global Search

- Endpoint: `GET /search/{query}`
- Description: Performs a global search across all product features.
- Parameters:
  - **query**: The query word to search products on.
- Response: JSON object containing all products that match the query.

## Data Store

The inventory is stored in a Python dictionary, representing the data store for this API. Each product is identified by its SKU, and the dictionary stores the following
