# import requests
# import pytest
# from unittest.mock import patch, MagicMock
#
# from functions import wait_for_service
#
#
# @patch('requests.get')
# def test_wait_for_service_successful(mock_get):
#     mock_response = MagicMock(status_code=200)
#     mock_get.return_value = mock_response
#
#     wait_for_service()
#
#     assert True
#
#
# @patch('requests.get')
# def test_wait_for_service_connection_error_then_success(mock_get):
#     mock_get.side_effect = [requests.ConnectionError, MagicMock(status_code=200)]
#
#     wait_for_service()
#
#     assert True
#
#
# @patch('requests.get')
# def test_wait_for_service_multiple_attempts(mock_get):
#     mock_get.side_effect = [requests.ConnectionError, requests.ConnectionError, MagicMock(status_code=200)]
#
#     wait_for_service()
#
#     assert True
#
#
# @patch('requests.get')
# def test_wait_for_service_unsuccessful_healthcheck_then_success(mock_get):
#     mock_response_unsuccessful = MagicMock(status_code=500)
#     mock_response_successful = MagicMock(status_code=200)
#     mock_get.side_effect = [mock_response_unsuccessful, mock_response_successful]
#
#     wait_for_service()
#
#     assert True
#
#
# @patch('requests.get')
# def test_wait_for_service_timeout_on_healthcheck(mock_get):
#     mock_get.side_effect = requests.Timeout
#
#     with pytest.raises(requests.Timeout):
#         wait_for_service()
#
#
# @patch('requests.get')
# def test_wait_for_service_unexpected_exception(mock_get):
#     mock_get.side_effect = Exception
#
#     with pytest.raises(Exception):
#         wait_for_service()
