class CSVFile:
    def __init__(self,name):

 

        if isinstance(name, str):
            self.name=name
        else:
            raise Exception('Il nome del file non è una stringa')

        self.can_read=True

        try:
            file=open(self.name,'r')
            file.readline()
        except Exception as e:
            self.can_read=False
            print('Errore in apertura del file: {}\n'.format(e))

 

    def get_data(self, start=None, end=None):

 

        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None

        else:
            file=open(self.name,'r')
            list_list=[]
            n_max=0
            for line in file:
                    n_max=n_max+1

 

            if not isinstance(start, int) and start is not None:
                raise Exception('start va di tipo intero')
            if not isinstance(end, int) and end is not None:
                raise Exception('end va di tipo intero')

 

            if start is not None and end is not None and start>end:
                raise Exception('Errore: start è maggiore di end')

 

            if start is not None and start<=0:
                raise Exception('Il parametro start "{}" non ha un indice accettabile; è sotto il minimo(1) '.format(start))

 

            if start is not None and start>n_max:
                raise Exception('Il parametro start "{}" non ha un indice accettabile; va oltre il massimo ({})'.format(start,n_max))

 

            if end is not None and end>n_max:
                raise Exception('Il parametro end "{}" non ha un indice accettabile; va oltre il massimo ({})'.format(end,n_max))

            if end is not None and end<=0:
                raise Exception('Il parametro end "{}" non ha un indice accettabile; è sotto il minimo(1)'.format(end))

 

            if start is None:
                file=open(self.name,'r')
                if end is None:
                    for line in file:
                        elements=line.strip('\n').split(',')
                        if elements[0]!='Date':
                            list_list.append(elements)
                else:
                    if end==1:
                        list_list=[]
                    else:
                        for i, line in enumerate(file):
                            if i<end:
                                elements=line.strip('\n').split(',')
                                if elements[0]!='Date':
                                    list_list.append(elements)
            else:
                file=open(self.name,'r')
                if start==1:

                    if end==1:
                        file.close()
                        return(list_list)
                    else:
                        start=start+1

                if end is None:
                    for i, line in enumerate(file):
                        if i>=start-1:
                            elements=line.strip('\n').split(',')
                            if elements[0]!='Date':
                                list_list.append(elements)
                else:
                    for i, line in enumerate(file):
                        print(i)
                        if i>=start-1 and i<end:
                            elements=line.strip('\n').split(',')
                            if elements[0]!='Date':
                                list_list.append(elements)

 

            file.close()
            return(list_list)

 

class NumericalCSVFile(CSVFile):   
    def get_data(self):#, *args, **kwargs
        lista_lista=super().get_data()#*args, **kwargs
        if lista_lista!=None:
        #print(lista_lista)
            for l in lista_lista:
                for i,item in enumerate(l):
                    if i!=0:
                        if item!='Sales':
                            try:
                                    l[i]=float(item)
                                    #print(isinstance(item[1],float))
                                    #print('{}'.format(item[1]))
                            except ValueError:
                                print('Errore il dato che si presumeva float non lo è! Lo ha generato: {}'.format(l[i]))
                            except TypeError:
                                print('Errore hai sbagliato il tipo di dato!')
                            except Exception as e:
                                print('Errore generico: {}'.format(e))

        return lista_lista
        
file_csv = CSVFile('shampoo_sales.csv')
print(file_csv.get_data(start='6'))  #end esplicito esempio end=5
print('{}'.format(file_csv.get_data(4,9)))