q_numbers=3
my_number=[]
cont=0
max_number=0

while (cont+1)<=q_numbers:
    
    mi_num.append(int(input(f'Ingrese el numero{cont+1}')))
    if max_number<=my_number[cont]:
        max_number=my_number[cont]
    cont+=1
print (max_number)