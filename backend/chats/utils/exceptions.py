from rest_framework.exceptions import APIException


class UserNotFound(APIException):
    status_code = 404
    default_detail = 'Usuário não encontrado.'
    default_code = 'User not found'


class ChatNotFound(APIException):
    status_code = 404
    default_detail = 'Chat não encontrado e/ou não pertence ao usuário'
    default_code = 'Chat not found'
