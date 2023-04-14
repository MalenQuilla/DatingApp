import tkinter as tk
from tkinter import ttk

class ChatGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chat App")
        self.window.geometry('1280x720')
        self.window.resizable(width= False, height= False)

        self.num_lines = 1
        
        # Create a vertical notebook with tabs on the left
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill='both', expand=True)

        #import image
        self.img = tk.PhotoImage(file = "GUI/MAIN/chat_img/who_chat_img.png")
        
        # Create a frame for each tab
        self.tabs = []
        for i in range(3):  # create 3 tabs
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab,image= self.img, compound='left')

            # Create a frame for avatar and username
            info_frame = ttk.Frame(tab)
            info_frame.pack(side='top', fill='x')

            # Create a chat box for each tab
            chat_frame = ttk.Frame(tab)
            chat_frame.pack(side='left', fill='both', expand=True)

            self.x = 10
            chat_box = tk.Text(chat_frame, state='disabled')
            chat_box.pack(side='top', fill='both', expand=True)

            # Create a frame for the box chat
            box_frame = ttk.Frame(chat_frame, width=250)
            box_frame.pack(side='left', fill='y', padx=5, pady=5)

            # Create the box chat
            box_chat = tk.Text(box_frame, height= 1)  # set initial height to 1
            box_chat.pack(side='top', fill='both', expand=True)

            def resize():
                self.num_lines = box_chat.get("1.0", "end-1c").count('\n') + 2
                box_chat.insert("end", "\n")
                box_chat.config(height= self.num_lines)
                box_frame.config(height= self.num_lines * 20)
                
                # self.x -= 1
                # chat_box.config(height= self.x)

            # Bind the Shift-Return event to the box chat
            box_chat.bind('<Return>', lambda e: resize())
            self.tabs.append(tab)

        # Set the first tab as the active one
        self.notebook.select(self.tabs[0])

        # Bind the NotebookTabChanged event to a command
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

    def _on_tab_changed(self, event):
        self.num_lines = 1


    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = ChatGUI()
    gui.run()
