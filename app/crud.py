from .models import Memo


memos = []

def get_memos():
    return memos

def add_memo(text: str):
    memo = Memo(text)
    memos.append(memo)

def update_memo(memo_id: str, text: str):
    for memo in memos:
        if memo.id == memo_id:
            memo.text = text
            return True
    return False

def delete_memo(memo_id: str):
    global memos
    memos = [memo for memo in memos if memo.id != memo_id]
