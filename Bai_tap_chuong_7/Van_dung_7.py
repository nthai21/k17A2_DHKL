tien_doi=int(input("Nhập số tiền muốn đổi :"))
so_to_1=tien_doi//500000
tien_con_lai=tien_doi%500000
print("Số tờ 500000 là :",so_to_1)
so_to_2=tien_con_lai//200000
tien_con_lai=tien_con_lai%200000
print("Số tờ 200000 là :",so_to_2)
so_to_3=tien_con_lai//100000
tien_con_lai=tien_con_lai%100000
print("Số tờ 100000 là :",so_to_3)
so_to_4=tien_con_lai//50000
tien_con_lai=tien_con_lai%50000
print("Số tờ 50000 là :",so_to_4)
print("Số tiền còn lại là :",tien_con_lai)