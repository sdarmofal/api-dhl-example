# Example of connection with Polish DHL API

## TODO: project description

## Technology stack:
* Python 3.7.3
* Zeep
* Falcon

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
