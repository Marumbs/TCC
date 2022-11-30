import os
import pandas as pd

from analytics import config

class Analytics:

    def __init__(self):
        dataFrames = self.GetExpensesValue()
        for key, value in dataFrames:
            print("O maior Valor Pago nas {0} foi de R${1}".format(key, value["ValorPago"].max()))

    def GetExpensesValue(self):
        expensesDict = {}
        for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
            for file in files:
                if "despesas" in file:
                    expensesDict[file.split(config.DIR_CSV_FILES)[0].split(".csv")[0]] = pd.read_csv(config.DIR_CSV_FILES + file, encoding='UTF-8-SIG', delimiter = ";")
        return expensesDict