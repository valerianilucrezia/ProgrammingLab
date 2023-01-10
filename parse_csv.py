def sum_list(nome_file):
    values = []
    my_file = open(nome_file, 'r')
    #lines = my_file.readlines()
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
    return sum(values) ##qua 
print(sum_list('shampoo_sales.csv'))


#f = 'shampoo_sales.csv'
#res = sum_csv(f)
#print(res)


