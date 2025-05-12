# As bibliotecas necessarias 
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

# a leitura da Planilha Exel
DadosAgricolas = pd.read_csv('C:\Python\Ciência de Dados\Dados Agricolas\dados_agricolas_amazonas_atualizado.csv',delimiter=';')

# A limpeza dos Dados Da Planilha 

def verficarValoresAusentes():
    print(DadosAgricolas.isnull().sum())
    print(DadosAgricolas[DadosAgricolas.isnull().any(axis=1)])

def RemoveLinhaDuplicada():
    print(DadosAgricolas.drop_duplicates())

# Analise Exploratoria

def ResumoEstatisticoDados():
    print(DadosAgricolas.describe())

def QuantidadeTotalMunicipio():
    Producao = DadosAgricolas.groupby('Município')['Produção(ton)'].sum()
    print(Producao)

def DistribuicaoAreaPlantadaGF():
    plt.figure("Distribuição área Plantada ao logo dos Meses",figsize=(16,6))
    plt.title("Distribuição por Àrea Plantada")
    plt.plot(DadosAgricolas['Mês'],DadosAgricolas['ÁreaPlantada(ha)'],marker = 'o')
    plt.xlabel("Meses")
    plt.ylabel("Àrea Plantada")
    plt.show()

#Visualização dos Dados

def GraficoBarras():
    plt.figure("Grafico de Barras",figsize=(14,6))
    plt.bar(DadosAgricolas['Município'],DadosAgricolas['Produção(ton)'],color='skyblue', label='Dados')
    plt.title("Producão de Municipios do Amazonas")
    plt.xlabel("Municipios do Amazonas")
    plt.ylabel("Produção/Municipio")
    plt.tight_layout()
    plt.show()

def GraficoLinha():
  plt.figure("Grafico de Linha",figsize=(14,6))
  plt.plot(DadosAgricolas['Mês'],DadosAgricolas['ÁreaPlantada(ha)'], color='blue', label='Linha Azul')  # Linha azul
  plt.title("Mostrando A variação mensal da Área Plantada")
  plt.xlabel("Meses")
  plt.ylabel("Área plantada")
  plt.tight_layout()
  plt.show()

def GraficoHistograma():
  plt.figure("Grafico Histograama",figsize=(14,6))
  plt.title("Distribuição da Produção")
  plt.hist(DadosAgricolas['Produção(ton)'],bins=20, color=['orange'], edgecolor='black')
  plt.xlabel("Produção")
  plt.ylabel("Frequência")
  plt.tight_layout()
  plt.show()

def GraficoBoxplot():
  plt.figure("Grafico BoxPlot",figsize=(14,6))
  plt.title("Distribuição da Produção")
  sn.boxplot(x=DadosAgricolas['Produto'],y=DadosAgricolas['ÁreaColhida(ha)'],data=DadosAgricolas)
  plt.xlabel("Produto")
  plt.ylabel("Área Colhida(ha)")
  plt.tight_layout()
  plt.show()

# Chamada das funções estão todas aqui #

#verficarValoresAusentes()
#RemoveLinhaDuplicada()
#ResumoEstatisticoDados()
#QuantidadeTotalMunicipio()
#DistribuicaoAreaPlantadaGF()
#GraficoBarras()
#GraficoLinha()
#GraficoHistograma()
#GraficoBoxplot()