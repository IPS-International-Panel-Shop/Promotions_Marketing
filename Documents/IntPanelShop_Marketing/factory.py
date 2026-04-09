import os

# Your specific Western Cape target list
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
    <title>High-Spec Auto Body Repairs in {suburb} | Int Panel Shop</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white font-sans">
    <div class="min-h-screen flex items-center justify-center p-6">
        <div class="max-w-4xl w-full bg-slate-800 border border-slate-700 rounded-3xl p-8 md:p-16 shadow-2xl">
            <header class="mb-8">
                <span class="text-blue-500 font-bold tracking-widest uppercase text-sm">Now Serving {suburb}</span>
                <h1 class="text-5xl font-black tracking-tighter mt-2">INT PANEL SHOP</h1>
            </header>
            
            <p class="text-2xl text-slate-300 leading-snug mb-10">
                Premium structural repairs and factory-grade spray painting for clients in <span class="text-white font-semibold">{area_name}</span>. 
                Experience workshop excellence with local convenience.
            </p>

            <div class="grid md:grid-cols-2 gap-6 mb-12 text-left">
                <div class="bg-slate-700/50 p-6 rounded-xl border border-slate-600">
                    <h3 class="font-bold text-blue-400">Major Structural</h3>
                    <p class="text-sm text-slate-400 font-medium">Chassis straightening and heavy collision repair using factory specs.</p>
                </div>
                <div class="bg-slate-700/50 p-6 rounded-xl border border-slate-600">
                    <h3 class="font-bold text-blue-400">Refinishing</h3>
                    <p class="text-sm text-slate-400 font-medium">Computerized color matching and premium clear-coat finishing.</p>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row gap-4">
                <a href="https://wa.me/27661180036" class="bg-blue-600 hover:bg-blue-500 text-center text-white px-10 py-5 rounded-xl font-black text-xl transition-all">
                    WhatsApp Quote
                </a>
                <a href="tel:+27210000000" class="border-2 border-slate-600 hover:bg-slate-700 text-center text-white px-10 py-5 rounded-xl font-bold text-xl transition-all">
                    Call Workshop
                </a>
            </div>
            
            <footer class="mt-12 pt-8 border-t border-slate-700 text-slate-500 text-sm">
                &copy; 2026 Int Panel Shop | Expert Automotive Refinishing for {area_name}
            </footer>
        </div>
    </div>
</body>
</html>
"""

if not os.path.exists("dist"): os.makedirs("dist")

for s in suburbs:
    filename = s.lower().replace(" ", "-")
    with open(f"dist/{filename}.html", "w", encoding="utf-8") as f:
        f.write(template.format(suburb=s, area_name=s))

print(f"✅ Factory Output: {len(suburbs)} pages generated in the 'dist' folder.")
