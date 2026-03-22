# Fact-Check Social — Automated Fact Checker for Vernacular News

A full-stack social media platform with AI-powered automated fact-checking.

---

## 🚀 Quick Start

### 1. Backend Setup

```bash
cd backend
python -m venv venv

# Activate (Windows):
venv\Scripts\activate
# Activate (macOS/Linux):
source venv/bin/activate

pip install -r requirements.txt
python run.py
# → Runs at http://localhost:8000
# → API docs at http://localhost:8000/docs
```

> **Note:** First run downloads AI models (~500 MB). This only happens once.

### 2. Frontend Setup (new terminal)

```bash
cd frontend
npm install
npm run dev
# → Runs at http://localhost:5173
```

### 3. Open the App

Go to **http://localhost:5173** and log in with any username + password.

---

## 🧪 Sample Verification Scenarios

| Post Caption | Expected Verdict |
|---|---|
| Great Wall visible from space | ❌ FALSE |
| We use only 10% of our brain | ❌ FALSE |
| COVID vaccines contain microchips | ❌ FALSE |
| Elon Musk is CEO of Twitter | ⏰ OUTDATED |
| Drink 8 glasses of water daily | ⚠️ MISLEADING |
| Everest is the tallest mountain | ✅ TRUE |

---

## 🛠️ Tech Stack

**Backend:** Python, FastAPI, Sentence-Transformers, FAISS, Transformers (NLI)

**Frontend:** React 18, Vite, Tailwind CSS, Axios, Lucide Icons

---

## 📁 Project Structure

```
fact-check-social/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry
│   │   ├── config.py            # Config & thresholds
│   │   ├── models/              # Pydantic models
│   │   ├── routes/              # auth, posts, verify
│   │   ├── services/            # AI pipeline
│   │   │   ├── preprocess.py
│   │   │   ├── claim_detector.py
│   │   │   ├── claim_extractor.py
│   │   │   ├── retrieval.py     # FAISS semantic search
│   │   │   ├── verifier.py      # NLI verification
│   │   │   ├── freshness_check.py
│   │   │   └── historical_context.py
│   │   └── data/
│   │       └── verified_facts.json
│   └── requirements.txt
└── frontend/
    └── src/
        ├── pages/       # Login, Feed
        ├── components/  # Header, PostCard, Modals, etc.
        ├── services/    # API calls
        └── utils/       # Auth helpers
```

---

## 🔧 Troubleshooting

**Models won't download:**
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

**Port already in use:**  
Change `port=8000` in `backend/run.py` and update `vite.config.js` proxy target.

**npm install fails:**
```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```
