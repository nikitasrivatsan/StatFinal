#!/usr/bin/env python

# Usage: ./part2a.py projectData1.txt

from random import randint
import sys

NUM_SAMPLES = 10000

def main():
    # read in data
    data = readData(sys.argv[1])
    mean = float(sum(data)) / len(data)
    variance = float(sum([(x - mean) ** 2 for x in data])) / len(data)

    # get bootstrap samples and take their means
    means = [0] * NUM_SAMPLES
    for n in range(0,len(means)):
        indeces = []
        for i in range (0,len(data)):
            indeces.append(randint(0,len(data) - 1))
        # compute bootstrap mean
        means[n] = float(sum([data[x] for x in indeces])) / len(data)

    # calculate mean and variance of means
    mean_means = float(sum(means)) / len(means)
    var_means = float(sum([(x - mean_means) ** 2 for x in means])) / len(means)

    # print data
    print "T:  " + str(mean)
    print "T*: " + str(mean_means)
    print "Var(T):  " + str(variance / len(data))
    print "Var(T*): " + str(var_means)

def readData(filename):
    data = []
    for line in open(filename):
        data.append(float(line))
    return data

if __name__ == "__main__":
    main()
