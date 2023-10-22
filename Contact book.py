import tkinter as tk
from tkinter import messagebox, simpledialog


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # Add Contact button
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        # View Contact List button
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()

        # Search Contact button
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contact_win = tk.Toplevel(self.root)
        contact_win.title("Contacts")

        for contact in self.contacts:
            label = tk.Label(contact_win, text=f"{contact.name} - {contact.phone}")
            label.pack()

        tk.Button(contact_win, text="Close", command=contact_win.destroy).pack()

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter Name or Phone Number:")
        results = [contact for contact in self.contacts if query in (contact.name, contact.phone)]

        search_win = tk.Toplevel(self.root)
        search_win.title("Search Results")

        if not results:
            messagebox.showinfo("Search", "No matching contact found!")
            return

        for contact in results:
            label = tk.Label(search_win, text=f"{contact.name} - {contact.phone}")
            label.pack()
            tk.Button(search_win, text="Update", command=lambda c=contact: self.update_contact(c)).pack(side=tk.LEFT)
            tk.Button(search_win, text="Delete", command=lambda c=contact: self.delete_contact(c)).pack(side=tk.LEFT)

        tk.Button(search_win, text="Close", command=search_win.destroy).pack()

    def update_contact(self, contact):
        new_name = simpledialog.askstring("Update", "Enter New Name:", initialvalue=contact.name)
        new_phone = simpledialog.askstring("Update", "Enter New Phone Number:", initialvalue=contact.phone)
        new_email = simpledialog.askstring("Update", "Enter New Email:", initialvalue=contact.email)
        new_address = simpledialog.askstring("Update", "Enter New Address:", initialvalue=contact.address)

        if new_name: contact.name = new_name
        if new_phone: contact.phone = new_phone
        if new_email: contact.email = new_email
        if new_address: contact.address = new_address

        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self, contact):
        if messagebox.askyesno("Delete", f"Are you sure you want to delete {contact.name}?"):
            self.contacts.remove(contact)
            messagebox.showinfo("Success", "Contact deleted successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
