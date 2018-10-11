import json
import uuid


class MessageHeader():
    def __init__(self, message, *args, **kwargs):
        if 'header' in kwargs:
            for k, v in kwargs['header'].items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

        if not hasattr(self, 'requestId'):
            self.requestId = str(uuid.uuid4())

        if not hasattr(self, 'messagePurpose'):
            self.messagePurpose = "message"

        if not hasattr(self, 'version'):
            self.version = 1

        if not hasattr(self, 'messageType'):
            self.messageType = "commandRequest"

    def serialize(self):
        result = {}
        for k, v in self.__dict__.items():
            if not callable(v) and k[0] != '_':
                result[k] = v
        return result


class MessageBody():
    def __init__(self, message, *args, **kwargs):
        if 'body' in kwargs:
            for k, v in kwargs['body'].items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def serialize(self):
        result = {}
        for k, v in self.__dict__.items():
            if not callable(v) and k[0] != '_':
                result[k] = v
        return result


class Message():
    header_class = MessageHeader
    body_class = MessageBody

    def __init__(self, *args, **kwargs):
        self._header = self.header_class(self, *args, **kwargs)
        self._body = self.body_class(self, *args, **kwargs)

    @property
    def header(self):
        return self._header

    @property
    def body(self):
        return self._body

    def serialize(self):
        return {"header": self.header.serialize(), "body": self.body.serialize()}

    def __str__(self):
        return json.dumps(self.serialize())




if __name__ == "__main__":
    source = {
        "header": {
            "foo": "bar"
        },
        "body": {
            "tub": "poon"
        }
    }
    msg = Command(**source)

    print(msg)
