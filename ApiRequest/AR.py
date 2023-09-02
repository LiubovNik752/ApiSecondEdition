class ApiRequest:
    """Создание класса ApiRequest с атрибутами request_type и payload"""

    def __init__(self, request_type = '', payload = ''):
        """Инициализация класса с динамическими атрибутами request_type и payload"""
        self.request_type = request_type
        self.payload = payload

    def get_payload(self):
        """Метод получения значения атрибута payload"""
        return self.payload

    def set_payload(self, value):
        """Метод изменения атрибута экземпляра класса"""
        if not isinstance(value, str):
            raise ValueError("Payload must be a string!")
        self.payload = value

