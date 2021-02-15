from textblob import TextBlob


def flesch_index(asl: float, asw: float):
    """
    Влас, эту функцию делаешь ты
    :param asl: средняя длина предложения в словах
    :param asw: средняя длина слова в слогах
    :return: FRE = 206.835 − (1.3 × ASL) − (60.1 × ASW) - индекс удобочитаемости
    классификацию = текст хорошо читается (загугли классификацию)
    """
    return index, text


def chech_language(s):
    return


def main():
    text = TextBlob(input("Введите текст: "))
    print(f"Предложений: {0}")
    print(f"Слов: {0}")
    print(f"Слогов: {0}")
    asl, asw = 0, 0
    print(f"Средняя длина предложения в словах: {0}")
    print(f"Средняя длина слова в слогах: {0}")
    index, text = flesch_index(asl, asw)
    print(f"Индекс удобочитаемости Флеша: {index}")
    print(text)
    print(f"Тональность текста: {0}")
    print(f"Объективнсоть: {0}")


if __name__ == "__main__":
    main()
