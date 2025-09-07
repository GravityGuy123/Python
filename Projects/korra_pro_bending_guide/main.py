# korra_pro_bending_guide_fixed.py
# Creates a detailed Pro-Bending strategy PDF for The Legend of Korra (2014).

import sys
import os

# Ensure reportlab is available
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak,
        ListFlowable, ListItem, Table, TableStyle
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak,
        ListFlowable, ListItem, Table, TableStyle
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors

def build_pdf(path: str):
    styles = getSampleStyleSheet()
    # Custom styles
    styles.add(ParagraphStyle(name="H1", parent=styles["Heading1"], fontSize=18, spaceBefore=0, spaceAfter=4))
    styles.add(ParagraphStyle(name="H2", parent=styles["Heading2"], fontSize=14, spaceBefore=4, spaceAfter=3))
    styles.add(ParagraphStyle(name="Body", parent=styles["Normal"], fontSize=10.5, leading=14, spaceBefore=0, spaceAfter=3))
    styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontSize=11, leading=13, spaceBefore=0, spaceAfter=0))

    story = []
    title = "The Legend of Korra (2014) – Pro-Bending Arena Strategy Guide"
    subtitle = "Keyboard & Mouse Tactics, Knockout Order, Opponent-Specific Counters, and Combos"

    story.append(Paragraph(title, styles["H1"]))
    story.append(Paragraph(subtitle, styles["Subtitle"]))

    # --- First section (immediately after subtitle, no big gap) ---
    story.append(Paragraph("Controls You’ll Rely On (Default PC Keyboard)", styles["H2"]))
    controls = [
        "Left Click (Light Attack): quick elemental strikes.",
        "Right Click (Heavy Attack): stronger knockback, slower recovery.",
        "Space: dodge (i-frames if timed just before impact).",
        "Shift (hold): charge attacks for bigger pushback.",
        "Number Keys (1–4): switch elements (in Pro-Bending mainly Waterbending).",
    ]
    story.append(ListFlowable([ListItem(Paragraph(c, styles["Body"])) for c in controls], bulletType="bullet"))

    # --- Core tactics ---
    story.append(Paragraph("Killer Tactics for Pro-Bending", styles["H2"]))
    tactics = [
        "Own the center: staying mid-arena gives you space to recover if you get clipped.",
        "Bread-and-butter combo: Light → Light → Heavy. Use lights to flinch, then heavy for pushback.",
        "Dodge-punish rhythm: tap Space just before impact, then immediately Heavy for free shove.",
        "Target priority: focus one opponent at a time. Don’t spread damage.",
        "Charged Heavy at the edge: hold Shift + Right Click to send foes multiple zones when they’re near the boundary.",
        "Bait overcommit: step back slightly to invite a rush, sidestep with Space, then Heavy.",
        "Stamina discipline: don’t spam dodges; save them for clutch moments and punish windows.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(t, styles["Body"])) for t in tactics], bulletType="bullet"))

    # --- Pro-Bending mechanics ---
    story.append(Paragraph("How Pro-Bending Works", styles["H2"]))
    info = [
        "Each team has 3 zones (lines). Attacks push opponents back line by line.",
        "You win by pushing an opponent out completely (ring-out) or by forcing all opponents to their last zone and maintaining control.",
        "Multiple knockbacks are typically needed to progress zone 1 → zone 2 → zone 3 → out, unless you land a charged heavy near the edge.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(i, styles["Body"])) for i in info], bulletType="bullet"))

    # --- Strategy focus ---
    story.append(Paragraph("Focus vs. Line-by-Line Push", styles["H2"]))
    story.append(Paragraph(
        "Prioritize one opponent and push them line by line unless you see a clean ring-out chance. "
        "Once it becomes 2-on-1 or 1-on-1, the fight snowballs in your favor. "
        "Keep peripheral awareness to avoid blindside hits while you tunnel on your target.",
        styles["Body"]
    ))

    # --- Knockout order ---
    story.append(Paragraph("Best Knockout Order", styles["H2"]))
    order = [
        "1) Earthbender first – slowest and easiest to shove; removing the frontliner reduces shield pressure on their team.",
        "2) Firebender second – aggressive and rush-happy; easy to dodge-punish into big pushback.",
        "3) Waterbender last – strongest zoning, but much less dangerous when isolated.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(o, styles["Body"])) for o in order], bulletType="bullet"))

    # --- Why this order works ---
    story.append(Paragraph("Why This Order Works", styles["H2"]))
    why = [
        "Eliminating the Earthbender removes the tank that anchors their line.",
        "Taking out the Firebender next stops the constant rushdown attempts.",
        "The Waterbender relies on spacing and cover; alone, she’s easy to corner and push.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(w, styles["Body"])) for w in why], bulletType="bullet"))

    # --- Opponent-specific breakdown ---
    story.append(PageBreak())
    story.append(Paragraph("Opponent-Specific Gameplan", styles["H1"]))

    story.append(Paragraph("Earthbender (First Target)", styles["H2"]))
    earth = [
        "Behavior: slower start-up, strong knockback if he connects, often plays front line.",
        "Punish windows: any whiffed heavy or telegraphed projectile—sidestep (Space) then Heavy.",
        "Best moves vs. him: Light–Light–Heavy to keep him flinched, Charged Heavy when he’s at zone edge.",
        "Positioning: stay slightly off-axis (diagonal) to make his straight shots miss.",
        "Mistakes to avoid: trading heavies; his wins will shove you back more when you’re near your edge.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(e, styles["Body"])) for e in earth], bulletType="bullet"))

    story.append(Paragraph("Firebender (Second Target)", styles["H2"]))
    fire = [
        "Behavior: rushes in and overextends; best bait target.",
        "Punish windows: as he dashes or after any forward heavy—late dodge then immediate Heavy.",
        "Best moves vs. him: single Light poke to check, then Heavy; or pure dodge → Heavy.",
        "Positioning: micro-step back to invite the dash, then sidestep to create his whiff.",
        "Mistakes to avoid: mashing lights when he’s charging—you’ll get counter-hit. Respect the start-up, then punish.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(f, styles["Body"])) for f in fire], bulletType="bullet"))

    story.append(Paragraph("Waterbender (Last Target)", styles["H2"]))
    water = [
        "Behavior: best zoning and lateral movement; harder to pin down when teammates are alive.",
        "Punish windows: after she commits to a ranged string—dodge toward her to close distance, then Heavy.",
        "Best moves vs. her: Light–Light to break rhythm, then step Heavy; Charged Heavy if she’s cornered.",
        "Positioning: herd her toward a barrier by cutting off angles rather than chasing directly.",
        "Mistakes to avoid: chasing in straight lines; use diagonals and short burst steps between projectiles.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(w, styles["Body"])) for w in water], bulletType="bullet"))

    # --- Cheatsheet ---
    story.append(PageBreak())
    story.append(Paragraph("One-Page Cheatsheet", styles["H1"]))
    cheat = [
        "Default combo: Light → Light → Heavy.",
        "Ring-out confirm: Charged Heavy near edge (Shift + Right Click).",
        "Dodge timing: press Space just before the hit lands; Heavy immediately after.",
        "Target order: Earth → Fire → Water.",
        "Never fight at your edge; rotate back to center after each exchange.",
    ]
    story.append(ListFlowable([ListItem(Paragraph(c, styles["Body"])) for c in cheat], bulletType="bullet"))

    story.append(Paragraph("Combo Quick-Reference Table", styles["H2"]))
    data = [
        ["Combo Name", "Input (Keyboard/Mouse)", "Effect"],
        ["Quick Jab", "Left Click", "Fast poke, interrupts opponents."],
        ["Double Jab + Push", "Left Click → Left Click → Right Click", "Steady knockback, good for line pushes."],
        ["Charged Heavy (Ring-Out)", "Hold Shift + Right Click", "Big shove; instant ring-out if near edge."],
        ["Dodge → Counter Heavy", "Space (just before hit) → Right Click", "Punishes enemy with strong knockback."],
        ["Jump Heavy Smash", "Space (jump) → Right Click", "Aerial strike that disrupts zoning."],
        ["Light → Dodge Cancel", "Left Click → Space", "Quick poke then reposition safely."],
    ]
    table = Table(data, colWidths=[1.8*inch, 2.5*inch, 2.8*inch])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 8),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
    ]))
    story.append(table)

    story.append(Paragraph(
        "Good luck in the arena — once the first opponent is out, momentum is yours!",
        styles["Body"]
    ))

    # Build PDF
    doc = SimpleDocTemplate(path, pagesize=letter,
        leftMargin=0.8*inch, rightMargin=0.8*inch,
        topMargin=0.7*inch, bottomMargin=0.7*inch)
    doc.build(story)

if __name__ == "__main__":
    out_name = "legend_of_korra_pro_bending_strategy_fixed2.pdf"
    out_path = os.path.abspath(out_name)
    build_pdf(out_path)
    print(f"PDF created: {out_path}")