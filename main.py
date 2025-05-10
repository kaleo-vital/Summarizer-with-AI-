
---

### `main.py`

```python
from summarizer.pdf_reader import extract_text_from_pdf
from summarizer.ai_summarizer import generate_summary
import sys

if len(sys.argv) < 2:
    print("Uso: python main.py <caminho_pdf>")
    exit()

pdf_path = sys.argv[1]

print("📄 Extraindo texto do PDF...")
text = extract_text_from_pdf(pdf_path)

print("🧠 Gerando resumo com IA...")
summary = generate_summary(text)

with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("\n✅ Resumo salvo em summary.txt")
