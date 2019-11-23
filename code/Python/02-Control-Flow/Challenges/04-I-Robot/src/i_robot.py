"""
Control the movements of a basic robot
"""
import math

def main():

	x, y = (0,0)
	while True:

		instruction = input("What is ur direction")
		if instruction == 'quit':
			print(x, y)
			break
		else :
			direction, steps = instruction.split(" ")
		
		steps = int(steps)

		if direction == 'UP':
			y += steps
		elif direction == 'DOWN':
			y -= steps
		elif direction == 'RIGHT':
			x += steps
		elif direction == 'LEFT':
			x -= steps
		

	distance = math.sqrt(x**2 + y**2)
	print("Total distance from original point : {}".format(distance))


if __name__ == '__main__':
    main()

