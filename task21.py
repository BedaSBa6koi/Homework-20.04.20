#Функция для удаления знаков препинания из предложения
def func():
    text = input('Enter text:\n')
    e = ',', '.', '!'
    for i in range(len(e)):
        text = text.replace(e[i], "")
    print(text)
func()

