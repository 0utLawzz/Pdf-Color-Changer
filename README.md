# PDF Color Changer

A simple Windows desktop tool that changes dark/black text, table borders, and lines
in a PDF to a custom color (e.g. maroon, dark green, navy) — **without changing the
wording or layout** of the document.

Built with Python (Tkinter GUI) and [PyMuPDF](https://pymupdf.readthedocs.io/).

---

## ✨ Features

- Simple point-and-click GUI (no command line needed)
- Recolors dark neutral pixels (black/dark gray text, borders, lines)
- Preserves existing colored/saturated artwork (logos, colored graphics stay untouched)
- Built-in color presets (Maroon, Orange, Green, Navy, Black) + custom HEX picker
- Adjustable output resolution (DPI) and darkness threshold
- Works page-by-page, outputs a new PDF (original file is never modified)

---

## ⚠️ Important — How this runs

This is a **desktop application**, not a website or web app.

- GitHub only stores and version-controls the code — it does **not** run this app for you.
- To use it, you need to download/clone this repo and run it **on your own Windows PC**
  with Python installed.
- There is no online/browser version of this tool.

---

## 🖥️ Requirements

- **Windows** (this build uses `RUN.bat` and Tkinter, which ships with Windows Python)
- **Python 3.8+** — [Download here](https://www.python.org/downloads/) (during install,
  check ✅ "Add Python to PATH")
- Internet connection (only needed once, to install the `PyMuPDF` package)

---

## 🚀 Installation & Usage

### Option A — Easiest (double-click)

1. [Download this repo as a ZIP](../../archive/refs/heads/main.zip) and extract it
   (or `git clone` it — see below).
2. Double-click **`RUN.bat`**.
   - It will automatically check for Python, install `PyMuPDF` if missing, and launch the app.
3. In the app:
   - Click **Browse…** and select your PDF.
   - Pick a color preset or enter a custom HEX code.
   - Adjust resolution/threshold if needed.
   - Click **CONVERT PDF** and choose where to save the output.

### Option B — Manual (command line)

```bash
git clone https://github.com/<your-username>/pdf-color-changer.git
cd pdf-color-changer
pip install -r requirements.txt
python PDF_Color_Changer.py
```

---

## ⚙️ Settings explained

| Setting | What it does |
|---|---|
| **Preset / HEX** | The target color that dark elements will be shifted toward |
| **Resolution (DPI)** | Higher = sharper output but larger file & slower processing. 300 is a good default |
| **Darkness threshold** | How "dark" a pixel must be before it gets recolored. Lower = only the very darkest pixels change; higher = more mid-tones get affected too |

---

## 📁 Project structure

```
PDF-Color-Changer/
├── PDF_Color_Changer.py   # Main application (GUI + conversion logic)
├── RUN.bat                # One-click launcher for Windows
├── requirements.txt       # Python dependencies (PyMuPDF)
├── LICENSE                # MIT License
└── README.md              # This file
```

---

## 🛠️ Built with

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — built-in GUI toolkit
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) — PDF rendering & manipulation

---

## 📄 License

Released under the [MIT License](LICENSE) — free to use, modify, and share.
