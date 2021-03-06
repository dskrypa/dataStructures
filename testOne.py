'''
Author: Douglas Skrypa
Date: 2014.09.18
'''
import timeit

if __name__ == "__main__":
	repFreq = 1000
	numTests = 3
	stp = '''
import random
t = set()
s = set()
for x in range(1000):
	t.add(random.randint(0,1000))
	s.add(random.randint(0,1000))
'''
	t = timeit.Timer("s.intersection(t)", stp)
	runTime = t.timeit(repFreq)						#Time in seconds
	runAvg = (runTime/repFreq)*1000000				#Time in microseconds
	
	print("Time for "+str(repFreq)+" runs: "+str(runTime)+" s\t(Avg: "+str(runAvg)+" microseconds")
	print("Repeating 3 times...")
	
	r = t.repeat(3, repFreq)
	repMin = min(r)
	repMin_avg = repMin/repFreq*1000000
	repMax = max(r)
	repMax_avg = (repMax/repFreq)*1000000
	print("Min run time: "+str(repMin)+"s\t(Avg: "+str(repMin_avg)+" microseconds)")
	print("Max run time: "+str(repMax)+"s\t(Avg: "+str(repMax_avg)+" microseconds)")
#/main
