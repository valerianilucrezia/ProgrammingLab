class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        file = open(self.name, 'r')
        lines = file.readlines()
        values = []
        for l in lines[1:]:
            v1 = l.split(',')[0]
            v2 = str(l.split(',')[1].strip('\n'))
            values.append([v1, v2])
        return values


#file = CSVFile('shampoo_sales.csv')
#print(file.name)
#print(file.get_data())
