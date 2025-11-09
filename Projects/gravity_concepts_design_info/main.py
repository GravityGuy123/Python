from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Output PDF path
pdf_path = "tailwind_color_system.pdf"

# Create canvas
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(1*inch, height - 1*inch, "Tailwind Color System (Light + Dark Mode)")

# Content
content = """
🎨 Brand Color System (Light + Dark Mode)

1. Primary (Deep Navy Blue: rgb(47, 78, 118))
- Light mode: Headers, navbars, buttons, strong text accents
- Dark mode: Lighter grayish-blue for readability
Class:
bg-[rgb(47,78,118)] text-white
dark:bg-[rgb(28,41,61)] dark:text-[rgb(220,230,240)]

2. Accent (Rich Purple: rgb(106, 27, 154))
- Light mode: Call-to-action buttons, highlights, section titles
- Dark mode: Softer purple to avoid eye strain
Class:
bg-[rgb(106,27,154)] text-white
dark:bg-[rgb(150,70,200)] dark:text-[rgb(240,230,250)]

3. Neutral Background (Soft Gray: #f7f7f7)
- Light mode: Section backgrounds
- Dark mode: Very dark gray
Class:
bg-[#f7f7f7] text-[rgb(40,40,40)]
dark:bg-[rgb(20,20,25)] dark:text-[rgb(220,220,220)]

4. Text Colors
- Light mode:
  Main text: text-[rgb(40,40,40)]
  Secondary text: text-[rgb(90,90,90)]
- Dark mode:
  Main text: dark:text-[rgb(220,220,220)]
  Secondary text: dark:text-[rgb(160,160,160)]

5. Interactive States
Example Buttons:
Primary Navy:
<button class="bg-[rgb(47,78,118)] text-white px-4 py-2 rounded-lg 
             hover:bg-[rgb(30,60,100)] 
             dark:bg-[rgb(28,41,61)] dark:hover:bg-[rgb(20,30,50)]">
  Contact Us
</button>

Accent Purple:
<button class="bg-[rgb(106,27,154)] text-white px-4 py-2 rounded-lg 
             hover:bg-[rgb(90,20,130)] 
             dark:bg-[rgb(150,70,200)] dark:hover:bg-[rgb(120,50,160)]">
  Get Started
</button>

✅ Visual Strategy for Professional Look
- Navbar: Navy background, white text
- Buttons: Purple accent for CTAs, navy for secondary actions
- Background: Mostly white/light-gray sections (#f7f7f7), alternating dark sections in dark mode
- Headings: Bold navy in light mode, soft gray-blue in dark mode
- Links: Purple accent with hover underline

⚡ This setup will:
- Keep professional trust (navy)
- Add creative flair (purple)
- Stay clean and minimal (gray backgrounds, good text contrast)
- Work seamlessly with dark mode
"""

# Write content to PDF
c.setFont("Helvetica", 10)
y = height - 1.5*inch
for line in content.split("\n"):
    if y < 1*inch:  # new page if needed
        c.showPage()
        c.setFont("Helvetica", 10)
        y = height - 1*inch
    c.drawString(1*inch, y, line)
    y -= 14

# Save the PDF
c.save()

print(f"PDF successfully created: {pdf_path}")
