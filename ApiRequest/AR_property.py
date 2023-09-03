
class ApiRequestProperty:
    """Создание класса ApiRequest_property для получения и изменения атрибутов через свойства"""

    def __init__(self, request_type = None, payload = None):
        """Инициализация класса с атрибутами request_type и payload"""
        self.request = request_type
        self.payload_data = payload

    @property
    def payload_data(self):
        """Метод получения значения атрибута payload"""
        return self.__payload_data

    @property
    def request_type(self):
        """Метод получения значения атрибута request"""
        return self.__request

    @payload_data.setter
    def payload_data(self, value):
        """Метод изменения атрибута экземпляра класса с произвольными проверками (в данном случае, на тип атрибута и его длину)"""
        if not isinstance(value, str):
            raise TypeError("Payload must be a string")
        if len(value) > 15:
            raise ValueError("Length of payload must be less 16")
        self.__payload_data = value

    @payload_data.deleter
    def payload_data(self):
        """Метод удаления атрибута экземпляра класса"""
        del self.__payload_data



