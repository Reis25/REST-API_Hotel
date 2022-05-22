from flask_restful import Resource,reqparse


#reqparser: recebe dados de uma requisição

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
    
     #Aceitando os argumentos: 
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('avaliacao')
    argumentos.add_argument('cidade')
    argumentos.add_argument('diaria')
    
    def find_hotel(hotel_id):
        for hotel in lista_hoteis: 
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
    
    # select: Visualizar os dados 
    def get(self, hotel_id):
        
        ht = hoteis.find_hotel(hotel_id)
        if ht:
            return ht
        return {'message': 'Hotel not found'}, 404 #status da aplicação: Not Found
        
    # Insert: Inserindo dados na lista/base de dados.
    def post(self, hotel_id):
        
        #Construtor: recebe dados chaves e valores passado na requisição
        dados = hoteis.argumentos.parse_args()
        
        novo_hotel =  {
        'hotel_id': hotel_id,
        'nome': dados['nome'],
        'avaliacao': dados['avaliacao'],
        'cidade': dados['cidade'],
        'diaria': dados['diaria']
        }
        
        #Adicionando o hotel vindo da requisição na lista de hoteis: 
        lista_hoteis.append(novo_hotel)
        
        return novo_hotel, 200
        
    #Update/Insert: Se o ID já existir ele atualiza, caso contrário ele cria. 
    def put(self, hotel_id):
        
        dados = hoteis.argumentos.parse_args()
        
        # usando o conceito de kargs em **dados
        novo_hotel =  {
        'hotel_id': hotel_id,
        **dados
        }
        
        hotel = hoteis.find_hotel(hotel_id)
        
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 # codigo de codigo com sucesso. 
        lista_hoteis.append(novo_hotel)
        return novo_hotel, 201 # codigo de insersão na lista/banco
        
         
        
         
    
    
    #Deletando dados 
    def delete(self, hotel_id): 
        pass 