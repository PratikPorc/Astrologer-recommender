# 🔮 Vedaz: LLM-Based Smart Astrologer Recommendation Engine

A lightweight and scalable NLP-based recommendation engine that connects users to the most relevant astrologers using state-of-the-art open-source LLMs and semantic search techniques.

## 🚀 Overview

Vedaz intelligently matches user queries with astrologer profiles using embedding similarity and contextual analysis powered by Sentence Transformers and LLMs like Mixtral from Together.ai. Built with fast and scalable components including FAISS for vector similarity search and FastAPI for API handling.

## ✨ Features

- 🔍 **Smart Matching**: Finds astrologers most suited to the user's query using semantic similarity (e.g., love, career, health).
- 🧠 **LLM Integration**: Adds reasoning via open-source LLMs for short response generation and tone adaptation.
- 🧾 **Embeddings**: Uses `all-mpnet-base-v2` for high-quality vector representations of text.
- 🧪 **Similarity Scoring**: FAISS-based top-k search from user queries to astrologer bios.
- ⚙️ **API-first Architecture**: Modular and scalable using FastAPI.
- 💸 **Budget-Friendly**: Runs on open LLMs via Together.ai or HuggingFace, vector store via Chroma or FAISS.

---

## 📁 Project Structure

```

vedaz-astrologer-recommendation/
├──  palmreader.py              # palmreader and horoscope generator
└── dataset/
│       └── astrologers.json # Sample astrologer dataset
└── notebook/
│       └── vedaz.ipynb # model training
├── .env                     # API keys and secrets (not committed)
├── requirements.txt         # Python dependencies
└── README.md

````

---

## 🛠️ Technologies Used

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Embeddings**: `sentence-transformers/all-mpnet-base-v2`
- **Vector Search**: FAISS
- **LLM API**: Together.ai (Mixtral-8x7B-Instruct)
- **Frontend (Optional)**: React or Next.js

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/vedaz-astrologer-llm.git
cd vedaz-astrologer-llm
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your `.env` file

```env
TOGETHER_API_KEY=your_api_key_here
```

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

### 5. Try the API

* POST `/recommend`: Get relevant astrologers based on a user query.
* POST `/chat`: (Optional) Get a short LLM-generated response related to query context.

---

## 📊 Example Query

```json
{
  "query": "I’m facing delays in my career growth. Which astrologer can help?"
}
```

### ✅ Response

```json
{
  "recommended_astrologers": [
    {
      "name": "Shalini R.",
      "specialty": "Career & Finance",
      "score": 0.78
    },
    ...
  ]
}
```

---

## 💡 Future Enhancements

* Fine-tune LLM on astrology Q\&A.
* Add user feedback loop to refine recommendations.
* Integrate payment and scheduling APIs for astrologer bookings.

---

## 🧠 Author

**Pratik Guha Roy**
[LinkedIn](https://www.linkedin.com/in/pratikfromindia/)
Prepared as a part of AI-based recommendation engine POC for Vedaz.

---

## ⚖️ License

MIT License. Feel free to fork, improve, and use for educational or commercial projects (with attribution).

```

