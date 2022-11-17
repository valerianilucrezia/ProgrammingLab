def sum_csv(file):
    my_file = open(file, 'r')
    lines = my_file.readlines()
    values = []
    for l in lines[1:]:
        values.append(float(l.split(',')[1]))
    my_file.close()
    sum_all = sum(values)
    return sum_all

f = 'shampoo_sales.csv'
res = sum_csv(f)
#print(res)


