from uuid import uuid4


class Memo:
    def __init__(self, text: str):
        self.id = str(uuid4())
        self.text = text
