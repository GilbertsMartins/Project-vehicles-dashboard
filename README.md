# Project-vehicles-dashboard 🏎️🚙🚗🚓
Esse projeto conta com um aplicativo web utilizando funções do streamlit para entregar um acesso interativo e agradável ao banco de dados onde se encontram os carros listados para venda, como também acompanha um arquivo notebook que auxilia na observação dos dados tratados, e criação dos gráficos. 

## 🚀 Começando
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste, como também contará com o link de acesso ao aplicativo web para acesso via navegadores, e por fim também poderá executar nosso projeto criado no formato do jupyter notebook para criação de gráficos interativos.

### 📋 Pré-requisitos
Para acessar o aplicativo web utilize um navegador de sua preferência clicando no hyperlink a seguir - [project-vehicles-dashboard](https://project-vehicles-dashboard.onrender.com) 

Para o arquivo que se encontra dentro do diretório [notebooks](https://github.com/GilbertsMartins/Project-vehicles-dashboard/tree/main/notebooks) recomendo utilizar o [VsCode](https://code.visualstudio.com), juntamente com a extensão jupyter notebook para abertura do arquivo ".ipynb".

Neste projeto foram utilizadas algumas bibliotecas que estão listadas em [requirements](https://github.com/GilbertsMartins/Project-vehicles-dashboard/blob/main/requirement.txt), as mesmas são de extrema importância para o desenvolvimento e execução do código criado.

### 🔧 Instalação
- O aplicativo web é acessado diretamente pelo link, sendo apenas necessário aguardar a inicialização do mesmo (pode levar alguns breves minutos), pois o mesmo se encontra hospedado na plataformar Render, e por falta de orçamento "$$$" estamos utilizando o modo gratuito. (sorry about that rsrs)
- Para executar o "EDA.ipynb" prontamente e ter acesso aos gráficos criados, é necessário utilizar um editor compatível com arquivos ".ipynb".
- Para realizar modificações em sua máquina local no arquivo principal do aplicativo web "app.py", pode-se utilizar a IDE de sua preferência.

**Recomendo as seguintes versões do python e bibliotecas:**

python: 3.12.4 or latest.

pandas: 2.3.3

plotly: 6.5.0

streamlit: 1.51.0


## ⚙️ Executando os testes
**[Aplicativo Web](https://project-vehicles-dashboard.onrender.com):**
1. Selecione a caixa "Filter" para iniciar.
2. Insira um valor mínimo e máximo para criar uma tabela filtrada do banco de dados de veículos.
3. Selecione a fabricante desejada, e após isso o modelo do veículo.

**Para execução do aplicativo localmente - app.py:**
1. Abra seu terminal Anaconda.
2. Defina um ambiente virtual para utilização (se não houver nenhum configurado): $ conda create -n env exemplo_env
3. Ative o ambiente virtual: $ conda activate exemplo_env
4. Instale as bibliotecas recomendadas em [requirements](https://github.com/GilbertsMartins/Project-vehicles-dashboard/blob/main/requirement.txt) ou no tópico de **[instalação](#-Insta%C3%A7%C3%A3o)**.
5. Rode o arquivo app.py no terminal com o seguinte código: $ streamlit run app.py
6. Será iniciada uma aba no seu navegador padrão automaticamente, caso não ocorra, pode acessar via o seguinte link: [App_Teste](http://localhost:10000)
7. Siga o mesmo passo-a-passo dado ao aplicativo web acima.
8. Se quiser parar o teste, volte ao seu terminal e aperte: CTRL + C
9. Desative seu ambiente virtual: $ conda deactivate

**Para execução do arquivo no jupyter notebook - EDA.ipynb:**
1. Abra o arquivo no editor compatível.
2. Rode os códigos normalmente.
3. O programa irá requistar que seja inserido alguns dados para fins de realizar filtragens.
4. Estará explícito as informações necessárias para dar continuidade ao processo de análise e criação dos gráficos interativos.

## 🛠️ Construído com

* [Python](https://www.python.org/downloads/release/python-3124/) - Linguagem de programação usada
* [VsCode](https://code.visualstudio.com) - IDE usada
* [Streamlit](https://streamlit.io) - Biblioteca usada para criação do aplicativo web
* [Render](https://render.com) - Plataforma cloud usada

## ✒️ Autores

Gilbert Martins - Desenvolvimento & Documentação - [GilbertsMartins](https://github.com/GilbertsMartins)
