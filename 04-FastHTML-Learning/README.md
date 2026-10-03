# ⚡ FastHTML & HTMX Progressive Learning Lab

A progressive series of tutorials, experiments, and mini-applications showcasing modern Python-based web development with **FastHTML**, **HTMX**, and **Pico CSS**.

---

## 🗺️ Learning Roadmap

### 1. Fundamentals of FastHTML (`1_fast_html_*.py`)
- Basic application initialization with `fast_app()`.
- Returning HTML tags directly as Python objects (`H1`, `P`, `Div`, `A`).
- Routing basics, path parameters, and static responses.

### 2. Modern UI with Pico CSS (`2_fast_html_pico*.py`)
- Declarative styling using lightweight semantic CSS (`Pico CSS`).
- UI Grid systems, containers, cards, and responsive headers.
- Building modern dashboards without heavy JavaScript frameworks.

### 3. Forms & State Handling (`3_fast_html_form*.py`)
- HTML forms (`Form`, `Input`, `Button`, `Select`).
- Parsing query parameters, form payloads, and user inputs into typed Python arguments.

### 4. HTTP Verbs & REST Architecture (`4_fast_html_http_*.py`)
- Implementing `GET`, `POST`, `PUT`, `DELETE` routes with `@rt`.
- Redirect responses, status code manipulation, and error handling.

### 5. Asynchronous Interactivity with HTMX (`5_fast_html_ajax_*.py`)
- Declarative AJAX using `hx-get`, `hx-post`, `hx-target`, and `hx-swap`.
- Debounced live search inputs (`hx-trigger="keyup delay:500ms"`).
- Dynamic list insertion and live counters without full page reloads.

### 6. Interactive Mini Applications
- [`6_fast_html_book.py`](6_fast_html_book.py): Book catalog and review submission.
- [`7_fast_html_2_page.py`](7_fast_html_2_page.py): Multi-page navigation and transitions.
- [`7_fast_html_increment.py`](7_fast_html_increment.py): Real-time reactive counter.
- [`7_fast_html_popup.py`](7_fast_html_popup.py): Modal dialogs and popups.
- [`sport_complex.py`](sport_complex.py): Sports facility booking system with visual cards.
- [`todo.py`](todo.py): Full CRUD Todo app with dynamic task completion.

---

## 🚀 Running any FastHTML Script
```bash
pip install python-fasthtml
python 04-FastHTML-Learning/todo.py
```
Open `http://localhost:5001` in your browser.
