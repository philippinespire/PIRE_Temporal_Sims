###Python/pyslim code for generating tree sequences under recent demographic decline scenarios

##Import needed packages
import subprocess
import multiprocessing

##set up needed paths
dir="/scratch/br450/SLiM_temp/"

slim_template= dir + "g1_decline_vars.slim"

output_dir= dir + "g1_n10e3_td300_l99/"

##set up function for running a given demographic scenario: nhistoric=10e3, tdecline=300, lambda=99
def run_sim_n10e3_td300_l99(i):
	TSOF=output_dir+"i"+str(i)+".trees"
	BOF=output_dir+"i"+str(i)+"_breedingsexes.txt"
	MOF=output_dir+"i"+str(i)+"_maleparents.txt"
	FOF=output_dir+"i"+str(i)+"_femaleparents.txt"
	subprocess.check_output(["/home/br450/build/slim","-m","-d","Nhistoric=1000","-d","Tdecline=300","-d","lambda=0.99","-d","TSOutFile='"+TSOF+"'","-d","BOutFile='"+BOF+"'","-d","MOutFile='"+MOF+"'","-d","FOutFile='"+FOF+"'",slim_template])

##run five iterations
a_pool = multiprocessing.Pool()
result = a_pool.map(run_sim_n10e3_td300_l99, range(5))


#next scenario (tdecline=330)

output_dir= dir + "g1_n10e3_td330_l99/"

def run_sim_n10e3_td330_l99(i):
	TSOF=output_dir+"i"+str(i)+".trees"
	BOF=output_dir+"i"+str(i)+"_breedingsexes.txt"
	MOF=output_dir+"i"+str(i)+"_maleparents.txt"
	FOF=output_dir+"i"+str(i)+"_femaleparents.txt"
	subprocess.check_output(["/home/br450/build/slim","-m","-d","Nhistoric=1000","-d","Tdecline=330","-d","lambda=0.99","-d","TSOutFile='"+TSOF+"'","-d","BOutFile='"+BOF+"'","-d","MOutFile='"+MOF+"'","-d","FOutFile='"+FOF+"'",slim_template])

##run five iterations
a_pool = multiprocessing.Pool()
result = a_pool.map(run_sim_n10e3_td330_l99, range(5))


#next scenario (tdecline=360)

output_dir= dir + "g1_n10e3_td360_l99/"

def run_sim_n10e3_td360_l99(i):
	TSOF=output_dir+"i"+str(i)+".trees"
	BOF=output_dir+"i"+str(i)+"_breedingsexes.txt"
	MOF=output_dir+"i"+str(i)+"_maleparents.txt"
	FOF=output_dir+"i"+str(i)+"_femaleparents.txt"
	subprocess.check_output(["/home/br450/build/slim","-m","-d","Nhistoric=1000","-d","Tdecline=360","-d","lambda=0.99","-d","TSOutFile='"+TSOF+"'","-d","BOutFile='"+BOF+"'","-d","MOutFile='"+MOF+"'","-d","FOutFile='"+FOF+"'",slim_template])

##run five iterations
a_pool = multiprocessing.Pool()
result = a_pool.map(run_sim_n10e3_td360_l99, range(5))


#next scenario (tdecline=390)

output_dir= dir + "g1_n10e3_td390_l99/"

def run_sim_n10e3_td390_l99(i):
	TSOF=output_dir+"i"+str(i)+".trees"
	BOF=output_dir+"i"+str(i)+"_breedingsexes.txt"
	MOF=output_dir+"i"+str(i)+"_maleparents.txt"
	FOF=output_dir+"i"+str(i)+"_femaleparents.txt"
	subprocess.check_output(["/home/br450/build/slim","-m","-d","Nhistoric=1000","-d","Tdecline=390","-d","lambda=0.99","-d","TSOutFile='"+TSOF+"'","-d","BOutFile='"+BOF+"'","-d","MOutFile='"+MOF+"'","-d","FOutFile='"+FOF+"'",slim_template])

##run five iterations
a_pool = multiprocessing.Pool()
result = a_pool.map(run_sim_n10e3_td390_l99, range(5))


#last scenario (lambda = 0.95, tdecline=390)

output_dir= dir + "g1_n10e3_td390_l95/"

def run_sim_n10e3_td390_l95(i):
	TSOF=output_dir+"i"+str(i)+".trees"
	BOF=output_dir+"i"+str(i)+"_breedingsexes.txt"
	MOF=output_dir+"i"+str(i)+"_maleparents.txt"
	FOF=output_dir+"i"+str(i)+"_femaleparents.txt"
	subprocess.check_output(["/home/br450/build/slim","-m","-d","Nhistoric=1000","-d","Tdecline=390","-d","lambda=0.95","-d","TSOutFile='"+TSOF+"'","-d","BOutFile='"+BOF+"'","-d","MOutFile='"+MOF+"'","-d","FOutFile='"+FOF+"'",slim_template])

##run five iterations
a_pool = multiprocessing.Pool()
result = a_pool.map(run_sim_n10e3_td390_l95, range(5))


#next scenario (constant!)

output_dir= dir + "g1_n10e3_constant/"

def run_sim_n10e3_constant(i):
	TSOF=output_dir+"i"+str(i)+".trees"
	BOF=output_dir+"i"+str(i)+"_breedingsexes.txt"
	MOF=output_dir+"i"+str(i)+"_maleparents.txt"
	FOF=output_dir+"i"+str(i)+"_femaleparents.txt"
	subprocess.check_output(["/home/br450/build/slim","-m","-d","Nhistoric=1000","-d","Tdecline=500","-d","lambda=0.95","-d","TSOutFile='"+TSOF+"'","-d","BOutFile='"+BOF+"'","-d","MOutFile='"+MOF+"'","-d","FOutFile='"+FOF+"'",slim_template])

##run five iterations
a_pool = multiprocessing.Pool()
result = a_pool.map(run_sim_n10e3_constant, range(5))
