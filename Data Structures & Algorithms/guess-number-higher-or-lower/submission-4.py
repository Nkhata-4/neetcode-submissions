# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        lower = 1
        upper = n
        k = n//2
        res = guess(k)
        while res != 0:
            if res == 1:
                lower = k
                k = upper - round((upper - lower)/2)
            elif res == -1:
                upper = k
                k = lower + round((upper - lower)/2)
            res = guess(k)
        return k

