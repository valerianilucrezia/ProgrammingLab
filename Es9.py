class Model():

    def fit(self, data):
        raise NotImplementedError("Metodo non implementato.")

    def predict(self, data):
        raise NotImplementedError("Metodo non implementato.")
            

class IncrementModel(Model):

    def _check_input_data(self, data):
        if type(data) is not list:
            raise TypeError
        if len(data) <= 1:
            raise Exception("La lunghezza del file deve essere > 1.")

    def _compute_mean_increment(self, data):
        sum_increments = 0
        for i, item in enumerate(data):
            if i > 0:
                sum_increments += item - data[i-1]
        mean_increment = sum_increments / (len(data)-1)
        return mean_increment

    def predict(self, data):
        self._check_input_data(data)
        mean_increment = self._compute_mean_increment(data)
        prediction = data[-1] + mean_increment
        return prediction


class FitIncrementModel(IncrementModel):
    
    def predict(self, data):
        super()._check_input_data(data)
        mean_increment = super()._compute_mean_increment(data)
        prediction = data[-1] + (mean_increment + self.global_avg_increment) / 2
        return prediction
        
    def fit(self, data):
        super()._check_input_data(data)
        self.global_avg_increment = super()._compute_mean_increment(data)


# # PROVE
# values = [8, 19, 31, 41, 50, 52, 60]
# # values = {'1': 1}
# increment_model = FitIncrementModel()
# increment_model.fit(values[:4])
# print(increment_model.predict(values[-3:]))