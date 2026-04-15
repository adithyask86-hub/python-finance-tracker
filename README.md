# Finance Toolkit — Flask Web App

A full-featured financial planning web app built with Python (Flask).

## Features
- **Dashboard** — live summary of all calculations + saved history
- **EMI Calculator** — home loan EMI with months/years toggle
- **Loan Calculator** — personal loan calculator
- **SIP Calculator** — systematic investment plan with bar chart
- **Lump Sum Calculator** — one-time investment with compounding options
- **Interest Calculator** — simple & compound interest toggle

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser at: **http://localhost:5050**

## Project Structure
```
finance_app/
├── app.py              # Flask backend + API routes
├── requirements.txt
└── templates/
    └── index.html      # Frontend (HTML/CSS/JS)
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/emi` | EMI calculation |
| POST | `/api/sip` | SIP calculation |
| POST | `/api/lumpsum` | Lump sum FV calculation |
| POST | `/api/interest` | Simple/compound interest |
