# APP Consulta de CEP

### Essa aplicação tem como finalidade consultar um CEP e retornar os dados do mesmo ao usuário.

### Finalidade:
    1. Praticar o uso de API's externas com Python utilizando a biblioteca requests.
    2. Praticar o uso do Streamlit para desenvolver um app simples usando Streamlit.
    3. Praticar o uso de Docker.

### Para executar o app:
    1. clone o repositório.
    '''bash
    git clone https://github.com/alerrandrofrederik/app_consulta_cep.git
    '''

    2. Entre na pasta do repositório.
    '''bash
    cd app_consulta_cep
    '''

    3. Instale as dependências.
    '''bash
    pip install -r requirements.txt
    '''

    4. Construa a imagem Docker.
    '''bash
    docker build -t app_consulta_cep .
    '''

    5. Execute o container.
    '''bash
    docker run -p 8501:8501 -d --name streamlit-app consulta_cep
    '''
    
    6. Acesse o app em http://localhost:8501