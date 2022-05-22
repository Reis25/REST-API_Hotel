from flask import Flask
from flask_restful import Resource, Api
from resources.nome_hoteis import hoteis, listando_hoteis

app = Flask(__name__)
api = Api(app)


    
api.add_resource(listando_hoteis, '/hoteis')

api.add_resource(hoteis, '/hoteis/<int:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True) #enquanto estivermos desenvolvendo. 

