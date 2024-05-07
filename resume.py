import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk
import cv2

def generate_resume():
    name = name_entry.get()
    email = email_entry.get()
    introduction = introduction_text.get("1.0", tk.END)
    experience = experience_text.get("1.0", tk.END)
    education = education_text.get("1.0", tk.END)
    skills = skills_text.get("1.0", tk.END)
    interests = interests_text.get("1.0", tk.END)

    if not name or not email or not introduction.strip() or not experience.strip() or not education.strip() or not skills.strip():
        messagebox.showerror("Error", "Please fill in all the mandatory fields.")
        return

    # Ask user to select photo
    file_path = filedialog.askopenfilename()
    if not file_path:
        messagebox.showerror("Error", "Please select a photo.")
        return

    # Generate PDF resume
    generate_pdf(name, email, introduction, experience, education, skills, interests, file_path)

    messagebox.showinfo("Success", "Resume PDF generated successfully!")

def generate_pdf(name, email, introduction, experience, education, skills, interests, photo_path):
    pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf")
    if not pdf_file:
        return

    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, "Name: " + name)
    c.drawString(100, 730, "Email: " + email)
    c.drawString(100, 710, "Introduction:\n" + introduction)
    c.drawString(100, 650, "Professional Experience:\n" + experience)
    c.drawString(100, 550, "Education:\n" + education)
    c.drawString(100, 450, "Skills:\n" + skills)
    c.drawString(100, 350, "Personal Interests:\n" + interests)

    # Add photo to PDF
    try:
        c.drawImage(photo_path, 400, 500, width=100, height=100)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add photo to PDF: {e}")

    c.save()

# Create main window
root = tk.Tk()
root.title("Resume Builder")

# Name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Introduction
introduction_label = tk.Label(root, text="Introduction:")
introduction_label.grid(row=2, column=0, sticky="w")
introduction_text = tk.Text(root, width=30, height=3)
introduction_text.grid(row=2, column=1, padx=10, pady=5)

# Professional Experience
experience_label = tk.Label(root, text="Professional Experience:")
experience_label.grid(row=3, column=0, sticky="w")
experience_text = tk.Text(root, width=30, height=5)
experience_text.grid(row=3, column=1, padx=10, pady=5)

# Education
education_label = tk.Label(root, text="Education:")
education_label.grid(row=4, column=0, sticky="w")
education_text = tk.Text(root, width=30, height=3)
education_text.grid(row=4, column=1, padx=10, pady=5)

# Skills
skills_label = tk.Label(root, text="Skills:")
skills_label.grid(row=5, column=0, sticky="w")
skills_text = tk.Text(root, width=30, height=3)
skills_text.grid(row=5, column=1, padx=10, pady=5)

# Personal Interests
interests_label = tk.Label(root, text="Personal Interests:")
interests_label.grid(row=6, column=0, sticky="w")
interests_text = tk.Text(root, width=30, height=3)
interests_text.grid(row=6, column=1, padx=10, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Resume", command=generate_resume)
generate_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
