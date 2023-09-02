import tkinter as tr
import random
import string
import tkinter.messagebox as tm

class RandomPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator App")

        self.length_label = tr.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tr.Entry(root)
        self.length_entry.pack()

        self.exclude_chars_label = tr.Label(root, text="Characters to Exclude:")
        self.exclude_chars_label.pack()

        self.exclude_chars_entry = tr.Entry(root)
        self.exclude_chars_entry.pack()

        self.complexity_label = tr.Label(root, text="Password Complexity:")
        self.complexity_label.pack()

        self.complexity_frame = tr.Frame(root)
        self.complexity_frame.pack()

        self.low_button = tr.Button(self.complexity_frame, text="Low", command=lambda: self.set_complexity("low"))
        self.medium_button = tr.Button(self.complexity_frame, text="Medium", command=lambda: self.set_complexity("medium"))
        self.high_button = tr.Button(self.complexity_frame, text="High", command=lambda: self.set_complexity("high"))

        self.low_button.pack(side="left")
        self.medium_button.pack(side="left")
        self.high_button.pack(side="left")

        self.generate_button = tr.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = tr.Label(root, text="")
        self.result_label.pack()

        self.copy_button = tr.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

        self.complexity = "low"  

    def set_complexity(self, level):
        self.complexity = level
        self.result_label.config(text="")

    def generate_password(self):
        password_length = int(self.length_entry.get())
        if password_length <= 0:
            self.result_label.config(text="Invalid password length")
            return

        exclude_chars = self.exclude_chars_entry.get()
        complexity_levels = {
            "low": string.ascii_lowercase,
            "medium": string.ascii_letters + string.digits,
            "high": string.ascii_letters + string.digits + string.punctuation }
        characters = ''.join([char for char in complexity_levels[self.complexity] if char not in exclude_chars])

        if not characters:
            self.result_label.config(text="No characters available")
            return

        generated_pass = ''.join(random.choice(characters) for _ in range(password_length))
        self.result_label.config(text="Generated Password: " + generated_pass)

        self.generated_pass = generated_pass 

    def copy_to_clipboard(self):
        try:
            self.root.clipboard_clear()  
            self.root.clipboard_append(self.generated_pass)  
            self.root.update() 
            tm.showinfo("Copied", "Password copied to Clipboard!")
        except AttributeError:
            tm.showwarning("Warning", "Generate a password first.")

if __name__ == "__main__":
    root = tr.Tk()
    app = RandomPasswordGenerator(root)
    root.mainloop()
