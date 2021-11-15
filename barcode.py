str1 = str(input("Enter Barcode: "))
s1=[int(str1[i])for i in range(0,11,2)]
s2=[int(str1[i])for i in range(1,11,2)]
sum_s1=sum(s1)*3
sum_s2=sum(s2)
s3=sum_s1+sum_s2
s3=s3%10
if s3==0:
    last_digit=s3
else:
    last_digit=10-s3

x=int(str1[11])

if x==last_digit:
    print("Barcode's check_digit is correct")
else:
    print("Barcode's check digit is incorrect")

