from app.database import SessionLocal
from app.models import Product
from app.embeddings import create_embedding
from app.utils import load_dataset, clean_text


df = load_dataset(
    "data/amazon_products.csv"
)

db = SessionLocal()

print(f"Loaded {len(df)} rows")

for index, row in df.iterrows():

    try:

        product_name = clean_text(
            row["Product Name"]
        )

        brand_name = clean_text(
            row["Brand Name"]
        )

        category = clean_text(
            row["Category"]
        )

        color = clean_text(
            row["Color"]
        )

        description = clean_text(
            row["Product Description"]
        )

        combined_text = f"""
        Product: {product_name}
        Brand: {brand_name}
        Category: {category}
        Color: {color}
        Description: {description}
        """

        embedding = create_embedding(
            combined_text
        )

        price = 0

        try:
            price = float(
                str(row["Selling Price"])
                .replace("$", "")
                .replace(",", "")
            )
        except:
            pass

        product = Product(

            uniq_id=row["Uniq Id"],

            product_name=product_name,

            brand_name=brand_name,

            category=category,

            color=color,

            selling_price=price,

            product_description=description,

            embedding=embedding
        )

        db.add(product)

        if index % 100 == 0:
            db.commit()
            print(f"Inserted {index} products")

    except Exception as e:

        print(f"Error on row {index}: {e}")

db.commit()

print("Done inserting products!")
