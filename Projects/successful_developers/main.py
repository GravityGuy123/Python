from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

# File name of the PDF to be generated
pdf_file = "Successful_Developers.pdf"

# Document setup
doc = SimpleDocTemplate(pdf_file, pagesize=A4,
                        rightMargin=50, leftMargin=50,
                        topMargin=50, bottomMargin=50)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Heading',
                          fontSize=14,
                          leading=18,
                          spaceAfter=12,
                          bold=True))
styles.add(ParagraphStyle(name='Body',
                          fontSize=11,
                          leading=16,
                          spaceAfter=10))

# Content as a list of paragraphs
content = [
    "🏆 Successful Web Developers & Software Engineers: The Hows and Whys",

    "1. They Master Fundamentals First\n"
    "How:\n"
    "- Learn HTML, CSS, JavaScript, SQL, backend languages.\n"
    "- Understand algorithms & data structures.\n"
    "- Learn clean code principles.\n"
    "Why:\n"
    "- Frameworks change, fundamentals remain.\n"
    "- Strong base = quick adaptation.\n",

    "2. They Keep Learning (Continuous Growth)\n"
    "How:\n"
    "- Read docs, blogs, take courses, join meetups.\n"
    "- Contribute to open source or study projects.\n"
    "Why:\n"
    "- Tech evolves fast, staying updated = employable.\n",

    "3. They Build & Ship Projects\n"
    "How:\n"
    "- Start small: calculators, blogs, to-do apps.\n"
    "- Scale: e-commerce sites, dashboards, APIs.\n"
    "- Deploy to Netlify, Vercel, AWS.\n"
    "Why:\n"
    "- Employers value results, not just certificates.\n",

    "4. They Are Problem Solvers\n"
    "How:\n"
    "- Break down problems into smaller pieces.\n"
    "- Debug systematically, search effectively.\n"
    "- Practice coding challenges.\n"
    "Why:\n"
    "- Software = solving problems, not just writing code.\n",

    "5. They Have Strong Soft Skills\n"
    "How:\n"
    "- Explain tech to non-tech people.\n"
    "- Collaborate well, give/receive feedback.\n"
    "- Write clear documentation.\n"
    "Why:\n"
    "- Most projects are team-based. Communication = success.\n",

    "6. They Are Consistent & Disciplined\n"
    "How:\n"
    "- Code daily (even 30–60 minutes).\n"
    "- Set clear goals and stay organized.\n"
    "Why:\n"
    "- Skills compound with time. Small habits win.\n",

    "7. They Showcase Their Work (Portfolio & Branding)\n"
    "How:\n"
    "- Maintain GitHub with clean repos.\n"
    "- Build a portfolio site, share blogs, tutorials.\n"
    "- Network in dev communities.\n"
    "Why:\n"
    "- Visibility builds trust and attracts jobs/clients.\n",

    "8. They Understand Business Value\n"
    "How:\n"
    "- Ask 'what problem does this solve?'\n"
    "- Learn UX/UI basics, align with business goals.\n"
    "Why:\n"
    "- Coding is not the end — value delivery is.\n",

    "9. They Are Resilient (Growth Mindset)\n"
    "How:\n"
    "- See bugs as lessons, not failures.\n"
    "- Handle rejection and keep improving.\n"
    "- Stay patient while debugging tough problems.\n"
    "Why:\n"
    "- Resilience separates quitters from successful devs.\n",

    "✅ Why They Succeed:\n"
    "- They master fundamentals.\n"
    "- They keep learning.\n"
    "- They build real projects.\n"
    "- They communicate well.\n"
    "- They understand business.\n"
    "- They are consistent.\n"
    "- They are resilient.\n"
]

# Build the PDF
story = []
for para in content:
    style = styles['Body']
    if para.startswith("🏆") or para[0].isdigit() or para.startswith("✅"):
        style = styles['Heading']
    story.append(Paragraph(para.replace("\n", "<br/>"), style))
    story.append(Spacer(1, 0.2 * inch))

doc.build(story)

print(f"PDF '{pdf_file}' has been created successfully.")
