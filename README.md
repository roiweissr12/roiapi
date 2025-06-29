# RoiAPI — FastAPI LLM Service

## Installation

Install dependencies with Poetry:

```bash
poetry install
```

---

## Running the Server

Start the FastAPI app with auto-reload:

```bash
poetry run uvicorn roiapi.main:app --reload
```

Open your browser and visit the interactive API docs at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Testing

Run the test suite with:

```bash
pytest
```

---

## Code Quality & Formatting

### Auto-format code with Black

```bash
poetry run black .
```

### Lint and auto-fix issues with Ruff

```bash
poetry run ruff check . --fix
```

---

### see typing problems
```bash
poetry run mypy .
```

Feel free to contribute or report issues!
