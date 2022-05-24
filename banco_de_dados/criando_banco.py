import sqlite3

connection = sqlite3.connect('Hospedagem.db')
cursor = connection.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id INTEGER PRIMARY KEY, \
                nome text,\
                avaliacao INTEGER,\
                cidade text,\
                diaria float)"
                
criar_hotel = "INSERT INTO hoteis Values \
                (7, 'REIS', 10, 'Maceio', 450)"

cursor.execute(criar_tabela)
cursor.execute(criar_hotel)

connection.commit()
connection.close()