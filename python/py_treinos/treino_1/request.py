import requests
from requests.models import Response 
def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    dados_cep = response.json()
    return dados_cep

def retorna_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon=response.json()
    return dados_pokemon

if __name__ == "__main__":
    print(retorna_cep('21021180'))
    print(retorna_pokemon('charizard'))
    