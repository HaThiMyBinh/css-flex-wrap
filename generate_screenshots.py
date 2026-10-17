import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    try:
        path = os.path.join("C:/Windows/Fonts", name)
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

font_title = get_font("segoeuib.ttf", 22)
font_subtitle = get_font("segoeui.ttf", 13)
font_h2 = get_font("segoeuib.ttf", 18)
font_h3 = get_font("segoeuib.ttf", 15)
font_body = get_font("segoeui.ttf", 13)
font_body_b = get_font("segoeuib.ttf", 13)
font_small = get_font("segoeui.ttf", 11)
font_tab = get_font("segoeui.ttf", 12)
font_code = get_font("consola.ttf", 13)
font_item = get_font("segoeuib.ttf", 16)
font_badge = get_font("segoeuib.ttf", 11)

def draw_browser_frame(draw, width, height, title, url):
    draw.rectangle([0, 0, width, 70], fill="#e2e8f0")
    draw.ellipse([14, 12, 24, 22], fill="#ef4444")
    draw.ellipse([30, 12, 40, 22], fill="#f59e0b")
    draw.ellipse([46, 12, 56, 22], fill="#10b981")

    draw.rounded_rectangle([68, 6, 320, 36], radius=5, fill="#ffffff")
    draw.text((82, 12), title, fill="#1e293b", font=font_tab)

    draw.rectangle([0, 36, width, 70], fill="#ffffff")
    draw.line([0, 36, width, 36], fill="#cbd5e1", width=1)
    draw.line([0, 70, width, 70], fill="#e2e8f0", width=1)

    draw.polygon([(14, 53), (20, 48), (20, 58)], fill="#64748b")
    draw.polygon([(34, 53), (28, 48), (28, 58)], fill="#64748b")

    draw.rounded_rectangle([50, 41, width - 15, 65], radius=11, fill="#f1f5f9", outline="#cbd5e1", width=1)
    draw.text((65, 45), url, fill="#475569", font=font_small)

def render_wrap_screenshot(out_path):
    w, h = 950, 600
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "flex-wrap: wrap Demo", "http://localhost:5500/index.html (flex-wrap: wrap)")

    start_y = 95
    draw.text((50, start_y), "Thực hành flex-wrap: wrap", fill="#0f172a", font=font_h2)
    start_y += 30
    draw.text((50, start_y), "Các Flex Items tự động xuống dòng mới khi chiều rộng Container không đủ chứa.", fill="#475569", font=font_body)

    # Container 600x260
    start_y += 35
    cx, cy = 50, start_y
    cw, ch = 600, 240
    draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=8, fill="#ffffff", outline="#0f172a", width=2)

    # 6 items: 180x80 each, gap 10. In 600px width (padding 10): 580 width inside.
    # Row 1: 3 items (180*3 + 20 = 560px <= 580px) -> fits!
    # Row 2: 3 items -> fits!
    # Rows go from top to bottom
    items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
    iw, ih = 180, 80
    gap = 10
    pad = 15

    for idx, name in enumerate(items):
        row = idx // 3
        col = idx % 3
        bx = cx + pad + col * (iw + gap)
        by = cy + pad + row * (ih + gap)

        draw.rounded_rectangle([bx, by, bx + iw, by + ih], radius=6, fill="#93c5fd", outline="#60a5fa", width=2)
        bbox = draw.textbbox((0, 0), name, font=font_item)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (iw - tw) // 2, by + (ih - th) // 2 - 2), name, fill="#1e3a8a", font=font_item)

    # Indicator arrows on side
    draw.text((cx + cw + 30, cy + 40), "Dòng 1: Item 1 - 3", fill="#2563eb", font=font_body_b)
    draw.text((cx + cw + 30, cy + 70), "↓ Hướng xuống dòng mới", fill="#16a34a", font=font_small)
    draw.text((cx + cw + 30, cy + 130), "Dòng 2: Item 4 - 6", fill="#2563eb", font=font_body_b)

    # Explanatory card
    info_y = cy + ch + 25
    draw.rounded_rectangle([50, info_y, w - 50, info_y + 60], radius=6, fill="#eff6ff", outline="#bfdbfe", width=1)
    draw.text((65, info_y + 12), "[Kết quả] flex-wrap: wrap;", fill="#1e40af", font=font_body_b)
    draw.text((65, info_y + 34), "Container 600px không đủ chứa 6 items (6 x 180px) trên 1 dòng nên tự bọc thành 2 dòng (3 items/dòng).", fill="#334155", font=font_small)

    img.save(out_path)
    print(f"Saved: {out_path}")

def render_nowrap_screenshot(out_path):
    w, h = 950, 600
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "flex-wrap: nowrap Demo", "http://localhost:5500/index.html (flex-wrap: nowrap)")

    start_y = 95
    draw.text((50, start_y), "Thực hành flex-wrap: nowrap (Giá trị mặc định)", fill="#0f172a", font=font_h2)
    start_y += 30
    draw.text((50, start_y), "Tất cả các Flex Items bắt buộc nằm trên 1 dòng duy nhất, không xuống dòng.", fill="#475569", font=font_body)

    # Container 600x240
    start_y += 35
    cx, cy = 50, start_y
    cw, ch = 600, 240
    draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=8, fill="#ffffff", outline="#0f172a", width=2)

    # Items shrink to fit 1 row! In 580px usable space, 6 items + 5 gaps (50px) = 530px => each item is ~88px
    iw_shrink = 85
    ih = 80
    gap = 8
    pad = 12

    for idx, name in enumerate(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]):
        bx = cx + pad + idx * (iw_shrink + gap)
        by = cy + pad + 20

        draw.rounded_rectangle([bx, by, bx + iw_shrink, by + ih], radius=6, fill="#bbf7d0", outline="#86efac", width=2)
        bbox = draw.textbbox((0, 0), name, font=font_body_b)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (iw_shrink - tw) // 2, by + (ih - th) // 2 - 2), name, fill="#14532d", font=font_body_b)

    # Right side indicator
    draw.text((cx + cw + 30, cy + 30), "Chỉ có 1 dòng duy nhất", fill="#16a34a", font=font_body_b)
    draw.text((cx + cw + 30, cy + 55), "→ Không xuống dòng", fill="#dc2626", font=font_body_b)
    draw.text((cx + cw + 30, cy + 80), "Các item tự động co lại", fill="#475569", font=font_small)
    draw.text((cx + cw + 30, cy + 100), "(flex-shrink) để vừa 1 dòng", fill="#475569", font=font_small)

    info_y = cy + ch + 25
    draw.rounded_rectangle([50, info_y, w - 50, info_y + 60], radius=6, fill="#f0fdf4", outline="#bbf7d0", width=1)
    draw.text((65, info_y + 12), "[Kết quả] flex-wrap: nowrap; (Giá trị mặc định)", fill="#166534", font=font_body_b)
    draw.text((65, info_y + 34), "Các item không được bọc xuống dòng mới. Nội dung ép nằm trên 1 hàng.", fill="#334155", font=font_small)

    img.save(out_path)
    print(f"Saved: {out_path}")

def render_wrap_reverse_screenshot(out_path):
    w, h = 950, 600
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, h, "flex-wrap: wrap-reverse Demo", "http://localhost:5500/index.html (flex-wrap: wrap-reverse)")

    start_y = 95
    draw.text((50, start_y), "Thực hành flex-wrap: wrap-reverse", fill="#0f172a", font=font_h2)
    start_y += 30
    draw.text((50, start_y), "Cho phép xuống dòng nhưng hướng của Cross Axis bị đảo ngược (dòng mới xếp lên trên).", fill="#475569", font=font_body)

    start_y += 35
    cx, cy = 50, start_y
    cw, ch = 600, 240
    draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=8, fill="#ffffff", outline="#0f172a", width=2)

    # In wrap-reverse:
    # Row 1 (Item 1-3) is placed at the BOTTOM!
    # Row 2 (Item 4-6) is placed at the TOP!
    iw, ih = 180, 80
    gap = 10
    pad = 15

    # Draw Items 4, 5, 6 at TOP (row 0)
    for idx, name in enumerate(["Item 4", "Item 5", "Item 6"]):
        bx = cx + pad + idx * (iw + gap)
        by = cy + pad

        draw.rounded_rectangle([bx, by, bx + iw, by + ih], radius=6, fill="#fecaca", outline="#fca5a5", width=2)
        bbox = draw.textbbox((0, 0), name, font=font_item)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (iw - tw) // 2, by + (ih - th) // 2 - 2), name, fill="#7f1d1d", font=font_item)

    # Draw Items 1, 2, 3 at BOTTOM (row 1)
    for idx, name in enumerate(["Item 1", "Item 2", "Item 3"]):
        bx = cx + pad + idx * (iw + gap)
        by = cy + pad + ih + gap

        draw.rounded_rectangle([bx, by, bx + iw, by + ih], radius=6, fill="#fecaca", outline="#fca5a5", width=2)
        bbox = draw.textbbox((0, 0), name, font=font_item)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx + (iw - tw) // 2, by + (ih - th) // 2 - 2), name, fill="#7f1d1d", font=font_item)

    # Indicator
    draw.text((cx + cw + 30, cy + 30), "Dòng 2 (Item 4-6): Xếp ở TRÊN", fill="#991b1b", font=font_body_b)
    draw.text((cx + cw + 30, cy + 60), "↑ Hướng dòng bị đảo ngược", fill="#ea580c", font=font_small)
    draw.text((cx + cw + 30, cy + 120), "Dòng 1 (Item 1-3): Xếp ở DƯỚI", fill="#991b1b", font=font_body_b)

    info_y = cy + ch + 25
    draw.rounded_rectangle([50, info_y, w - 50, info_y + 60], radius=6, fill="#fef2f2", outline="#fecaca", width=1)
    draw.text((65, info_y + 12), "[Kết quả] flex-wrap: wrap-reverse;", fill="#991b1b", font=font_body_b)
    draw.text((65, info_y + 34), "Cross Axis bị đảo chiều: Item 1-3 nằm hàng dưới, Item 4-6 đẩy lên hàng trên.", fill="#334155", font=font_small)

    img.save(out_path)
    print(f"Saved: {out_path}")

def render_combined_screenshot(out_path):
    w, h = 1050, 850
    img = Image.new("RGB", (w, h), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    # Header banner
    draw.rectangle([0, 0, w, 75], fill="#1e293b")
    draw.text((30, 22), "[Thực hành] Tổng hợp so sánh 4 giá trị của thuộc tính flex-wrap", fill="#ffffff", font=font_title)

    cards = [
        ("1. flex-wrap: wrap", "Cho phép xuống dòng theo hướng bình thường (trên xuống dưới)", [
            (["Item 1", "Item 2", "Item 3"], "#bfdbfe", "#1e3a8a"),
            (["Item 4", "Item 5", "Item 6"], "#bfdbfe", "#1e3a8a"),
        ], "↓ Dòng mới xếp xuống dưới", 30, 95),

        ("2. flex-wrap: nowrap", "Không cho xuống dòng, tất cả co lại trên 1 dòng (Mặc định)", [
            (["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"], "#bbf7d0", "#14532d"),
        ], "→ 1 dòng duy nhất, các item co lại", 540, 95),

        ("3. flex-wrap: wrap-reverse", "Cho phép xuống dòng nhưng đảo hướng Cross Axis (dưới lên trên)", [
            (["Item 4", "Item 5", "Item 6"], "#fecaca", "#7f1d1d"),
            (["Item 1", "Item 2", "Item 3"], "#fecaca", "#7f1d1d"),
        ], "↑ Hướng dòng đảo ngược: 1-3 ở dưới, 4-6 ở trên", 30, 440),

        ("4. flex-wrap: initial", "Đặt thuộc tính về giá trị mặc định của CSS (nowrap)", [
            (["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"], "#fef08a", "#713f12"),
        ], "≡ Tương đương nowrap (không xuống dòng)", 540, 440)
    ]

    card_w, card_h = 480, 310

    for title, desc, rows, note, x, y in cards:
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=8, fill="#ffffff", outline="#cbd5e1", width=1)
        
        # Badge
        draw.rounded_rectangle([x + 16, y + 14, x + 240, y + 38], radius=4, fill="#1e293b")
        draw.text((x + 24, y + 17), title, fill="#ffffff", font=font_badge)

        draw.text((x + 16, y + 46), desc, fill="#475569", font=font_small)

        # Container box
        box_y = y + 75
        box_h = 170
        draw.rounded_rectangle([x + 16, box_y, x + card_w - 16, box_y + box_h], radius=6, fill="#f8fafc", outline="#94a3b8", width=1)

        # Draw rows
        r_y = box_y + 12
        for items_in_row, bg, fg in rows:
            cnt = len(items_in_row)
            item_w = (card_w - 32 - 20 - (cnt - 1) * 8) // cnt
            item_h = 60 if len(rows) == 2 else 70
            
            for i_idx, iname in enumerate(items_in_row):
                bx = x + 26 + i_idx * (item_w + 8)
                draw.rounded_rectangle([bx, r_y, bx + item_w, r_y + item_h], radius=4, fill=bg, outline="#cbd5e1", width=1)
                bbox = draw.textbbox((0, 0), iname, font=font_small)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                draw.text((bx + (item_w - tw) // 2, r_y + (item_h - th) // 2 - 1), iname, fill=fg, font=font_small)

            r_y += item_h + 10

        # Note at bottom of card
        draw.text((x + 16, y + card_h - 30), note, fill="#2563eb", font=font_small)

    # Footer note
    draw.text((w // 2 - 150, h - 35), "CSS Flexbox Practice • flex-wrap Property Complete Demo", fill="#94a3b8", font=font_small)

    img.save(out_path)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\css-flex-wrap"
    render_wrap_screenshot(os.path.join(base_dir, "screenshot_wrap.png"))
    render_nowrap_screenshot(os.path.join(base_dir, "screenshot_nowrap.png"))
    render_wrap_reverse_screenshot(os.path.join(base_dir, "screenshot_wrap_reverse.png"))
    render_combined_screenshot(os.path.join(base_dir, "tat_ca_gia_tri.png"))
