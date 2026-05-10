from unittest.mock import patch, Mock


from tests.test_main import client


@patch('pizza_api_project.routers.orders.the_items_list_is_empty', return_value=False)
def test_success_post_order_endpoint(mock_order) -> None:
    # Act
    response = client.post("/orders", json={'customer_name': 'ofek', 'pizzas': [{"name": "Margherita", "price": 10.0}]})
    # Assert
    assert response.status_code == 200


#def test_post_order_endpoint():
 #   mock_order_request = Mock()
  #  mock_order_request.the_items_list_is_empty = Mock(return_value=True)
   # assert create_order(mock_order_request) ==

