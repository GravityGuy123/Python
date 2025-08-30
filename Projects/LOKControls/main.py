from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Output file name
file_path = "legend_of_korra_pc_controls.pdf"

# Create PDF document
doc = SimpleDocTemplate(file_path, pagesize=letter)
styles = getSampleStyleSheet()
story = []

content = """
🎮 The Legend of Korra – PC Default Keyboard & Mouse Controls
=============================================================

🟢 Movement & Camera
--------------------
W, A, S, D → Move Korra (W=forward, A=left, S=backward, D=right)
Mouse → Move the camera around Korra (aim & look around)
R (sometimes Q/E) → Lock-on to an enemy (focus camera on target)

🟢 Basic Combat
---------------
Left Mouse Button → Light Attack (quick strikes, fast combos)
Right Mouse Button → Heavy Attack (slower, stronger attacks)
Mouse Scroll Wheel → Switch Bending Element (Water, Earth, Fire, Air)
C → Counter / Perfect Guard (parry enemy strikes, counterattack)
Shift → Dodge / Evade (quick roll/flip to avoid attacks)

🟢 Movement Actions
-------------------
Spacebar → Jump (combine with attacks for aerial combos)
W + Spacebar → Forward leap (engage enemies, jump gaps)

🟢 Advanced Combat / Specials
-----------------------------
R (or Middle Mouse Button) → Lock-On Target
Q → Spirit Attack (special bending attack, consumes chi)
C + V (or combo) → Avatar State (unlocks later, Korra glows, all attacks boosted)

🟢 Items & Menus
----------------
Number Keys (1–4) → Use items (potions, etc.)
Esc → Pause/Menu (inventory, skills, settings)

🟢 Naga Riding Mini-Game
------------------------
W, A, S, D → Steer Naga
Shift → Slide under obstacles
Spacebar → Jump obstacles
LMB/RMB/Scroll → Use bending powers

🟢 How It Feels in Practice
---------------------------
- WASD + Mouse for main movement/combat
- LMB/RMB = core combos
- Scroll Wheel = swap bending mid-combo
- Shift (Dodge) + C (Counter) = survival keys
- Works best with an Xbox-style controller (use x360ce if needed)
"""

# Split content into paragraphs
for line in content.split("\n"):
    if line.strip() == "":
        story.append(Spacer(1, 12))
    else:
        story.append(Paragraph(line, styles["Normal"]))

# Build PDF
doc.build(story)

print(f"PDF created successfully: {file_path}")
