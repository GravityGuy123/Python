from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Preformatted,
    Table,
    TableStyle,
)
from reportlab.lib.units import inch

# Output PDF file
pdf_file = "Function_Arguments_Python_JavaScript_CheatSheet.pdf"

# Document setup with balanced margins
doc = SimpleDocTemplate(
    pdf_file,
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=48,
    bottomMargin=48,
    title="Function Arguments in Python & JavaScript",
)

# Base styles
styles = getSampleStyleSheet()

# Title style (colored highlight for header)
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    alignment=1,  # center
    fontSize=16,
    leading=20,
    spaceAfter=6,
    textColor=colors.HexColor("#0b3954"),
)

# Subtitle / description
subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Normal"],
    alignment=1,
    fontSize=10,
    leading=13,
    textColor=colors.HexColor("#11698e"),
    spaceAfter=14,
)

# Section heading
section_heading = ParagraphStyle(
    "SectionHeading",
    parent=styles["Heading2"],
    fontSize=12,
    leading=14,
    spaceBefore=10,
    spaceAfter=6,
    textColor=colors.HexColor("#063970"),
)

# Body paragraph
body_text = ParagraphStyle(
    "BodyText",
    parent=styles["Normal"],
    fontSize=10.5,
    leading=13.5,
    spaceAfter=6,
    textColor=colors.black,
)

# Code block style (preformatted)
code_style = ParagraphStyle(
    "CodeStyle",
    fontName="Courier",
    fontSize=9.5,
    leading=12,
    backColor=colors.whitesmoke,
    leftIndent=6,
    rightIndent=6,
    spaceBefore=6,
    spaceAfter=12,
)

# Table header style (we'll set colors in TableStyle)
table_col_widths = [110, 140, 140, 90]  # tweak to fit A4 nicely

# Build content
content = []

# Header
content.append(Paragraph("Function Arguments in Python & JavaScript", title_style))
content.append(
    Paragraph(
        "A complete cheat sheet explaining all argument types with examples.",
        subtitle_style,
    )
)
content.append(Spacer(1, 6))

# 1. Positional Arguments
content.append(Paragraph("1️⃣ Positional Arguments", section_heading))
content.append(Paragraph("Python: Order of arguments matters.", body_text))
content.append(
    Preformatted(
        '''def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Simon", 25)''',
        code_style,
    )
)
content.append(Paragraph("JavaScript: Works the same way — based on order.", body_text))
content.append(
    Preformatted(
        '''function greet(name, age) {
    console.log(`Hello ${name}, you are ${age} years old.`);
}
greet("Simon", 25);''',
        code_style,
    )
)

# 2. Default Arguments
content.append(Paragraph("2️⃣ Default Arguments", section_heading))
content.append(Paragraph("Python: Use default values when not provided.", body_text))
content.append(
    Preformatted(
        '''def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("Simon")       # Uses default
greet("Ella", 25)    # Overrides default''',
        code_style,
    )
)
content.append(Paragraph("JavaScript: Also supports default parameters.", body_text))
content.append(
    Preformatted(
        '''function greet(name, age = 18) {
    console.log(`Hello ${name}, you are ${age} years old.`);
}
greet("Simon");
greet("Ella", 25);''',
        code_style,
    )
)

# 3. Arbitrary Positional Arguments
content.append(Paragraph("3️⃣ Arbitrary Positional Arguments", section_heading))
content.append(
    Paragraph("Python: Uses *args to collect multiple values into a tuple.", body_text)
)
content.append(
    Preformatted(
        '''def add_numbers(*numbers):
    print(numbers)
    print(sum(numbers))

add_numbers(1, 2, 3, 4, 5)''',
        code_style,
    )
)
content.append(
    Paragraph(
        "JavaScript: Uses rest syntax (...args) to collect arguments into an array.",
        body_text,
    )
)
content.append(
    Preformatted(
        '''function addNumbers(...numbers) {
    console.log(numbers);
    console.log(numbers.reduce((a, b) => a + b));
}

addNumbers(1, 2, 3, 4, 5);''',
        code_style,
    )
)

# 4. Arbitrary Keyword Arguments
content.append(Paragraph("4️⃣ Arbitrary Keyword Arguments", section_heading))
content.append(Paragraph("Python: Uses **kwargs for named arguments.", body_text))
content.append(
    Preformatted(
        '''def introduce(**person):
    print(person)
    print(f"My name is {person['name']} and I am {person['age']} years old.")

introduce(name="Simon", age=25)''',
        code_style,
    )
)
content.append(Paragraph("JavaScript: Passes keyword-style arguments as objects.", body_text))
content.append(
    Preformatted(
        '''function introduce(person) {
    console.log(person);
    console.log(`My name is ${person.name} and I am ${person.age} years old.`);
}

introduce({ name: "Simon", age: 25 });''',
        code_style,
    )
)

# 5. Mixing Multiple Argument Types
content.append(Paragraph("5️⃣ Mixing Multiple Argument Types", section_heading))
content.append(Paragraph("Python: Combines *args and **kwargs.", body_text))
content.append(
    Preformatted(
        '''def order_pizza(size, *toppings, **details):
    print(f"Size: {size}")
    print("Toppings:", toppings)
    print("Details:", details)

order_pizza("Large", "pepperoni", "cheese", address="Lagos", delivery=True)''',
        code_style,
    )
)
content.append(Paragraph("JavaScript: Combines rest parameters and objects.", body_text))
content.append(
    Preformatted(
        '''function orderPizza(size, ...toppingsAndDetails) {
    console.log("Size:", size);
    console.log("Other arguments:", toppingsAndDetails);
}

orderPizza("Large", "pepperoni", "cheese", { address: "Lagos", delivery: true });''',
        code_style,
    )
)

# Spacer before summary
content.append(Spacer(1, 8))

# Summary comparison table
content.append(Paragraph("📊 Summary Comparison Table", section_heading))
summary_data = [
    ["Type", "Python", "JavaScript", "Stored As"],
    ["Positional", "def f(a, b)", "function f(a, b)", "Variables"],
    ["Default", "def f(a=1)", "function f(a=1)", "Variables"],
    ["Variable Positional", "*args", "...args", "Tuple / Array"],
    ["Variable Keyword", "**kwargs", "Object argument", "Dict / Object"],
    ["Keyword-only", "def f(*, x)", "N/A (use object)", "N/A"],
    ["Positional-only", "def f(x, /)", "N/A", "N/A"],
    ["Arbitrary args (legacy)", "N/A", "arguments", "Array-like object"],
]

table = Table(summary_data, colWidths=table_col_widths, hAlign="LEFT")
table_style = TableStyle(
    [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#cfe8ff")),  # header bg
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
)
table.setStyle(table_style)
content.append(table)

# Final small spacer
content.append(Spacer(1, 6))

# Build PDF
doc.build(content)

print(f"✅ PDF generated successfully: {pdf_file}")