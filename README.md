# README #

For a given Shopping Store, the app scraps the website and collects the addresses of all store locations of all cities in India.
The address is stored in a Relational Database and validates each location with location on Google Maps and flags the incorrect location
by validating with Google Map API. The application exposes an API endpoint ```/result``` which outputs the list of invalid store addresses.

### Techs Used ###
1. Beautifulsoup - For scrapping the Web and store the addresses
2. Django - Backend Service and REST API
3. MySQL - Database Storage

### Running the application ###
1. Clone the repository ```location-validator-app```
2. Go to directory ```location-validator-app```
3. Run the command ```docker-compose up -d```


### API Endpoint ###
1. The API endpoint is ```localhost:8000/result``` is a GET method.
2. The input to the API is provided in the request body in JSON format


### Input and Output ###
1. The API call is made to ```localhost:8000/result```
2. The output is returned as a JSON object of invalid location.<br>

### Tests ###
#### Test Case 1 ####
INPUT:<br>
OUTPUT:
RESULT: PASS <br>

### Demo ###
<img src="demo/app_running.png" width="100" height="100" >
<img src="demo/rest_api_call.png" width="100" height="100" >

