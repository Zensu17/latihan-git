from entities.Todo import Todo
from repositories.TodoRepository import TodoRepository

class TodoService():
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def show_todos(self):
        todos = self.todo_repository.get_all_todos()
        print("Daftar Todo:")
        if not todos:
            print("- Data todo belum tersedia!")
            return

        for counter, todo in enumerate(todos, start=1):
            print(todo)

    def add_todo(self, title: str):
        new_todo = Todo(title=title)
        self.todo_repository.add_todo(new_todo)
    
    def update_todo(self, id: int, new_title: str, new_status: bool):
        todo = self.todo_repository.find_by_id(id)
        if todo is None:
            print(f"[!] Todo dengan ID {id} tidak ditemukan.")
            return

        todo.title = new_title
        todo.is_finished = new_status

    def remove_todo(self, id: int):
        success = self.todo_repository.remove_todo(id)
        if not success:
            print(f"[!] Gagal menghapus todo dengan ID: {id}.")
    
    def search_todo(self, keyword: str):
        todos = self.todo_repository.get_all_todos()
        results = [todo for todo in todos if keyword.lower() in todo.title.lower()]

        if not results:
            print("- Todo tidak ditemukan.")
            return

        print("Hasil Pencarian:")
        for todo in results:
            print(todo)
    
    def sort_todo(self, by: str):
        todos = self.todo_repository.get_all_todos()

        if by == "judul":
            todos.sort(key=lambda todo: todo.title.lower())
        elif by == "status":
            todos.sort(key=lambda todo: todo.is_finished)
        else:
            print("[!] Kriteria tidak dikenal.")

