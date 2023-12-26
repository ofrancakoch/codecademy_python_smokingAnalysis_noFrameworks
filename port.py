class Insurance():
    def __init__(self):
        self.arquivo = 'insurance.csv'

    def OpenFile(self, index): #To open file 'insurance.csv and separate it by commas'
        with open(self.arquivo) as csvfile:
            lst = [line.split(',')[index] for line in csvfile]
        csvfile.close()
        return lst

    def UniqueValues(self, index):#To find unique values ​​in certain inserted columns
        lst = list()
        for element in self.OpenFile(index):
            if element not in lst:
                lst.append(element)
        return lst

    def ValueCounting(self, index):#To count occurrences of unique values
        dicio = {}   
        for element in self.OpenFile(index):
            if element in dicio:
                dicio[element] += 1
            else:
                dicio[element] = 1
        return sorted(dicio.items(), key=lambda x:x[1], reverse=True)

    def Filter(self, dicio: dict, index): #To choose by certain inserted conditions
        dio = {}
        for word, value in dicio.items():
            if word in self.UniqueValues(index):
                dio[word] = value
        return sorted(dio.items(), key=lambda x:x[1], reverse=True)

    def SmokingAnalysis(self, afirmneg: str): #Final Analysis (No smokers and smokers).
        dicio = {}
        with open(self.arquivo) as csvfile:
            lst = [line.split(',')for line in csvfile]
            for line in lst:
                if line[4] == afirmneg:
                    for word in line:
                        if word in dicio:
                            dicio[word] += 1
                        else:
                            dicio[word] = 1
        csvfile.close()
        if afirmneg == 'no':
            print("\n\n\t\tSummary\n")
            print("\t\tNo Smokers\n")
            print(f"There are 517 no smoking male and 547 no smoking female.\nProof:\n{self.Filter(dicio,1)}\n")
        elif afirmneg == 'yes':
            print("\n\n\t\tSummary\n")
            print("\t\tSmokers\n")
            print(f"There are 159 smoking male and 115 smoking female.\nProof:\n{self.Filter(dicio,1)}\n")
            print(f"Top three ages that smoke, respectively: 19, 18, 43.\nProof:\n{self.Filter(dicio,0)}\n")
            print(f"There are more smokers at southeast region and at northeast region, respectively.\nProof:\n{self.Filter(dicio,5)}\n")
            print(f"There are more people without children that smoke.\nProof:\n{self.Filter(dicio,3)}\n")
    
analysis = Insurance()
analysis.SmokingAnalysis('yes')
analysis.SmokingAnalysis('no')
print(analysis.UniqueValues(1))
print(analysis.ValueCounting(4))