class Vehicle():
    def __init__(self, company, model, year_of_production, registration_number, power, color):
        self.company = company
        self.model = model
        self.year_of_production = year_of_production
        self.registration_numberr = registration_number
        self.power = power
        self.color = color
    def __str__(self):
        return "Company that built that vehicle : {0}, Model of the vehicle: {1}, Year of product: {2}, Registration nuber: {3}, " \
               "Engine power: {4}kW, Colour: {5}".format(self.company, self.model, self.year_of_production, self.registration_numberr, self.power, self.color)
    def cost_of_registration(self):
        if int(self.year_of_production)< 1990:
            production_year_fee = 100
        elif int(self.year_of_production)< 2000:
            production_year_fee = 200
        elif int(self.year_of_production)< 2010:
            production_year_fee = 300
        else:
            production_year_fee = 400
        fee1 = production_year_fee + int(self.power)*2
        return fee1
class Bus(Vehicle):
     def __init__(self, company, model, year_of_production, registration_number, power, color, number_of_seats, ownership_of_the_company):
         Vehicle.__init__(self, company, model, year_of_production, registration_number, power, color)
         self.numer_of_seats=number_of_seats
         self.ownership_of_the_company=ownership_of_the_company
     def __str__(self):
         return "Company that built that bus : {0}, Model of the bus: {1}, Year of product: {2}, Registration number: {3}, Engine power: {4}kW, Colour: {5}, " \
                "Number of seats: {6}, Ownership of the company: {7}".format(self.company, self.model, self.year_of_production, self.registration_numberr,
                                                                             self.power, self.color,self.numer_of_seats,self.ownership_of_the_company)
     def cost_of_registration(self):
         fee2=int(Vehicle.cost_of_registration(self))+int(self.numer_of_seats)
         return fee2
print("")
vehicleNo1 = Vehicle("Audi", "A4", "2006", "BR-BP313", "77", "red" )
print(vehicleNo1)
print("Registration for this vehicle will cost : " + str(Vehicle.cost_of_registration(vehicleNo1)) +" EUR")
print("")
BusNo1=Bus("Iveco","Sanos","1995","PG-BP115","200","red","30","Bulatovic")
print(BusNo1)
print("Registration for this bus will cost : " + str(Bus.cost_of_registration(BusNo1)) +" EUR")