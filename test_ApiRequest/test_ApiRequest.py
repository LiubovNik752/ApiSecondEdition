from ApiRequest.ApiRequest import ApiRequest


class Test_ApiRequest:

    def test_check_attribute(self):
        self.request1 = ApiRequest()
        assert hasattr(self.request1, 'payload')
        assert hasattr(self.request1, 'request_type')

    def test_default(self):
        self.request1 = ApiRequest()
        assert self.request1.payload == ''

    def test_equality(self):
        self.request1.payload = 'data'  # Проверка изменения атрибута payload через property
        assert self.request1.payload == "data"
        self.request2 = ApiRequest(payload = "some_data")
        assert self.request2.payload == "some_data"
        self.request3 = ApiRequest(payload = 123)
        assert self.request3.payload == 123
        self.request4 = ApiRequest(payload = 123)
        assert self.request3.__dict__ == self.request4.__dict__

    def test_inequality(self):
        assert self.request1 != self.request2
        self.request5 = ApiRequest(payload = '123')
        assert self.request4 != self.request5


    def test_type(self):
        assert type(self.request2.payload) == str
        assert type(self.request3.payload) == int
        assert isinstance(self.request1, ApiRequest)

    def test_method_set_payload(self):
        self.request2.set_payload("new_data")
        assert self.request2.payload != "some_data"
        assert self.request2.payload == "new_data"
