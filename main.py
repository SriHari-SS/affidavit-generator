# main.py - Tkinter UI for Affidavit Generator
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import platform

# Defer win32api import to avoid errors in non-Windows environments
try:
    if platform.system() == "Windows":
        import win32api
except ImportError:
    win32api = None

# Defer affidavit_logic import to isolate module errors
try:
    from affidavit_logic import process_affidavit_text
except Exception as e:
    process_affidavit_text = None
    import_error = e
else:
    import_error = None

class AffidavitApp:
    def __init__(self, root):
        self.root = root
        root.title("Affidavit Generator")
        root.geometry("1200x700")

        # Input frame (left half)
        input_frame = tk.Frame(root)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(input_frame, text="Paste Client Message:").pack(anchor="w")
        self.input_text = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, height=20)
        self.input_text.pack(fill=tk.BOTH, expand=True)

        tk.Label(input_frame, text="Joining Date (YYYY-MM-DD):").pack(anchor="w", pady=(10, 0))
        self.date_entry = tk.Entry(input_frame)
        self.date_entry.pack(fill=tk.X)

        tk.Button(input_frame, text="Generate", command=self.generate).pack(pady=10)

        # Output frame (right half)
        output_frame = tk.Frame(root)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(output_frame, text="Editable Output Document:").pack(anchor="w")
        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, height=30)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        tk.Button(output_frame, text="Print", command=self.print_doc).pack(pady=10)

        self.generated_doc_path = None

    def generate(self):
        if not process_affidavit_text:
            messagebox.showerror("Module Error", f"affidavit_logic module could not be imported.\n\nDetails: {import_error}")
            return

        raw_message = self.input_text.get("1.0", tk.END).strip()
        join_date = self.date_entry.get().strip()

        if not raw_message or not join_date:
            messagebox.showerror("Input Error", "Please provide message and date.")
            return

        try:
            doc_text, file_path = process_affidavit_text(raw_message, join_date)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, doc_text)
            self.generated_doc_path = file_path
        except Exception as e:
            messagebox.showerror("Generation Error", str(e))

    def print_doc(self):
        if not self.generated_doc_path:
            messagebox.showwarning("No Document", "Generate document first.")
            return
        try:
            if platform.system() == "Windows" and win32api:
                win32api.ShellExecute(0, "print", self.generated_doc_path, None, ".", 0)
            else:
                messagebox.showinfo("Print Info", "Printing is supported only on Windows.")
        except Exception as e:
            messagebox.showerror("Print Error", f"Failed to print: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AffidavitApp(root)
    root.mainloop()
