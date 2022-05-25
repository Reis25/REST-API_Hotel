# Ponto de partida da imagem:
FROM nginx:1.19.4-alpine
# Responsável pela menutençã;
LABEL maintainer="demetrios Reis: demetriosreis1@gmail.com" 

# Para copiar arquivos desse diretório;
COPY . /home/demetrios/Downloads/Repositorios/REST-API_Hotel

# Tornando uma porta como padrão: (espelhando porta)
EXPOSE 80

