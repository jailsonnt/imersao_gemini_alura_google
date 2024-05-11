import functions_framework
import os
import requests
from dotenv import load_dotenv

@functions_framework.http
def search_places_for_gemini(request):
    load_dotenv()
    body_json = request.get_json(silent=True)
    #body_json = {"response":{"proxima_mensagem":"resposta da AI", "endereco": "endereco aproximado", "buscas": [{"tipo_google": "lawyer", "tipo":"advogado criminalista" }, {"tipo_google": "bar", "tipo":"boate" }]}}
    print(os.environ.get('PLACES_API_KEY'))
    print(os.environ.get('FIELDS_TO_SHOW'))
    url = 'https://places.googleapis.com/v1/places:searchText'
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': os.environ.get('PLACES_API_KEY'),
        'X-Goog-FieldMask': os.environ.get('FIELDS_TO_SHOW')
    }

    endereco = body_json['response']['endereco']
    print("endereco:", endereco)
    places_response_list = []
    for busca in body_json['response']['buscas']:
        includedType = busca['tipo_google']
        busca = busca['tipo']
        textQuery = busca + " em " + endereco
        print("tipo_google:", includedType)
        print("tipo:", busca)
        print("Query:", textQuery)
        data = {
            "textQuery": textQuery,
            "maxResultCount": 2,
            "languageCode": "pt",
            "rankPreference": "RELEVANCE",
            "includedType": includedType
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            for place in response.json()['places']:
                places_response = {
                    'nome': place['displayName']['text'],
                    'telefone': place.get('nationalPhoneNumber', None),
                    'endereco': place.get('formattedAddress', None),
                    'url_gmaps': place.get('googleMapsUri', None),
                    'site': place.get('websiteUri', None)
                }
                places_response_list.append(places_response)
        else:
            print(f"Erro: {response.status_code}")
    print(places_response_list)
    return places_response_list