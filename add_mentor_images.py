import re

images_map = {
    "Anand Kamat": "https://v3foundation.in/wp-content/uploads/2026/05/1-3.png",
    "Swapna Gupta": "https://v3foundation.in/wp-content/uploads/2026/05/2-2.png",
    "Rohit Srivastava": "https://v3foundation.in/wp-content/uploads/2026/05/3-3.png",
    "Sandip Chintawar": "https://v3foundation.in/wp-content/uploads/2026/05/4.png",
    "Ajay Kamalvanshi": "https://v3foundation.in/wp-content/uploads/2026/05/5.png",
    "Parag Deoras": "https://v3foundation.in/wp-content/uploads/2026/05/6.png",
    "Pravin Kamble": "https://v3foundation.in/wp-content/uploads/2026/05/7.png",
    "Sharad Bairathi": "https://v3foundation.in/wp-content/uploads/2026/05/8.png",
    "Mihirr Sose": "https://v3foundation.in/wp-content/uploads/2026/05/9.png",
    "Naveen Kumar Gonga": "https://v3foundation.in/wp-content/uploads/2026/05/10.png",
    "Mithun Shrivastava": "https://v3foundation.in/wp-content/uploads/2026/05/11.png",
    "Sharad Heda": "https://v3foundation.in/wp-content/uploads/2026/05/12.png",
    "Shirish Purohit": "https://v3foundation.in/wp-content/uploads/2026/05/13.png"
}

with open('v3f_ventures_venture_foundation/mentors.html', 'r', encoding='utf-8') as f:
    content = f.read()

def repl(m):
    initials_block = m.group(1)
    name = m.group(2)
    
    if name in images_map:
        img_url = images_map[name]
        new_block = f'''<div class="w-40 h-40 rounded-xl border-4 border-surface-container overflow-hidden flex items-center justify-center">
                <img src="{img_url}" alt="{name}" class="w-full h-full object-cover object-top"/>
              </div>'''
    else:
        new_block = initials_block

    return f'<div class="pt-8 pb-4 w-full flex justify-center">\n              {new_block}\n            </div>\n            <div class="px-6 pb-6 flex flex-col items-center flex-1 w-full">\n              <h3 class="font-display font-bold text-xl text-primary mb-1">{name}</h3>'

pattern = re.compile(
    r'<div class="pt-8 pb-4 w-full flex justify-center">\s*(<div class="w-40 h-40 rounded-xl border-4 border-surface-container bg-surface-container[^>]+>.*?</div>)\s*</div>\s*<div class="px-6 pb-6 flex flex-col items-center flex-1 w-full">\s*<h3 class="font-display font-bold text-xl text-primary mb-1">([^<]+)</h3>',
    re.DOTALL
)

new_content = pattern.sub(repl, content)

with open('v3f_ventures_venture_foundation/mentors.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Done")
