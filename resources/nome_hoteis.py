from flask_restful import Resource

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

class listando_hoteis(Resource):
    
    def get(self):
        return {'hoteis': lista_hoteis}
    
class hoteis(Resource):
    
    # Visualizar os dados 
    def get(self, hotel_id):
        for hotel in lista_hoteis: 
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found'}, 404 #status da aplicação: Not Found
        
    
    def post(self, hotel_id):
        pass 
    
    def put(self, hotel_id): 
        pass 
    
    def delete(self, hotel_id): 
        pass 