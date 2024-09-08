import customtkinter as ct
from config import configureApp
from ui.ui import createUi

def main():
    configureApp()

    root = ct.CTk()
    root.geometry("500x350")

    createUi(root)

    root.mainloop()

if __name__ == "__main__":
    main()
