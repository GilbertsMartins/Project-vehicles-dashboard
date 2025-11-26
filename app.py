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
car_data = car_data.dropna(subset=['model_year'])
car_data['model_year'] = car_data['model_year'].astype(int)

# cabeçalho do aplicativo
st.header('A dataset view of used vehicles for sale') 

build_table = st.checkbox('Filter vehicles by price') # Checkbox para criar uma tabela filtrada com o valor dos veículos

if build_table:
    by_price_min = st.number_input('Insert the min value of the vehicle',
                               value=None, placeholder='Type the price... $USD')
    by_price_max = st.number_input('Insert the max value of the vehicle',
                               value=None, placeholder='Type the price... $USD')
    filter_by_price = car_data[(car_data['price'] >= by_price_min) & (car_data['price'] <= by_price_max)]
    st.dataframe(filter_by_price)

    # criar um botão para o histograma
    hist_option_brand = st.selectbox('Select the brand', 
                           filter_by_price['manufacture'].unique(), 
                           placeholder="Select the brand...")
    # escrever uma mensagem
    st.write('Brand: ', hist_option_brand)
    if hist_option_brand: # se o botão for clicado
        # Filtrando a tabela pela marca escolhida pelo usuário
        filtered_models = filter_by_price[filter_by_price['manufacture'] == hist_option_brand]['model'].unique()

        # selectbox para o modelo do veículo
        hist_option_model = st.selectbox('Select the model', 
                            filtered_models, 
                            placeholder="Select the brand...")
        st.write('Model: ', hist_option_model) # escrever o modelo selecionado
        # criar um histograma
        if hist_option_model:
            st.write('The histogram above shows the correlation between vehicle price and mileage for the user-filtered vehicles.')
            filtered_cars = filter_by_price[(filter_by_price['manufacture'] == hist_option_brand) & 
                                    (filter_by_price['model'] == hist_option_model)]
            fig = px.histogram(filtered_cars, x='price', y='odometer', 
                               title='Correlation between vehicle price and mileage', 
                               color='model_year',
                                )
        # exibir um gráfico Plotly interativo
        st.plotly_chart(fig, width='stretch')

    # criar um botão para o gráfico de dispersão
    chart_button = st.button('Criar gráfico de dispersão') 

    if chart_button: # se o botão for clicado
        # escrever uma mensagem
        st.write('The chart above displays data from the advertisements, showing the cars’ ' \
        'odometer readings and model years. The odometer values are reported in miles.')
        # criar um gráfico de dispersão
        fig = px.scatter(filtered_cars, x='odometer', y='model_year')
        # exibir um gráfico Ploty interativo
        st.plotly_chart(fig, width='stretch')


# criar um gráfico de barras
fig = px.bar(car_data, x='manufacture', color='type', title='Vehicles types by manufacture')
# exibir um gráfico plotly interativo
st.plotly_chart(fig, width='stretch')

