# Python Script to Generate PDF containing movie recommendations

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# File output
file_path = "Bollywood_Movie_Recommendations.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)

styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Bollywood Movie Recommendations", styles["Title"]))
story.append(Spacer(1, 20))

movies = {
    "High-Energy Action / Stylish Thrillers": [
        ("War (2019)", "Hrithik Roshan and Tiger Shroff star..."),
        ("Bang Bang (2014)", "A Bollywood remake of Knight and Day..."),
        ("Commando (2013)", "Starring Vidyut Jammwal with martial arts..."),
        ("Dishoom (2016)", "Buddy-cop action comedy with John Abraham..."),
        ("R… Rajkumar (2013)", "Shahid Kapoor in a mass entertainer..."),
        ("Race (2008 & 2013)", "Stylish thrillers with betrayal and action."),
    ],
    "Fantasy, Magic & Mythology Vibes": [
        ("Brahmastra (2022)", "Modern mythological fantasy with Ranbir Kapoor..."),
        ("Krrish Series", "Hrithik Roshan as India's superhero..."),
        ("Ra.One (2011)", "Shah Rukh Khan as a video game character..."),
        ("Eega (2012)", "Unique Telugu fantasy where man reincarnates as fly..."),
        ("Magadheera (2009)", "Reincarnation epic with Ram Charan..."),
        ("Bahubali (2015 & 2017)", "Epic fantasy saga by Rajamouli."),
    ],
    # Add the rest following the text provided above
}

for category, films in movies.items():
    story.append(Paragraph(category, styles["Heading2"]))
    story.append(Spacer(1, 12))
    for title, description in films:
        story.append(Paragraph(f"<b>{title}</b>", styles["Heading3"]))
        story.append(Paragraph(description, styles["BodyText"]))
        story.append(Spacer(1, 8))
    story.append(Spacer(1, 20))

doc.build(story)
print(f"PDF saved as {file_path}")
