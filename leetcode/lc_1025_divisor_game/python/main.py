from typing import List


class Solution:
    def divisors(self, N: int) -> List[int]:
        """

        Divisors Helper Function

        Time Complexity: O(n)
        Space Complexity: O(n)

        """

        # initialize an output array to store divisors
        output = []

        # iterate from 1 to N (exclusive) and if the modulus
        # equals 0, append it to the output array
        for num in range(1, N):
            if N % num == 0:
                output.append(num)

        return output

    def divisorGame_dp(self, N: int) -> bool:
        """

        Dynamic Programming Solution (Bottom Up)

        Time Complexity: O(n)
        Space Complexity: O(n)

        """

        # create our results from solving subproblems
        dp = [False for _ in range(N + 1)]

        # start from the "bottom" and build up to the solution
        for num in range(2, N + 1):

            # find divisors and check if num - divisor is false is in
            # our results storage (represents Alice giving Bob a losing #)
            divisors_of_num = Solution.divisors(self, num)
            for divisor in divisors_of_num:
                if dp[num - divisor] == False:
                    dp[num] = True
                    break

        # return if Alice can win starting at N
        return dp[N]

    def divisorGame_math(self, N: int) -> bool:
        """

        Math Solution

        Time Complexity: O(1)
        Space Complexity: O(1)

        If the starting number is even, Alice can always
        force Bob into an odd number resulting in a win for
        Alice.

        If the starting number is odd, Alice can only give
        Bob an even number resulting in a win for Bob.

        """

        return N % 2 == 0
