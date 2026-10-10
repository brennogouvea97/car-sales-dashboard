import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
hist_title = st.header('Análise de anúncios de venda de carros nos EUA')
hist_button = st.checkbox('Criar histograma')
hist_checkbox = st.checkbox('Mostrar gráfico de dispersão')
box_checkbox = st.checkbox('Mostrar relação entre combustível e preço')

if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if hist_checkbox:
    st.write('Relação entre quilometragem e preço')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig)

if box_checkbox:
    st.write('Relação entre combustível e preço')

    fig = px.box(car_data, x="fuel", y="price")

    st.plotly_chart(fig)
