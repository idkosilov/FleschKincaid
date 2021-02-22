"""
Developers:
I. Kosilov (50%)
V. Vlasov (50%)
"""

from textblob import TextBlob
from collections import Counter


def readable_index(asl: float, asw: float, lang: str):
    if lang == "ru":
        value = 206.835 - 1.3 * asl - 60.1 * asw
    elif lang == "en":
        value = 206.835 - 1.015 * asl - 84.6 * asw
    else:
        raise Exception("Invalid language")
    return value


def metrics_text(text):
    lang = text.detect_language()
    sentences = len(text.sentences)
    words = len(text.words)
    syllables = 0
    letters_counter = Counter(text.lower())
    if lang == "ru":
        for vowel in ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]:
            syllables += letters_counter[vowel]
    elif lang == "en":
        for vowel in ["a", "e", "i", "o", "u", "y"]:
            syllables += letters_counter[vowel]
    return lang, sentences, words, syllables


def main():
    text = TextBlob(input("Введите текст: "))
    lang, sentences, words, syllables = metrics_text(text)
    asl = words / sentences
    asw = syllables / words
    value = readable_index(asl, asw, lang)
    if value < 30:
        readable = "Очень трудно читать."
    elif 30 < value < 65:
        readable = "Немного трудно читать."
    elif 65 < value < 80:
        readable = "Легко читать."
    else:
        readable = "Очень легко читать."
    sentiment, subjectivity = text.sentiment if lang == "en" else text.translate(to="en").sentiment
    if sentiment < -0.5:
        tonality = "Негативная"
    elif -0.5 <= sentiment < 0.5:
        tonality = "Нейтральная"
    elif sentiment >= 0.5:
        tonality = "Позитивная"
    print(f"Предложений: {sentences}",
          f"Слов: {words}",
          f"Слогов: {syllables}",
          f"Средняя длина предложения в словах: {asl}",
          f"Средняя длина слова в слогах: {asw}",
          f"Индекс удобочитаемости Флеша: {value}",
          f"{readable}",
          f"Тональность: {tonality}",
          f"Объективность: {subjectivity * 100}%", sep='\n')


if __name__ == "__main__":
    main()
