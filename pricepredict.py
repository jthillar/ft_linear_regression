#!/usr/bin/python
# -*-coding:Utf-8 -*

import csv

def opendata():
	theta0 = 0.0
	theta1 = 0.0
	try:
		file = open("thetas.csv","r")
		test=csv.reader(file)
		for row in test:
			theta0 = float(row[0])
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
		while 1:
			try:
				givenKm = input("Give a milesage to estimate a price ? ")
				givenKm = int(givenKm)
				break
			except:
				print("Km should be an integer")
		estimatePrice = theta0 + theta1 * givenKm
		print("A car with {} km should cost {} euros".format(int(round(givenKm, 0)), int(round(estimatePrice, 0))))

estimate()
