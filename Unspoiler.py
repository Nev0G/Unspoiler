import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Unspoiler by Nev0")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self, text="Entrer votre texte:")
        self.input_label.pack()
        self.input_text = tk.Text(self, height=10, width=50)
        self.input_text.pack()

        self.output_label = tk.Label(self, text="Résultat:")
        self.output_label.pack()
        self.output_text = tk.Text(self, height=10, width=50)
        self.output_text.pack()

        self.replace_button = tk.Button(self, text="Remplacer", command=self.replace_chars)
        self.replace_button.pack()

        self.quit_button = tk.Button(self, text="Quitter", command=self.master.destroy)
        self.quit_button.pack()

    def replace_chars(self):
        text = self.input_text.get("1.0", "end-1c")
        replaced_text = text.replace("e", "е").replace("d", "ԁ").replace("c", "с").replace("a", "а").replace("h", "h").replace("i", "і").replace("l", "ӏ").replace("n", "n").replace("o", "օ").replace("p", "р").replace("u", "ս").replace("x", "х").replace("y", "у")
        self.output_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", replaced_text)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
