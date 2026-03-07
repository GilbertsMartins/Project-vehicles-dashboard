# 🚙 DriveData - Explorador de Veículos Usados 🚗
Este projeto é uma aplicação web interativa construída com **Streamlit**, projetada para explorar e visualizar um banco de dados de veículos usados listados para venda. Além do aplicativo web, o repositório inclui um notebook Jupyter (`EDA.ipynb`) com todo o tratamento de dados e análises exploratórias detalhadas.

## 🚀 Começando

Estas instruções permitirão que você acesse o projeto online ou obtenha uma cópia para rodar na sua máquina local para fins de desenvolvimento e teste.

### 🌐 Acesso Rápido (Web App)
Você pode acessar o aplicativo web diretamente pelo navegador clicando no link abaixo:
👉 **[Acessar o Web App no Render](LINK_DO_SEU_APP_AQUI)**

*(Nota: Como o projeto está hospedado em um serviço de nuvem gratuito, o primeiro carregamento da página pode levar alguns instantes. Agradeço a paciência!)*

## 📋 Pré-requisitos e Ferramentas

Para rodar o projeto localmente, recomendo as seguintes versões:
* **Python:** 3.12.4 (ou superior)
* **Pandas:** 2.3.3
* **Plotly:** 6.5.0
* **Streamlit:** 1.51.0

Para explorar o arquivo `EDA.ipynb` na pasta `notebooks`, recomendo a utilização do **VS Code** com a extensão do Jupyter instalada.

## ⚙️ Executando Localmente

Se desejar clonar o projeto e rodar o aplicativo `app.py` na sua máquina, siga este passo a passo:

1. Abra o seu terminal (ex: Anaconda Prompt).
2. Crie um ambiente virtual (recomendado):
```bash
conda create -n vehicles_env python=3.12.4
```
3. Ative o ambiente virtual:
```bash
conda activate vehicles_env
```

4. Instale as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

5. Execute o aplicativo web:
```bash
streamlit run app.py
```

O Streamlit abrirá automaticamente uma nova aba no seu navegador padrão. Caso não abra, acesse o link local fornecido no terminal (geralmente `http://localhost:8501`).

Para encerrar a execução no terminal, pressione `CTRL + C` e, em seguida, desative o ambiente com `conda deactivate`.

---

## 📊 Utilizando o Dashboard

* Utilize a barra lateral para **Filtrar** os dados.
* Insira um valor mínimo e máximo de preço para refinar a busca.
* Selecione a fabricante e, em seguida, o modelo específico do veículo para visualizar os gráficos interativos e a tabela de dados brutos.

## 🛠️ Construído com

* **[Python](https://www.python.org/)** - Linguagem principal
* **[Streamlit](https://streamlit.io/)** - Framework para o Web App
* **[Plotly](https://plotly.com/) & [Pandas](https://pandas.pydata.org/)** - Análise e Visualização de Dados
* **[Render](https://render.com/)** - Plataforma de Cloud Hosting

## ✒️ Autor

* **Gilbert Martins** - Desenvolvimento e Documentação - [GilbertsMartins](https://github.com/GilbertsMartins)
