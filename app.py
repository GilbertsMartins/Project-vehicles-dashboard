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
car_data = car_data.dropna(subset=(['price', 'manufacture', 'model', 'model_year', 'condition', 'cylinders', 'fuel', 
          'odometer', 'transmission', 'type', 'paint_color', 'date_posted', 'days_listed'])) # removendo dados ausentes
car_data['is_4wd'] = car_data['is_4wd'].replace(1, True)
car_data['is_4wd'] = car_data['is_4wd'].fillna(0).replace(0, False) # preenchendo os valores ausentes com False
car_data['model_year'] = car_data['model_year'].astype(int) # forçando dados INT na coluna
car_data['price'] = car_data['price'].astype(int) # forçando dados INT na coluna
car_data['price'] = car_data['price'].clip(lower=1000, upper=100000) # limitando o valor máximo da coluna 'price' para 100.000 

# escrever uma mensagem 
st.write('Filter the dataset by price, brand, and model to explore the used vehicle market. Visualize the distribution of vehicle prices based on different model years and discover insights about the market trends.')

# inserir o valor mínimo que será utilizado para filtrar o dateset
by_price_min = st.number_input('Insert the min value of the vehicle',
                            value=None, placeholder='Type the price... $USD')
# inserir o valor máximo que será utilizado para filtrar o dateset
by_price_max = st.number_input('Insert the max value of the vehicle',
                            value=None, placeholder='Type the price... $USD')
# filtrar o dataset com base nos valores inseridos.
filter_by_price = car_data[(car_data['price'] >= by_price_min) & (car_data['price'] <= by_price_max)]
# mostrar a tabela filtrada
st.dataframe(filter_by_price)

# selectbox para a fabricante do veículo
hist_option_brand = st.selectbox('Select the brand', 
                        filter_by_price['manufacture'].unique(), 
                        placeholder="Select the brand...")

# escrever a fabricante selecionada
st.write('Brand: ', hist_option_brand) 

# filtrando a tabela pela marca escolhida pelo usuário
filtered_models = filter_by_price[filter_by_price['manufacture'] == hist_option_brand]['model'].unique()

# selectbox para o modelo do veículo
hist_option_model = st.selectbox('Select the model', 
                    filtered_models, 
                    placeholder="Select the model...")

# escrever o modelo selecionado
st.write('Model: ', hist_option_model)
# escrever uma mensagem
st.write('The histogram shows the distribution of vehicle prices, with colors representing different model years.')

# filtrando a tabela 'filter_by_price' pela fabricante e modelo selecionado.
filtered_cars = filter_by_price[(filter_by_price['manufacture'] == hist_option_brand) & 
                        (filter_by_price['model'] == hist_option_model)]
# simplificando cores para utilizar no histograma, assim evitando mais de 20 cores no gráfico
filtered_cars['year_range'] = pd.cut(filtered_cars['model_year'], 
                        bins=[1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020], 
                        labels=['1941-1950', '1951-1960', '1961-1970', '1971-1980', '1981-1990', 
                                '1991-2000', '2001-2010', '2011-2020']) # 8 possíveis cores
# criando histograma
fig = px.histogram(filtered_cars, x='price', 
                        title=(f'Distribution of Prices - {hist_option_brand} | {hist_option_model}'), 
                        color='year_range',
                        labels={'price': 'Price ($USD)', 'year_range': 'Model Year Range'})
# exibir um gráfico Plotly interativo
st.plotly_chart(fig, width='stretch')

# escrever uma mensagem
st.write('The chart above displays data from the advertisements, showing the cars’ ' \
        'odometer readings and model years. The odometer values are reported in miles.')
# criar um gráfico de dispersão
fig = px.scatter(filtered_cars, 
                 x='odometer', 
                 y='model_year',
                 title=f'Odometer vs Model Year - {hist_option_brand} | {hist_option_model}',
                 labels={'odometer': 'Odometer (miles)', 'model_year': 'Model Year'})
# exibir um gráfico Ploty interativo
st.plotly_chart(fig, width='stretch')

# escrever uma mensagem
st.write('The bar chart below shows the vehicles filtered by manufacturer and type, ' \
    'with the data directly connected to the table generated based on the minimum and maximum values defined by the user.')
# criar um gráfico de barras
fig = px.bar(filter_by_price, 
             x='manufacture', 
             color='type', 
             title='Vehicles types by manufacture',
             labels={'manufacture': 'Manufacture', 'type': 'Vehicle Type'})
# exibir um gráfico plotly interativo
st.plotly_chart(fig, width='stretch')
