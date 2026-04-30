from PIL import Image, ImageOps
from fpdf import FPDF

def main():
    user_name = input("Name: ")
    pdf = PDF(user_name)
    pdf.add_page()
    pdf.output("shirtificate.pdf")

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", size=50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)
        # Rendering logo:
        self.image("./shirtificate.png", 20, 30, 170)
        # Performing a line break:
        self.ln(50)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", size=20)
        self.set_text_color(255, 255, 255)
        # Moving cursor to the right:
        self.cell(80, 180)
        # Printing title:
        self.cell(30, 10, f"{self.name} took CS50", align="C")
        # Performing a line break:
        self.ln(20)

if __name__ == "__main__":
    main()
