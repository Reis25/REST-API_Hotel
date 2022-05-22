from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

lista_hoteis = [
    {
        'hotel_id': 1,
        'nome': "alpha",
        'avaliacao': 5,
        'cidade': 'RJ',
        'diaria': 500
    }, 
    {
        'hotel_id': 2,
        'nome': "Beta",
        'avaliacao': 4,
        'cidade': 'SE',
        'diaria': 400
    },
    {
        'hotel_id': 3,
        'nome': "gama",
        'avaliacao': 3,
        'cidade': 'AL',
        'diaria': 300
    }
]

class Hoteis(Resource):
    
    def get(self):
        return {'hoteis': lista_hoteis}
    
api.add_resource(Hoteis, '/nome_hoteis')

if __name__ == '__main__':
    app.run(debug=True) #enquanto estivermos desenvolvendo. 

