#!/usr/bin/env python

from random import randint
import sys
import scipy
from scipy import stats
from numpy import random

NUM_SAMPLES = 10000

def main():
    # generate data
    data = genData()
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
        m2_n = sorted([data[1][x] for x in indeces2])[len(data[1]) / 2]
        T[n] = abs(m1_n - m2_n - (m1 - m2))

    # calculate percentile
    numLesser = 0
    for t in sorted(T):
        if t <= T_data:
            numLesser += 1
        else:
            break
    p_boot = 1 - (float(numLesser) / len(T))

    # compute T~ and p_sampling
    T_tilda = []
    for i in range(0, NUM_SAMPLES):
        datai = genData()
        datai[0].sort()
        datai[1].sort()
        m1i = data[0][len(data[0]) / 2]
        m2i = data[1][len(data[1]) / 2]
        T_tilda.append(abs(m1i - m2i - (m1 + m2)))

    # calculate percentile
    numLesser = 0
    for t in sorted(T_tilda):
        if t <= T_data:
            numLesser += 1
        else:
            break
    p_sampling = 1 - (float(numLesser) / len(T_tilda))

    # print data
    print "m1: " + str(m1)
    print "m2: " + str(m2)
    print "T_data: " + str(T_data)
    print "p_boot:     " + str(p_boot)
    print "P_sampling: " + str(p_sampling)

def genData():
    data = [[],[]]
    for i in range(0,150):
        data[0].append(random.gamma(2,2))
    for i in range(0,100):
        data[1].append(random.normal(1,2))
    return data

if __name__ == "__main__":
    main()
