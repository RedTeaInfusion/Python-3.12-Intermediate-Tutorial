'''
Lesson 07 - CSV
csv
writer()
writerow()
writerows()
reader()
'''
import os
import csv

CSV_FILE = 'course.csv'

def create_initial_csv():
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Lesson number', 'Lesson name', 'Completed', 'Difficulty', 'Notes'])

def add_or_update_lesson(lesson_number, lesson_name, completed, difficulty, notes):
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        if row[0] == lesson_number:
            row[1] = lesson_name
            row[2] = completed
            row[3] = difficulty
            row[4] = notes
            break
    else:
        rows.append([lesson_number, lesson_name, completed, difficulty, notes])
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print(f'Updated {CSV_FILE}')

def view_progress():
    print('\nViewing progress: ')
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    if not os.path.exists(CSV_FILE):
        create_initial_csv()
    while True:
        print('\nOptions:')
        print('1. Add or update a lesson')
        print('2. View progress')
        print('0. Exit')

        choice = input('Enter your choice: ')
        match choice:
            case '1':
                lesson_number = input('Enter lesson number: ')
                lesson_name = input('Enter lesson name: ')
                completed = input('Is the lesson completed? ')
                difficulty = input('Enter perceived difficulty: ')
                notes = input('Enter any notes: ')
                add_or_update_lesson(lesson_number, lesson_name, completed, difficulty, notes)
            case '2':
                view_progress()
            case '0':
                print('Exiting program.')
                break
            case _:
                print('\nInvalid choice')

if __name__ == '__main__':
    main()