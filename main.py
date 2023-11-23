

# def read_end(lines, file):
#     try:
#         lines = int(lines)
#         if lines <= 0:
#             print("Пожалуйста, введите положительное целое число для количества строк.")
#             return
#     except ValueError:
#         print("Пожалуйста, введите положительное целое число для количества строк.")
#         return

#     try:
#         with open(file, 'r', encoding='utf-8') as f:
#             all_lines = f.readlines()
#             if lines > len(all_lines):
#                 lines = len(all_lines)
#             for line in all_lines[-lines:]:
#                 print(line.strip())
#     except FileNotFoundError:
#         print(f"Файл {file} не найден.")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
# read_end(3, 'arf.txt')





# import os

# def print_reps(directory):
#     try:
#         for root, dirs, files in os.walk(directory):
#             print(f'Папка: {root}')
#             print('Файлы:')
#             for file in files:
#                 print(f'  {file}')
#             print('---')
#     except FileNotFoundError:
#         print(f"Папка {directory} не найдена.")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")

# print_reps('путь к ващему venv файлу, у меня она в другом месте было')

def longest_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()

            letters_count = len(text)
            words_count = len(text.split())
            lines_count = len(text.splitlines())

            words = text.split()
            max_length = max(len(word) for word in words)
            longest_words_list = [word for word in words if len(word) == max_length]

            print(f"Input file contains:")
            print(f"{letters_count} letters")
            print(f"{words_count} words")
            print(f"{lines_count} lines")

            if longest_words_list:
                print(f"\nLongest word(s): {', '.join(longest_words_list)}")
            else:
                print("\nNo words found.")
    except FileNotFoundError:
        print(f"File {file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
longest_words('poem.txt')




def file_statistics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        letter_count = sum(c.isalpha() for c in content)

        word_count = len(content.split())

        line_count = content.count('\n') + 1

    print(f"Input file contains:\n{letter_count} letters\n{word_count} words\n{line_count} lines")

file_statistics('file.txt')
