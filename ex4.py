cars = 100
space_in_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_car
average_passanger_per_car = passangers / cars_driven
print("There are", cars, "available")
print("There are only", drivers, "available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", car_pool_capacity, "people today")
print("We have", passangers, "passangers to car pool toady")
print("We have to put about", average_passanger_per_car, "passangers per car")