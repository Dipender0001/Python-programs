#program to find simple interest and the total amount ,when the principal ,Rate of interest and time are entered by user
p = float(input("enter the principal value : "))
r = float(input("enter the rate of interest: "))
t = float(input("enter the time:"))
si = (p*r*t)/100
print("simple interst is",si)
