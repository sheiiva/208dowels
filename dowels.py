############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#          Project : 208dowels_2019        #
#                                          #
############################################


from sys import argv
from copy import deepcopy

from compute import Compute

dist_table = [[99, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 2, 1],
              [0.00, 0.02, 0.06, 0.15, 0.27, 0.45, 0.71, 1.07, 1.64, 2.71, 3.84, 5.41, 6.63],
              [0.02, 0.21, 0.45, 0.71, 1.02, 1.39, 1.83, 2.41, 3.22, 4.61, 5.99, 7.82, 9.21],
              [0.11, 0.58, 1.01, 1.42, 1.87, 2.37, 2.95, 3.66, 4.64, 6.25, 7.81, 9.84, 11.34],
              [0.30, 1.06, 1.65, 2.19, 2.75, 3.36, 4.04, 4.88, 5.99, 7.78, 9.49, 11.67, 13.28],
              [0.55, 1.61, 2.34, 3.00, 3.66, 4.35, 5.13, 6.06, 7.29, 9.24, 11.07, 13.39, 15.09],
              [0.87, 2.20, 3.07, 3.83, 4.57, 5.35, 6.21, 7.23, 8.56, 10.64, 12.59, 15.03, 16.81],
              [1.24, 2.83, 3.82, 4.67, 5.49, 6.35, 7.28, 8.38, 9.80, 12.02, 14.07, 16.62, 18.48],
              [1.65, 3.49, 4.59, 5.53, 6.42, 7.34, 8.35, 9.52, 11.03, 13.36, 15.51, 18.17, 20.09],
              [2.09, 4.17, 5.38, 6.39, 7.36, 8.34, 9.41, 10.66, 12.24, 14.68, 16.92, 19.68, 21.67],
              [2.56, 4.87, 6.18, 7.27, 8.30, 9.34, 10.47, 11.78, 13.44, 15.99, 18.31, 21.16, 23.21]]

class Dowels():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._compute = Compute()
        self._input = []
        self._x = [[i] for i in range(9)]
        self._Ox = []
        self._Tx = []
        self._p = 0
        self._chiSquare = 0
        self._freedom = 0

    def parseInput(self):

        """
        Parse input into the _input list.
        """

        for index in range(1, len(argv)):
            self._input.append(int(argv[index]))
        self._Ox = deepcopy(self._input)

    def statisticalArray(self):

        """
        Compute and print an array showing observed
            and theoretical sizes for each statistical class (with totals).
        """

        def normalizeEntries():

            """
            Compute ._x and .Ox lists' values.
            """

            def merge(lst, index):
                lst[index] += lst[index+1]
                lst.pop(index+1)

            i = 0
            while i < len(self._Ox):
                if self._Ox[i] < 10:
                    if i is 0:
                        merge(self._Ox, i)
                        merge(self._x, i)
                    elif i is len(self._Ox)-1:
                        merge(self._Ox, i-1)
                        merge(self._x, i-1)
                    else:
                        if (self._Ox[i-1] <= self._Ox[i+1]):
                            merge(self._Ox, i-1)
                            merge(self._x, i-1)
                        else:
                            merge(self._Ox, i)
                            merge(self._x, i)
                else:
                    i += 1

        def printXLine():
            print(" x\t|", end='')
            for x in self._x:
                if (len(x) > 1):
                    if (x[-1] is 8):
                        print(" {}+\t|".format(x[0]), end='')
                    else:
                        print(" {}-{}\t|".format(x[0], x[-1]), end='')
                else:
                    if (x[0] is 8):
                        print(" {}+\t|".format(x[0]), end='')
                    else:
                        print(" {}\t|".format(x[0]), end='')
            print(" Total")

        def printOxLine():
            print("0x\t|", end='')
            for Ox in self._Ox:
                print(" {}\t|".format(Ox), end='')
            print(" 100")

        def printTxLine():
            print("Tx\t|", end='')
            rest = 100
            for xray in self._x:
                tmp = 0
                for x in xray:
                    tmp += self._compute.computeTheoreticalSize(x, 100, 100, self._p)
                rest -= tmp
                if xray is self._x[-1]:
                    tmp += rest
                self._Tx.append(tmp)
                print(" {:.1f}\t|".format(tmp), end='')
            print(" 100")

        normalizeEntries()
        printXLine()
        printOxLine()
        printTxLine()

    def distribution(self):

        """
        Compute and print distribution.
        """

        print("Distribution:\t\tB(100, {:.4f})".format(self._p))

    def chiSquared(self):

        """
        Compute and print chi-squared.
        """

        for i in range(len(self._Ox)):
            self._chiSquare += ((self._Ox[i] - self._Tx[i]) ** 2) / self._Tx[i]

        print("Chi-squared:\t\t{:.3f}".format(self._chiSquare))

    def freedomDegrees(self):

        """
        Compute and print degrees of freedom.
        """

        self._freedom = len(self._x) - 2

        print("Degrees of freedom:\t{:d}".format(self._freedom))

    def fitValidity(self):

        """
        Compute and print fit validity.
        """

        v = []
        
        for x in range(len(dist_table[self._freedom])):
                if (dist_table[self._freedom][x] < self._chiSquare) and (x < 12):
                    v.append(dist_table[0][x + 1])

        if (len(v) == 0):
            print("Fit validity:\t\tP > 99%")
        elif (len(v) > 0 and (self._chiSquare > dist_table[self._freedom][len(v)])):
            print("Fit validity:\t\tP < 1%")
        else:
            print("Fit validity:\t\t{}% < P < {}%".format(v[len(v) - 1], v[len(v) - 2]))

    def run(self):

        """
        Run computations and process output printing.
        """

        self.parseInput()
        self._p = self._compute.computeProbabilty(100, 100, self._x, self._Ox)
        self.statisticalArray()
        self.distribution()
        self.chiSquared()
        self.freedomDegrees()
        self.fitValidity()
