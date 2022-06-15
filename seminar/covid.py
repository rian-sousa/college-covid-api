#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##RIAN SOUSA FLORENTINO DAS CHAGAS##

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
print("Estado com mais mortes de covid-19: ", covid.iloc[covid['totalMortes'].idxmax(),5]," - ", covid.iloc[covid['totalCasos'].idxmax(),1])
print("Estado com menos mortes de covid-19: ", covid.iloc[covid['totalMortes'].idxmin(),5]," - ", covid.iloc[covid['totalCasos'].idxmin(),1])


estados5MaisMortes = covid.nlargest(5, 'totalMortes', keep='first')
estados5MenosMortes = covid.nsmallest(5, 'totalMortes')








plt.bar(estados5MaisMortes['Estado'], estados5MaisMortes['totalMortes'])
plt.show

sns.histplot(data=estados5MenosMortes, x='Estado', y='totalMortes')






# %%
