# Исходный список
lst = [1, 5, 3, 9, 2]

# Обратный порядок
reversed_lst = lst[::-1]
print("Обратный порядок:", reversed_lst)
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

# Пример использования:
nums = [3, -10, 2, -7, 5]
print("Сортировка по убыванию абсолютных значений:", list_sort(nums))
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Пример использования:
items = [10, 20, 30, 40]
print("После замены первого и последнего элемента:", change(items))
