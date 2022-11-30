from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
    )
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
    )
import os
import math
from analytics import config
import pandas as pd

class Telegram():

    def __init__(self):
        self.df_csv = {}
        for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
            for file in files:
                if "csv" in file:
                    print("Criando o DataFrame do arquivo {0}".format(file))
                    self.df_csv[file.split(".csv")[0]] = pd.read_csv(config.DIR_CSV_FILES + "\\" + file, encoding='UTF-8-SIG', delimiter = ";")

    ############################## BOT ####################################################
    def start(self, update, context):
        update.message.reply_text("Olá, eu sou o Bot de Consulta de Dados do governo do Espírito Santo. Para consultar algum dado, basta digitar /info para obter as informações.")

    def info(self, update, context):
        menu_main = [[InlineKeyboardButton("Despesas", callback_data="dp")],
                     [InlineKeyboardButton("Restos a Pagar", callback_data="rp")]]
        reply_markup = InlineKeyboardMarkup(menu_main)
        update.message.reply_text("Selecione qual base de dados quer consultar:", reply_markup=reply_markup)

    def email(self, update, context):
        update.message.reply_text("Para entrar em contato com o suporte basta mandar um e-mail para o contato suporteconsultadadoses@gmail.com")
    
    def main_menu(self, update, context):
        query = update.callback_query
        if query.data == "mp":
            menu_main = [[InlineKeyboardButton("Despesas", callback_data="dp")],
                        [InlineKeyboardButton("Restos a Pagar", callback_data="rp")]]
            reply_markup = InlineKeyboardMarkup(menu_main)
            update.callback_query.edit_message_text("Selecione qual base de dados quer consultar:", reply_markup=reply_markup)
    
    def menu_infos(self, update, context):
        query = update.callback_query
        if query.data == "dp":
            menu_dp = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        count_files += 1
                        menu_dp.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="d{0}".format(count_files))])
            menu_dp.append([InlineKeyboardButton("Menu Principal", callback_data="mp")])
            reply_markup = InlineKeyboardMarkup(menu_dp)
            update.callback_query.edit_message_text("Escolha o ano que quer consultar:", reply_markup=reply_markup)
        elif query.data == "sd":
            menu_sd = []
            menu_sd.append([InlineKeyboardButton("Farmácia", callback_data="a1")])
            menu_sd.append([InlineKeyboardButton("Menu Principal", callback_data="mp")])
            reply_markup = InlineKeyboardMarkup(menu_sd)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "rp":
            menu_rp = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("restos" in file) or ("Restos" in file):
                        count_files += 1
                        menu_rp.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="r{0}".format(count_files))])
            menu_rp.append([InlineKeyboardButton("Menu Principal", callback_data="mp")])
            reply_markup = InlineKeyboardMarkup(menu_rp)
            update.callback_query.edit_message_text("Escolha o ano que quer consultar:", reply_markup=reply_markup)

    def menu_dp(self, update, context):
        query = update.callback_query
        if query.data == "d1":
            menu_dp1 = []
            menu_dp1.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m1")])
            menu_dp1.append([InlineKeyboardButton("Valor Pago total", callback_data="v1")])
            menu_dp1.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c1")])
            menu_dp1.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp1)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d2":
            menu_dp2 = []
            menu_dp2.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m2")])
            menu_dp2.append([InlineKeyboardButton("Valor Pago total", callback_data="v2")])
            menu_dp2.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c2")])
            menu_dp2.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp2)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d3":
            menu_dp3 = []
            menu_dp3.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m3")])
            menu_dp3.append([InlineKeyboardButton("Valor Pago total", callback_data="v3")])
            menu_dp3.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c3")])
            menu_dp3.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp3)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d4":
            menu_dp4 = []
            menu_dp4.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m4")])
            menu_dp4.append([InlineKeyboardButton("Valor Pago total", callback_data="v4")])
            menu_dp4.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c4")])
            menu_dp4.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp4)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d5":
            menu_dp5 = []
            menu_dp5.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m5")])
            menu_dp5.append([InlineKeyboardButton("Valor Pago total", callback_data="v5")])
            menu_dp5.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c5")])
            menu_dp5.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp5)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d6":
            menu_dp6 = []
            menu_dp6.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m6")])
            menu_dp6.append([InlineKeyboardButton("Valor Pago total", callback_data="v6")])
            menu_dp6.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c6")])
            menu_dp6.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp6)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d7":
            menu_dp7 = []
            menu_dp7.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m7")])
            menu_dp7.append([InlineKeyboardButton("Valor Pago total", callback_data="v7")])
            menu_dp7.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c7")])
            menu_dp7.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp7)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d8":
            menu_dp8 = []
            menu_dp8.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m8")])
            menu_dp8.append([InlineKeyboardButton("Valor Pago total", callback_data="v8")])
            menu_dp8.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c8")])
            menu_dp8.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp8)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d9":
            menu_dp9 = []
            menu_dp9.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m9")])
            menu_dp9.append([InlineKeyboardButton("Valor Pago total", callback_data="v9")])
            menu_dp9.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c9")])
            menu_dp9.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp9)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "d10":
            menu_dp10 = []
            menu_dp10.append([InlineKeyboardButton("Maior valor pago de despesa", callback_data="m10")])
            menu_dp10.append([InlineKeyboardButton("Valor Pago total", callback_data="v10")])
            menu_dp10.append([InlineKeyboardButton("Comparar Valor Pago Total com outra Despesa", callback_data="c10")])
            menu_dp10.append([InlineKeyboardButton("Outras Despesas", callback_data="dp")])
            reply_markup = InlineKeyboardMarkup(menu_dp10)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)

    def menu_rp(self, update, context):
        query = update.callback_query
        if query.data == "r1":
            menu_rp1 = []
            menu_rp1.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp1")])
            menu_rp1.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt1")])
            menu_rp1.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp1)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "r2":
            menu_rp2 = []
            menu_rp2.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp2")])
            menu_rp2.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt2")])
            menu_rp2.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp2)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "r3":
            menu_rp3 = []
            menu_rp3.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp3")])
            menu_rp3.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt3")])
            menu_rp3.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp3)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "r4":
            menu_rp4 = []
            menu_rp4.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp4")])
            menu_rp4.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt4")])
            menu_rp4.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp4)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "r5":
            menu_rp5 = []
            menu_rp5.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp5")])
            menu_rp5.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt5")])
            menu_rp5.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp5)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "r6":
            menu_rp6 = []
            menu_rp6.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp6")])
            menu_rp6.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt6")])
            menu_rp6.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp6)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "r7":
            menu_rp7 = []
            menu_rp7.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp7")])
            menu_rp7.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt7")])
            menu_rp7.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp7)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
        elif query.data == "r8":
            menu_rp8 = []
            menu_rp8.append([InlineKeyboardButton("Maior valor processado de Restos A Pagar", callback_data="mp8")])
            menu_rp8.append([InlineKeyboardButton("Valor total de Restos A Pagar", callback_data="vt8")])
            menu_rp8.append([InlineKeyboardButton("Outros Restos A Pagar", callback_data="rp")])
            reply_markup = InlineKeyboardMarkup(menu_rp8)
            update.callback_query.edit_message_text("Selecione a informação que quer obter:", reply_markup=reply_markup)
    
    def menu_dp_max(self, update, context):
        query = update.callback_query
        if query.data == "m1":
            menu_dp1_max = []
            index_max = self.df_csv["Despesas-2004"][self.df_csv["Despesas-2004"]["ValorPago"] == self.df_csv["Despesas-2004"]["ValorPago"].max()].index[0]
            menu_dp1_max.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp1_max)
            if (type(self.df_csv["Despesas-2004"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2004"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2004"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2004"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2004"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2004"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2004"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2004"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2004"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2004"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m2":
            menu_dp2_max = []
            index_max = self.df_csv["Despesas-2006"][self.df_csv["Despesas-2006"]["ValorPago"] == self.df_csv["Despesas-2006"]["ValorPago"].max()].index[0]
            menu_dp2_max.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp2_max)
            if (type(self.df_csv["Despesas-2006"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2006"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2006"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2006"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2006"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2006"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2006"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2006"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2006"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2006"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m3":
            menu_dp3_max = []
            index_max = self.df_csv["Despesas-2007"][self.df_csv["Despesas-2007"]["ValorPago"] == self.df_csv["Despesas-2007"]["ValorPago"].max()].index[0]
            menu_dp3_max.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp3_max)
            if (type(self.df_csv["Despesas-2007"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2007"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2007"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2007"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2007"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2007"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2007"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2007"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2007"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2007"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m4":
            menu_dp4_max = []
            index_max = self.df_csv["Despesas-2009"][self.df_csv["Despesas-2009"]["ValorPago"] == self.df_csv["Despesas-2009"]["ValorPago"].max()].index[0]
            menu_dp4_max.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp4_max)
            if (type(self.df_csv["Despesas-2009"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2009"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2009"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2009"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:    
                if (math.isnan(self.df_csv["Despesas-2009"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2009"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2009"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2009"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2009"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2009"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m5":
            menu_dp5_max = []
            index_max = self.df_csv["Despesas-2010"][self.df_csv["Despesas-2010"]["ValorPago"] == self.df_csv["Despesas-2010"]["ValorPago"].max()].index[0]
            menu_dp5_max.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp5_max)
            if (type(self.df_csv["Despesas-2010"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2010"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2010"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2010"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:    
                if (math.isnan(self.df_csv["Despesas-2010"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2010"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2010"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2010"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2010"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2010"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m6":
            menu_dp6_max = []
            index_max = self.df_csv["Despesas-2011"][self.df_csv["Despesas-2011"]["ValorPago"] == self.df_csv["Despesas-2011"]["ValorPago"].max()].index[0]
            menu_dp6_max.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp6_max)
            if (type(self.df_csv["Despesas-2011"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2011"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2011"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2011"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2011"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2011"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2011"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2011"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2011"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2011"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m7":
            menu_dp7_max = []
            index_max = self.df_csv["Despesas-2012"][self.df_csv["Despesas-2012"]["ValorPago"] == self.df_csv["Despesas-2012"]["ValorPago"].max()].index[0]
            menu_dp7_max.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp7_max)
            if (type(self.df_csv["Despesas-2012"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2012"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2012"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2012"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2012"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2012"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2012"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2012"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2012"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2012"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m8":
            menu_dp8_max = []
            index_max = self.df_csv["Despesas-2013"][self.df_csv["Despesas-2013"]["ValorPago"] == self.df_csv["Despesas-2013"]["ValorPago"].max()].index[0]
            menu_dp8_max.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp8_max)
            if (type(self.df_csv["Despesas-2013"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2013"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2013"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2013"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2013"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2013"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2013"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2013"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2013"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2013"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m9":
            menu_dp9_max = []
            index_max = self.df_csv["Despesas-2020"][self.df_csv["Despesas-2020"]["ValorPago"] == self.df_csv["Despesas-2020"]["ValorPago"].max()].index[0]
            menu_dp9_max.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp9_max)
            if (type(self.df_csv["Despesas-2020"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2020"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2020"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2020"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2020"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2020"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2020"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2020"].loc[index_max]["ValorPago"].replace(",", ".")),2), self.df_csv["Despesas-2020"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2020"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
        elif query.data == "m10":
            menu_dp10_max = []
            index_max = self.df_csv["Despesas-2021"][self.df_csv["Despesas-2021"]["ValorPago"] == self.df_csv["Despesas-2021"]["ValorPago"].max()].index[0]
            menu_dp10_max.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp10_max)
            if (type(self.df_csv["Despesas-2021"].loc[index_max]["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2021"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2021"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2021"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
            else:
                if (math.isnan(self.df_csv["Despesas-2021"].loc[index_max]["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) 'Informação não disponivel.', no dia {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2021"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2021"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor pago foi de R${0}, realizado pelo(a) '{1}', no dia {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(self.df_csv["Despesas-2021"].loc[index_max]["ValorPago"].replace(",", ".")), 2), self.df_csv["Despesas-2021"].loc[index_max]["Favorecido"].encode('latin1').decode('utf8'), self.df_csv["Despesas-2021"].loc[index_max]["Data"].split(" ")[0]), reply_markup=reply_markup)

    def menu_dp_compare(self, update, context):
        query = update.callback_query
        if query.data == "c1":
            menu_dp1_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2004.csv") or (file == "despesas-2004.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp1_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cc{0}".format(count_files))])
            menu_dp1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp1_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c2":
            menu_dp2_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2006.csv") or (file == "Despesas-2006.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp2_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cv{0}".format(count_files))])
            menu_dp2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp2_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c3":
            menu_dp3_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2007.csv") or (file == "Despesas-2007.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp3_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cb{0}".format(count_files))])
            menu_dp3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp3_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c4":
            menu_dp4_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2009.csv") or (file == "Despesas-2009.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp4_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cn{0}".format(count_files))])
            menu_dp4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp4_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c5":
            menu_dp5_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2010.csv") or (file == "Despesas-2010.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp5_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cm{0}".format(count_files))])
            menu_dp5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp5_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c6":
            menu_dp6_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2011.csv") or (file == "Despesas-2011.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp6_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="ca{0}".format(count_files))])
            menu_dp6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp6_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c7":
            menu_dp7_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2012.csv") or (file == "Despesas-2012.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp7_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cs{0}".format(count_files))])
            menu_dp7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp7_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c8":
            menu_dp8_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2013.csv") or (file == "Despesas-2013.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp8_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cd{0}".format(count_files))])
            menu_dp8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp8_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c9":
            menu_dp9_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2020.csv") or (file == "Despesas-2020.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp9_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cf{0}".format(count_files))])
            menu_dp9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp9_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
        elif query.data == "c10":
            menu_dp10_compare = []
            for dir, subDir, files in os.walk(config.DIR_CSV_FILES):
                count_files = 0
                for file in files:
                    if ("despesas" in file) or ("Despesas" in file):
                        if (file == "Despesas-2021.csv") or (file == "Despesas-2021.csv"):
                            pass
                        else:
                            count_files += 1
                            menu_dp10_compare.append([InlineKeyboardButton(file.split(".csv")[0], callback_data="cg{0}".format(count_files))])
            menu_dp10_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp10_compare)
            update.callback_query.edit_message_text("Selecione a Despesa que quer comparar:", reply_markup=reply_markup)
                            
    def menu_dp_cc_compare(self, update, context):
        query = update.callback_query
        if query.data == "cc1":
            menu_dp_cc1_compare = []
            menu_dp_cc1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc2":
            menu_dp_cc2_compare = []
            menu_dp_cc2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc3":
            menu_dp_cc3_compare = []
            menu_dp_cc3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc4":
            menu_dp_cc4_compare = []
            menu_dp_cc4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc5":
            menu_dp_cc5_compare = []
            menu_dp_cc5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc6":
            menu_dp_cc6_compare = []
            menu_dp_cc6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc7":
            menu_dp_cc7_compare = []
            menu_dp_cc7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc8":
            menu_dp_cc8_compare = []
            menu_dp_cc8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cc9":
            menu_dp_cc9_compare = []
            menu_dp_cc9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cc9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2004 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2004 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cv_compare(self, update, context):
        query = update.callback_query
        if query.data == "cv1":
            menu_dp_cv1_compare = []
            menu_dp_cv1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv2":
            menu_dp_cv2_compare = []
            menu_dp_cv2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv3":
            menu_dp_cv3_compare = []
            menu_dp_cv3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv4":
            menu_dp_cv4_compare = []
            menu_dp_cv4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv5":
            menu_dp_cv5_compare = []
            menu_dp_cv5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv6":
            menu_dp_cv6_compare = []
            menu_dp_cv6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv7":
            menu_dp_cv7_compare = []
            menu_dp_cv7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv8":
            menu_dp_cv8_compare = []
            menu_dp_cv8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cv9":
            menu_dp_cv9_compare = []
            menu_dp_cv9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cv9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2006 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2006 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cb_compare(self, update, context):
        query = update.callback_query
        if query.data == "cb1":
            menu_dp_cb1_compare = []
            menu_dp_cb1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb2":
            menu_dp_cb2_compare = []
            menu_dp_cb2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb3":
            menu_dp_cb3_compare = []
            menu_dp_cb3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb4":
            menu_dp_cb4_compare = []
            menu_dp_cb4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb5":
            menu_dp_cb5_compare = []
            menu_dp_cb5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb6":
            menu_dp_cb6_compare = []
            menu_dp_cb6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb7":
            menu_dp_cb7_compare = []
            menu_dp_cb7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb8":
            menu_dp_cb8_compare = []
            menu_dp_cb8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cb9":
            menu_dp_cb9_compare = []
            menu_dp_cb9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cb9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2007 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2007 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cn_compare(self, update, context):
        query = update.callback_query
        if query.data == "cn1":
            menu_dp_cn1_compare = []
            menu_dp_cn1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn2":
            menu_dp_cn2_compare = []
            menu_dp_cn2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn3":
            menu_dp_cn3_compare = []
            menu_dp_cn3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn4":
            menu_dp_cn4_compare = []
            menu_dp_cn4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn5":
            menu_dp_cn5_compare = []
            menu_dp_cn5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn6":
            menu_dp_cn6_compare = []
            menu_dp_cn6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn7":
            menu_dp_cn7_compare = []
            menu_dp_cn7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn8":
            menu_dp_cn8_compare = []
            menu_dp_cn8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cn9":
            menu_dp_cn9_compare = []
            menu_dp_cn9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cn9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2009 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2009 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cm_compare(self, update, context):
        query = update.callback_query
        if query.data == "cm1":
            menu_dp_cm1_compare = []
            menu_dp_cm1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm2":
            menu_dp_cm2_compare = []
            menu_dp_cm2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm3":
            menu_dp_cm3_compare = []
            menu_dp_cm3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm4":
            menu_dp_cm4_compare = []
            menu_dp_cm4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm5":
            menu_dp_cm5_compare = []
            menu_dp_cm5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm6":
            menu_dp_cm6_compare = []
            menu_dp_cm6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm7":
            menu_dp_cm7_compare = []
            menu_dp_cm7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm8":
            menu_dp_cm8_compare = []
            menu_dp_cm8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cm9":
            menu_dp_cm9_compare = []
            menu_dp_cm9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cm9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2010 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2010 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_ca_compare(self, update, context):
        query = update.callback_query
        if query.data == "ca1":
            menu_dp_ca1_compare = []
            menu_dp_ca1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca2":
            menu_dp_ca2_compare = []
            menu_dp_ca2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca3":
            menu_dp_ca3_compare = []
            menu_dp_ca3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca4":
            menu_dp_ca4_compare = []
            menu_dp_ca4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca5":
            menu_dp_ca5_compare = []
            menu_dp_ca5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca6":
            menu_dp_ca6_compare = []
            menu_dp_ca6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca7":
            menu_dp_ca7_compare = []
            menu_dp_ca7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca8":
            menu_dp_ca8_compare = []
            menu_dp_ca8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "ca9":
            menu_dp_ca9_compare = []
            menu_dp_ca9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_dp_ca9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2011 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2011 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cs_compare(self, update, context):
        query = update.callback_query
        if query.data == "cs1":
            menu_dp_cs1_compare = []
            menu_dp_cs1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs2":
            menu_dp_cs2_compare = []
            menu_dp_cs2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs3":
            menu_dp_cs3_compare = []
            menu_dp_cs3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs4":
            menu_dp_cs4_compare = []
            menu_dp_cs4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs5":
            menu_dp_cs5_compare = []
            menu_dp_cs5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs6":
            menu_dp_cs6_compare = []
            menu_dp_cs6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs7":
            menu_dp_cs7_compare = []
            menu_dp_cs7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs8":
            menu_dp_cs8_compare = []
            menu_dp_cs8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cs9":
            menu_dp_cs9_compare = []
            menu_dp_cs9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cs9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2012 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2012 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cd_compare(self, update, context):
        query = update.callback_query
        if query.data == "cd1":
            menu_dp_cd1_compare = []
            menu_dp_cd1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd2":
            menu_dp_cd2_compare = []
            menu_dp_cd2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd3":
            menu_dp_cd3_compare = []
            menu_dp_cd3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd4":
            menu_dp_cd4_compare = []
            menu_dp_cd4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd5":
            menu_dp_cd5_compare = []
            menu_dp_cd5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd6":
            menu_dp_cd6_compare = []
            menu_dp_cd6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd7":
            menu_dp_cd7_compare = []
            menu_dp_cd7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd8":
            menu_dp_cd8_compare = []
            menu_dp_cd8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cd9":
            menu_dp_cd9_compare = []
            menu_dp_cd9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cd9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2013 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2013 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cf_compare(self, update, context):
        query = update.callback_query
        if query.data == "cf1":
            menu_dp_cf1_compare = []
            menu_dp_cf1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf2":
            menu_dp_cf2_compare = []
            menu_dp_cf2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf3":
            menu_dp_cf3_compare = []
            menu_dp_cf3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf4":
            menu_dp_cf4_compare = []
            menu_dp_cf4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf5":
            menu_dp_cf5_compare = []
            menu_dp_cf5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf6":
            menu_dp_cf6_compare = []
            menu_dp_cf6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf7":
            menu_dp_cf7_compare = []
            menu_dp_cf7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf8":
            menu_dp_cf8_compare = []
            menu_dp_cf8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cf9":
            menu_dp_cf9_compare = []
            menu_dp_cf9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cf9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2020 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2021 comparado com as Despesas de 2020 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_dp_cg_compare(self, update, context):
        query = update.callback_query
        if query.data == "cg1":
            menu_dp_cg1_compare = []
            menu_dp_cg1_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg1_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2004 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg2":
            menu_dp_cg2_compare = []
            menu_dp_cg2_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg2_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2006 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg3":
            menu_dp_cg3_compare = []
            menu_dp_cg3_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg3_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2007 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg4":
            menu_dp_cg4_compare = []
            menu_dp_cg4_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg4_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2009 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg5":
            menu_dp_cg5_compare = []
            menu_dp_cg5_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg5_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2010 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg6":
            menu_dp_cg6_compare = []
            menu_dp_cg6_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg6_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2011 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg7":
            menu_dp_cg7_compare = []
            menu_dp_cg7_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg7_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2012 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg8":
            menu_dp_cg8_compare = []
            menu_dp_cg8_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg8_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2013 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
        elif query.data == "cg9":
            menu_dp_cg9_compare = []
            menu_dp_cg9_compare.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_dp_cg9_compare)
            dp_compare_value = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() - pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            dp_compare_percent = pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum() / pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum()
            if (dp_compare_value < 0):
                update.callback_query.edit_message_text("Houve um aumento no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2021 no valor de R${0}. Resultando em um aumento de {1}%.\n\n".format(round(dp_compare_value*(-1), 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)
            else:
                update.callback_query.edit_message_text("Houve uma queda no Valor Total pago nas Despesas de 2020 comparado com as Despesas de 2021 no valor de R${0}. Resultando em uma queda de {1}%.\n\n".format(round(dp_compare_value, 2), round(dp_compare_percent*100, 2)), reply_markup=reply_markup)

    def menu_vp_total(self, update, context):
        query = update.callback_query
        if query.data == "v1":
            menu_vp1_total = []
            menu_vp1_total.append([InlineKeyboardButton("Outras Informações", callback_data="d1")])
            reply_markup = InlineKeyboardMarkup(menu_vp1_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2004 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2004"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v2":
            menu_vp2_total = []
            menu_vp2_total.append([InlineKeyboardButton("Outras Informações", callback_data="d2")])
            reply_markup = InlineKeyboardMarkup(menu_vp2_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2006 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2006"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v3":
            menu_vp3_total = []
            menu_vp3_total.append([InlineKeyboardButton("Outras Informações", callback_data="d3")])
            reply_markup = InlineKeyboardMarkup(menu_vp3_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2007 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2007"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v4":
            menu_vp4_total = []
            menu_vp4_total.append([InlineKeyboardButton("Outras Informações", callback_data="d4")])
            reply_markup = InlineKeyboardMarkup(menu_vp4_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2009 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2009"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v5":
            menu_vp5_total = []
            menu_vp5_total.append([InlineKeyboardButton("Outras Informações", callback_data="d5")])
            reply_markup = InlineKeyboardMarkup(menu_vp5_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2010 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2010"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v6":
            menu_vp6_total = []
            menu_vp6_total.append([InlineKeyboardButton("Outras Informações", callback_data="d6")])
            reply_markup = InlineKeyboardMarkup(menu_vp6_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2011 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2011"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v7":
            menu_vp7_total = []
            menu_vp7_total.append([InlineKeyboardButton("Outras Informações", callback_data="d7")])
            reply_markup = InlineKeyboardMarkup(menu_vp7_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2012 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2012"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v8":
            menu_vp8_total = []
            menu_vp8_total.append([InlineKeyboardButton("Outras Informações", callback_data="d8")])
            reply_markup = InlineKeyboardMarkup(menu_vp8_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2013 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2013"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v9":
            menu_vp9_total = []
            menu_vp9_total.append([InlineKeyboardButton("Outras Informações", callback_data="d9")])
            reply_markup = InlineKeyboardMarkup(menu_vp9_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2020 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2020"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "v10":
            menu_vp10_total = []
            menu_vp10_total.append([InlineKeyboardButton("Outras Informações", callback_data="d10")])
            reply_markup = InlineKeyboardMarkup(menu_vp10_total)
            update.callback_query.edit_message_text("O Valor Total pago nas Despesas de 2021 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["Despesas-2021"]["ValorPago"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)

    def menu_rp_max(self, update, context):
        query = update.callback_query
        if query.data == "mp1":
            menu_rp1_max = []
            menu_rp1_max.append([InlineKeyboardButton("Outras Informações", callback_data="r1")])
            reply_markup = InlineKeyboardMarkup(menu_rp1_max)
            rp_max = self.df_csv["RestosAPagar-2012"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2012"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
        elif query.data == "mp2":
            menu_rp2_max = []
            menu_rp2_max.append([InlineKeyboardButton("Outras Informações", callback_data="r2")])
            reply_markup = InlineKeyboardMarkup(menu_rp2_max)
            rp_max = self.df_csv["RestosAPagar-2013"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2013"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
        elif query.data == "mp3":
            menu_rp3_max = []
            menu_rp3_max.append([InlineKeyboardButton("Outras Informações", callback_data="r3")])
            reply_markup = InlineKeyboardMarkup(menu_rp3_max)
            rp_max = self.df_csv["RestosAPagar-2014"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2014"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
        elif query.data == "mp4":
            menu_rp4_max = []
            menu_rp4_max.append([InlineKeyboardButton("Outras Informações", callback_data="r4")])
            reply_markup = InlineKeyboardMarkup(menu_rp4_max)
            rp_max = self.df_csv["RestosAPagar-2015"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2015"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
        elif query.data == "mp5":
            menu_rp5_max = []
            menu_rp5_max.append([InlineKeyboardButton("Outras Informações", callback_data="r5")])
            reply_markup = InlineKeyboardMarkup(menu_rp5_max)
            rp_max = self.df_csv["RestosAPagar-2016"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2016"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
        elif query.data == "mp6":
            menu_rp6_max = []
            menu_rp6_max.append([InlineKeyboardButton("Outras Informações", callback_data="r6")])
            reply_markup = InlineKeyboardMarkup(menu_rp6_max)
            rp_max = self.df_csv["RestosAPagar-2017"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2017"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
        elif query.data == "mp7":
            menu_rp7_max = []
            menu_rp7_max.append([InlineKeyboardButton("Outras Informações", callback_data="r7")])
            reply_markup = InlineKeyboardMarkup(menu_rp7_max)
            rp_max = self.df_csv["RestosAPagar-2018"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2018"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
        elif query.data == "mp8":
            menu_rp8_max = []
            menu_rp8_max.append([InlineKeyboardButton("Outras Informações", callback_data="r8")])
            reply_markup = InlineKeyboardMarkup(menu_rp8_max)
            rp_max = self.df_csv["RestosAPagar-2019"].loc[pd.to_numeric(self.df_csv["RestosAPagar-2019"]["ValorProcessado"].str.replace(",", ".")).argmax()]
            if (type(rp_max["Favorecido"]) == str):
                update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
            else:
                if (math.isnan(rp_max["Favorecido"])):
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) 'Informação não disponível' no {1}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)
                else:
                    update.callback_query.edit_message_text("O maior valor processado foi de R${0}, realizado pelo(a) '{1}' no {2}.\n\nCaso queira selecionar outra informação, basta clicar em Outras Informações".format(round(float(rp_max["ValorProcessado"].replace(",", ".")), 2), rp_max["Favorecido"].encode('latin1').decode('utf8'), rp_max["Poder"].encode('latin1').decode('utf8')), reply_markup=reply_markup)

    def menu_rp_total(self, update, context):
        query = update.callback_query
        if query.data == "vt1":
            menu_rp_vp1_total = []
            menu_rp_vp1_total.append([InlineKeyboardButton("Outras Informações", callback_data="r1")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp1_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2012 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2012"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "vt2":
            menu_rp_vp2_total = []
            menu_rp_vp2_total.append([InlineKeyboardButton("Outras Informações", callback_data="r2")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp2_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2013 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2013"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "vt3":
            menu_rp_vp3_total = []
            menu_rp_vp3_total.append([InlineKeyboardButton("Outras Informações", callback_data="r3")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp3_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2014 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2014"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "vt4":
            menu_rp_vp4_total = []
            menu_rp_vp4_total.append([InlineKeyboardButton("Outras Informações", callback_data="r4")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp4_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2015 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2015"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "vt5":
            menu_rp_vp5_total = []
            menu_rp_vp5_total.append([InlineKeyboardButton("Outras Informações", callback_data="r5")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp5_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2016 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2016"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "vt6":
            menu_rp_vp6_total = []
            menu_rp_vp6_total.append([InlineKeyboardButton("Outras Informações", callback_data="r6")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp6_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2017 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2017"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "vt7":
            menu_rp_vp7_total = []
            menu_rp_vp7_total.append([InlineKeyboardButton("Outras Informações", callback_data="r7")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp7_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2018 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2018"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
        elif query.data == "vt8":
            menu_rp_vp8_total = []
            menu_rp_vp8_total.append([InlineKeyboardButton("Outras Informações", callback_data="r8")])
            reply_markup = InlineKeyboardMarkup(menu_rp_vp8_total)
            update.callback_query.edit_message_text("O Valor Total pago de Restos A Pagar no ano de 2019 foi de R${0}\n\n".format(round(pd.to_numeric(self.df_csv["RestosAPagar-2019"]["ValorProcessado"].str.replace(",", ".")).sum(), 2)), reply_markup=reply_markup)
    
    def echo(self, update, context):
        """Echo the user message."""
        update.message.reply_text("Não foi possível reconhecer o comando informado. Para consultar algum dado, basta digitar /info para obter as informações.")

    def main(self):
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        updater = Updater(config.TOKEN_BOT, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(CommandHandler("info", self.info))
        dp.add_handler(CommandHandler("email", self.email))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_infos, pattern='dp'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp, pattern='d10'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_compare, pattern='c10'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cc_compare, pattern='cc9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cv_compare, pattern='cv9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cb_compare, pattern='cb9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cn_compare, pattern='cn9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cm_compare, pattern='cm9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_ca_compare, pattern='ca9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cs_compare, pattern='cs9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cd_compare, pattern='cd9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cf_compare, pattern='cf9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_cg_compare, pattern='cg9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp, pattern='r8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_dp_max, pattern='m10'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v9'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_vp_total, pattern='v10'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_total, pattern='vt8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp1'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp2'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp3'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp4'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp5'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp6'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp7'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_rp_max, pattern='mp8'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_infos, pattern='sd'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.menu_infos, pattern='rp'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.main_menu, pattern='mp'))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, self.echo))

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()