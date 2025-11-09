from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER

def create_pdf(filename="all_quotes.pdf"):
    # Create PDF document
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "title_style",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=18,
        spaceAfter=20
    )
    quote_style = ParagraphStyle(
        "quote_style",
        parent=styles["Normal"],
        fontSize=12,
        leading=16,
        spaceAfter=12
    )

    # Add Title
    elements.append(Paragraph("Graphics & Web Development Quotes", title_style))
    elements.append(Spacer(1, 12))

    # ✅ All quotes (original + branding-focused + variations)
    quotes = [
        # Original completion
        "From design to development, we bring your ideas to life with stunning visuals and seamless digital experiences.",

        # Branding-focused alternatives
        "From design to development, we bring your ideas to reality with creativity, precision, and innovation.",
        "From design to development, we bring your ideas to life with bold creativity and sleek functionality.",
        "From design to development, we bring your ideas to life—building brands that stand out and connect.",

        # SEO-optimized variations
        "From design to development, we bring your ideas to life with custom graphics, modern web design, and user-friendly digital experiences that grow your brand.",
        "From design to development, we create professional graphics, responsive websites, and powerful digital solutions that help your business stand out online.",
        "From design to development, we transform your ideas into stunning visuals and engaging websites that leave a lasting impression.",
        "From design to development, we deliver creative graphics and functional websites designed to attract customers and elevate your brand presence.",
        "From design to development, we craft sleek graphics and innovative websites that bring your vision to reality."
    ]

    # Add each quote to PDF
    for i, quote in enumerate(quotes, 1):
        elements.append(Paragraph(f"<b>Quote {i}:</b> {quote}", quote_style))

    # Build PDF
    doc.build(elements)
    print(f"✅ PDF '{filename}' created successfully!")

# Run function
if __name__ == "__main__":
    create_pdf()