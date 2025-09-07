from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

guide_text = """
THE LEGEND OF KORRA (2014) – CH. 4 BOSS GUIDE (MEGA TANK) + CONTROLS + COMBOS

Quick Status
- You currently have: Martial Arts (Unarmed) + Waterbending.
- You have NOT unlocked Earthbending yet.
- Beating the Mega Tank unlocks Firebending next.

Default PC Controls (Keyboard + Mouse)
- Move: W / A / S / D
- Camera/Aim: Mouse
- Light Attack: Left Click
- Heavy Attack (hold for charge): Right Click
- Block / Counter (timed): Shift
- Dodge / Evade: Spacebar (use with A/D to side-dodge)
- Jump: Spacebar (tap)
- Spirit Charge (Chi ability): E
- Switch Bending Style: Q (cycles through unlocked elements)
- Pause/Menu: Esc

Boss: Mega Tank – How It Works
- Weak point: the cockpit/eye area (revealed after you stagger it).
- Big tells: engine rev (straight-line charge), wide melee sweeps.
- Safest plan: stay mid-range, bait the charge, punish recovery windows.

Fight Plan (No Earthbending Yet)
1) Circle at mid-range (WASD) and bait the charge.
2) As it dashes, dodge SIDEWAYS (Spacebar + A/D) at the last moment.
3) When it’s stuck recovering, unload WATER attacks:
   - Water Whip Chain: Left, Left, Left (safe DPS).
   - Water Burst Finisher: Left, Left, Right (brief stun/extra damage).
   - Charged Torrent: hold Right Click (big water projectile) while it’s stationary.
4) Block/Counter select melee swings (tap Shift right before impact) to stagger it,
   then pour in a Charged Torrent or a Left, Left, Right string.
5) Build Chi and use Spirit Charge (E) whenever available for huge damage.
6) Repeat the cycle: Bait charge → Side dodge → Punish → (Counter) → Spirit Charge.

Waterbending Move Reference (KB+Mouse)
- Light Chain (safe): Left, Left, Left
- Light→Heavy Finisher: Left, Left, Right
- Charged Projectile: hold Right Click
- Aerial Poke: Jump (Spacebar) → Left Click in air

Martial Arts (Unarmed) Reference
- Basic Punch String: Left, Left, Left
- Heavy Slam (only if stunned): hold Right Click
- Aerial Punches: Jump → mash Left Click

Common Mistakes (Avoid These)
- Back-dodging the charge (you’ll still get hit) – side-dodge instead.
- Standing in front of the cannon too long – strafe to the flanks.
- Using slow heavy punches when it’s active – wait for a stun/recovery.
- Forgetting Spirit Charge (E) – it melts boss health; use it on cooldown.

What You Unlock Next
- After defeating this Mega Tank, you unlock FIREBENDING (fast, aggressive).
- Earthbending comes later, so don’t worry that you haven’t got it yet.

(Preview) Firebending Starter Combos (for when it unlocks next)
- Fire Rush (fast pressure): Left, Left, Left
- Flame Burst Ender: Left, Left, Right
- Charged Fireball: hold Right Click
- Style Weave: Use Q mid-string to rotate elements and extend combos

Micro-Checklist During the Fight
[ ] I dodge sideways, not backwards, on charges.
[ ] I punish recoveries with Left, Left, Right or a Charged Torrent.
[ ] I counter melee swings with Shift when possible.
[ ] I press E (Spirit Charge) as soon as it’s up.
[ ] I keep distance and strafe around the tank’s front arc.

You’ve got this. Win the fight → unlock Firebending → enjoy the power spike!
"""

def save_pdf(filename, text):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER
    margin = inch * 0.75
    text_object = c.beginText(margin, height - margin)
    text_object.setFont("Courier", 11)
    for line in text.splitlines():
        text_object.textLine(line)
        if text_object.getY() < margin:
            c.drawText(text_object)
            c.showPage()
            text_object = c.beginText(margin, height - margin)
            text_object.setFont("Courier", 11)
    c.drawText(text_object)
    c.save()

# Save the PDF
save_pdf("Korra_Chapter4_Mega_Tank_Guide.pdf", guide_text)
print("PDF saved as Korra_Chapter4_Mega_Tank_Guide.pdf")
