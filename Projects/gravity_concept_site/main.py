from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

# File path
pdf_path = "gravity_concepts_website_structure.pdf"

# Document setup
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        rightMargin=40, leftMargin=40,
                        topMargin=40, bottomMargin=40)

# Styles
styles = getSampleStyleSheet()
title_style = styles['Title']
heading_style = styles['Heading2']
body_style = styles['BodyText']
body_style.spaceAfter = 12

# Flowables (content)
content = []

# Title
content.append(Paragraph("Gravity Concepts – Website Structure & Content Draft", title_style))
content.append(Spacer(1, 12))

# Pages content
pages_info = {
    "Home Page": [
        "Header / Navigation: Logo (Gravity Concepts), Menu: Home | About | Services | Portfolio | Contact",
        "Hero Section: Headline – 'Creative Graphics & Web Solutions That Elevate Your Brand'. Subtext, CTA buttons.",
        "Quick Services Overview: Graphics Design, Branding, Web Development.",
        "Why Choose Us: Fast & Reliable, Professional Designs, Affordable Pricing, 3+ Years Experience.",
        "Call-to-Action: 'Let’s build something amazing together.' Button: Contact Us."
    ],
    "About Page": [
        "Who We Are: Gravity Concepts is a creative hub where innovation meets design.",
        "Mission & Vision: Mission – deliver designs and digital solutions that connect brands with people. Vision – to become a leading creative agency.",
        "Our Team (Optional): Short bios of team members.",
        "Experience & Achievements: 50+ satisfied clients, 100+ successful projects."
    ],
    "Products & Services Page": [
        "Graphics Design: Logos, Flyers, Business Cards, Social Media Banners, Mockups.",
        "Web Development: Portfolio sites, Business websites, E-commerce, Landing pages, Maintenance.",
        "Packages (Optional): Basic, Standard, Premium.",
        "Portfolio Showcase: Grid of past works.",
        "Client Testimonials: Quote-style reviews."
    ],
    "Contact Page": [
        "Contact Form: Fields – Name, Email, Phone, Message.",
        "Direct Contact Info: Email, Phone/WhatsApp.",
        "Location: 'Based in Nigeria, serving clients worldwide.'",
        "Social Media Links: Facebook, Instagram, LinkedIn, Twitter/X."
    ],
    "Portfolio Page (Optional)": [
        "Showcase projects by category: Graphics, Branding, Web Development.",
        "Each project: Image + Short Description + Tools Used."
    ],
    "Blog Page (Optional)": [
        "Example Posts: 'How to Build a Brand Identity in 2025', 'Why Every Business Needs a Website', 'Tips for Effective Flyer Design'."
    ],
    "Footer": [
        "Quick Links: Home | About | Services | Portfolio | Contact.",
        "Contact Info: Email, Phone.",
        "Social Media: Facebook, Instagram, LinkedIn, Twitter/X.",
        "Newsletter Signup (Optional).",
        "Copyright: © 2025 Gravity Concepts. All Rights Reserved."
    ]
}

# Add sections to content
for page, details in pages_info.items():
    content.append(Paragraph(page, heading_style))
    items = [ListItem(Paragraph(item, body_style)) for item in details]
    content.append(ListFlowable(items, bulletType='bullet'))
    content.append(Spacer(1, 12))

# Build PDF
doc.build(content)

print(f"PDF generated successfully: {pdf_path}")