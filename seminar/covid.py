#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##RIAN SOUSA FLORENTINO DAS CHAGAS E RAFAEL FRAZÃO BORGES DA SILVA##

uri = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv'

covid = pd.read_csv(uri)
covid.columns = ['País', 'Estado', 'Cidade', 'ibgeID', 'totalMortes', 'totalCasos','Morte_por_100Khab','Casos_por_100Khab','Morte_por_TotalCasos',
                '_fonte','data','novosCasos','novasMortes','dataUltimaInfo']

#print(covid.head())
        #0-País 1-Estado 2-Cidade 

tCasos = covid['totalCasos'].sum()
tMortes = covid['totalMortes'].sum()

mediaCasosEstado = tCasos / 27

print("===================")

print("Media de casos por estado: ", int(mediaCasosEstado))
print("Mediana de total de casos: ", np.median(covid['totalCasos']))
print("Estado com mais mortes de covid-19: ", covid.iloc[covid['totalMortes'].idxmax(),5]," - ", covid.iloc[covid['totalCasos'].idxmax(),1])
print("Estado com menos mortes de covid-19: ", covid.iloc[covid['totalMortes'].idxmin(),5]," - ", covid.iloc[covid['totalCasos'].idxmin(),1])
print("Desvio padrão de total de casos: ", np.std(covid['totalCasos']))

estados5MaisMortes = covid.nlargest(5, 'totalMortes', keep='first')
estados5MenosMortes = covid.nsmallest(5, 'totalMortes')

#estados5MaisCasos = covid.nlargest(5, 'totalCasos', keep='first')
#estados5MenosCasos = covid.nsmallest(5, 'totalCasos')


plt.bar(estados5MaisMortes['Estado'], estados5MaisMortes['totalMortes'])
plt.show


# %%
