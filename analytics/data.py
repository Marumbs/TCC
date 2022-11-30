import requests

from analytics import config

class Data():

    def __init__(self):
        if config.ALREADY_DOWNLOADDED == False:
            print("Iniciando a captura de dados...")
            database = requests.get(config.URL_DATABASE_ID)
            dictDataBase = self.GetURLs(database)
            self.DownloadCSVs(dictDataBase)
            config.ALREADY_DOWNLOADDED = True
        else:
            print("O download dos arquivos já foram realizados.")

    def GetURLs(self, data) -> dict:
        dictURLs = {}
        dataSplit = data.text.split(config.URL_TO_SPLIT)
        for i in range(len(dataSplit)):
            if (".csv" in dataSplit[i]):
                if ("title" not in dataSplit[i]):
                    dictURLs[dataSplit[i-1].split('title="')[1].split(".csv")[0]] = dataSplit[i].split('a href="')[1].split('" class')[0]
                else:
                    continue
            else:
                continue
        return dictURLs

    def DownloadCSVs(self, dictData) -> None:
        for key, value in dictData.items():
            print("Realizando o download de {0}.csv".format(key))
            data = requests.get(value)
            dataCSV = data.text.replace('\r', '')
            fileCSV = open(config.DIR_TO_SAVE+"{0}.csv".format(key), "w", encoding='UTF-8-SIG')
            fileCSV.write(dataCSV)
            fileCSV.close()