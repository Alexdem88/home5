# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
result={}
with open ('hw6_file.txt') as file: #Сам не осилил, но детально разобрался
    file_lines = file.readlines()

for line in file_lines:
    data = line.split()
    hours = 0
    for elem in data[1:]:
        if elem != '-':
            num='0'
            for i in elem:
                if i.isdigit():
                    num += i
                else:
                    break
            hours += int(num)
    result.update({data[0].strip(':'):hours})
print(result)



