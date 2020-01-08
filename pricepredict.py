#!/usr/bin/python
# -*-coding:Utf-8 -*

import csv

def opendata():
	theta0 = 0.0
	theta1 = 0.0
	try:
		file = open("thetas.csv", "r")
		test = csv.reader(file)
		for row in test:
			if row[0] == 'theta0':
				theta0 = float(row[1])
			if row[0] == 'theta1':
				theta1 = float(row[1])
	except:
		theta0 = 0.0
		theta1 = 0.0
	return theta0, theta1

def estimate():
	# givenKM = float(input("For what mileage you would like estimate your price ? :"))
	theta0, theta1 = opendata()
	if theta0 == 0.0 and theta1 == 0:
		print("thetas are not yet been evaluated")
	else:
		while True:
			try:
				givenKm = input("Give a milesage to estimate a price ? ")
				if givenKm == 'quit':
					break
				givenKm = int(givenKm)
				if givenKm < 0:
					print("milesage must be positive")
				else:
					estimatePrice = theta0 + theta1 * givenKm
					if estimatePrice >= 0:
						print("A car with {} km should cost {} euros".format(int(round(givenKm, 0)), int(round(estimatePrice, 0))))
					else:
						print("The regression shows that a car with {} km should cost {} euros, so it means 0 euros".format(int(round(givenKm, 0)), int(round(estimatePrice, 0))))
					break
			except:
				print("Km should be an integer")



if __name__ == '__main__':
	estimate()
