class Solution:
    def pattern10(self, n):

        # Increasing
        for i in range(1, n + 1):
            for j in range(0, i):
                print("*", end="")
            print()

        # Decreasing
        for k in range(n - 1, 0, -1):
            for m in range(0, k):
                print("*", end="")
            print()