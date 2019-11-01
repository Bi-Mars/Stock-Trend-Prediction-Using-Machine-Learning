import csv
dataset = []

with open('apple training dataset (10-14).csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')
	i = 0
	for row in readCSV:
		#print(row)
		dataset.append(row)
		print(dataset[i])
		i += 1