import asyncpg
from app.models import TransactionIn

DB_URL = "postgresql://postgres:postgres@db:5432/transactions"

async def init_db():
    conn = await asyncpg.connect(DB_URL)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            user TEXT,
            transaction_id TEXT PRIMARY KEY,
            amount FLOAT
        )
    """)
    await conn.close()

async def insert_transaction(transaction: TransactionIn):
    conn = await asyncpg.connect(DB_URL)
    await conn.execute("""
        INSERT INTO transactions (user, transaction_id, amount)
        VALUES ($1, $2, $3)
    """, transaction.user, transaction.transaction_id, transaction.amount)
    await conn.close()
