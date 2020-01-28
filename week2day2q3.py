s1=int("21")
s2=int("70")
s3=int("72")
s4=int("72")
s5=int("13")

avg=(s1+s2+s3+s4+s4+s5)/5

if(avg>=90):
    print("G: A")
elif(avg>=70 and avg<90):
    print("G: B")
elif(avg>=50 and avg<70):
    print("G: C")
elif(avg>=30 and avg<50):
    print("G: D")
else:
    print("G: F")