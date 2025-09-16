# Implementation:
# 0)    Find highest spectral peak within a chosen frequency band
#       Call this spectral peak F_m
#       Make sure to remove DC component and apply Hamming window if needed beforehand
#
# 1)    Calculate total power within the frequency range of F_m +- L/2, as S_L
# 2)    Calculate totwer power within the frequency range ranging from F_m +- w/2
#       Call that S_W
#       Where w is simply a range of values between 0 to and including L/2
#
# 3)    Calculate R_w as ratio of S_w  to S_L for a given w/2
# 4)    Calculate Hsi as area under curve of R_w, convert Hsi to a percentage
#       So just divide the AUC by L to get a % result
#
# a)    Typically, a frequency band of 0.15 Hz to 0.45 Hz can be used
# b)    Typically, an L value of 0.14 Hz can be used
# c)    Typically, we can use 5 minute segments of R-R interval data
