import matplotlib.pyplot as plot

class NumericalMethodResult:
	def __init__(self, number_of_points, point_list, estimated_circumference, estimated_area,
		actual_circumference, actual_area, time_area, time_circumference, time_point_list, method):
		self.number_of_points = number_of_points
		self.point_list = point_list
		self.estimated_circumference = estimated_circumference
		self.estimated_area = estimated_area
		self.actual_circumference = actual_circumference
		self.actual_area = actual_area
		self.time_area = time_area
		self.time_circumference = time_circumference
		self.time_point_list = time_point_list
		self.method = method

	def get_x_coordinates(self):
		x_array = []
		for point in self.point_list:
			x_array.append(point[1])
		return x_array

	def get_y_coordinates(self):
		y_array = []
		for point in self.point_list:
			y_array.append(point[2])
		return y_array

	def print(self):
		print('estimated circumference: {} ({} seconds)'.format(self.estimated_circumference, self.time_circumference))
		print('actual permieter: {}'.format(self.actual_circumference))
		print('estimated area: {} ({} seconds)'.format(self.estimated_area, self.time_area))
		print('actual area: {}'.format(self.actual_area))

	# credit to Team-A for laying out how to do the plot
	def plot(self):
		fig, ax = plot.subplots()
		ax.scatter(self.get_x_coordinates(), self.get_y_coordinates(), color="green")
		plot.title(str(self.number_of_points) + (' evenly' if self.method == 1 else ' randomly') + ' spaced points',
			fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 20,
		})
		plot.xlabel("X Coordinates", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.ylabel("Y Coordinates", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		ax.axis('equal')
		plot.show()
