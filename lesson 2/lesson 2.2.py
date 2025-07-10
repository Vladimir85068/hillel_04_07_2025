number_five =10417

f = number_five//10000
d = (number_five%100)//1000
c = (number_five%1000)//100
b = (number_five%100)//10
a = number_five%10

print(a*10000 + b*1000 + c*100 + d*10 + f)
