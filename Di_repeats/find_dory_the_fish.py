from collections import Counter

# список файлов fasta, которые нужно проверить
files = ['O60469.fasta', 'P11308.fasta']

# словарь для хранения результатов поиска повторов в каждом файле
results = {}

# функция для поиска повторов любой длины
def find_repeats(seq):
    # пустой словарь для хранения количества повторений каждой подстроки
    repeats = Counter()
    # проходимся по каждому символу в последовательности и создаем все возможные подстроки
    for i in range(len(seq)):
        for j in range(i+1, len(seq)+1):
            substring = seq[i:j]
            repeats[substring] += 1
    # возвращаем список подстрок, которые встречаются более одного раза
    return [k for k, v in repeats.items() if v > 1]

# проходимся по каждому файлу
for file in files:
    # открываем файл fasta и читаем содержимое
    with open(file) as f:
        content = f.read().split('>')

    # удаляем первый элемент списка, так как он пустой
    content.pop(0)

    # список для хранения повторов в каждой последовательности в файле
    repeats_list = []

    # проходимся по каждой последовательности в файле
    for sequence in content:
        # разделяем заголовок и последовательность
        parts = sequence.split('\n')
        header = parts[0]
        seq = ''.join(parts[1:])

        # ищем повторяющиеся последовательности любой длины в последовательности
        repeats = find_repeats(seq)

        # сохраняем результаты для каждой последовательности в списке
        repeats_list.append(repeats)

    # сохраняем результаты поиска повторов для данного файла в словаре
    results[file] = repeats_list

# выводим результаты поиска повторов для каждого файла
for file, repeats_list in results.items():
    print(f"File: {file}")
    for i, repeats in enumerate(repeats_list):
        print(f"Sequence {i+1} repeats: {', '.join(repeats)}")
    print()
