import whisper

# Załaduj model (np. "small", "medium" lub "large")
model = whisper.load_model("medium")

# Opcjonalne: podaj ścieżkę do pliku audio
audio_path = r"data/les_parisiennes.wav"

# Transkrypcja z użyciem określonego języka
result = model.transcribe(audio_path, language="fr")

# Wyświetl wynik transkrypcji
print(result['text'])
# Zapisz wynik transkrypcji
with open('data/transcryption.txt', 'w') as f:
    f.write(result['text'])
