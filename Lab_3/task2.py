# TODO Напишите функцию find_common_participants
# Методы строк
def find_common_participants(group1, group2, separator=','):
    Stroka1 = set(group1.split(separator))
    Stroka2 = set(group2.split(separator))
    common = list(Stroka1 & Stroka2)
    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common)