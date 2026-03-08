# 🔥 Ember — Entropy-Seeded URL Shortener

> A URL shortener that uses a live lava lamp animation as a pseudo-random seed for short code generation — inspired by [Cloudflare's lava lamp wall](https://blog.cloudflare.com/randomness-101-lavarand-in-production/).

---

## Demo Video

<video controls src="Final_Draft_Demo.mp4" title="Title"></video>
---

## How It Works

Most URL shorteners just increment an ID. `1`, `2`, `3`. Predictable and guessable.

Ember renders a live metaball lava lamp simulation in the browser. When you shorten a link, it samples pixel data from the animation at that exact moment and mixes it into the short code seed. Every code is unique and unpredictable — derived from real-time visual chaos.

It's pseudo-random, not true entropy. But it's a better story than `id + 1`.

---

## Stack

- **Backend** — Python, Flask, SQLite
- **Frontend** — HTML, CSS, JavaScript, GSAP
- **Algorithm** — Base62 encoding seeded with canvas pixel sampling

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Clone the repo

```bash
git clone https://github.com/jay06rathod/Ember.git
cd Ember
```

### Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### Install dependencies

```bash
pip install flask
```

### Run

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Project Structure

```
Ember/
├── app.py          # Flask routes and core logic
├── db.py           # Database setup
├── index.html      # Frontend — lava lamp + UI
├── urls.db         # SQLite database (auto-generated)
└── README.md
```

---

## License

MIT License — feel free to use, modify, and distribute.

---

## Author

**Jay Rathod**
- GitHub: [@jay06rathod](https://github.com/jay06rathod)
- Twitter: [@Jay_Rathod_06](https://x.com/Jay_Rathod_06)
