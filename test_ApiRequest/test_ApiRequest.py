from ApiRequest.AR import ApiRequest


class Test_ApiRequest:
    """Тест-класс для класса ApiRequest"""

    def test_class(self):
        self.request1 = ApiRequest()
        assert isinstance(self.request1, ApiRequest)

    def test_check_attribute(self):
        request1 = ApiRequest()
        assert hasattr(request1, 'payload')
        assert hasattr(request1, 'request_type')

    def test_type(self):
        value1 = "data"
        self.request1 = ApiRequest(payload=value1)
        assert type(self.request1.payload) == str

    def test_default(self):
        self.request1 = ApiRequest()
        assert self.request1.payload == ''
        assert self.request1.request_type == ''

    def test_equality(self):
        value1 = "some_data"
        self.request1 = ApiRequest(payload = value1)
        assert self.request1.payload == "some_data"

    def test_inequality(self):
        value1 = "data"
        value2 = "new_data"
        self.request1 = ApiRequest(payload=value1)
        self.request2 = ApiRequest(payload=value2)
        assert self.request1 != self.request2

    def test_method_set_payload(self):
        self.request1 = ApiRequest()
        value = "new_data"
        self.request1.set_payload(value)
        assert self.request1.payload == value

    def test_check_dict_value(self):
        value1 = "some_data"
        value2 = "some_type"
        self.request = ApiRequest(payload=value1, request_type=value2)
        assert self.request.__dict__ == {'request_type': value2, 'payload': value1}

