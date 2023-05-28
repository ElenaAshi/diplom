import configuration
import requests
import data

def post_new_order( body ):
    return requests.post( configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json = body)

def get_order_info( track ):
    return requests.get( configuration.URL_SERVICE + configuration.GET_TRACK + str( track ))

#def post_new_client_kit( body, token ):
   # headers = data.headers.copy()
    #headers[ "Authorization" ] = f"Bearer {token}"
    #response = requests.post( configuration.URL_SERVICE + configuration.CREATE_KITS, json = body, headers = headers )
    #return response
