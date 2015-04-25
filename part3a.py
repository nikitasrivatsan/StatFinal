#!/usr/bin/env python

# Usage: ./part3c.py projectData3.txt

from random import randint
import sys
import scipy
from scipy import stats

NUM_SAMPLES = 10000

def main():
    # read in data
    data = readData(sys.argv[1])
    data[0].sort()
    data[1].sort()
    m1 = data[0][len(data[0]) / 2]
    m2 = data[1][len(data[1]) / 2]
    T_data = abs(m1 - m2)

    # get bootstrap samples and take their medians
    T = [0] * NUM_SAMPLES
    for n in range(0,len(T)):
        indeces1 = []
        for i in range (0,len(data[0])):
            indeces1.append(randint(0,len(data[0]) - 1))
        indeces2 = []
        for i in range (0,len(data[1])):
            indeces2.append(randint(0,len(data[1]) - 1))

        # compute bootstrap medians and T
        m1_n = sorted([data[0][x] for x in indeces1])[len(data[0]) / 2]
        m2_n = sorted([data[1][x] for x in indeces1])[len(data[1]) / 2]
        T[n] = abs(m1_n - m2_n - (m1 - m2))

    # calculate percentile
    numLesser = 0
    for t in sorted(T):
        if t <= T_data:
            numLesser += 1
        else:
            break
    p = 1 - (float(numLesser) / len(T))

    # print data
    print "m1: " + str(m1)
    print "m2: " + str(m2)
    print "T_data: " + str(T_data)
    print "p: " + str(p)

def readData(filename):
    data = [[],[]]
    for line in open(filename):
        (obs, population) = line.split()
        data[int(population) - 1].append(float(obs))
    return data

if __name__ == "__main__":
    main()
