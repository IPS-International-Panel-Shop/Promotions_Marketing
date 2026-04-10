import os
from datetime import datetime

# 1. THE ASSETS & SETTINGS
suburbs = [
    "Cape Town", "Goodwood", "Durbanville", "Milnerton", "Sunningdale", 
    "Table View", "Bellville", "Gardens", "Sea Point", "Green Point", 
    "Atlantic Seaboard", "Stellenbosch", "Hout Bay", "Fresnaye", "CBD", 
    "Tamboerskloof", "Kloofnek", "Camps Bay", "Parklands", "Paarl", 
    "Brackenfell", "Somerset West", "Panorama", "Canal Walk", "N1 City", 
    "Century City", "Blouberg", "Blauwberg", "Melkbostrand", "Bishops Court", 
    "Constantia", "Northern Suburbs", "Claremont"
]

services = ["Panelbeating", "Spray Painting", "Scratch & Dent Repair", "Buff and Polish", "Rust Repairs", "Write off Repairs", "Accident Damage"]
services_list_html = "".join([f'<div class="border border-white/10 p-8 rounded-2xl bg-white/5 hover:bg-white/10 transition-colors"><h4 class="text-2xl font-black uppercase tracking-tighter brand-font">{s}</h4></div>' for s in services])

# 2. THE HTML TEMPLATE
template = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert Auto Body Repair in {suburb} | International Panel Shop</title>
    <link rel="icon" type="image/png" href="assets/ipslogo.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.cdnfonts.com/css/avenir-lt-std" rel="stylesheet">
    <style>
        @font-face {{ font-family: 'Gasterol'; src: url('https://fonts.cdnfonts.com/s/76254/Gasterol-Regular.woff') format('woff'); }}
        h1, h2, h3, h4, .brand-font {{ font-family: 'Gasterol', sans-serif !important; }}
        body {{ font-family: 'Avenir LT Std', sans-serif !important; font-size: 1.25rem; }}
        .accent-text {{ color: #D5FF3F; }}
        .accent-bg {{ background-color: #D5FF3F; }}
    </style>
</head>
<body class="bg-black text-white antialiased">
    <nav class="sticky top-0 z-50 bg-black/95 backdrop-blur-md border-b border-white/10 p-5">
        <div class="max-w-7xl mx-auto flex justify-between items-center uppercase">
            <img src="assets/ipslogo.png" alt="IPS Logo" class="h-10 md:h-16">
            <a href="tel:+27218018007" class="accent-text font-black text-xl tracking-tighter brand-font">021 801 8007</a>
        </div>
    </nav>
    <main class="max-w-7xl mx-auto px-6 md:px-10 py-16">
        <div class="grid lg:grid-cols-12 gap-12 items-start mb-32">
            <div class="lg:col-span-8 space-y-8 text-left">
                <span class="inline-block px-4 py-1 accent-bg text-black font-black text-sm uppercase rounded-sm tracking-widest">Serving {suburb}</span>
                
                <h1 class="text-4xl md:text-6xl lg:text-[5rem] leading-[0.9] tracking-[-0.05em] uppercase brand-font font-black">
                    INTERNATIONAL<br><span class="accent-text font-black">PANEL SHOP</span>
                </h1>
                
                <div class="space-y-6 text-xl md:text-2xl text-slate-200 font-medium max-w-2xl leading-snug">
                    <p>Premium structural repairs and factory-grade spray painting for the <span class="text-white font-black uppercase tracking-tight">{suburb}</span> zone.</p>
                    <p class="border-l-8 border-[#D5FF3F] pl-6 italic text-lg md:text-xl text-slate-400">
                        <strong>Collection & Drop-off Available:</strong> Free within 15km. Standard Uber rates apply for return trips outside this radius.
                    </p>
                </div>
                
                <div class="flex flex-col sm:flex-row items-center gap-10 pt-4">
                    <a href="https://wa.me/27661180036" class="w-full sm:w-auto accent-bg text-black px-12 py-7 rounded-2xl font-black text-3xl text-center hover:scale-105 transition-all">WhatsApp Quote</a>
                    <img src="assets/google.webp" alt="4.8 Star Rated" class="h-28 hidden sm:block">
                </div>
            </div>
            
            <div class="lg:col-span-4 bg-[#111827]/80 border border-white/10 p-12 rounded-[2rem] lg:mt-10 shadow-2xl backdrop-blur-sm">
                <h3 class="text-4xl mb-8 accent-text uppercase italic tracking-tighter brand-font leading-none">DRIVE NOW<br>PAY LATER</h3>
                <p class="text-xl text-slate-300 mb-10 leading-relaxed font-bold italic uppercase">Specialized credit solutions via <strong>Mobicred</strong> and <strong>RCS</strong> through Payfast.</p>
                <div class="space-y-8"><img src="assets/mobicred.webp" alt="Mobicred" class="h-12 w-auto"><img src="assets/rcs.png" alt="RCS" class="h-12 w-auto"></div>
            </div>
        </div>

        <section class="mb-32">
            <h2 class="text-4xl md:text-6xl mb-16 uppercase italic tracking-[0.2em] accent-text brand-font">Specialized Services</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16 uppercase font-bold italic tracking-tighter">{services_list_html}</div>
            <div class="bg-white/5 border border-dashed border-[#D5FF3F]/30 p-10 rounded-3xl text-center">
                <h3 class="text-3xl mb-6 brand-font tracking-widest uppercase italic font-bold">Insurance Quotes Provided</h3>
                <a href="https://wa.me/27661180036" class="inline-block border-2 border-[#D5FF3F] text-[#D5FF3F] px-12 py-6 rounded-xl font-black text-2xl hover:accent-bg hover:text-black transition-all">GET QUOTE NOW</a>
            </div>
        </section>

        <section class="mb-32 text-center uppercase font-bold italic">
            <h2 class="text-4xl md:text-6xl mb-16 brand-font text-center font-black tracking-[0.2em]">Precision Workmanship</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
                <div class="group space-y-6 text-center"><img src="assets/audi-before.jpg" class="w-full rounded-2xl grayscale group-hover:grayscale-0 transition-all duration-500"><img src="assets/audi-after.jpg" class="w-full rounded-2xl border-4 border-[#D5FF3F]"><p class="text-lg uppercase tracking-widest opacity-60 font-black">Audi Refinishing</p></div>
                <div class="group space-y-6 text-center"><img src="assets/bmw-before.jpg" class="w-full rounded-2xl grayscale group-hover:grayscale-0 transition-all duration-500"><img src="assets/bmw-after.jpeg" class="w-full rounded-2xl border-4 border-[#D5FF3F]"><p class="text-lg uppercase tracking-widest opacity-60 font-black">BMW Structural</p></div>
                <div class="group space-y-6 text-center"><img src="assets/merc-before.jpg" class="w-full rounded-2xl grayscale group-hover:grayscale-0 transition-all duration-500"><img src="assets/merc after.jpg" class="w-full rounded-2xl border-4 border-[#D5FF3F]"><p class="text-lg uppercase tracking-widest opacity-60 font-black">Mercedes Refinishing</p></div>
            </div>
        </section>
    </main>
    <footer class="bg-black py-24 px-8 border-t border-white/10 text-center uppercase font-bold italic">
        <img src="assets/ipslogo.png" alt="IPS" class="h-16 mx-auto mb-12">
        <img src="assets/google.webp" alt="Google Reviews" class="h-32 mx-auto mb-12 text-center">
        <div class="space-y-4">
            <p class="text-2xl text-white font-black brand-font tracking-widest uppercase">7 Bloem Street, Townsend Estate, Goodwood</p>
            <p class="text-slate-500 text-lg italic uppercase tracking-widest font-medium tracking-tighter">International Panel Shop | Estd 2003</p>
            <p class="text-slate-700 text-sm mt-12 tracking-tighter font-normal">© 2026 Serving {suburb} and the Western Cape</p>
        </div>
    </footer>
</body>
</html>
"""

# 3. RUNNER & AI FILE GENERATION
if not os.path.exists("dist"): os.makedirs("dist")

for s in suburbs:
    page_name = s.lower().replace(" ", "-") + ".html"
    with open(f"dist/{page_name}", "w", encoding="utf-8") as f:
        f.write(template.format(suburb=s, services_list_html=services_list_html))

with open("dist/ai-agents.txt", "w") as a:
    a.write(f"IPS Details: 7 Bloem Street, Goodwood. Areas: {', '.join(suburbs)}. USP: Mobicred/RCS financing and vehicle collection.")

with open("dist/robots.txt", "w") as r:
    r.write("User-agent: *\\nAllow: /\\nSitemap: https://promo.intpanelshop.co.za/sitemap.xml")

today = datetime.now().strftime('%Y-%m-%d')
sitemap_urls = "".join([f'  <url>\\n    <loc>https://promo.intpanelshop.co.za/{s.lower().replace(" ", "-")}.html</loc>\\n    <lastmod>{today}</lastmod>\\n    <priority>0.8</priority>\\n  </url>\\n' for s in suburbs])
with open("dist/sitemap.xml", "w") as sm:
    sm.write(f'<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n{sitemap_urls}</urlset>')

print(f"✅ Factory Build Complete: Header Shrunk & AI files updated.")
