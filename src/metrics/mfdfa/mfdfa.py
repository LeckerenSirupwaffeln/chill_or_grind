# Implementation:
# 0)    Find mean value of our signal of length N
# 1)    Find the cumulative sum of our signal without the mean
# 2)    Select a T set of integers
#       Where the smallest integer is 4, and the largest is N/4
#       Where the integers have geometric progression ( just double it every time )
#
# 3)    For each value of T, divide our cumulative sum into consecutive segments
#       Where each consecutive segment has a length of chosen T integer
#
# 4)    Compute the local trend within a segment using least-squares straight-line fit
#       Alternatively, consider a more robust linear regression method
#       Alternatively, you could even use a non-linear method
#       Whatever can de-trend the signal can be used
#
# 5)    Compute the RMSD from the local trend of each segment
# 6)    Compute the average fluctuation with q order for each q value:
#       If q != 0 then:
#           Take the computed RMSD values of each segment
#           Raise it to the power of q
#           And do that for each segment while summing the result
#           Then take the sum and divide it by the number of segments used
#           This is your mean value of the RMSD values raised to the (q)th order
#           Now raise the final value to 1/q
#
# 7)    Plot log(chosen T value) vs log(fluctuation of q order)
# 8)    Compute the slope of our graph, this is the DFA q order alpha exponent
# 9)    Do all previous steps for every new q value
# 10)   Plot DFA q order alpha exponents against all of the q values
# 11)   Calculate position of the peak and width of the peak for analysis
#
# a)    Typically, the T set integers correspond to time in seconds
# b)    Typically, N will be approximately 5 minutes in length
# c)    Typically, there will be 2 alpha slopes in human R-R interval data
#       The first one is called a1, the second one is called a2
#       If you do not calculate two slopes, you will use a2 by default
#       a1 is for shorter time windows and a2 is for longer time windows
#
# d)    Alternatively, consider sliding window instead in and after step 3
