import math
import random
import time
from numerical_method_result import NumericalMethodResult
from metrics import Metrics

def main():
	# These are lists that are built up while performing the estimation on [3..number_of_points] points
	time_circumference_list = []       # execution times in estimating the circumference
	time_area_list = []                # execution times in estimating the area
	accuracy_circumference_list = []   # [0%..100%] accuracy list in circumference estimation
	accuracy_area_list = []            # [0%..100%] accuracy list in area estimation
	number_of_points_list = []         # list of the number_of_points
	estimated_circumference_list = []  # list of the estimated circumferences
	estimated_area_list = []           # list of the estimated areas

	center_x, center_y, radius, number_of_points, method = get_inputs()

	# run the following for all number_of_points, but just plot the last one
	for n in range(3, number_of_points + 1):
		result = run_numerical_method(center_x, center_y, radius, n, method)
		time_circumference_list.append(result.time_circumference)
		time_area_list.append(result.time_area)
		number_of_points_list.append(n)
		estimated_circumference_list.append(result.estimated_circumference)
		estimated_area_list.append(result.estimated_area)
		accuracy_circumference = accuracy(result.actual_circumference, result.estimated_circumference)
		accuracy_area = accuracy(result.actual_area, result.estimated_area)
		accuracy_circumference_list.append(accuracy_circumference)
		accuracy_area_list.append(accuracy_area)
		# print('number of points: {}, circumference accuracy: {}%, area_accuracy: {}%, time: {}s'.format(n, accuracy_circumference, accuracy_area, result.time_point_list + result.time_circumference + result.time_area))
		# result.print()
		if n == number_of_points:
			# extra credit #3, just take an estimated circumference and divide by 2*radius
			print('pi estimated to be approximately {}.'.format(result.estimated_circumference / (2 * radius) ))
			result.plot()

	# gather the metrics from above and stuff them into a Metrics object for nice packaging, show various plots
	metrics = Metrics(time_circumference_list, time_area_list, number_of_points_list, accuracy_circumference_list,
		accuracy_area_list, estimated_circumference_list, estimated_area_list)
	metrics.plot_n_vs_circumference()
	metrics.plot_n_vs_area()
	metrics.plot_n_vs_circumference_cpu_time()
	metrics.plot_n_vs_area_cpu_time()

def get_inputs():
	while True:
		try:
			center_x = float(input('x-coordinate of center of circle: '))
		except ValueError:
			print('requires a float, try again.')
			continue
		break
		
	while True:
		try:
			center_y = float(input('y-coordinate of center of circle: '))
		except ValueError:
			print('requires a float, try again.')
			continue
		break
		
	while True:
		try:
			radius = float(input('radius of circle: '))
			if radius < 0:
				raise ValueError()
		except ValueError:
			print('requires a non-negative float, try again.')
			continue
		break

	while True:
		try:
			number_of_points = int(input('number of points on the circumference: '))
			if number_of_points < 3:
				raise ValueError()
		except ValueError:
			print('requires an integer greater than 2, try again.')
			continue
		break

	while True:
		try:
			method = int(input('point generation method (1=evenly spaced, 2=randomly spaced): '))
			if method != 1 and method != 2:
				raise ValueError()
		except ValueError:
			print('requires either 1 or 2, try again.')
			continue
		break

	return center_x, center_y, radius, number_of_points, method;

# calls the methods that generate the point list, estimate circumference, and estimate area
def run_numerical_method(center_x, center_y, radius, number_of_points, method):
	point_list, time_point_list = generate_point_list(center_x, center_y, radius, number_of_points, method)
	estimated_circumference, time_circumference = estimate_circumference(point_list)
	actual_circumference = math.pi * radius * 2
	estimated_area, time_area = estimate_area_by_summing_radial_triangles(point_list, center_x, center_y, method)
	# below is an implementation to satisfy extra credit #2
	# estimated_area, time_area = estimate_area_by_summing_oriental_fan_triangles(point_list, center_x, center_y, method)
	actual_area = math.pi * radius * radius
	result = NumericalMethodResult(
		number_of_points,
		point_list,
		estimated_circumference,
		estimated_area,
		actual_circumference,
		actual_area,
		time_area,
		time_circumference,
		time_point_list,
		method
		)
	return result

# generates either an evenly or randomly distributed list of points on a circle;
# the returned point_list is a list of triples of the form (theta, x, y)
def generate_point_list(center_x, center_y, radius, number_of_points, method):
	start_time = time.time()
	point_list = []
	theta = random.uniform(0, 360)
	current_point = 0
	while current_point < number_of_points:
		x, y = locate_point(center_x, center_y, radius, theta)
		point_list.append((theta, x, y))
		theta = theta + 360 / number_of_points if method == 1 else random.uniform(0, 360)
		current_point += 1
	point_list.sort()
	end_time = time.time()
	return point_list, end_time - start_time

# given a circle and theta (angle in degrees), returns the point on the circle at theta degrees
def locate_point(center_x, center_y, radius, theta):
	x = center_x + radius * math.cos(math.radians(theta))
	y = center_y + radius * math.sin(math.radians(theta))
	return x, y

# simle method to compare an event to the ground truth target and return an accuracy rating in [0%..100%]
def accuracy(target, event):
	return (1 - (abs(target - event) / target)) * 100

# calculates circumference by summing up the line segments determined by adjacent points in the point_list
def estimate_circumference(point_list):
	start_time = time.time()
	size = len(point_list)
	index = 0
	distance = 0
	while index < size - 1:
		distance += euclidean_distance(point_list[index], point_list[index + 1])
		index += 1
	distance += euclidean_distance(point_list[size - 1], point_list[0]) # add int he last one to make the circle complete
	end_time = time.time()
	return distance, end_time - start_time

# calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
	return math.sqrt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

# calculates the area by summing up the areas of the isosceles triangles formed by two adjacent points and the center
def estimate_area_by_summing_radial_triangles(point_list, center_x, center_y, method):
	start_time = time.time()
	center_tuple = (0, center_x, center_y)
	size = len(point_list)
	index = 0
	area = 0
	# Team-B did this optimization
	if method == 1:
		area = area_of_triangle(center_tuple, point_list[0], point_list[1]) * size
	elif method == 2:
		while index < size - 1:
			area += area_of_triangle(center_tuple, point_list[index], point_list[index + 1])
			index += 1
		area += area_of_triangle(center_tuple, point_list[size - 1], point_list[0])
	end_time = time.time()
	return area, end_time - start_time

# calculates the area by summing up the areas of the triangles formed by two adjacent
# points and the first point in the list (somewhat looks like an oriental fan)
def estimate_area_by_summing_oriental_fan_triangles(point_list, center_x, center_y, method):
	start_time = time.time()
	center_tuple = (0, center_x, center_y)
	size = len(point_list)
	index = 0
	area = 0
	while index < size - 2:
		area += area_of_triangle(point_list[0], point_list[index + 1], point_list[index + 2])
		index += 1
	end_time = time.time()
	return area, end_time - start_time

# calculate the area of an arbitrary triangle by summing the discriminants of a matrix of coeficients (points),
# a point index of 1 is the x-coordinate, an index of 2 is the y-coordinate
def area_of_triangle(p1, p2, p3):
	return abs(
		(p1[1] * p2[2] - (p2[1] * p1[2])) +
		(p2[1] * p3[2] - (p3[1] * p2[2])) +
		(p3[1] * p1[2] - (p1[1] * p3[2]))
		) / 2

if __name__ == '__main__':
	main()
