#!/usr/bin/env python

# Usage: ./part2b.py projectData1.txt

from random import randint
import sys
import scipy
from scipy import stats

NUM_SAMPLES = 10000

def main():
    # read in data
    data = readData(sys.argv[1])
    mean = float(sum(data)) / len(data)
    variance = float(sum([(x - mean) ** 2 for x in data])) / len(data)

    # calculate e
    e = 1.96 * (variance ** 0.5) / (len(data) ** 0.5)

    # get bootstrap samples and take their means
    means = [0] * NUM_SAMPLES
    for n in range(0,len(means)):
        indeces = []
        for i in range (0,len(data)):
            indeces.append(randint(0,len(data) - 1))
        # compute bootstrap mean
        means[n] = float(sum([data[x] for x in indeces])) / len(data)
    mean_means = float(sum(means)) / len(means)

    # calculate quantile
    distribution = [abs(x - mean) for x in means]
    quantile = stats.scoreatpercentile(distribution, 95)

    # print data
    print "Theoretical CI: " + str(mean) + " +- " + str(e)
    print "Bootstrap CI:   " + str(mean_means) + " +- " + str(quantile)

def readData(filename):
    data = []
    for line in open(filename):
        data.append(float(line))
    return data

if __name__ == "__main__":
    main()
