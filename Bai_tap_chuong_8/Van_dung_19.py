n=int(input("Nhập vào dãy số bất kỳ :"))
lat = 0 
while n!=0:
    lat= lat *10  + n % 10
    n//=10
print(lat)