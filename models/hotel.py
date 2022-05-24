class HotelModel: #não precisa de parametros; 
    
    #construtor: 
    def __init__(self, hotel_id, nome, avaliacao, cidade, diaria):
        self.hotel_id = hotel_id
        self.nome = nome
        self.avaliacao = avaliacao
        self.cidade = cidade
        self.diaria = diaria
    
    # Criando um objeto para instanciarmos a classe objeto; 
    # Passamos o dados como dicionário e recebemos no formato json
    def json(self): 
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'avaliacao': self.avaliacao,
            'cidade': self.cidade,
            'diaria': self.diaria
        }
        
    