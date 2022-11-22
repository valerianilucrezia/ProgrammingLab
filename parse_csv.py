def sum_csv(file):
    my_file = open(file, 'r')
    lines = my_file.readlines()
    values = []
    for l in lines[1:]:
        value = l.split(',')[1]
        try:
            float(value)
        except:
            pass
        values.append(float(value))
    my_file.close()
    sum_all = sum(values)
    return sum_all

#f = 'shampoo_sales.csv'
#res = sum_csv(f)
#print(res)


