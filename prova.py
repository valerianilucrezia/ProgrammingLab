class Model():

    def fit(self, data):
        #Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')


#creo un oggetto IncrementModel che estende Model e implemento
#la funzione predict()
class IncrementModel(Model):

    def predict(self, data):
        if type(data) is not list:
            raise TypeError

        if len(data) == 1:
            raise Exception

        succ = None
        sum_suc = 0
        prediction = None

        #il valore corrente (t) non deve essere contato:
        #se osservo l'esempio n=3 ma divide per 2
        i = -1
        val_prec = None
        for item in data:
            if (val_prec != None):
                succ = item - val_prec
                sum_suc += succ
            val_prec = item
            i += 1

        prediction = val_prec + int(sum_suc / i)

        return prediction


#model = IncrementModel()
#print(model.predict([None, 2, 3]))
