import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def generate_resume():
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    linkedin = linkedin_entry.get()
    introduction = introduction_text.get("1.0", tk.END)
    experience = experience_text.get("1.0", tk.END)
    education = education_text.get("1.0", tk.END)
    skills = skills_text.get("1.0", tk.END)
    interests = interests_text.get("1.0", tk.END)
    references = references_text.get("1.0", tk.END)

    if not name or not email or not mobile or not introduction.strip() or not experience.strip() or not education.strip() or not skills.strip():
        messagebox.showerror("Error", "Please fill in all the mandatory fields.")
        return

    # Ask user to select photo
    file_path = filedialog.askopenfilename()
    if not file_path:
        messagebox.showerror("Error", "Please select a photo.")
        return

    # Get selected background color
    bg_color = color_var.get()

    # Generate PDF resume
    generate_pdf(name, email, mobile, linkedin, introduction, experience, education, skills, interests, references, file_path, bg_color)

    messagebox.showinfo("Success", "Resume PDF generated successfully!")

def generate_pdf(name, email, mobile, linkedin, introduction, experience, education, skills, interests, references, photo_path, bg_color):
    pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf")
    if not pdf_file:
        return

    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Draw background color
    c.setFillColor(bg_color)
    c.rect(0, 0, letter[0], letter[1], fill=True)

    # Draw text content
    c.setFillColorRGB(0, 0, 0)  # Reset fill color to black
    c.drawString(100, 750, "Name: " + name)
    c.drawString(100, 730, "Contact:")
    c.drawString(120, 710, "Email: " + email)
    c.drawString(120, 690, "Mobile: " + mobile)
    c.drawString(120, 670, "LinkedIn: " + linkedin)
    c.drawString(100, 650, "Introduction:\n" + introduction)

    # Draw experience
    c.drawString(100, 580, "Professional Experience:")
    draw_points(c, 100, 560, experience)

    # Draw education
    c.drawString(100, 470, "Education:")
    draw_points(c, 100, 450, education)

    # Draw skills
    c.drawString(100, 350, "Skills:")
    draw_points(c, 100, 330, skills)

    # Draw interests
    c.drawString(100, 230, "Personal Interests:")
    draw_points(c, 100, 210, interests)

    # Draw references
    c.drawString(100, 110, "References:")
    draw_points(c, 100, 90, references)

    # Add photo to PDF
    try:
        c.drawImage(photo_path, 400, 500, width=100, height=100)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add photo to PDF: {e}")

    c.save()

def draw_points(canvas_obj, x, y, text):
    points = text.strip().split('\n')
    for point in points:
        if point.strip():
            canvas_obj.drawString(x, y, '\u2022 ' + point.strip())
            y -= 15

def choose_color():
    color_code = colorchooser.askcolor(title="Choose Background Color")
    if color_code[1]:
        color_var.set(color_code[1])

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

# Mobile Number
mobile_label = tk.Label(root, text="Mobile:")
mobile_label.grid(row=2, column=0, sticky="w")
mobile_entry = tk.Entry(root)
mobile_entry.grid(row=2, column=1, padx=10, pady=5)

# LinkedIn ID
linkedin_label = tk.Label(root, text="LinkedIn:")
linkedin_label.grid(row=3, column=0, sticky="w")
linkedin_entry = tk.Entry(root)
linkedin_entry.grid(row=3, column=1, padx=10, pady=5)

# Introduction
introduction_label = tk.Label(root, text="Introduction:")
introduction_label.grid(row=4, column=0, sticky="w")
introduction_text = tk.Text(root, width=30, height=3)
introduction_text.grid(row=4, column=1, padx=10, pady=5)

# Professional Experience
experience_label = tk.Label(root, text="Professional Experience:")
experience_label.grid(row=5, column=0, sticky="w")
experience_text = tk.Text(root, width=30, height=5)
experience_text.grid(row=5, column=1, padx=10, pady=5)

# Education
education_label = tk.Label(root, text="Education:")
education_label.grid(row=6, column=0, sticky="w")
education_text = tk.Text(root, width=30, height=3)
education_text.grid(row=6, column=1, padx=10, pady=5)

# Skills
skills_label = tk.Label(root, text="Skills:")
skills_label.grid(row=7, column=0, sticky="w")
skills_text = tk.Text(root, width=30, height=3)
skills_text.grid(row=7, column=1, padx=10, pady=5)

# Personal Interests
interests_label = tk.Label(root, text="Personal Interests:")
interests_label.grid(row=8, column=0, sticky="w")
interests_text = tk.Text(root, width=30, height=3)
interests_text.grid(row=8, column=1, padx=10, pady=5)

# References
references_label = tk.Label(root, text="References:")
references_label.grid(row=9, column=0, sticky="w")
references_text = tk.Text(root, width=30, height=3)
references_text.grid(row=9, column=1, padx=10, pady=5)

# Background Color
color_label = tk.Label(root, text="Background Color:")
color_label.grid(row=10, column=0, sticky="w")
color_var = tk.StringVar(root)
color_var.set("#FFFFFF")  # Default to white
color_entry = tk.Entry(root, textvariable=color_var, state='readonly')
color_entry.grid(row=10, column=1, padx=10, pady=5)
color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.grid(row=10, column=2, padx=5, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Resume", command=generate_resume)
generate_button.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()
