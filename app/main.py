from fastapi import FastAPI

from app.search import semantic_search

app = FastAPI(
    title="Ecommerce Vector Search API"
)


@app.get("/")


def home():

    return {
        "message": "Ecommerce Vector Search API"
    }


@app.get("/search")


def search(q: str, limit: int = 10):

    results = semantic_search(
        query=q,
        limit=limit
    )

    products = []

    for row in results:

        products.append({

            "id": row.id,

            "product_name": row.product_name,

            "brand_name": row.brand_name,

            "category": row.category,

            "color": row.color,

            "price": row.selling_price,

            "description": row.product_description,

            "distance": row.distance
        })

    return {

        "query": q,

        "count": len(products),

        "results": products
    }
