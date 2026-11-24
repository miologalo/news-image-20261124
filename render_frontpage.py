#!/usr/bin/env python3
"""Render the front page of THE WORLD TODAY, Tuesday 24 November 2026.

Deterministic PIL drawing. No network. Output: entry.png (768x1024, < 1 MiB).
Run: python3 render_frontpage.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 768, 1024
PAPER = (253, 251, 245)
INK = (18, 18, 18)
GREY = (90, 88, 82)
RULE = (18, 18, 18)
GREEN = (118, 185, 0)
RED = (178, 34, 34)
LIGHTGREY = (210, 208, 200)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill=INK):
    w_ = draw.textlength(text, font=fnt)
    draw.text((cx - w_ / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 2


def draw_block(draw, x, y, max_w, lines, fnt, leading, fill=INK, align="left"):
    for ln in lines:
        if align == "center":
            w_ = draw.textlength(ln, font=fnt)
            draw.text((x + (max_w - w_) / 2, y), ln, font=fnt, fill=fill)
        else:
            draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 42
    x0, x1 = M, W - M
    cw = x1 - x0

    y = 18
    # ---- top thin rule + date line ----
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 8
    f_small = font(SANS, 14)
    left = "No. 328  •  Price: Free"
    right = "Tuesday 24 November 2026"
    d.text((x0, y), left, font=f_small, fill=GREY)
    rw = d.textlength(right, font=f_small)
    d.text((x1 - rw, y), right, font=f_small, fill=GREY)
    y += 22

    # ---- masthead (fits: 58pt) ----
    f_mast = font(SERIF_B, 58)
    y = draw_centered(d, W // 2, y, "THE WORLD TODAY", f_mast)
    y += 1
    d.line([(x0, y), (x1, y)], fill=RULE, width=4)
    y += 5
    d.line([(x0, y), (x1, y)], fill=RULE, width=1)
    y += 10

    # ---- kicker ----
    f_kick = font(SANS_B, 15)
    y = draw_centered(d, W // 2, y, "TECH  •  POLITICS  •  THE BOARDROOM U-TURN", f_kick, fill=RED)
    y += 6

    # ---- lead headline ----
    f_lead = font(SERIF_B, 44)
    lead = "NVIDIA REHIRES HUANG IN STUNNING REVERSAL AFTER TRUMP PUSH"
    lines = wrap(d, lead, f_lead, cw)
    y = draw_block(d, x0, y, cw, lines, f_lead, 50, align="center")
    y += 8

    # ---- lead visual: compact green chip ----
    vw, vh = 260, 100
    vx, vy = (W - vw) // 2, y
    d.rounded_rectangle([vx, vy, vx + vw, vy + vh], radius=9, fill=(24, 24, 24))
    for i in range(5):
        px = vx + 24 + i * 48
        d.rectangle([px, vy - 10, px + 13, vy], fill=(120, 120, 120))
        d.rectangle([px, vy + vh, px + 13, vy + vh + 10], fill=(120, 120, 120))
    f_chip = font(SANS_B, 44)
    tw = d.textlength("NVDA", font=f_chip)
    d.text((vx + (vw - tw) / 2, vy + 12), "NVDA", font=f_chip, fill=GREEN)
    pts = [(vx + 24, vy + 96), (vx + 82, vy + 72), (vx + 130, vy + 84),
           (vx + 178, vy + 56), (vx + 232, vy + 36)]
    d.line(pts, fill=GREEN, width=6, joint="curve")
    ax, ay = pts[-1]
    d.polygon([(ax, ay - 12), (ax + 17, ay - 2), (ax - 2, ay + 10)], fill=GREEN)
    y = vy + vh + 14

    # ---- lead standfirst ----
    f_stand = font(SERIF, 20)
    stand = ("Jensen Huang is back as Nvidia chief executive after a stunning board "
             "reversal, with President Trump and Vice-President J. D. Vance pressing "
             "the chipmaker to reinstate him.")
    lines = wrap(d, stand, f_stand, cw)
    y = draw_block(d, x0, y, cw, lines, f_stand, 26)
    y += 10
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 12

    # ---- secondary stories: two columns ----
    col_w = (cw - 24) // 2
    f_h2 = font(SERIF_B, 22)
    f_body = font(SERIF, 17)
    ly = y
    a_head = "SEOUL SCRAMBLES JETS AS WARPLANES ENTER AIR ZONE"
    a_lines = wrap(d, a_head, f_h2, col_w)
    ly = draw_block(d, x0, ly, col_w, a_lines, f_h2, 27)
    ly += 3
    a_body = ("Russian warplanes and a suspected North Korean aircraft breached South "
              "Korean airspace near Ulleung island; residents were ordered to shelter.")
    b_lines = wrap(d, a_body, f_body, col_w)
    ly = draw_block(d, x0, ly, col_w, b_lines, f_body, 22)
    ry = y
    b_head = "DEMOCRATS CLINCH HISTORIC HOUSE MAJORITY"
    b_lines = wrap(d, b_head, f_h2, col_w)
    ry = draw_block(d, x1 - col_w, ry, col_w, b_lines, f_h2, 27)
    ry += 3
    b_body = ("At least 258 seats — the largest Democratic majority in the House "
              "since 1992 — in a midterm repudiation of the White House.")
    bb_lines = wrap(d, b_body, f_body, col_w)
    ry = draw_block(d, x1 - col_w, ry, col_w, bb_lines, f_body, 22)
    mid_x = W // 2
    top_y = y
    bot_y = max(ly, ry)
    d.line([(mid_x, top_y), (mid_x, bot_y)], fill=LIGHTGREY, width=1)
    y = bot_y + 12
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 12

    # ---- third story (full width) ----
    f_h3 = font(SERIF_B, 25)
    c_head = "KYIV STRIKES KILL 14 AS WAR'S TOLL NEARS 500,000"
    c_lines = wrap(d, c_head, f_h3, cw)
    y = draw_block(d, x0, y, cw, c_lines, f_h3, 30)
    y += 3
    c_body = ("Russian strikes on the Kyiv region killed at least 14, while newly hacked "
              "data puts Russia's own Ukraine death toll near half a million. Allies warn "
              "Moscow may launch a nuclear space weapon next month; NATO vows a space defence.")
    cb_lines = wrap(d, c_body, f_body, cw)
    y = draw_block(d, x0, y, cw, cb_lines, f_body, 22)
    y += 12
    d.line([(x0, y), (x1, y)], fill=RULE, width=2)
    y += 10

    # ---- bottom briefs ----
    f_brief_h = font(SANS_B, 15)
    f_brief = font(SANS, 15)
    briefs = [
        ("TRUMP HALTS BLAST:", "President pauses the planned detonation of degraded explosives at an Iowa plant pending a court ruling."),
        ("GROK SUED:", "US states sue Musk firms over sexualised images made by the Grok chatbot."),
        ("SPACE RACE:", "NATO vows space defence after a report of a Russian nuclear satellite."),
    ]
    for head, body in briefs:
        d.text((x0, y), head, font=f_brief_h, fill=INK)
        hw = d.textlength(head + " ", font=f_brief_h)
        rest_w = cw - hw
        blines = wrap(d, body, f_brief, rest_w)
        if blines:
            d.text((x0 + hw, y), blines[0], font=f_brief, fill=INK)
            yy = y + 20
            for ln in blines[1:]:
                d.text((x0, yy), ln, font=f_brief, fill=INK)
                yy += 20
            y = yy
        y += 3
    y += 4
    d.line([(x0, y), (x1, y)], fill=RULE, width=4)
    y += 8
    f_foot = font(SANS, 13)
    foot = "THE WORLD TODAY  •  Tuesday 24 November 2026  •  All the day's world news in one page"
    draw_centered(d, W // 2, y, foot, f_foot, fill=GREY)
    print("final y (footer baseline):", y, "canvas H:", H)

    out = "/home/hatch/workspace/makefun/news-image-20261124/entry.png"
    img.save(out, "PNG", optimize=True)
    import os
    print("saved", out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
