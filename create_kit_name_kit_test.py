import sender_stand_requests
import data

def get_new_order_track():
    response = sender_stand_requests.post_new_order( data.order_body )
    assert response.status_code == 201
    return response.json()[ 'track' ]

def test_get_new_order_info():
    track = get_new_order_track()
    response = sender_stand_requests.get_order_info( track )
    assert response.status_code == 200

#Елена Ашихмина, 4-ая когорта-Финальный проект. Инженер по тестированию плюс.