# Example of connection with Polish DHL API

## About
This project is an example for blog post on https://sdarmofal.dev. It's a sample of establishing connection with polish 
DHL API.  

## Technology stack:
* Python 3.9.0
* Zeep
* Falcon

## Available API endpoints

* `/version` - check DHL API version
* `/shipment` - create shipment
* `/pickup` - book courier for shipment
* `/label` - get shipment label

## Request examples:
### Create shipment
```json
{
	"shipper": {
		"name": "Testomir Testalski",
		"postalCode": "10003",
		"city": "Olsztyn",
		"street": "Testowa",
		"houseNo": "1a"
	},
	"receiver": {
		"name": "Odbiorca Odbieralski",
		"postalCode": "10001",
		"city": "Olsztyn",
		"street": "Testowa",
		"houseNo": "1a",
		"country": "PL"
	},
	"packages": [
		{
			"type": "PACKAGE",
			"width": 1,
			"height": 1,
			"length": 1,
			"weight": 1,
			"quantity": 1
		},
		{
			"type": "PACKAGE",
			"width": 2,
			"height": 2,
			"length": 2,
			"weight": 2,
			"quantity": 1
		}
	],
	"services": {
		"product": "AH"
	},
	"shipment_date": "2019-04-10",
	"content": "test"
}
```

### Courier pickup
```json
{
	"shipment_id": "90006589406",
	"pickup_date": "2019-04-11",
	"hour_from": "09:00",
	"hour_to": "16:00"
}
```

### Get label
```json
{
	"label_type": "LP", 
	"shipment_id": "90006589406"
}
```

## Configuration

To establish connection with DHL API you need access data. 
If you have it, you must properly set environment variables to run this application.
I prefer to use .env file to do this. 

In project files you can find `.env.default` that contains placeholders for required
environment variables. Save it as `.env` and change placeholders to your access data.

### Environment variables

* `DHL.WSDL` - url to DHL API WSDL file
* `DHL.SAP` - payer client identifier (SAP). Necessary for payer type set to USER or SHIPPER
* `DHL.user` - DHL client username
* `DHL.pass` - DHL client password 
  
## Running

To run the application follow the steps from [Configuration](#configuration). Then 
use pipenv to create environment:

```shell
pipenv install
```

After that you can run application from virtualenv:

```shell
pipenv shell
gunicorn src.api.api:api
```
