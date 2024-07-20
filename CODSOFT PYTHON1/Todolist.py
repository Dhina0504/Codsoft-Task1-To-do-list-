import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.attributes('-fullscreen', True)

        # Set up the background color
        self.root.configure(bg="#ADD8E6")

        self.tasks = []

        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 24), bg="#ADD8E6")
        self.title_label.pack(pady=20)

        self.frame = tk.Frame(self.root, bg="#ADD8E6")
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10, bd=0, selectmode=tk.SINGLE, font=("Helvetica", 18))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.root, width=50, font=("Helvetica", 18))
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=20, font=("Helvetica", 18), command=self.add_task, bg="#90EE90")
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Complete Task", width=20, font=("Helvetica", 18), command=self.complete_task, bg="#FFD700")
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, font=("Helvetica", 18), command=self.delete_task, bg="#FF6347")
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All Tasks", width=20, font=("Helvetica", 18), command=self.clear_tasks, bg="#FFA07A")
        self.clear_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", width=20, font=("Helvetica", 18), command=self.exit_app, bg="#FA8072")
        self.exit_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append((task, False))
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            task, completed = self.tasks[task_index]
            if not completed:
                self.tasks[task_index] = (task, True)
                self.update_listbox()
            else:
                messagebox.showinfo("Info", "Task is already completed.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All Tasks", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task, completed in self.tasks:
            if completed:
                self.listbox.insert(tk.END, task + " (Completed)")
                self.listbox.itemconfig(tk.END, {'bg':'#90EE90'})
            else:
                self.listbox.insert(tk.END, task)

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
