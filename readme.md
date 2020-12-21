# REST API for webshop
This application provides the handler for saving, fetching and managing order data to and from database.

## Get started
For start this application you should be installed following requirements:
- Programming language is [Python 3.8.5](https://www.python.org/downloads/release/python-385/).
- All dependencies install from `pip install -r requirements.txt`.

Declare default environment variables in .env file:
- SECRET_KEY - secret key for a particular Django installation.
- DEBUG - debug mode.
- DATABASE_URL - Django database connection dictionary, populated with all the data specified in your URL. For more information please read the [DJ-Database-URL documentation](https://github.com/jacobian/dj-database-url).

## How to use
Before run the application it recommended to install the virtual environment. In Linux it can be doing like this:

```bash
python3 -m venv env
source env/bin/activate
```
Make a migration:

```bash
./manage.py migrate
```
And run application
```bash
./manage.py runserver
```
### Provided the fillowing functions:
- *Create product* - api/v1/product/create/.
- *All products list* - api/v1/products/all/.
- *Product detail* - api/v1/product/(product_id)/ Change the product data, delete the product.
- *Create order* - api/order/create/.
- *All orders list* - api/order/create/.
- *Order detail* - api/v1/order/(order_id) Change the order data, delete the product.

## License

You can copy, distribute and modify the software.


