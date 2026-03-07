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


with st.sidebar:
        # inserir o valor mínimo que será utilizado para filtrar o dateset
        by_price_min = st.number_input('Insert the min value of the vehicle',
                                value=None, placeholder='Type the price... $USD')
        # inserir o valor máximo que será utilizado para filtrar o dateset
        by_price_max = st.number_input('Insert the max value of the vehicle',
                                value=None, placeholder='Type the price... $USD')

        # filtrar o dataset com base nos valores inseridos.
        filter_by_price = car_data[(car_data['price'] >= by_price_min) & (car_data['price'] <= by_price_max)]
        # mostrar a tabela filtrada
        st.metric(label="Filtered Rows", value=len(filter_by_price))

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

# calculando as métricas com base nos dados filtrados pelo usuário
total_vehicles = len(filter_by_price)
price_avg = filter_by_price['price'].mean()
odometer_avg = filter_by_price['odometer'].mean()

# separando o topo da página em 3 colunas
kpi1, kpi2, kpi3 = st.columns(3)

# preenche cada coluna com um st.metric
with kpi1:
    st.metric(
        label="🚗 Total Vehicles", 
        value=f"{total_vehicles:,}".replace(",", ".")
    )

with kpi2:
    st.metric(
        label="💰 AVG Price", 
        value=f"${price_avg:,.2f}"
    )

with kpi3:
    st.metric(
        label="🛣️ AVG Miles", 
        value=f"{odometer_avg:,.0f} mi"
    )
# adiciona uma linha de separação visual
st.divider()

# escrever uma mensagem
st.subheader('Vehicle Concentration by Price Range and Year')

# escrever o modelo selecionado
st.write('Model: ', hist_option_model)

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
                        labels={'count': 'Count','price': 'Price ($USD)', 'year_range': 'Model Year Range'})
# criar um gráfico de dispersão
fig2 = px.scatter(filtered_cars, 
                 x='model_year', 
                 y='odometer',
                 title=f'Model Year vs Odometer - {hist_option_brand} | {hist_option_model}',
                 labels={'odometer': 'Odometer (miles)', 'model_year': 'Model Year'})
# criando duas colunas de larguras iguais
col1, col2 = st.columns(2)

with col1:
    # exibir um gráfico Ploty interativo
    st.plotly_chart(fig, use_container_width=True)
with col2:
    # exibir um gráfico Ploty interativo
    st.plotly_chart(fig2, use_container_width=True)

# verificando se as duas variáveis contêm números válidos
if by_price_min is not None and by_price_max is not None:
    st.subheader('Available Vehicle Types (${:,.0f} - {:,.0f})'.format(by_price_min, by_price_max))
else:
    # título alternativo de segurança caso o utilizador apague os números do filtro
    st.subheader("Available Vehicle Types")

# o parâmetro 'normalize=True' devolve a proporção de 0 a 1 em vez da contagem absoluta
type_percentages = filter_by_price['type'].value_counts(normalize=True)
# filtra apenas os tipos de veículos que representam menos de 5% (0.05)
types_to_group = type_percentages[type_percentages < 0.05].index
# usamos o método .replace() para trocar a lista de tipos minoritários por uma única string
filter_by_price['type_grouped'] = filter_by_price['type'].replace(types_to_group, 'Other')

# criar um gráfico de barras
fig = px.bar(filter_by_price, 
             y='type_grouped', 
             color='type_grouped', 
             labels={'manufacture': 'Manufacture', 'type_grouped': 'Vehicle Type', 'count': 'Count'},
             orientation='h')
# exibir um gráfico plotly interativo
st.plotly_chart(fig, width='stretch')

with st.expander('View raw data 📊'):
    st.write('The table below shows the data filtered by price, brand, and model. ')
    st.dataframe(filtered_cars)