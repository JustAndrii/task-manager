

from crud import add_task, show_tasks, count_tasks, delete_task,update_task,complete_task,search_task,show_completed_task

while True:
    print()
    print("=" * 45)
    print("              📋 TASK MANAGER")
    print("=" * 45)
    print("1. Add task")
    print("2. Show all tasks")
    print("3. Count tasks")
    print("4. Delete task")
    print("5. Update task")
    print("6. Complete task")
    print("7. Search task by ID")
    print("8. Show completed tasks")
    print("0. Exit")
    print("=" * 45)
    print()


    choice = input('Enter your choice: ')


    if choice == '1':
        title = input('Enter your title: ')
        description = input('Enter your description: ')
        add_task(title, description)

    elif choice == '2':
          show_tasks()

    elif choice == '3':
        count_tasks()

    elif choice == '4':
        delete_task()

    elif choice == '5':
        update_task()

    elif choice == '6':
        complete_task()

    elif choice == '7':
        search_task()

    elif choice == '8':
        show_completed_task()

    elif choice == '0':
        print('Thanks for using Task Manager!\nGoodbye 👋')
        break

    else:
        print("Please select a valid option.")
