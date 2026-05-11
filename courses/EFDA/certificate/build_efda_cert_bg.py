"""
EFDA Certificate of Completion — background PDF generator.
Output: 297×210mm landscape A4 with all static design elements.
Dynamic placeholders (student name, date, verification code) overlaid by Moodle Customcert.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
import os

# Output
OUT = "/sessions/cool-eloquent-noether/mnt/FDA Moodle/EFDA-Certificate-Background.pdf"
LOGO = "/sessions/cool-eloquent-noether/mnt/FDA Moodle/FIDA-logo-extracted.png"

# Page (landscape A4)
W, H = landscape(A4)  # ~842 x 595 pt

# Brand colors (WorldTeachPathways design system)
NAVY = HexColor("#1B365D")
TEAL = HexColor("#2D6F73")
GOLD = HexColor("#9C7C2E")  # subtle accent
CREAM = HexColor("#FBFAF6")
GRAY = HexColor("#6B7785")
INK = HexColor("#1F2A37")

c = canvas.Canvas(OUT, pagesize=landscape(A4))

# ── Background fill ──
c.setFillColor(CREAM)
c.rect(0, 0, W, H, fill=1, stroke=0)

# ── Corner accent — top-left navy block ──
c.setFillColor(NAVY)
c.rect(0, H-25*mm, 85*mm, 25*mm, fill=1, stroke=0)
# Teal sliver under it
c.setFillColor(TEAL)
c.rect(0, H-29*mm, 85*mm, 4*mm, fill=1, stroke=0)

# ── Footer bar — full-width navy + teal stripe ──
c.setFillColor(TEAL)
c.rect(0, 0, W, 20*mm, fill=1, stroke=0)
c.setFillColor(NAVY)
c.rect(0, 20*mm, W, 3*mm, fill=1, stroke=0)

# ── FIDA Logo (top-left, on navy block) ──
# The PNG is on dark/black background but logo is actually for light bg.
# We'll just drop it onto the navy block — design contrast.
try:
    logo = ImageReader(LOGO)
    iw, ih = logo.getSize()
    # Place logo at top-left within the navy accent, sized to ~60mm wide
    logo_w = 65*mm
    logo_h = logo_w * (ih/iw)
    c.drawImage(logo, 12*mm, H-21*mm, width=logo_w, height=logo_h, mask='auto', preserveAspectRatio=True)
except Exception as e:
    print(f"Logo failed: {e}")

# ── Top-right: Certificate № label (small, navy on cream) ──
c.setFillColor(NAVY)
c.setFont("Helvetica", 9)
c.drawRightString(W-15*mm, H-15*mm, "CERTIFICATE NUMBER")
# Code placeholder line — Customcert will overlay actual code here
c.setStrokeColor(TEAL)
c.setLineWidth(0.5)
c.line(W-55*mm, H-22*mm, W-15*mm, H-22*mm)

# ── Hero block ──
hero_y = H - 70*mm  # baseline for the eyebrow

# Eyebrow
c.setFillColor(TEAL)
c.setFont("Helvetica-Bold", 11)
c.drawCentredString(W/2, hero_y, "F L O R I D A   I N S T I T U T E   O F   D E N T A L   A S S I S T I N G")

# Main title — large serif
c.setFillColor(NAVY)
c.setFont("Times-Bold", 48)  # Closest to Playfair Display in default ReportLab fonts
c.drawCentredString(W/2, hero_y - 22*mm, "Certificate of Completion")

# Subtitle accent line
c.setStrokeColor(GOLD)
c.setLineWidth(1.2)
c.line(W/2 - 30*mm, hero_y - 28*mm, W/2 + 30*mm, hero_y - 28*mm)

# "This certifies that"
c.setFillColor(GRAY)
c.setFont("Helvetica-Oblique", 13)
c.drawCentredString(W/2, hero_y - 40*mm, "This certifies that")

# ── Student name placeholder — large serif (Customcert overlays actual name) ──
# Just draw a subtle baseline; the studentname element will land here.
name_y = hero_y - 56*mm
# (Customcert will print the name centered at this Y)

# ── Achievement paragraph ──
para_y = name_y - 18*mm
c.setFillColor(INK)
c.setFont("Helvetica", 11.5)
line1 = "has successfully completed the 20-hour Expanded Functions Dental Assisting Certification Course,"
line2 = "satisfying the training requirements of FAC 64B5-16.002, FAC 64B5-16.005 and 64B5-16.0051,"
line3 = "and §466.024(6), Florida Statutes, under the supervision of a Florida-licensed dentist."
c.drawCentredString(W/2, para_y, line1)
c.drawCentredString(W/2, para_y - 6*mm, line2)
c.drawCentredString(W/2, para_y - 12*mm, line3)

# ── Signature block — bottom-left ──
sig_x = 35*mm
sig_y = 38*mm
# Signature line
c.setStrokeColor(NAVY)
c.setLineWidth(0.8)
c.line(sig_x, sig_y, sig_x + 70*mm, sig_y)
# Name
c.setFillColor(NAVY)
c.setFont("Helvetica-Bold", 11)
c.drawString(sig_x, sig_y - 5*mm, "Debbie Sanders, EFDA")
# Title
c.setFillColor(GRAY)
c.setFont("Helvetica-Oblique", 9.5)
c.drawString(sig_x, sig_y - 10*mm, "Instructor of Record · Co-Founder, FIDA")

# ── Date block — bottom-right (above teal sweep) ──
date_x = W - 35*mm - 70*mm
date_line_y = 38*mm
c.setStrokeColor(NAVY)
c.setLineWidth(0.8)
c.line(date_x, date_line_y, date_x + 70*mm, date_line_y)
# Label
c.setFillColor(GRAY)
c.setFont("Helvetica", 9.5)
c.drawString(date_x, date_line_y - 5*mm, "Date of Issue")
# Actual date placeholder — Customcert will print the date below the line
# (we draw nothing here; Customcert element will land at right Y)

# ── Footer banner inside teal sweep ──
c.setFillColor(CREAM)
c.setFont("Helvetica-Bold", 10)
c.drawCentredString(W/2, 11*mm, "Florida Board of Dentistry Approved · Program #6501 · Issued June 11, 2021")
c.setFont("Helvetica", 8.5)
c.drawCentredString(W/2, 6*mm, "Verify at  fldentalassisting.moodlecloud.com/mod/customcert/verify")

c.save()
print(f"Wrote {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
