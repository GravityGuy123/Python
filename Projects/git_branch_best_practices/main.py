from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm

pdf_file = "Git_Branching_Merge_Detailed_Guide.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(width / 2, height - 2*cm, "Git Branching & Merge Best Practices")

# Subtitle
c.setFont("Helvetica-Oblique", 12)
c.drawCentredString(width / 2, height - 2.8*cm, "A detailed guide for main, dev, and feature branches")

# Initial Y position
y = height - 4*cm
line_height = 14

# Set font for main content
c.setFont("Helvetica", 11)

# Content sections
sections = [
    ("1. Introduction",
     "Git is a distributed version control system that allows developers to work on multiple branches of a project "
     "simultaneously. Branching helps organize features, bug fixes, and releases without affecting the stable main codebase. "
     "Proper branch management is crucial for collaborative projects and for maintaining a clean history."),

    ("2. Branching Model",
     "A common branching model includes:\n"
     "- main (or master): Production-ready, stable code only.\n"
     "- dev (or develop): Integration/testing branch where features are merged.\n"
     "- feature/*: Short-lived branches created off dev for individual features or tasks.\n\n"
     "This model ensures that main always reflects the latest stable release while dev and feature branches are used for development and testing."),

    ("3. Recommended Workflow",
     "Step-by-step recommended workflow:\n"
     "1. Never work directly on 'main'. All new work should be done on dev or feature branches.\n"
     "2. Create a feature branch from dev for your task or feature:\n"
     "   git checkout -b feature/add-login dev\n"
     "   git commit -am 'Implement login feature'\n"
     "   git push origin feature/add-login\n"
     "3. Merge the feature branch back into dev for integration and testing:\n"
     "   git checkout dev\n"
     "   git pull origin dev\n"
     "   git merge feature/add-login\n"
     "   Resolve conflicts if any, then test the dev branch.\n"
     "4. Once dev is stable, merge dev into main:\n"
     "   git checkout main\n"
     "   git pull origin main\n"
     "   git merge dev\n"
     "   git push origin main\n"
     "This ensures main always contains a tested, production-ready version."),

    ("4. Local Merge vs Remote Merge",
     "Local Merge:\n"
     "- Merge branches locally, resolve conflicts, test functionality, and push to GitHub.\n"
     "- Recommended for teams or critical projects to prevent untested code from reaching main.\n\n"
     "Remote Merge (GitHub UI):\n"
     "- Merge branches directly on GitHub.\n"
     "- Suitable for solo projects or small changes.\n"
     "- Limited control and testing before merge; conflicts are resolved on GitHub."),

    ("5. Handling Conflicts",
     "Conflicts occur when the same lines of code are modified in two branches. Steps to handle:\n"
     "1. Git will notify you of conflicts during a merge.\n"
     "2. Open the conflicted files, identify sections marked by Git:\n"
     "<<<<<<< HEAD\nYour changes\n=======\nIncoming changes\n>>>>>>> branch\n"
     "3. Decide which changes to keep or combine.\n"
     "4. Stage the resolved file: git add <file>\n"
     "5. Complete the merge: git commit\n"
     "6. Test thoroughly before pushing to the repository."),

    ("6. Best Practices Summary",
     "- Always pull the latest main before merging.\n"
     "- Keep main stable and clean.\n"
     "- Test all merges locally before pushing.\n"
     "- Use feature branches for all new work.\n"
     "- Merge: feature → dev → main.\n"
     "- Document merges and commit messages clearly.\n"
     "- Resolve conflicts carefully; never rush.\n"
     "- Regularly sync branches with upstream to reduce conflicts."),

    ("7. Diagram of Branch Flow",
     "The typical branch flow is as follows:\n"
     "feature/* → dev → main\n"
     "Multiple feature branches can exist simultaneously and merge into dev. Once dev is stable, it merges into main.\n"
     "This process avoids direct edits to main and keeps history organized.")
]

# Draw text
for title, text in sections:
    # Section title
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2*cm, y, title)
    y -= line_height + 2

    # Section text
    c.setFont("Helvetica", 11)
    for line in text.split('\n'):
        c.drawString(2.5*cm, y, line)
        y -= line_height
    y -= 5  # small gap after section

# Draw simple branch diagram
y -= 1*cm
c.setFont("Helvetica-Bold", 12)
c.drawString(2*cm, y, "Branch Flow Diagram:")

# Boxes and arrows
y -= 1*cm
box_width = 3*cm
box_height = 1*cm
x_start = 12*cm

# main box
c.setFillColor(colors.lightblue)
c.rect(x_start, y-box_height, box_width, box_height, fill=1)
c.setFillColor(colors.black)
c.drawCentredString(x_start + box_width/2, y - box_height/2 + 4, "main")

# dev box
x_dev = x_start - 5*cm
c.setFillColor(colors.lightgreen)
c.rect(x_dev, y-3*cm, box_width, box_height, fill=1)
c.setFillColor(colors.black)
c.drawCentredString(x_dev + box_width/2, y - 3*cm - box_height/2 + 4, "dev")

# feature box
x_feature = x_dev - 5*cm
c.setFillColor(colors.orange)
c.rect(x_feature, y-5*cm, box_width, box_height, fill=1)
c.setFillColor(colors.black)
c.drawCentredString(x_feature + box_width/2, y - 5*cm - box_height/2 + 4, "feature/*")

# Arrows
c.setStrokeColor(colors.black)
c.setLineWidth(1.2)
c.line(x_feature + box_width, y-5*cm - box_height/2, x_dev, y-3*cm - box_height/2)  # feature -> dev
c.line(x_dev + box_width, y-3*cm - box_height/2, x_start, y - box_height/2)         # dev -> main

# Save PDF
c.showPage()
c.save()
print(f"PDF created successfully: {pdf_file}")