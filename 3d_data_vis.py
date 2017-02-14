from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import csv
import os

def return_csv_data(filename):

	x = []
	y = []
	z = []

	with open (filename, 'r') as csvfile:
		data = csv.reader(csvfile, delimiter=',')
		for row in data:
			x.append((float(row[0])))
			y.append((float(row[1])))
			z.append((float(row[1])))

	return x, y, z

def save_snapshot(x, y, z, inc_value):
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(x,y,z)

	ax.set_xlabel('X Axis')
	ax.set_ylabel('Y Axis')
	ax.set_zlabel('Z Axis')

	ax.view_init(elev=10, azim=inc_value % 180)
	filename = '{}.png'.format(inc_value)
	plt.savefig(filename, bbox_inches='tight')
	plt.close()

def main():
	inc_value = 0
	for f in os.listdir('.'):
		if f.endswith('.csv'):
			x, y, z = return_csv_data(f)
			save_snapshot(x, y, z, inc_value)
			print "[+] On number {}".format(inc_value)
			inc_value += 1



main()



# GRAPH STUFF
# READ DATA FROM A CSV FILE, PLOT IT, TAKE SNAPSHOT (Eventually multiple while it rotates), LOAD NEXT CSV, PLOT, SNAPSHOT, ETC
# 