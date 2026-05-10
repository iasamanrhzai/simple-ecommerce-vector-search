from sqlalchemy import Column, Integer, Text, Float
from pgvector.sqlalchemy import Vector

from app.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    uniq_id = Column(Text)

    product_name = Column(Text)

    brand_name = Column(Text)

    category = Column(Text)

    color = Column(Text)

    selling_price = Column(Float)

    product_description = Column(Text)

    embedding = Column(Vector(384))
