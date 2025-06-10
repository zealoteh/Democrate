from flask import Flask,jsonify

app = Flask(__name__)
app.json.sort_keys = False 
# Lista de sapatos
sapatos = [
    {
        "id": 1,
        "marca": "Nike",
        "tipo_sapato": "Tênis",
        "numero": 42,
        "cor": "Preto",
        "cod_prod": "NK-001"
    },
    {
        "id": 2,
        "marca": "Adidas",
        "tipo_sapato": "Chinelo",
        "numero": 40,
        "cor": "Azul",
        "cod_prod": "AD-002"
    },
    {
        "id": 3,
        "marca": "Vans",
        "tipo_sapato": "Tênis",
        "numero": 39,
        "cor": "Vermelho",
        "cod_prod": "VN-003"
    },
    {
        "id": 4,
        "marca": "Puma",
        "tipo_sapato": "Bota",
        "numero": 43,
        "cor": "Marrom",
        "cod_prod": "PM-004"
    },
    {
        "id": 5,
        "marca": "Mizuno",
        "tipo_sapato": "Sapatênis",
        "numero": 41,
        "cor": "Branco",
        "cod_prod": "MZ-005"
    }
]

@app.route('/')
def home():
    return "oi"

@app.route('/sapatos',methods=['GET'])
def lista_sapatos():
    return jsonify(
           {
            "Messagem" : "Lista de Sapatos",
            "Dados":sapatos
            }
        )

app.run()