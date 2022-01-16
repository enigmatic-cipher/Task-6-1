# Given n as input, print the following pattern.
"""
n = 2
y1 
y1y2
"""

n = 5
st = ""
pt = "y"
for i in range(1,n+1):
  st = st + pt + str(i)
  print(st)
