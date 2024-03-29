import sqlite3
import tkinter as tk
from tkinter import simpledialog, messagebox


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('todolist.db')
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                               (id INTEGER PRIMARY KEY, task TEXT, due_date DATE, priority TEXT)''')
        self.conn.commit()

    def add_task(self, task, due_date, priority):
        self.cursor.execute("INSERT INTO tasks (task, due_date, priority) VALUES (?, ?, ?)", (task, due_date, priority))
        self.conn.commit()

    def get_tasks(self):
        self.cursor.execute("SELECT id, task, due_date, priority FROM tasks ORDER BY due_date")
        return self.cursor.fetchall()

    def edit_task(self, task_id, task, due_date, priority):
        self.cursor.execute("UPDATE tasks SET task = ?, due_date = ?, priority = ? WHERE id = ?",
                            (task, due_date, priority, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()


class ToDoApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title('To-Do List Application')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=100, pady=100 )

        self.listbox = tk.Listbox(self.frame, width=100, height=20)
        self.listbox.grid(row=0, column=0, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.add_button = tk.Button(self.frame, text='Add', command=self.add_task , bg='Lavender')
        self.add_button.grid(row=1, column=0, sticky='w', pady=(10, 0))

        self.edit_button = tk.Button(self.frame, text='Edit', command=self.edit_task , bg='Lavender')
        self.edit_button.grid(row=1, column=0, sticky='e', pady=(10, 0))

        self.delete_button = tk.Button(self.frame, text='Delete', command=self.delete_selected_task , bg='Lavender')
        self.delete_button.grid(row=2, column=0, pady=(10, 0))

        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        tasks = self.db.get_tasks()
        for task in tasks:
            self.listbox.insert(tk.END, f"{task[1]} | {task[2]} | {task[3]}")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            due_date = simpledialog.askstring("Due Date", "Enter the due date (YYYY-MM-DD):")
            priority = simpledialog.askstring("Priority", "Enter priority (Low, Medium, High):")
            self.db.add_task(task, due_date, priority)
            self.refresh_list()

    def edit_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Edit Task", "No task selected!")
            return
        task_id = self.db.get_tasks()[selected[0]][0]

        new_task = simpledialog.askstring("Edit Task", "Enter the updated task:")
        new_due_date = simpledialog.askstring("Edit Due Date", "Enter the updated due date (YYYY-MM-DD):")
        new_priority = simpledialog.askstring("Edit Priority", "Enter updated priority (Low, Medium, High):")

        self.db.edit_task(task_id, new_task, new_due_date, new_priority)
        self.refresh_list()

    def delete_selected_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Delete Task", "No task selected!")
            return
        task_id = self.db.get_tasks()[selected[0]][0]
        self.db.delete_task(task_id)
        self.refresh_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
