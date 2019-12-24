import random as r
# N : nombre d attaque
# q : relative hashrate 
# v : double spend attack
# A : maximum authorized attacka
# n : nombre d'attaques 
#This method is a simulation of a simple attack	 (1 cycle)
def simple_attack(A, q, z, v):
	revenue = 0
	nbrBlocksHon = 0
	#phase 0 :
	time = 1/q
	nbrBlocksAtt = 1 # preminage d'un bloc 
	#phase 1 :
	while nbrBlocksAtt != (nbrBlocksHon - A) and nbrBlocksHon <z:
		minedBlock = r.random()
		if minedBlock >= q :
			nbrBlocksHon = nbrBlocksHon + 1  #Honnete wins
		else :
			nbrBlocksAtt = nbrBlocksAtt + 1  #Attack wins
		time = time + 1
	if(nbrBlocksAtt > nbrBlocksHon):
		revenue = v + nbrBlocksAtt #change to Revenue
	#phase 2:
	while True :
		if(nbrBlocksAtt > nbrBlocksHon):
			revenue = v + nbrBlocksAtt
			return [revenue, time]
		if(nbrBlocksHon > nbrBlocksAtt + A):
 			return [0, time]
		minedBlock = r.random()
		if minedBlock >= q :
			nbrBlocksHon = nbrBlocksHon + 1  #Honnete wins
		else :
			nbrBlocksAtt = nbrBlocksAtt + 1  #Attack wins
		time = time + 1


# This methode is a simulation of a double spending attack ( n Cycle)
def double_depense_simulation(n, A, q, z, v):
	revenue_ratio = 0
	revenue = 0
	time = 0
	for i in range(n):
		tab = simple_attack(A, q, z, v)
		revenue = revenue + tab[0]
		time = time + tab[1]
		print("---------Cycle number ",i,"--------")
		print("Revenue of this cycle =", str(tab[0]))
		print("Time passed in this cycle  =",str(tab[1]))
		print("---------End Of Cycle number ",i,"--------")
		print()
	revenue_ratio =revenue / time
	print("------------------End Of the",str(n)," Cycles")
	print("Total Revenue is = ",str(revenue))
	print("Total Time passed is = ",str(time))
	print ("Revenue Ratio of ",str(n)," Cycle is ="+str(revenue_ratio)," CoinBase/UT")
	return revenue_ratio

# This methode is a simulation of a double spending attack ( n Cycle) that returns the revenue_ratio
def double_depense_simulation_without_details(n, A, q, z, v):
	revenue_ratio = 0
	revenue = 0
	time = 0
	for i in range(n):
		tab = simple_attack(A, q, z, v)
		revenue = revenue + tab[0]
		time = time + tab[1]
	revenue_ratio =revenue / time
	return revenue_ratio

# This methode is a simulation of a double spending attack ( n Cycle) that returns the total revenue
def double_depense_simulation_without_details_returns_revenue_perCycle(n, A, q, z, v):
	revenue_ratio = 0
	revenue = 0
	time = 0
	for i in range(n):
		tab = simple_attack(A, q, z, v)
		revenue = revenue + tab[0]
	return revenue / n

# This methode is a simulation of a double spending attack ( n Cycle) that returns the revenue_ratio
def double_depense_simulation_without_details_returns_total_time_perCycle(n, A, q, z, v):
	revenue_ratio = 0
	revenue = 0
	time = 0
	for i in range(n):
		tab = simple_attack(A, q, z, v)
		time = time + tab[1]
	return time / n

# Running an example with this parameters 
#Number of simulation
n=100
#maximum authorized delay 
A=6
#relative Hashrate
q=0.3
#Number of confirmations
z=2
#double spent (in Bitcoin)
v=5
double_depense_simulation(n,A,q,z,v)

#First graph : Ratio rate in function of q
import matplotlib.pyplot as plt
import numpy as np

# relative hashrates
q = np.linspace(0.05, 0.5, 10)
# n of confirmation
z = 2
# double spend amount
v = 1
# max authorized delay
A = 3
# n of simulations
n = 10000

func = []
for i in range(0, len(q)):
    func.append(double_depense_simulation_without_details(n,A,q[i],z,v)) 
# plot
print()
print("Revenue rate over q")
print("v =", v, "bitcoin | z =", z, "blocks | A =", A, "blocks","| n =",n) 
plt.plot(q, func)
plt.plot(q,q)
plt.xlabel("q")
plt.ylabel("revenue ratio (CoinBase/unité_temps)")
plt.show()


#Second Graph:Revenue Rate over q and z
import matplotlib.pyplot as plt
import numpy as np

# n of confirmation
z = np.linspace(1, 10, 10)
# relative hashrates
q = np.linspace(0.05, 0.5, 10)
# double spend amount
v = 5
# n of simulations
n= 10000
# max authorized delay
A = 10

print("")
print("Revenue rate over q and z")
print("v =", v, "Bitcoin")
print("A =", A, "blocks")
print("n =", n, "cycles")
for j in range(0, len(z)):
    func = []
    for i in range(0, len(q)):
        func.append(double_depense_simulation_without_details(n,A,q[i],z[j],v))

    # plot
    plt.plot(q, func, label = "z = "+str(z[j]))

# plot
plt.xlabel("q")
plt.ylabel("revenue rate (Coinbase/unité-temps)")
plt.legend()
plt.title("(d)")
plt.show()
print("")

# graph 4 : Medium Revenue per Cycle in function of q
import matplotlib.pyplot as plt
import numpy as np

# relative hashrates
q = np.linspace(0.05, 0.5, 10)
# n of confirmation
z = 2
# double spend amount
v = 5
# max authorized delay
A = 6
# n of simulations
n = 10000

func = []
for i in range(0, len(q)):
    func.append(double_depense_simulation_without_details_returns_revenue_perCycle(n,A,q[i],z,v))
   
# plot
print()
print("Medium Revenue per cycle over q")
print("v =", v, "bitcoin | z =", z, "blocks | A =", A, "blocks","| n =",n)
plt.plot(q, func)
plt.xlabel("q")
plt.ylabel("Medium Revenue per Cycle ") 
plt.show()


# graph 5 : Medium Time per Cycle in function of q
import matplotlib.pyplot as plt
import numpy as np

# relative hashrates
q = np.linspace(0.05, 0.5, 10)
# n of confirmation
z = 2
# double spend amount
v = 5
# max authorized delay
A = 6
# n of simulations
n = 10000

func = []
for i in range(0, len(q)):
    func.append(double_depense_simulation_without_details_returns_total_time_perCycle(n,A,q[i],z,v))
   
# plot
print()
print("Medium Time per cycle over q")
print("v =", v, "bitcoin | z =", z, "blocks | A =", A, "blocks","| n =",n)
plt.plot(q, func)
plt.xlabel("q")
plt.ylabel("Medium Time (total time per Cycle)") 
plt.show()
