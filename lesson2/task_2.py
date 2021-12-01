"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""
src_array = []

while True:
    user_input = input("Введите элемент списка ('exit' для выхода):")
    if user_input.lower() == 'exit':
        break
    src_array += user_input

print(f'Исходный список:\t\t\t{src_array}')

i = 1
while i < len(src_array):
    tmp = src_array[i]
    src_array[i] = src_array[i - 1]
    src_array[i - 1] = tmp
    i += 2

print(f'Список после перестановок:\t{src_array}')
