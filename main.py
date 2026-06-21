import tkinter as tk
from tkinter import messagebox

from content_item import TechnologyUpdate
from cms_manager import CMSManager
from html_generator import HTMLGenerator


class HealthcareTechWatchApp:
    """
    Tkinter GUI for the Healthcare Technology Watch CMS.
    """

    SUMMARY_LIMIT = 500
    WHY_LIMIT = 400

    def __init__(self, root):
        self.root = root
        self.root.title("Healthcare Technology Watch CMS")
        self.root.geometry("1200x850")
        self.root.configure(bg="#e8f7f5")

        self.manager = CMSManager()
        self.generator = HTMLGenerator()
        self.selected_index = None

        self.create_widgets()
        self.refresh_update_list()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="🏥 Healthcare Technology Watch CMS",
            font=("Arial", 24, "bold"),
            bg="#063b4c",
            fg="white",
            pady=18
        )
        title_label.pack(fill="x")

        subtitle_label = tk.Label(
            self.root,
            text="Create, review, save, and publish healthcare technology updates",
            font=("Arial", 13),
            bg="#e8f7f5",
            fg="#1f2933",
            pady=10
        )
        subtitle_label.pack()

        main_frame = tk.Frame(self.root, bg="#e8f7f5")
        main_frame.pack(fill="both", expand=True, padx=25, pady=10)

        form_frame = tk.Frame(main_frame, bg="#e8f7f5")
        form_frame.pack(side="left", fill="both", expand=True, padx=10)

        list_frame = tk.Frame(main_frame, bg="white", bd=2, relief="groove")
        list_frame.pack(side="right", fill="both", expand=True, padx=10)

        form_title = tk.Label(
            form_frame,
            text="Update Editor",
            font=("Arial", 18, "bold"),
            bg="#e8f7f5",
            fg="#063b4c"
        )
        form_title.pack(anchor="w", pady=(0, 10))

        self.employee_entry = self.create_labeled_entry(form_frame, "Employee Name:")
        self.department_entry = self.create_labeled_entry(form_frame, "Department:")
        self.category_entry = self.create_labeled_entry(form_frame, "Category:")
        self.news_title_entry = self.create_labeled_entry(form_frame, "News Title:")

        self.summary_text = self.create_labeled_text(
            form_frame,
            f"Summary (max {self.SUMMARY_LIMIT} characters):",
            height=4
        )

        self.why_text = self.create_labeled_text(
            form_frame,
            f"Why It Matters (max {self.WHY_LIMIT} characters):",
            height=3
        )

        self.source_entry = self.create_labeled_entry(form_frame, "Source Link:")

        status_label = tk.Label(
            form_frame,
            text="Status:",
            font=("Arial", 11, "bold"),
            bg="#e8f7f5"
        )
        status_label.pack(anchor="w", pady=(8, 2))

        self.status_var = tk.StringVar(value="Pending Review")
        self.status_menu = tk.OptionMenu(
            form_frame,
            self.status_var,
            "Pending Review",
            "Approved",
            "Rejected",
            "Featured"
        )
        self.status_menu.config(width=25)
        self.status_menu.pack(anchor="w", pady=(0, 10))

        button_frame = tk.Frame(form_frame, bg="#e8f7f5")
        button_frame.pack(fill="x", pady=10)

        tk.Button(button_frame, text="Add Update", command=self.add_update, width=18).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Update Selected", command=self.update_selected, width=18).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Delete Selected", command=self.delete_selected, width=18).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_fields, width=18).grid(row=1, column=1, padx=5, pady=5)

        publish_button = tk.Button(
            form_frame,
            text="Generate / Publish HTML Page",
            command=self.publish_html,
            font=("Arial", 11, "bold"),
            height=2
        )
        publish_button.pack(fill="x", pady=5)

        self.status_message = tk.Label(
            form_frame,
            text="Ready",
            font=("Arial", 10),
            bg="#e8f7f5",
            fg="#1f2933"
        )
        self.status_message.pack(anchor="w", pady=5)

        list_title = tk.Label(
            list_frame,
            text="Submitted Updates",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#063b4c",
            pady=12
        )
        list_title.pack()

        self.update_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 11),
            width=45,
            height=28
        )
        self.update_listbox.pack(fill="both", expand=True, padx=15, pady=10)
        self.update_listbox.bind("<<ListboxSelect>>", self.on_select)

    def create_labeled_entry(self, parent, label_text):
        label = tk.Label(
            parent,
            text=label_text,
            font=("Arial", 11, "bold"),
            bg="#e8f7f5"
        )
        label.pack(anchor="w", pady=(6, 2))

        entry = tk.Entry(parent, font=("Arial", 11))
        entry.pack(fill="x", pady=(0, 4))
        return entry

    def create_labeled_text(self, parent, label_text, height):
        label = tk.Label(
            parent,
            text=label_text,
            font=("Arial", 11, "bold"),
            bg="#e8f7f5"
        )
        label.pack(anchor="w", pady=(6, 2))

        text_box = tk.Text(parent, height=height, font=("Arial", 11), wrap="word")
        text_box.pack(fill="x", pady=(0, 4))
        return text_box

    def get_form_data(self):
        employee_name = self.employee_entry.get().strip()
        department = self.department_entry.get().strip()
        category = self.category_entry.get().strip()
        news_title = self.news_title_entry.get().strip()
        summary = self.summary_text.get("1.0", tk.END).strip()
        why_it_matters = self.why_text.get("1.0", tk.END).strip()
        source_link = self.source_entry.get().strip()
        status = self.status_var.get()

        if not employee_name or not department or not category or not news_title or not summary or not why_it_matters or not source_link:
            messagebox.showwarning("Missing Information", "Please fill in all fields.")
            return None

        if len(summary) > self.SUMMARY_LIMIT:
            messagebox.showwarning(
                "Summary Too Long",
                f"Summary must be {self.SUMMARY_LIMIT} characters or less."
            )
            return None

        if len(why_it_matters) > self.WHY_LIMIT:
            messagebox.showwarning(
                "Why It Matters Too Long",
                f"Why It Matters must be {self.WHY_LIMIT} characters or less."
            )
            return None

        return TechnologyUpdate(
            employee_name,
            department,
            category,
            news_title,
            summary,
            why_it_matters,
            source_link,
            status
        )

    def add_update(self):
        update = self.get_form_data()

        if update is None:
            return

        self.manager.add_update(update)
        self.generator.generate_page(self.manager.get_all_updates())
        self.refresh_update_list()
        self.clear_fields()
        self.status_message.config(text="Update added and website published.")

    def update_selected(self):
        if self.selected_index is None:
            messagebox.showwarning("No Selection", "Please select an update to edit.")
            return

        update = self.get_form_data()

        if update is None:
            return

        self.manager.update_item(self.selected_index, update)
        self.generator.generate_page(self.manager.get_all_updates())
        self.refresh_update_list()
        self.clear_fields()
        self.status_message.config(text="Selected update modified and website republished.")

    def delete_selected(self):
        if self.selected_index is None:
            messagebox.showwarning("No Selection", "Please select an update to delete.")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this update?"
        )

        if confirm:
            self.manager.delete_update(self.selected_index)
            self.generator.generate_page(self.manager.get_all_updates())
            self.refresh_update_list()
            self.clear_fields()
            self.status_message.config(text="Update deleted and website republished.")

    def publish_html(self):
        self.generator.generate_page(self.manager.get_all_updates())
        self.status_message.config(text="HTML page generated successfully.")

    def refresh_update_list(self):
        self.update_listbox.delete(0, tk.END)

        for index, update in enumerate(self.manager.get_all_updates(), start=1):
            display_text = f"{index}. {update.news_title} | {update.category} | {update.status}"
            self.update_listbox.insert(tk.END, display_text)

    def on_select(self, event):
        selection = self.update_listbox.curselection()

        if not selection:
            return

        self.selected_index = selection[0]
        update = self.manager.get_all_updates()[self.selected_index]

        self.clear_fields(clear_selection=False)

        self.employee_entry.insert(0, update.employee_name)
        self.department_entry.insert(0, update.department)
        self.category_entry.insert(0, update.category)
        self.news_title_entry.insert(0, update.news_title)
        self.summary_text.insert("1.0", update.summary)
        self.why_text.insert("1.0", update.why_it_matters)
        self.source_entry.insert(0, update.source_link)
        self.status_var.set(update.status)

        self.status_message.config(text=f"Selected: {update.news_title}")

    def clear_fields(self, clear_selection=True):
        self.employee_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.news_title_entry.delete(0, tk.END)
        self.summary_text.delete("1.0", tk.END)
        self.why_text.delete("1.0", tk.END)
        self.source_entry.delete(0, tk.END)
        self.status_var.set("Pending Review")

        if clear_selection:
            self.selected_index = None
            self.update_listbox.selection_clear(0, tk.END)

        self.status_message.config(text="Ready")


if __name__ == "__main__":
    root = tk.Tk()
    app = HealthcareTechWatchApp(root)
    root.mainloop()