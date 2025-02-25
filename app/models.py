from uuid import uuid4


class Memo:
    def __init__(self, text: str):
        self.id = str(uuid4())  # IDを文字列化
        self.text = text
