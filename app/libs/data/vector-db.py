from pgvector.sqlalchemy import Vector
from sqlalchemy import Column


class Embedding(Base):
    __tablename__ = "embeddings"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    embedding = Column(Vector(1536))  # embedding dimension, adjust as needed
