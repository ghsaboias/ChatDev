'''
This is the main file of the note-taking app.
'''
import tkinter as tk
from datetime import datetime
class Note:
    def __init__(self, content):
        self.content = content
        self.created_date = datetime.now()
        self.last_modified_date = self.created_date
    def edit(self, new_content):
        self.content = new_content
        self.last_modified_date = datetime.now()
class NoteApp:
    def __init__(self):
        self.notes = []
        self.selected_note = None
        self.root = tk.Tk()
        self.root.title("Note Taking App")
        self.note_listbox = tk.Listbox(self.root)
        self.note_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.note_listbox.bind("<<ListboxSelect>>", self.on_note_selected)
        self.note_text = tk.Text(self.root)
        self.note_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.new_button = tk.Button(self.root, text="New Note", command=self.create_note)
        self.new_button.pack(side=tk.TOP, padx=10, pady=10)
        self.edit_button = tk.Button(self.root, text="Edit Note", command=self.edit_note)
        self.edit_button.pack(side=tk.TOP, padx=10, pady=10)
        self.delete_button = tk.Button(self.root, text="Delete Note", command=self.delete_note)
        self.delete_button.pack(side=tk.TOP, padx=10, pady=10)
        self.load_notes()
    def load_notes(self):
        # Load notes from a file or database
        # For simplicity, let's assume we have some pre-defined notes
        note1 = Note("Note 1 content")
        note2 = Note("Note 2 content")
        note3 = Note("Note 3 content")
        self.notes = [note1, note2, note3]
        for note in self.notes:
            self.note_listbox.insert(tk.END, note.created_date.strftime("%Y-%m-%d %H:%M:%S"))
    def create_note(self):
        content = self.note_text.get("1.0", tk.END).strip()
        if content:
            note = Note(content)
            self.notes.append(note)
            self.note_listbox.insert(tk.END, note.created_date.strftime("%Y-%m-%d %H:%M:%S"))
            self.note_text.delete("1.0", tk.END)
    def edit_note(self):
        if self.selected_note:
            content = self.note_text.get("1.0", tk.END).strip()
            if content:
                self.selected_note.edit(content)
                self.note_listbox.delete(self.note_listbox.curselection())
                self.note_listbox.insert(tk.END, self.selected_note.last_modified_date.strftime("%Y-%m-%d %H:%M:%S"))
                self.note_text.delete("1.0", tk.END)
    def delete_note(self):
        if self.selected_note:
            self.notes.remove(self.selected_note)
            self.note_listbox.delete(self.note_listbox.curselection())
            self.note_text.delete("1.0", tk.END)
    def on_note_selected(self, event):
        if self.note_listbox.curselection():
            index = self.note_listbox.curselection()[0]
            self.selected_note = self.notes[index]
            self.note_text.delete("1.0", tk.END)
            self.note_text.insert(tk.END, self.selected_note.content)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = NoteApp()
    app.run()