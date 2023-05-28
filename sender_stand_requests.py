import configuration
import requests
import data

def post_new_order( body ):
    return requests.post( configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json = body)

def get_order_info( track ):
    return requests.get( configuration.URL_SERVICE + configuration.GET_TRACK + str( track ))
