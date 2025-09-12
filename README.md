# chill_or_grind

How do you know when to chill or when to grind? Sweat not, this is the perfect script to find out
Analyze your heart-rate interval data to get the answers you have always sought
Learn when is the best time to sleep, eat, poop, work, or do sports, and much more!
Basically this module shows you when your parasympathetic nervous system is dominant and when your sympathetic system is dominant

# Implementation
For fun and hopefully a better solution let us avoid doing doing the detrended fluctuation analysis the usual way, instead let us:

1) Find trends using segmented regression
2) Detrend those trends
3) Use a sliding window approach to calculate fluctuation