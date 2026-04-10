import os

suburbs = [
    "Cape Town", "Goodwood", "Durbanville", "Milnerton", "Sunningdale", 
    "Table View", "Bellville", "Gardens", "Sea Point", "Green Point", 
    "Atlantic Seaboard", "Stellenbosch", "Hout Bay", "Fresnaye", "CBD", 
    "Tamboerskloof", "Kloofnek", "Camps Bay", "Parklands", "Paarl", 
    "Brackenfell", "Somerset West", "Panorama", "Canal Walk", "N1 City", 
    "Century City", "Blouberg", "Blauwberg", "Melkbostrand", "Bishops Court", 
    "Constantia", "Northern Suburbs", "Claremont"
]

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert Auto Body Repair in {suburb} | International Panel Shop</title>
    
    <link rel="icon" type="image/png" href="assets/ipslogo.png">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.cdnfonts.com/css/avenir-lt-std" rel="stylesheet">
    
    <style>
        @font-face {{
            font-family: 'Gasterol';
            src: url('https://fonts.cdnfonts.com/s/76254/Gasterol-Regular.woff') format('woff');
        }}
        h1, h2, h3, .brand-font {{ font-family: 'Gasterol', sans-serif; }}
        body {{ font-family: 'Avenir LT Std', sans-serif; }}
        .accent-text {{ color: #D5FF3F; }}
        .accent-bg {{ background-color: #D5FF3F; }}
    </style>

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "AutoBodyShop",
      "name": "International Panel Shop - {suburb}",
      "image": "https://promo.intpanelshop.co.za/assets/ipslogo.png",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "140 Upper Canterbury St, Gardens",
        "addressLocality": "Cape Town",
        "postalCode": "8001",
        "addressCountry": "ZA"
      }},
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": -33.9319,
        "longitude": 18.4233
      }},
      "url": "https://promo.intpanelshop.co.za/{filename}",
      "telephone": "+27218018007",
      "priceRange": "$$"
    }}
    </script>
</head>
<body class="bg-[#000000] text-white">

    <nav class="p-6 border-b border-white/10 flex justify-between items-center max-w-7xl mx-auto">
        <img src="assets/ipslogo.png" alt="IPS Logo" class="h-12">
        <div class="hidden md:block text-sm font-bold tracking-widest uppercase accent-text">
            Estd 2003 | Quality Meets Affordability
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-6 py-12 md:py-20">
        <div class="grid lg:grid-cols-2 gap-16 items-center">
            
            <div>
                <span class="inline-block px-4 py-1 accent-bg text-black font-black text-xs uppercase mb-6 rounded">
                    Now Serving {suburb}
                </span>
                <h1 class="text-5xl md:text-7xl mb-6 leading-tight">INTERNATIONAL<br>PANEL SHOP</h1>
                <p class="text-xl text-slate-400 leading-relaxed mb-8">
                    Premium structural repairs and factory-grade spray painting for high-spec vehicles in <span class="text-white font-bold">{suburb}</span>.
                </p>
                
                <div class="flex flex-wrap gap-4">
                    <a href="https://wa.me/27661180036" class="accent-bg text-black px-10 py-5 rounded-full font-black text-xl hover:scale-105 transition-transform">
                        WhatsApp for Quote
                    </a>
                    <a href="tel:+27218018007" class="border-2 border-white/20 hover:bg-white/10 px-10 py-5 rounded-full font-bold text-xl transition-all">
                        Call Workshop
                    </a>
                </div>
            </div>

            <div class="bg-slate-900 border border-white/10 p-8 rounded-3xl">
                <h3 class="text-2xl mb-4 accent-text uppercase italic">Drive Now, Pay Later</h3>
                <p class="text-slate-400 mb-6">We are the only shop in the region offering flexible credit through Mobicred and RCS via PayFast.</p>
                <div class="flex items-center gap-6 opacity-80">
                    <img src="https://mobicred.co.za/images/logo.png" alt="Mobicred" class="h-8 filter brightness-200">
                    <img src="https://www.payfast.co.za/assets/images/logo.svg" alt="PayFast" class="h-6 filter brightness-200">
                </div>
            </div>
        </div>

        <section class="mt-24">
            <h2 class="text-3xl mb-12 uppercase text-center tracking-widest">Mastering the Finish</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="space-y-4">
                    <div class="rounded-2xl overflow-hidden border border-white/5"><img src="assets/audi-before.jpg" class="w-full"></div>
                    <div class="rounded-2xl overflow-hidden border border-white/5 accent-bg p-1"><img src="assets/audi-after.jpg" class="w-full rounded-xl"></div>
                </div>
                <div class="space-y-4">
                    <div class="rounded-2xl overflow-hidden border border-white/5"><img src="assets/bmw-before.jpg" class="w-full"></div>
                    <div class="rounded-2xl overflow-hidden border border-white/5 accent-bg p-1"><img src="assets/bmw-after.jpeg" class="w-full rounded-xl"></div>
                </div>
                <div class="space-y-4">
                    <div class="rounded-2xl overflow-hidden border border-white/5"><img src="assets/merc-before.jpg" class="w-full"></div>
                    <div class="rounded-2xl overflow-hidden border border-white/5 accent-bg p-1"><img src="assets/merc-after.jpg" class="w-full rounded-xl"></div>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-white/5 border-t border-white/10 p-12 mt-20">
        <div class="max-w-7xl mx-auto text-center">
            <img src="assets/ipslogo.png" alt="IPS" class="h-8 mx-auto mb-6">
            <p class="text-slate-500 text-sm italic">140 Upper Canterbury St, Gardens, Cape Town</p>
            <p class="mt-4 text-xs tracking-widest text-slate-600 uppercase">Expert Automotive Refinishing for {suburb} & Surroundings</p>
        </div>
    </footer>

</body>
</html>
"""

if not os.path.exists("dist"): os.makedirs("dist")

for s in suburbs:
    filename = s.lower().replace(" ", "-") + ".html"
    with open(f"dist/{filename}", "w", encoding="utf-8") as f:
        f.write(template.format(suburb=s, filename=filename))

# Create robots.txt to specifically call to AI and Search Bots
with open("dist/robots.txt", "w") as r:
    r.write("User-agent: *\\nAllow: /\\n\\nSitemap: https://promo.intpanelshop.co.za/sitemap.xml")

print(f"✅ Factory Output: {len(suburbs)} pages generated with Brand Guidelines.")
