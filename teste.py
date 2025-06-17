from flask import Flask,jsonify

app = Flask(__name__)
app.json.sort_keys = False

# Lista de sapatos
estoque_sapatos = [
    {"ID": 1, "Cod_sapato": "SAP001", "Modelo": "Tênis", "Marca": "Nike", "Genero": "Masculino", "Numero": 42, "Quantidade": 10, "Cor": "Preto"},
    {"ID": 2, "Cod_sapato": "SAP002", "Modelo": "Sapatilha", "Marca": "Moleca", "Genero": "Feminino", "Numero": 37, "Quantidade": 15, "Cor": "Bege"},
    {"ID": 3, "Cod_sapato": "SAP003", "Modelo": "Bota", "Marca": "Timberland", "Genero": "Masculino", "Numero": 43, "Quantidade": 5, "Cor": "Marrom"},
    {"ID": 4, "Cod_sapato": "SAP004", "Modelo": "Sandália", "Marca": "Havaianas", "Genero": "Unissex", "Numero": 39, "Quantidade": 20, "Cor": "Azul"},
    {"ID": 5, "Cod_sapato": "SAP005", "Modelo": "Scarpin", "Marca": "Vizzano", "Genero": "Feminino", "Numero": 36, "Quantidade": 4, "Cor": "Vermelho"},
    {"ID": 6, "Cod_sapato": "SAP006", "Modelo": "Chinelo", "Marca": "Rider", "Genero": "Masculino", "Numero": 41, "Quantidade": 12, "Cor": "Cinza"},
    {"ID": 7, "Cod_sapato": "SAP007", "Modelo": "Mocassim", "Marca": "Ferracini", "Genero": "Masculino", "Numero": 40, "Quantidade": 7, "Cor": "Preto"},
    {"ID": 8, "Cod_sapato": "SAP008", "Modelo": "Salto Alto", "Marca": "Arezzo", "Genero": "Feminino", "Numero": 38, "Quantidade": 6, "Cor": "Dourado"},
    {"ID": 9, "Cod_sapato": "SAP009", "Modelo": "Slip On", "Marca": "Vans", "Genero": "Unissex", "Numero": 39, "Quantidade": 9, "Cor": "Branco"},
    {"ID": 10, "Cod_sapato": "SAP010", "Modelo": "Oxford", "Marca": "Democrata", "Genero": "Masculino", "Numero": 42, "Quantidade": 4, "Cor": "Marrom"},
]

@app.route('/')
def MensagemPrincipal():
    return 'Ola, Seja bem vindo a Democrate'

@app.route('/lista_sapatos',methods=['GET'])
def lista_sapatos():
    return jsonify(
            {
                "Mensagem":"Lista de Sapatos",
                "Dados":estoque_sapatos
            }
        )

@app.route('/lista_sapatos_vendedores',methods=['GET'])
def lista_sapatos_vendedores():
    sapatos_filtrados = [sapato for 
                         sapato in 
                         estoque_sapatos if 
                         sapato['Quantidade']>5 ]
    return jsonify({
                    "Mensagem":"Lista de Sapatos para Vendedores",
                    "Dados": sapatos_filtrados
                    })

@app.route('/lista_marcas_modelo',methods=['GET'])
def lista_marca_modelo():
    dados = [{"modelo": sapato["Modelo"], 
              "marca": sapato["Marca"]} 
              for sapato in estoque_sapatos]
    return jsonify({
                    "Mensagem":"Lista de Marcas e Modelos",
                    "Dados": dados
                    })

app.run()

