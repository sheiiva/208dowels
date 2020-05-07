############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#          Project : 208dowels_2019        #
#                                          #
############################################


class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for arguments validity.
        """

        def isInt(value) -> bool:
            
            """Expect for value to be an integer."""

            try:
                int(value)
            except ValueError:
                return False
            else:
                return True

        aSum = 0

        if len(argv) is not 10:
            print("Wrong number of arguments. Please retry with -h.")
            return 84
        for i in range(1, len(argv)):
            if not isInt(argv[i]) or int(argv[i]) < 0:
                print("Arguments must be positive integers. Please retry with -h.")
                return 84
            aSum += int(argv[i])
        if aSum is not 100:
            print("Arguments' sum must be equal to 100. Please retry with -h.")
            return 84
        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
