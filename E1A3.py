user =input("PLITHOS ORWN MONO AKERWN THETIKWN:===>")
while True:
 user =input("PLITHOS ORWN MONO AKERWN THETIKWN:===>")
 if user.isdigit():
  user=int(user)
  break
 else:
   user =input("mono akereoi thetikoi")

#apo=0#apotelesma teliko
count=1
for x in range(1,user,1):
 count=count*2
 d=1+1/x*2
print(d)
