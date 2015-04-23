#!/usr/bin/env python

from random import randint

def main():
    Z = [0] * 1000
    for n in range(1,1001):
        vals = {}
        for i in range (1,n+1):
            vals[randint(1,n)] = 1
        Z[n - 1] = len(vals.keys())

    # print out Z
    output = open("output", "w")
    for i in range(1,1001):
        output.write(str(i) + "," + str(Z[i - 1]) + "\n")

if __name__ == "__main__":
    main()
