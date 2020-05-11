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

        chiSquare = 0

        for i in range(len(self._Ox)):
            chiSquare += ((self._Ox[i] - self._Tx[i]) ** 2) / self._Tx[i]

        print("Chi-squared:\t\t{:.3f}".format(chiSquare))

    def freedomDegrees(self):

        """
        Compute and print degrees of freedom.
        """

        

        print("Degrees of freedom:\t{:d}".format(0))

    def fitValidity(self):

        """
        Compute and print fit validity.
        """

        print("Distribution:\t\t[..]")

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
