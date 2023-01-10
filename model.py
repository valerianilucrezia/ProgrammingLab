class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):

    def __init__(self, finestra):
        super().__init__()
        self.finestra = finestra

    def compute_avg_inc(self, data):
        if type(data) is not list:
            raise TypeError

        nmesi = len(data)
        if nmesi == 1:
            raise Exception

        prev_value = 0
        for i, item in enumerate(data[:-1]):
            prev_value += data[i + 1] - data[i]
        return prev_value / (nmesi - 1)

    def predict(self, data):
        increment = self.compute_avg_inc(data)
        prediction = increment + data[-1]
        return prediction

    def evaluate(self, data):
        errors = []
        for i in range(len(data) - self.finestra):
            prediction = self.predict(data[i:i + self.finestra])
            error = abs(data[i + self.finestra] - prediction)
            errors.append(error)
        return sum(errors) / len(errors)


class FitIncrementModel(IncrementModel):

    def predict(self, data):
        increment = super().compute_avg_inc(data)
        prediction = data[-1] + (increment + self.global_avg_increment) / 2
        return prediction

    def fit(self, data):
        self.global_avg_increment = super().compute_avg_inc(data)


#model = IncrementModel()
#print(model.predict([None, 2, 3]))

#model = FitIncrementModel()
#model.fit([8, 19, 31, 41])
#print(model.predict([50, 52, 60]))
