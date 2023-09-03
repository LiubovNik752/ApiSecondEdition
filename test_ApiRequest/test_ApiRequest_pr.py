from ApiRequest.AR_property import ApiRequestProperty


class Test_ApiRequest_property:
    """Тест-класс для класса ApiRequestProperty"""

    def test_check_class(self):
        self.request1 = ApiRequestProperty("some_type", "some_data")
        assert isinstance(self.request1, ApiRequestProperty)

    def test_ValueError(self):
        self.request1 = ApiRequestProperty("some_type", "some_data")
        try:
            self.request1.payload_data = "very long value of attribute"
        except ValueError:
            print("Length of payload must be less 16")

    def test_TypeError(self):
        self.request1 = ApiRequestProperty("some_type", "some_data")
        try:
            self.request1.payload_data = ["data1", "data2"]
        except TypeError:
            print("Payload must be a string")

    def test_check_setter_positive(self):
        value1 = "some_type"
        value2 = "some_data"
        self.request1 = ApiRequestProperty(value1, value2)
        self.request1.payload_data = "new_data"
        assert self.request1.payload_data == "new_data"

    def test_check_setter_negative(self):
        value1 = "some_type"
        value2 = "some_data"
        self.request1 = ApiRequestProperty(value1, value2)
        self.request1.payload_data = "new_data"
        assert self.request1.payload_data != value2

    def test_check_deleter(self):
        self.request1 = ApiRequestProperty("some_type", "some_data")
        del self.request1.payload_data
        assert "payload_data" not in self.request1.__dict__
        assert "request" in self.request1.__dict__
