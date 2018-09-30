# Homework02

In order to successfully complete this homework complete following tasks.

1. Create class `Vehicle` which represents any vehicle and carries general
info about the vehicle like: company that built that vehicle, model of the vehicle,
year of production, registration number, engine power and color.
   
	- Override `__str__` method in order to properly display info about the vehicle.
	- Create method `cost_of_registration()` that will return how much will registration
	  cost for that instance of vehicle.
    
	  Use this formula:
    
	       - Production year fees: 100 EUR  if production year < 1990
	                               200 EUR  if production year < 2000
	                               300 EUR  if production year < 2010 
	                               400 EUR  if production year < 2020
	       - On production year fee add engine fee:   (engine power in kw * 2 EUR)

2. Create class `Bus` which extends class `Vehicle` which additionally carries
info about the number of available seats and which company owns it.

    - Override `__str__` method in order to properly display info about the bus.
    - Override method `cost_of_registration()` which will add extra fee for
       number of seats on standard cost of registration.
       Number of seats fee: `(number of seats * 1 EUR)`

Deadline for homework submission is 5th October 2018 at midnight.
You will need to fork this project in order to get your homework reviewed.
