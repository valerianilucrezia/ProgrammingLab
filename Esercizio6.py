class CSVFile():

    def __init__(self, name):
        if type(name) is not str:
            raise Exception(
                "Initialize the CSVFile object with a string, not with a {} object."
                .format(type(name)))
        else:
            self.name = name

    def get_data(self, start=None, end=None):
        try:
            file = open(self.name)
        except Exception:
            print(f'Errore: il file specificato "{self.name}" non esiste.')
            return

        file_lines = file.readlines()

        # Controllo che il file non sia vuoto
        if len(file_lines) == 0:
            return []

        # Controllo che start sia convertibile in int e sanitizzo
        if start is None:
            start_clean = 1
        elif type(start) is int or type(start) is float:
            start_clean = int(start)
        elif type(start) is str and start.isdigit():
            start_clean = int(start)
        else:
            raise Exception("Couldn't convert start to int")

        # Controllo che end sia convertibile in int e sanitizzo
        if end is None:
            end_clean = len(file_lines)
        elif type(end) is int or type(end) is float:
            end_clean = int(end)
        elif type(end) is str and end.isdigit():
            end_clean = int(end)
        else:
            raise Exception("Couldn't convert end to int")

        # Ora start e end sono due interi, ma servono altri controlli
        if start_clean <= 0:
            raise Exception("start should be greater than 0.")
        elif start_clean > len(file_lines):
            raise Exception("start should be smaller than the file lenght.")
        elif end_clean > len(file_lines):
            raise Exception("end should be smaller than the file lenght.")
        elif end_clean < start_clean:
            raise Exception("end should be larger than start.")
        else:
            start_clean -= 1
            end_clean -= 1

        data = []

        for i, line in enumerate(file_lines):
            if i > 0 and i >= start_clean and i <= end_clean:
                l = line.strip().split(',')
                data.append(l)
        file.close()
        return data


class NumericalCSVFile(CSVFile):

    def __init__(self, name):
        super().__init__(name)

    def get_data(self, *args, **kwargs):
        numerical_data = super().get_data(*args, **kwargs)
        for values in numerical_data:
            for i, value in enumerate(values):
                if i > 0:
                    try:
                        values[i] = float(value)
                    except Exception as e:
                        print(f'Errore: {e}.')
        return numerical_data


# Comment the following lines to test the program with Autograding
file_name = 'shampoo_sales.csv'

csv_file = CSVFile(file_name)
values = csv_file.get_data(1,2)
print(values)

