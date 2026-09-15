# PDF Color Changer

A tool that changes dark/black text, table borders, and lines in a PDF to a custom
color (maroon, dark green, navy, etc.) — **without changing the wording or layout**
of the document.

This repo has **two versions** of the same tool:

| Version | Where it runs | Best for |
|---|---|---|
| 🖥️ [`desktop/`](desktop) | Your Windows PC (Python) | Bulk processing, large/high-DPI PDFs |
| 🌐 [`docs/`](docs) | Any browser — online **or** fully offline | Quick one-off use, no install needed |

Both use the **exact same recolor algorithm** — verified pixel-for-pixel identical
across 140,000+ test values.

---

## 🌐 Web Version — Online

**👉 [Open the live tool](https://REPLACE-WITH-YOUR-USERNAME.github.io/pdf-color-changer/)**

_(Replace the link above with your actual GitHub Pages URL once enabled — see
"Enabling GitHub Pages" below.)_

- Works in any modern browser (Chrome, Edge, Firefox)
- Your PDF is **never uploaded anywhere** — everything happens inside your own
  browser, in memory. Nothing is sent to any server.

## 📴 Web Version — Fully Offline (no internet needed)

The exact same tool also works with **zero internet connection**:

1. Download this repo (Code → Download ZIP, or `git clone`)
2. Open the `docs` folder
3. Double-click `index.html`
4. It opens in your browser and works completely offline

This works because the required libraries (PDF.js, jsPDF) are bundled **inside**
the `docs/vendor/` folder — nothing is fetched from the internet at runtime.

> ⚠️ Note: offline mode runs slightly slower than the online version on large
> PDFs, because of a Chrome security restriction on background workers for
> local files (`file://`). It still works correctly — just not as fast on very
> large/high-DPI files. See comments in `docs/index.html` for details.

---

## 🖥️ Desktop Version (Windows, Python)

See [`desktop/README`](#desktop-installation--usage) below, or just:

1. Download this repo
2. Go into the `desktop` folder
3. Double-click `RUN.bat`

### Desktop installation & usage

**Requirements:**
- Windows
- [Python 3.8+](https://www.python.org/downloads/) (check ✅ "Add Python to PATH" during install)

**Steps:**
```bash
cd desktop
pip install -r requirements.txt
python PDF_Color_Changer.py
```
Or simply double-click `RUN.bat` — it auto-installs the one dependency (`PyMuPDF`) if missing.

**Settings:**

| Setting | What it does |
|---|---|
| Preset / HEX | Target color that dark elements shift toward |
| Resolution (DPI) | Higher = sharper output, larger file, slower processing. 300 is a good default |
| Darkness threshold | How dark a pixel must be before it's recolored |

---

## ⚙️ Enabling GitHub Pages (one-time setup)

1. On GitHub, go to your repo → **Settings** → **Pages**
2. Under "Build and deployment" → **Source**: select **Deploy from a branch**
3. **Branch**: `main`, **Folder**: `/docs` → **Save**
4. Wait ~1 minute, then your live link will appear at the top of that same Pages settings screen
   (format: `https://<your-username>.github.io/pdf-color-changer/`)
5. Update the link in this README's "Web Version — Online" section above

No coding needed for this step — it's all clicking in GitHub's settings UI.

---

## 📁 Project structure

```
pdf-color-changer/
├── desktop/
│   ├── PDF_Color_Changer.py   # Main Python app (GUI + conversion logic)
│   ├── RUN.bat                # One-click launcher for Windows
│   └── requirements.txt       # Python dependency (PyMuPDF)
├── docs/                      # GitHub Pages serves this folder
│   ├── index.html             # The web app itself
│   └── vendor/                # Bundled libraries (for offline use)
│       ├── pdf.min.js
│       ├── pdf.worker.min.js
│       ├── jspdf.umd.min.js
│       ├── LICENSE-pdfjs.txt
│       └── LICENSE-jspdf.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🛠️ Built with

- [Python](https://www.python.org/) + [Tkinter](https://docs.python.org/3/library/tkinter.html) + [PyMuPDF](https://pymupdf.readthedocs.io/) — desktop version
- [PDF.js](https://mozilla.github.io/pdf.js/) (Apache-2.0) + [jsPDF](https://github.com/parallax/jsPDF) (MIT) — web version, bundled locally in `docs/vendor/`

---

## 📄 License

Released under the [MIT License](LICENSE) — free to use, modify, and share.
Bundled third-party libraries keep their own licenses (see `docs/vendor/LICENSE-*.txt`).
