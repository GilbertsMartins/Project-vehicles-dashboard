import pandas as pd #type: ignore
import plotly.express as px #type: ignore
import streamlit as st #type: ignore

# lendo o dataset
car_data = pd.read_csv('vehicles.csv')
# separando o conteúdo da coluna 'model'
car_data[['manufacture', 'model']] = car_data['model'].str.split(' ', n=1, expand=True)
# reorganizando as colunas do dataset
car_data = car_data[['price', 'manufacture', 'model', 'model_year', 'condition', 'cylinders', 'fuel', 
          'odometer', 'transmission', 'type', 'paint_color', 'is_4wd', 'date_posted', 'days_listed']]
car_data = car_data.dropna(subset=['model_year']) # Removendo dados ausentes
car_data['model_year'] = car_data['model_year'].astype(int) # Forçando dados INT na coluna

# cabeçalho do aplicativo
st.header('A dataset view of used vehicles for sale')
# escrever uma mensagem 
st.write('This is a way to filter vehicles by the price you choose.')
# Filter vehicles by price using this button
build_table = st.checkbox('Filter') # checkbox para começar as filtragens.

if build_table: # Se o checkbox for selecionado
    # Inserir o valor mínimo que será utilizado para filtrar o dateset
    by_price_min = st.number_input('Insert the min value of the vehicle',
                               value=None, placeholder='Type the price... $USD')
    # Inserir o valor máximo que será utilizado para filtrar o dateset
    by_price_max = st.number_input('Insert the max value of the vehicle',
                               value=None, placeholder='Type the price... $USD')
    # Filtrar o dataset com base nos valores inseridos.
    filter_by_price = car_data[(car_data['price'] >= by_price_min) & (car_data['price'] <= by_price_max)]
    # Mostrar a tabela filtrada
    st.dataframe(filter_by_price)

    # Selectbox para a fabricante do veículo
    hist_option_brand = st.selectbox('Select the brand', 
                           filter_by_price['manufacture'].unique(), 
                           placeholder="Select the brand...")
    
    st.write('Brand: ', hist_option_brand) # escrever a fabricante selecionada

    # Filtrando a tabela pela marca escolhida pelo usuário
    filtered_models = filter_by_price[filter_by_price['manufacture'] == hist_option_brand]['model'].unique()

    # selectbox para o modelo do veículo
    hist_option_model = st.selectbox('Select the model', 
                        filtered_models, 
                        placeholder="Select the brand...")
    st.write('Model: ', hist_option_model) # escrever o modelo selecionado
    
    # escrever uma mensagem
    st.write('The histogram shows the distribution of vehicle prices, with colors representing different model years.')
    # Filtrando a tabela 'filter_by_price' pela fabricante e modelo selecionado.
    filtered_cars = filter_by_price[(filter_by_price['manufacture'] == hist_option_brand) & 
                            (filter_by_price['model'] == hist_option_model)]
    # Simplificando cores para utilizar no histograma, assim evitando mais de 20 cores no gráfico
    filtered_cars['year_range'] = pd.cut(filtered_cars['model_year'], 
                            bins=[1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020], 
                            labels=['1941-1950', '1951-1960', '1961-1970', '1971-1980', '1981-1990', 
                                    '1991-2000', '2001-2010', '2011-2020']) # 8 possíveis cores
    # Criando histograma
    fig = px.histogram(filtered_cars, x='price', 
                            title=(f'Distribution of Prices - {hist_option_brand} | {hist_option_model}'), 
                            color='year_range',
                                )
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, width='stretch')
    # escrever uma mensagem
    st.write('The chart above displays data from the advertisements, showing the cars’ ' \
            'odometer readings and model years. The odometer values are reported in miles.')
     # criar um gráfico de dispersão
    fig = px.scatter(filtered_cars, x='odometer', y='model_year')
    # exibir um gráfico Ploty interativo
    st.plotly_chart(fig, width='stretch')

    # escrever uma mensagem
    st.write('The bar chart below shows the vehicles filtered by manufacturer and type, ' \
        'with the data directly connected to the table generated based on the minimum and maximum values defined by the user.')
    # criar um gráfico de barras
    fig = px.bar(filter_by_price, x='manufacture', color='type', title='Vehicles types by manufacture')
    # exibir um gráfico plotly interativo
    st.plotly_chart(fig, width='stretch')

else:
    st.write('Check the box to use the app.')