from database import conn,cursor

def print_tasks(row):
            task_id = row[0]
            title = row[1]
            description = row[2]
            completed = row[3]
            created_at = row[4]
            if completed:
                completed = '✅'
            else:
                completed = '❌'
            print(
                f'\nID: {task_id}\nTitle: {title}\nDescription: {description}\nCompleted: {completed}\nCreated at: {created_at}\n',
                '-' * 40)



def add_task(title,description):
    """Add new task"""
    cursor.execute("INSERT INTO tasks (title,description) VALUES (%s,%s)",(title,description,))
    conn.commit()
    print("✅ Task added!")

def show_tasks():
    """Show all tasks"""
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    if not rows:
        print("📭 No tasks found.")
        return
    print('\n📋 Your tasks:')
    for row in rows:
        print_tasks(row)

def count_tasks():
    """Show count of tasks"""
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    print(f"\n📊 Total tasks: {len(rows)}")
    print(f"✅ Task completed!")

def delete_task():
    """Delete task"""
    try:
        task_id = int(input("Enter task ID to delete: "))
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        print("🗑️ Task deleted!")
    except ValueError:
        print("❌ Please enter a number!")
    except Exception:
        print("❌ Something went wrong.")


def update_task():
    """Update task"""
    try:
        print("1. Change title")
        print("2. Change description")
        print("3. Change both")
        choice = input("Choose option: ")
        task_id = int(input("Enter task ID: "))

        if choice == "1":
            title = input("New title: ")
            cursor.execute("UPDATE tasks SET title = %s WHERE id = %s", (title, task_id))
        elif choice == "2":
            desc = input("New description: ")
            cursor.execute("UPDATE tasks SET description = %s WHERE id = %s", (desc, task_id))
        elif choice == "3":
            title = input("New title: ")
            desc = input("New description: ")
            cursor.execute("UPDATE tasks SET title = %s, description = %s WHERE id = %s",
                         (title, desc, task_id))
        else:
            print("Invalid choice")
            return

        conn.commit()
        print("✅ Task updated!")
    except Exception:
        print("❌ Error. Check ID.")

def complete_task():
    """Mark task as completed"""
    try:
     task_id = int(input("What task would you like to complete\nEnter your task ID: "))
     cursor.execute("SELECT * FROM tasks where id = %s", (task_id,))
     rows = cursor.fetchall()
     if not rows:
        print('\n❌ ID not found!')
     else:
        cursor.execute("UPDATE tasks SET completed = True  where id = %s",(task_id,))
        conn.commit()
        print('\n✅ Task completed!')
    except ValueError:
        print("\n❌ Please enter a valid task ID (number).")

def search_task():
    """Search tasks"""
    try:
     task_id = int(input("Enter your task ID: "))
     cursor.execute("SELECT * FROM tasks where id = %s",(task_id,))
     rows = cursor.fetchall()
     if not rows:
        print('\n❌ID not found!')
     else:
         for row in rows:
             print_tasks(row)
    except ValueError:
           print('\n❌ Please enter a valid ID!')

def show_completed_task():
    """Show completed tasks"""
    cursor.execute("SELECT * FROM tasks WHERE completed = true")
    rows = cursor.fetchall()
    if not rows:
        print('\n❌ Task not found!')
    else:
        for row in rows:
         print_tasks(row)
