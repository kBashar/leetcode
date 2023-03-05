class Solution:

    def minimumSum(self, num: int) -> int:
        """
        Sort the digits in ascending order.
        create two 2 digit number.
        Numbers should have smallest number at the most significant position.
        Sum the resultant two number and return.

        Example:
         4203
         sort => [0, 2, 3, 4]
         2 digit numbers => 04, 23
         Minumum Sum => 27 

         1100
         sort => [0, 0, 1, 1]
         2 digit numbers => 01, 01
         Minumum Sum => 2 
        """

        num_s = list(str(num))
        num_s.sort()

        # create a two digit number using smllest and largest digit
        right_half = int(num_s[0]+num_s[3])

        # create a two digit number using second smllest and second largest digit
        left_half = int(num_s[1]+num_s[2])

        return right_half + left_half
        
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSum(2304))
    print(sol.minimumSum(1100))

