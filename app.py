import pandas as pd #type: ignore
import plotly.express as px #type: ignore
import streamlit as st #type: ignore

car_data = pd.read_csv('vehicles.csv') # lendo o dataset
hist_button = st.button('Criar histograma') # criar um botão para o histograma
chart_button = st.button('Criar gráfico de dispersão') # criar um botão para o gráfico de dispersão

st.header('Visualizando os anúncios dos carros a venda') # cabeçalho do aplicativo

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig = px.histogram(car_data, x='odometer')
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if chart_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x='odometer', y='price')
    # exibir um gráfico Ploty interativo
    st.plotly_chart(fig, use_container_width=True)
    