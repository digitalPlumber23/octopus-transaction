from pydantic import BaseModel

class TransactionIn(BaseModel):
    user: str
    transaction_id: str
    amount: float

class Transaction(TransactionIn):
    pass
