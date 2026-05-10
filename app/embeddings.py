from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "all-MiniLM-L6-v2"
)

model = SentenceTransformer(MODEL_NAME)


def create_embedding(text: str):

    embedding = model.encode(text)

    return embedding.tolist()
