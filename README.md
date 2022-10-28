# NLLB-Translator

## Install

```bash
pip install git+https://github.com/huggingface/transformers
pip install torch
```

## Run

```bash
python inference.py
```

Output:

```text
Source text:
well i shared what my friend got (i dont need imaginary, i have real, if you know what that means)

---

Destination text:
Ну, я поділився тим, що отримав мій друг ( мені не потрібно уявного, у мене є реальний, якщо ви знаєте, що це означає)
```

## server

```bash
pip install python-multipart transformers torch uvicorn fastapi
./server.py

```
Server will listen on http://127.0.0.1:8080/docs
