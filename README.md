# trace-inator
Microservice to get routes and place coordinates points

### Getting started
Install dependencies
```
pip install -r requirements.txt
```

Run app in debug mode
```
flask run --debug
```

Port can be set with env variable. E.g. `FLASK_RUN_PORT=2137`. To do this in development mode you can use `.flaskenv` file.
More options can be found in https://flask.palletsprojects.com/en/3.0.x/cli/.

### Documentation
- Flask: https://flask.palletsprojects.com/en/3.0.x/quickstart/
- Schemas: https://flask-marshmallow.readthedocs.io/en/latest/

### API
`GET /api/places`
#### Parameters
- q - text query with place description.
- lat (optional) - latitude of searched area.
- lon (optional) - longitude of searched area.
#### Result
```
{
  "places": [
    {
      "name": str,
      "address": str,
      "coordinates": {
        "lat": float,
        "lon": float
      }
    }
  ]
}
```

`GET /api/trace`
#### Parameters
- origin - lagitude and longitude of starting location, separated by comma.
- destination - lagitude and longitude of destination location, separated by comma.
- mode - transportation mode. Avaialbe `bicycle` and `walking`
- waypoints (optional) - Additional points to pass by. Values are passed as latitude and longitude separated by comma. Multiple waypoints (max allowed 10) must be separated by pipe.
#### Result
```
{
  "paths": [
    {
      "distance": int,
      "duration": int,
      "end_address: str,
      "end_coordinates": {
        "lat": float,
        "lon": float
      },
      "start_address": str,
      "start_coordinates": {
        "lat": str,
        "lon": str
      },
      "steps": [
        {
          "distance": int,
          "duration": int,
          "end_coordinates": {
            "lat": float,
            "lon": float
          },
          "start_coordinates": {
            "lat": str,
            "lon": str
          },
          "instruction": str
        }
      ]
    }
  ]
}
```
