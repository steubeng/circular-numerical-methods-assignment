import matplotlib.pyplot as plot

# this class holds the data for extra cretid #1
class Metrics:
	def __init__(self, time_circumference_list, time_area_list, number_of_points_list, accuracy_circumference_list,
		accuracy_area_list, estimated_circumference_list, estimated_area_list):
		self.time_circumference_list = time_circumference_list
		self.time_area_list = time_area_list
		self.number_of_points_list = number_of_points_list
		self.accuracy_circumference_list = accuracy_circumference_list
		self.accuracy_area_list = accuracy_area_list
		self.estimated_circumference_list = estimated_circumference_list
		self.estimated_area_list = estimated_area_list

	def plot_n_vs_circumference(self):
		fig, ax = plot.subplots()
		ax.scatter(self.number_of_points_list, self.estimated_circumference_list, color="green")
		plot.title('N vs Circumference', fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 20,
		})
		plot.xlabel("Number of Points", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.ylabel("Estimated Circumference (units)", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.show()

	def plot_n_vs_area(self):
		fig, ax = plot.subplots()
		ax.scatter(self.number_of_points_list, self.estimated_area_list, color="green")
		plot.title('N vs Area', fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 20,
		})
		plot.xlabel("Number of Points", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.ylabel("Estimated Area (square units)", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.show()

	def plot_n_vs_circumference_cpu_time(self):
		fig, ax = plot.subplots()
		ax.scatter(self.number_of_points_list, self.time_circumference_list, color="green")
		plot.title('N vs Circumference CPU Time', fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 20,
		})
		plot.xlabel("Number of Points", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.ylabel("Time (seconds)", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.show()

	def plot_n_vs_area_cpu_time(self):
		fig, ax = plot.subplots()
		ax.scatter(self.number_of_points_list, self.time_area_list, color="green")
		plot.title('N vs Area CPU Time', fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 20,
		})
		plot.xlabel("Number of Points", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.ylabel("Time (seconds)", fontdict={'family':'serif',
			'color':'black',
			'weight':'bold',
			'size': 12,
		})
		plot.show()
