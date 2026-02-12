import faiss
import os
import json
import numpy as np

INDEX_PATH = "app/storage/faiss/index.bin"
META_PATH = "app/storage/faiss/meta.json"


class VectorStore:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

        if os.path.exists(INDEX_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            with open(META_PATH, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)

    def add(self, vectors, metadatas):
        vectors = np.array(vectors).astype("float32")
        self.index.add(vectors)
        self.metadata.extend(metadatas)
        self._persist()

    def search(self, vector, k=3):
        vector = np.array([vector]).astype("float32")
        distances, indices = self.index.search(vector, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results

    def _persist(self):
        faiss.write_index(self.index, INDEX_PATH)
        with open(META_PATH, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, indent=2)