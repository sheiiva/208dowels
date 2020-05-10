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

from compute import Compute

class Dowels():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._compute = Compute()
        self._input = []
        self._p = 0

    def parseInput(self):
        
        """
        Parse input into the _input list.
        """

        for index in range(1, len(argv)):
            self._input.append(int(argv[index]))

    def statisticalArray(self):

        """
        Compute and print an array showing observed
            and theoretical sizes for each statistical class (with totals).
        """

        return 0

    def run(self):

        """
        Run computations and process output printing.
        """

        self.parseInput()

        return 0
