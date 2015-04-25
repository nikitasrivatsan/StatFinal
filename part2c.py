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
    data.sort()
    median = data[len(data) / 2]

    # get bootstrap samples and take their medians
    medians = [0] * NUM_SAMPLES
    for n in range(0,len(medians)):
        indeces = []
        for i in range (0,len(data)):
            indeces.append(randint(0,len(data) - 1))
        # compute bootstrap median
        medians[n] = sorted([data[x] for x in indeces])[len(data) / 2]

    # calculate quantile
    distribution = [abs(x - median) for x in medians]
    quantile = stats.scoreatpercentile(distribution, 95)

    # print data
    print "Bootstrap CI:   " + str(median) + " +- " + str(quantile)

def readData(filename):
    data = []
    for line in open(filename):
        data.append(float(line))
    return data

if __name__ == "__main__":
    main()
