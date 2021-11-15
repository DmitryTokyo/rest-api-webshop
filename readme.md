# REST API for webshop
This application provides the handler for saving, fetching and managing order data to and from database. It is a test of python web developer vacancy.

## Get started
For start this application you should be installed following requirements:
- Programming language is [Python 3.10.0](https://www.python.org/downloads/release/python-3100/).
- All dependencies install from `pip install -r requirements.txt`.

Declare default environment variables in .env file. Read more in [django-environ](https://django-environ.readthedocs.io/en/latest/):
- SECRET_KEY - secret key for a particular Django installation.
- DEBUG - debug mode.
- DATABASE_URL - Django database connection dictionary, populated with all the data specified in your URL.

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


