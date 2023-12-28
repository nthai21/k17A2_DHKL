a=float(input("Lãi suất 1 năm (%):"))
b=int(input("Số tiền gửi :"))
c=int(input("Số tháng gửi :"))
tien_lai = (b*c)*a
tong=b+tien_lai
print("Tiền lãi :",tien_lai,"vnd")
print("Tiền vốn + lãi: ",tong,"vnd")