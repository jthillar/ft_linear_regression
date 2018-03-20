#!/usr/bin/python
# -*-coding:Utf-8 -*
import csv
import matplotlib.pyplot as plt

def clean_title(km, price):
    del km[0]
    del price[0]
    return km, price

def opendata():
    file=open("data.csv","r")
    test=csv.reader(file)
    km = list()
    price = list()
    for row in test:
        try:
            km.append(float(row[0]))
            price.append(float(row[1]))
        except:
            km.append(row[0])
            price.append(row[1])
    km, price = clean_title(km, price)
    plt.plot(km, price, "ro")
    plt.xlabel('Km')
    plt.ylabel('Price in Euros')
    plt.scatter(km, price)
    plt.show()
    return km, price

def reduce_list(liste):
    max_list = float(max(liste))
    new_list = []
    for i in range(len(liste)):
        new_list.append(liste[i] / max_list)
    return new_list, max_list

def calc_tmptheta0(km, price, theta0, theta1, alpha):
    m = len(km)
    diff = 0.0
    i = 0
    while i < m:
        diff += (hypothesis(theta0, theta1, km[i]) - price[i])
        i+=1
    tmp0 = theta0 - (alpha * ((1 / float(m)) * diff))
    return tmp0

def calc_tmptheta1(km, price, theta0, theta1, alpha):
    m = len(km)
    diff = 0.0
    i = 0
    for i in range(m):
        diff += (hypothesis(theta0, theta1, km[i]) - price[i]) * km[i]
    tmp1 = theta1 - ((alpha / float(m)) * diff)
    return tmp1

def calc_theta(km, price, theta0, theta1):
    J = float()
    tmpJ = -1.0
    m = len(km)
    alpha = 0.01
    while round(tmpJ, 20) != round(J, 20):
        tmpJ = J
        tmp0 = calc_tmptheta0(km, price, theta0, theta1, alpha)
        tmp1 = calc_tmptheta1(km, price, theta0, theta1, alpha)
        theta0 = tmp0
        theta1 = tmp1
        sumJ = 0.0
        for i in range(m):
            sumJ = sumJ + (hypothesis(theta0, theta1, km[i]) - price[i])**2
        J = (1 / (2 * float(m))) * sumJ
    return(theta0, theta1)

def hypothesis(theta0, theta1, km):
    estimatePrice = float()
    estimatePrice = theta0 + (theta1 * km)
    return (estimatePrice)

def plot_data(theta0, theta1, km, price):
    plt.plot([hypothesis(theta0, theta1, x) for x in range(250000)], "b", linewidth=3)
    plt.plot(km, price, "ro")
    plt.show()

def save_thetas(theta0, theta1):
    fname = "thetas.csv"
    file = open(fname, "wb")
    writer = csv.writer(file)
    print(theta0,theta1)
    writer.writerow((theta0, theta1))

def estimate():
    i = 0
    km, price = opendata()
    m = len(price)
    theta0 = 0.0
    theta1 = 0.0
    km_reduce, max_km = reduce_list(km)
    price_reduce, max_price = reduce_list(price)
    theta0, theta1 = calc_theta(km_reduce, price_reduce, theta0, theta1)
    theta0 = theta0 * max_price
    theta1 = (theta1 * max_price) / max_km
    save_thetas(theta0, theta1)
    plot_data(theta0, theta1, km, price)

estimate()
