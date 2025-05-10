import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(text):
    if len(text) > 3000:
        text = text[:3000]  # Limita o tamanho para a API

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou gpt-4 se disponível
        messages=[
            {"role": "system", "content": "Você é um assistente que resume textos longos."},
            {"role": "user", "content": f"Resuma o seguinte texto: {text}"}
        ]
    )

    return response['choices'][0]['message']['content'].strip()
