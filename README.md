# Fact-Check Social — Automated Fact Checker for Vernacular News

An AI-powered, full-stack social media platform that analyzes claims in social posts and provides automated fact-checking verdicts using natural language processing and machine learning.

## Overview

Fact-Check Social combines a social media feed with an automated claim-verification pipeline. It is designed to explore how NLP, semantic search, and natural language inference can help identify potentially false, misleading, or outdated claims.

## Features

- **Automated fact-checking:** Analyzes claims and produces verification verdicts.
- **Claim detection and extraction:** Identifies factual claims from post content.
- **Semantic retrieval:** Uses Sentence Transformers and FAISS to retrieve relevant information from a verified-facts dataset.
- **NLI-based verification:** Uses natural language inference models to assess relationships between claims and retrieved evidence.
- **Freshness checks:** Supports identifying claims that may be outdated.
- **Historical context:** Includes a component for considering historical information.
- **Social media interface:** Provides a React-based frontend with login and feed pages.
- **REST API:** Uses FastAPI to expose backend functionality.

> **Important:** Automated verdicts are model-generated assessments, not guarantees of truth. Verify important claims against reliable, current sources.

## Tech Stack

| Component | Technologies |
|---|---|
| Backend | Python, FastAPI |
| NLP and machine learning | Sentence Transformers, Transformers, Natural Language Inference (NLI) |
| Semantic search | FAISS |
| Frontend | React 18, Vite |
| Styling | Tailwind CSS |
| API communication | Axios |
| Icons | Lucide Icons |

## Project Structure

```text
fact-check-social/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   │   ├── preprocess.py
│   │   │   ├── claim_detector.py
│   │   │   ├── claim_extractor.py
│   │   │   ├── retrieval.py
│   │   │   ├── verifier.py
│   │   │   ├── freshness_check.py
│   │   │   └── historical_context.py
│   │   └── data/
│   │       └── verified_facts.json
│   └── requirements.txt
└── frontend/
    └── src/
        ├── pages/
        ├── components/
        ├── services/
        └── utils/
```

## Getting Started

### Prerequisites

Install the following before running the project:

- Python compatible with the backend dependencies
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/kushiarsur/automated-factchecker.git
cd automated-factchecker
```

### 2. Set up the backend

Open a terminal in the repository root:

```bash
cd backend
python -m venv venv
```

Activate the virtual environment.

**Windows (Command Prompt):**

```bat
venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

Install dependencies and start the backend:

```bash
pip install -r requirements.txt
python run.py
```

The backend is expected to run at `http://localhost:8000`, with interactive API documentation at `http://localhost:8000/docs`, if configured as described.

### 3. Set up the frontend

Open a second terminal at the repository root:

```bash
cd frontend
npm install
npm run dev
```

Vite typically serves the frontend at `http://localhost:5173`, unless the project configuration specifies another port.

### 4. Open the application

Visit `http://localhost:5173` in your browser.

Use the authentication flow configured by the application. If development mode supports arbitrary usernames and passwords, follow that behavior; otherwise, use the credentials and registration process configured by the project.

## Example Verification Scenarios

The following are illustrative test cases for evaluating the application's verdicts. They are not guaranteed outputs.

| Claim | Expected evaluation |
|---|---|
| The Great Wall of China is easily visible from the Moon with the naked eye. | False |
| Humans use only 10% of their brains. | False |
| COVID-19 vaccines contain microchips. | False |
| Elon Musk is the CEO of Twitter. | Outdated; evaluate against the relevant date and current company structure |
| Everyone must drink exactly eight glasses of water daily. | Misleading; individual hydration needs vary |
| Mount Everest is Earth's highest mountain above sea level. | True |

## Troubleshooting

### AI models fail to download

Check your internet connection and install the backend dependencies. You can test the Sentence Transformers model separately:

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

The first model download may require significant disk space and time, depending on your environment.

### Backend port is already in use

Check the port configuration in `backend/run.py` and update any corresponding frontend proxy configuration if necessary. Restart the application after changing the settings.

### Frontend dependencies fail to install

Try:

```bash
npm cache verify
npm install
```

If the issue persists, inspect the npm error before deleting dependency files or clearing the cache.

## Future Improvements

Potential enhancements include:

- Integrating trusted, up-to-date evidence sources.
- Displaying evidence and explanations alongside verdicts.
- Improving multilingual claim processing and vernacular-language support.
- Adding automated tests for retrieval, verification, and API endpoints.
- Evaluating model accuracy using a labeled test dataset.

## Disclaimer

This project demonstrates an NLP-based fact-checking approach for educational and research purposes. Model predictions can be incomplete or incorrect and should not replace verification using reliable sources.

## Author

**Kushi A. N.**

GitHub: [@kushiarsur](https://github.com/kushiarsur)
