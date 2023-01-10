class Model():

    def fit(self, data):
        raise NotImplementedError("Metodo non implementato.")

    def predict(self, data):
        raise NotImplementedError("Metodo non implementato.")
            

class IncrementModel(Model):

    def __init__(self, finestra):
        super().__init__()
        self.finestra = finestra

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

    def evaluate(self, data):
        errors = []
        for i in range(len(data)-self.finestra):
            prediction = self.predict(data[i:i+self.finestra])
            error = abs(data[i+self.finestra] - prediction)
            #print(data[i:i+self.finestra], data[i+self.finestra], prediction, error)
            errors.append(error)
        return sum(errors) / len(errors)      
        

class FitIncrementModel(IncrementModel):

    def __init__(self, finestra):
        super().__init__(finestra)
        self.global_avg_increment = None
    
    def predict(self, data):
        super()._check_input_data(data)
        mean_increment = super()._compute_mean_increment(data)
        prediction = data[-1] + (mean_increment + self.global_avg_increment) / 2
        return prediction
        
    def fit(self, data):
        super()._check_input_data(data)
        self.global_avg_increment = super()._compute_mean_increment(data)


# PROVE
# values = [8, 19, 31, 41, 50, 52, 60]
# # values = {'1': 1}
# increment_model = FitIncrementModel(finestra=3)
# increment_model.fit(values[:4])
# print(increment_model.predict(values[-3:]))
# print(increment_model.evaluate(values[-4:]))

# shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

# increment_model_shampoo = IncrementModel(3)
# fit_increment_model_shampoo = FitIncrementModel(3)
# fit_increment_model_shampoo.fit(shampoo_sales[:24])

# print(increment_model_shampoo.evaluate(shampoo_sales[-12:]))
# print(fit_increment_model_shampoo.evaluate(shampoo_sales[-12:]))