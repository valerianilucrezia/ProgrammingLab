my_file = open('shampoo_sales.csv', 'r')
lines = my_file.readlines()
values = []
for l in lines[1:]:
    values.append(float(l.split(',')[1]))
print(sum(values))
my_file.close()
