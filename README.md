# TailorCV

**Turn any job posting into a tailored, ATS ready resume in seconds powered by Gemini AI.**

TailorCV is a Chrome extension backed by a FastAPI service that reads a candidate's master CV once, then generates a role specific, fact checked resume for every job application  delivered as a polished, ready to send `.docx` file.

---

## Why I built this

Tailoring a resume for every application is repetitive and easy to get wrong  either you spend hours rewriting bullets by hand, or you let an AI "help" and end up with fabricated experience that doesn't survive an interview. TailorCV is built around a simple constraint: **the AI can rephrase, reorder, and emphasize  it can never invent.** Every claim in the output has to trace back to something in the source CV.

## How it works

1. **Upload once**  the user uploads their master CV as a PDF it's stored locally in the browser via `chrome.storage.local`.
2. **Paste a job description**  for any role they're applying to.
3. **Generate** — the extension sends both to the backend, which:
   - Sends the CV + job description to Gemini with a strict system prompt and a structured output schema (Pydantic).
   - Gemini returns tailored, reworded content  matching the employer's language where it's truthfully supported, and *omitting* anything the CV doesn't back up.
   - The structured result is rendered into a formatted Word document (headers, borders, bullet lists, skill groupings) with `python-docx`.
4. **Download** — the tailored `.docx` downloads automatically with a clean filename: `Name_Company_CV.docx`.

```
┌──────────────┐      ┌──────────────────────┐      ┌────────────────────┐
│ Chrome       │ POST │ FastAPI backend      │      │ Gemini API         │
│ Extension    │ ───► │ /generate            │ ───► │ (structured output)│
│ (popup.js)   │      │ main.py              │      │ gemini.py          │
└──────────────┘      └──────────────────────┘      └────────────────────┘
                                  │
                                  ▼
                        ┌──────────────────────┐
                        │ docx_generator.py    │
                        │ builds .docx from    │
                        │ structured CV dat    │
                        └──────────────────────┘
                                  │
                                  ▼
                         Tailored resume (.docx)
                         streamed back & downloaded
```

## Key features

-  **Fact-locked tailoring** — a system prompt with explicit anti-hallucination rules prevents invented employers, dates, metrics, or skills.
-  **Structured output end to end** — Gemini responds against a Pydantic schema (`TailoredCV`), which flows directly into document generation, no brittle text parsing.
-  **Professional formatting out of the box** — consistent headers, section borders, aligned company/date rows, categorized skills, generated with `python-docx`.
-  **One time CV upload** — the master CV is stored locally in the browser and reused across every generation.
-  **Scoped extension permissions** — only `storage` and `downloads`, and the extension only talks to its own backend host.

## Tech stack

| Layer | Tech |
|---|---|
| Extension | Chrome Manifest V3, vanilla JS/HTML/CSS |
| Backend | FastAPI, Uvicorn |
| AI | Google Gemini (`google-genai`), structured JSON output |
| Document generation | `python-docx` |
| Validation | Pydantic |
| Hosting | Render |

## Project structure

```
.
├── manifest.json         # Chrome extension config
├── popup.html/css/js     # Extension UI + client logic
├── main.py                # FastAPI app, /generate endpoint
├── gemini.py               # Gemini prompt, schema, and API call
├── docx_generator.py       # Structured data → formatted .docx
└── requirements.txt         # Backend dependencies
```

## Getting started

### Backend

```bash
git clone https://github.com/AqibSiddiqui12/TailorCV.git
cd TailorCV
pip install -r requirements.txt
```

Create a `.env` file with your Gemini API key:

```
GEMINI_API_KEY=your_key_here
```

Run the server:

```bash
python main.py
# Server runs on http://0.0.0.0:10000
```

### Chrome extension

1. Go to `chrome://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the project folder.
4. Update `BACKEND_URL` in `popup.js` and `host_permissions` in `manifest.json` if you're pointing at your own backend deployment.

## License

MIT

---

<sub>Built by [Aqib Siddiqui](https://github.com/AqibSiddiqui12)</sub>
