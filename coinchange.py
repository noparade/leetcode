def mincoins(amount,coins):
  if not coins or amount < min(coins):
    return None
  d = [float('inf')]*(amount+1)
  for i in xrange(1,amount+1):
    temp = float('inf')
    for e in coins:
      if e <= i:
        temp = min(temp,d[i-e]+1)
    d[i] = min(d[i],temp)
  return d[-1]
  
#def dynamicCoinChange( T, L ):

#	Opt = [0 for i in range(0, L+1)]
#	n = len(T)
#	for i in range(1, L+1):
#		smallest = float("inf")
#		for j in range(0, n):
#			if (T[j] <= i):
#				smallest = min(smallest, Opt[i - T[j]]) 
#		Opt[i] = 1 + smallest 
#	return Opt[L]
