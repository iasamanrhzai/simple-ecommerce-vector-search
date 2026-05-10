from sqlalchemy import text

from app.database import SessionLocal
from app.embeddings import create_embedding

db = SessionLocal()


def semantic_search(query: str, limit: int = 10):

    query_embedding = create_embedding(query)

    sql = text("""

        SELECT
            id,
            product_name,
            brand_name,
            category,
            color,
            selling_price,
            product_description,

            embedding <=> :embedding
            AS distance

        FROM products

        ORDER BY distance

        LIMIT :limit

    """)

    results = db.execute(

        sql,

        {
            "embedding": query_embedding,
            "limit": limit
        }

    )

    return results.fetchall()
