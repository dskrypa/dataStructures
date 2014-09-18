'''
Author: Douglas Skrypa
Date: 2014.09.18
'''
import timeit

def getSetup(sizeT, sizeS):
	stp = '''
import random
t = set()
s = set()
for x in range('''+str(sizeT)+'''):
	t.add(random.randint(0,'''+str(sizeT)+'''))
for x in range('''+str(sizeS)+'''):
	s.add(random.randint(0,'''+str(sizeS)+'''))
'''
	return stp
#/getSetup

def μSecs(secs):
	return secs*1000000
#/μSecs

if __name__ == "__main__":
	exps = {3,4,5,6}
	repFreq = 1000
	numTests = 3
	fmt = "{:4,f}"
	
	for et in exps:
		et = pow(10, et)
		for es in exps:
			es = pow(10, es)
			print("len(t): "+"{:,}".format(et)+"\tlen(s): "+"{:,}".format(es))
			
			t = timeit.Timer("s.intersection(t)", getSetup(et, es))
			timed = t.timeit(repFreq)
			timed_avg = μSecs(timed/repFreq)
			print("Time for "+"{:,}".format(repFreq)+" runs: "+fmt.format(timed)+" s\t(Avg: "+fmt.format(timed_avg)+"μs)")
			
			print("Repeating "+str(numTests)+" times...")
			r = t.repeat(numTests, repFreq)
			repMin = min(r)
			repMin_avg = μSecs(repMin/repFreq)
			repMax = max(r)
			repMax_avg = μSecs(repMax/repFreq)
			print("Min run time: "+fmt.format(repMin)+"s\t(Avg: "+fmt.format(repMin_avg)+" μs)")
			print("Max run time: "+fmt.format(repMax)+"s\t(Avg: "+fmt.format(repMax_avg)+" μs)")
			print("----------------------------------------")
#/main
