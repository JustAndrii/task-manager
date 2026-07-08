import psycopg2            # підключили бібліотеку

conn = psycopg2.connect(   # створили з'єднання
database="learning_sql",    # до якої бази підключаємось
user="postgres" ,           # під яким користувачем
password="1234567"  ,       # пароль цього користувача
host="localhost"  ,         # база на цьому комп'ютері
port="5432"                # через який порт підключаємось
)

cursor = conn.cursor() # створити “посередника”, через якого будемо відправляти SQL.



# cursor.execute()
    # виконати SQL-запит.



# rows = cursor.fetchall() # забери всі рядки
# print(rows)

# while True:
#     print()
#     print("MY TASKS")
#     print('-'*40)
#     print("1. Add task")
#     print("2. Show tasks")
#     print('3. Count tasks')
#     print("4. Delete task")
#     print("5. Update task")
#     print('0. Exit')
#     print('-'*40)
#     print()
#
#
#     choice = input("Enter your choice: ")
#
#     if choice == '1':
#         t = input("Enter your title: ")
#         d = input("Enter your description: ")
#         cursor.execute(f"INSERT INTO tasks (title, description) VALUES ('{t}', '{d}')")
#         conn.commit()
#         print('\nTask added!')
#
#     elif choice == '2':
#         cursor.execute("SELECT * FROM tasks")
#         rows = cursor.fetchall()
#         for row in rows:
#             id = row[0]
#             title = row[1]
#             description = row[2]
#             completed = row[3]
#             created_at = row[4]
#             print(f'ID: {id}\nTitle: {title}\nDescription: {description}\nCompleted: {completed}\nCreated at: {created_at}\n','-'*40)
#
#     elif choice == '3':
#         count = 0
#         cursor.execute("SELECT * FROM tasks")
#         rows = cursor.fetchall()
#         for row in rows:
#             count += 1
#         print(f'\nTask count: {count}')
#
#     elif choice == '4':
#         id = input("Enter your task ID: ")
#         cursor.execute(f"delete from tasks where id = '{id}'")
#         conn.commit()
#         print('\nTask deleted!')
#
#     elif choice == '5':
#         print('='*40)
#         print('1. Change title')
#         print('2. Change description')
#         print('3. Change title + description')
#         print('='*40)
#         print()
#         choice1 = input("What do you want to change?\nPlease enter your choice: ")
#         print()
#         if choice1 == '1':
#            t = input("Enter your title: ")
#            id = input("Enter your ID: ")
#            cursor.execute(f"UPDATE tasks set title = '{t}' where id = '{id}'")
#            conn.commit()
#            print('\nTask updated!')
#
#
#         elif choice1 == '2':
#             d = input("Enter your description: ")
#             id = input("Enter your ID: ")
#             cursor.execute(f"UPDATE tasks set description = '{d}' where id = '{id}'")
#             conn.commit()
#             print('\nTask updated!')
#
#
#         elif choice1 == '3':
#             t = input("Enter your title: ")
#             d = input("Enter your description: ")
#             id = input("Enter your ID: ")
#             cursor.execute(f"UPDATE tasks set title = '{t}',description = '{d}' where id = '{id}'")
#             conn.commit()
#             print('\nTask updated!')
#
#         else:
#             print('\nERROR!!!\nTry again!')
#
#
#     elif choice == '0':
#         print('Bye!:)')
#         break
#
#     else:
#         print('ERROR!!!\nTry again!')

