# Ecommerce Vector Search

Semantic ecommerce search using:
- FastAPI
- PostgreSQL + pgvector
- Sentence Transformers

Dataset used:
Amazon Product Dataset 2020
https://www.kaggle.com/datasets/promptcloud/amazon-product-dataset-2020

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start PostgreSQL

```bash
docker compose up -d
```

### 3. Enable pgvector

```sql
CREATE EXTENSION vector;
```

### 4. Create products table

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,

    uniq_id TEXT,
    product_name TEXT,
    brand_name TEXT,
    category TEXT,
    color TEXT,
    selling_price FLOAT,
    product_description TEXT,

    embedding VECTOR(384)
);
```

### 5. Download Dataset

Download:
https://www.kaggle.com/datasets/promptcloud/amazon-product-dataset-2020

Place CSV inside:

data/amazon_products.csv

### 6. Run ingestion

```bash
python app/ingest.py
```

### 7. Create Vector Index

```sql
CREATE INDEX products_embedding_idx
ON products
USING hnsw (embedding vector_cosine_ops);

ANALYZE products;
```

### 8. Start FastAPI

```bash
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000/docs
