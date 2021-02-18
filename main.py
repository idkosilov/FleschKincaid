from textblob import TextBlob
from collections import Counter


def readable_index(asl: float, asw: float, lang: str):
    """
    Влас, эту функцию делаешь ты для русского и английского языка в зависимости от языка должны быть разные формулы
    :param lang: язык текста
    :param asl: средняя длина предложения в словах
    :param asw: средняя длина слова в слогах
    :return: FRE = 206.835 − (1.3 × ASL) − (60.1 × ASW) - индекс удобочитаемости
    классификацию = текст хорошо читается (загугли классификацию)
    """
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
    sentiment, subjectivity = text.sentiment if lang == "en" else text.translate(to="en").sentiment


if __name__ == "__main__":
    main()
