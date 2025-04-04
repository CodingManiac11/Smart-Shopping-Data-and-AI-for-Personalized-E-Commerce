from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample product dataset
products = [
    {"name": "Laptop", "category": "Electronics", "description": "High-performance laptop for gaming and work"},
    {"name": "Shoes", "category": "Fashion", "description": "Comfortable running shoes for daily wear"},
    {"name": "Headphones", "category": "Electronics", "description": "Noise-canceling headphones for great sound"},
]

# Encode product descriptions
product_embeddings = model.encode([p["description"] for p in products])

def recommend_products(user_input):
    user_embedding = model.encode([user_input])
    similarities = cosine_similarity(user_embedding, product_embeddings)
    ranked_products = np.argsort(similarities[0])[::-1]  # Sort in descending order
    recommendations = [products[i] for i in ranked_products[:3]]  # Return top 3
    return recommendations
