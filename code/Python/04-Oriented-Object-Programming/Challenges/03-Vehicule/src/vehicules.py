from datetime import datetime

class Vehicules():
	"""
    Write a class Vehicle :
    Parameters:
    -----------
    year
    brand
    color
    wheels 
    consumption
    fuel
    kilometers
    speed = 0
    start()
    stop()
    accelerate()
    brake()
    with an increment or decrement of speed by 10 each time it is called.
    Start a timer when the vehicle start and stop the timer when the vehicle 
    stop. Meanwhile, update the kilometersand the fuel depending on the driving (speed, accelerate and stop)
    Write two new classes Car and Motorbikes. Imagine what could 
    change in the attributes and methods.
    Review the control access in all the previous classes.
	"""
	def __init__(self, year, brand, color, wheels, consumption, fuel, kilometers, speed = 0):
		self.year = year
		self.brand = brand
		self.color = color
		self.wheels = wheels
		self.consumption = consumption
		self.fuel = fuel
		self.kilometers = kilometers
		self.speed = speed
		self.start_time = 0
		self.duration = 0

	def start(self):
		return datetime.now().microsecond
		

	def stop(self, start_time):
		duration = datetime.now().microsecond - start_time
		distance = [(duration, 0)]
		return distance 

	def accelerate(self, start_time):
		self.speed += 10 
		duration = datetime.now().microsecond - start_time
		distance = [(duration, self.speed)]
		return distance 

	def brake(self, start_time):
		self.speed -= 10 
		duration = datetime.now().microsecond - start_time
		distance = [(duration, self.speed)]
		return distance 


#print(Vehicules.accelerate())
vehicule1 = Vehicules(2018, 'Peugeot', 'bleue', 'weel', 5, 50, 10, 0) 
start = vehicule1.start()

deplacement = []

deplacement += vehicule1.accelerate(start)
deplacement += vehicule1.accelerate(start)
deplacement += vehicule1.brake(start)
deplacement += vehicule1.accelerate(start)
deplacement += vehicule1.accelerate(start)
deplacement += vehicule1.accelerate(start)
deplacement += vehicule1.brake(start)
deplacement += vehicule1.stop(start)

print(deplacement)

'''
for dep in deplacement:
	if dep[1] == 0 :
	print(dep[1])
'''


class Car(Vehicules):
	def __init__(self):
		super().__init__()
		pass

class Motorbikes(Vehicules):
	def __init__(self):
		super().__init__()
		pass
