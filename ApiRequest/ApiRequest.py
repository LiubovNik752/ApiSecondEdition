class ApiRequest:
    """Создание класса ApiRequest с атрибутами request_type и payload"""


    def __init__(self, request_type = '', payload = ''):
        """Инициализация класса с динамическими атрибутами request_type и payload"""
        self.request_type = request_type
        self.payload = payload


    def set_payload(self, new_payload):
        """Метод изменения атрибута экземпляра класса"""
        if not isinstance(new_payload, str):
            raise ValueError("Payload must be a string!")
        self.payload = new_payload


    """Изменение атрибута payload через property"""
    payload = property(fset=set_payload)