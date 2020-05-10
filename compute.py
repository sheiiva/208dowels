############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#          Project : 208dowels_2019        #
#                                          #
############################################


from math import factorial


class Compute():

    """
    Computation class.
    """

    def computeProbabilty(self, piecePerSample, nbSample, x, Ox) -> int:

        """
        Return the probability to have a defective piece out of a sample.
        """

        sumfactorial = 0
        for i in range(len(x)):
            sumfactorial += (x[i][0] * Ox[i])
        return sumfactorial / (piecePerSample * nbSample)

    def binomialCoef(self, n, k) -> int:
        
        """
        Return binomial coefficient as B(n, p).
        """

        return factorial(n) // (factorial(k) * factorial(n-k))

    def binomial(self, n, k, p) -> int:

        """
        Return the probability distribution of the number of successes
            in independent Bernouilli trials of probability p.
        """

        return self.binomialCoef(n, k) * (p**k) * ((1-p)**(n-k))

    def computeTheoreticalSize(self, x, piecePerSample, nbSample, p) -> int:

        """
        Return theorical size.
        """ 

        return nbSample * self.binomial(piecePerSample, x, p)