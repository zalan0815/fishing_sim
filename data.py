'''
Name;MinMass;MaxMass;MinLength;MaxLength;IsEndangered
Ponty;2,0;20,0;0,3;1,0;N
'''
class data:
    def __init__(self, row: str):
        data = row.split(';')
        self.name = data[0]
        self.min_mass = float(data[1].replace(',', '.'))
        self.max_mass = float(data[2].replace(',', '.'))
        self.min_length = float(data[3].replace(',', '.'))
        self.max_length = float(data[4].replace(',', '.'))
        self.endangered = data[5]

class data2:
    def __init__(self, row: str):
        data = row.split(';')
        self.name = data[0]
        self.mass = float(data[1].replace(',', '.'))
        self.length = float(data[2].replace(',', '.'))




