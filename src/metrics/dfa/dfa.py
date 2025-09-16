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
# 6)    Compute the fluctuation ( RMS ) of all the computed RMSD values of all segments
# 7)    Plot log(chosen T value) vs log(fluctuation)
# 8)    Compute the slope of our graph, this is the DFA alpha exponent
#
# a)    Typically, the T set integers correspond to time in seconds
# b)    Typically, N will be approximately 5 minutes in length
# c)    Typically, there will be 2 alpha slopes in human R-R interval data
#       The first one is called a1, the second one is called a2
#       If you do not calculate two slopes, you will use a2 by default
#       a1 is for shorter time windows and a2 is for longer time windows
#
# d)    Alternatively, consider sliding window instead in and after step 3
