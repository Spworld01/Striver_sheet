class Solution:
    def pattern11(self, n):

        for i in range(0, n):

            if i % 2 == 0:
                start = 1
            else:
                start = 0

            for j in range(0, i + 1):

                print(start, end="")

                if j != i:
                    print(" ", end="")

                start = 1 - start

            print()