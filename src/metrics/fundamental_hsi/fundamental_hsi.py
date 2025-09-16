# Implementation:
# 0)    Remove the DC component of the signal
#       Which is just removing the mean of the signal
#
# 1)    Apply hamming window on the signal
# 2)    Perform RFFT on the signal
# 3)    Set all real values to log(magnitude)
# 4)    Set all imaginary values to 0.0
# 5)    Perform IRFFT on the signal to enter the cepstrum domain
#       Which is just the usual time domain but with overlapping cosine frequencies now
#
# 6)    Calculate the Hsi on our fundamental frequency spectrum now
#       This is fundametal Hsi
