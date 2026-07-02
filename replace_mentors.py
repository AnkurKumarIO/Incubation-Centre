import re

with open('v3f_ventures_venture_foundation/mentors.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS
css_to_add = '''
  /* ── Card flip ── */
  .flip-card { perspective: 1000px; cursor: pointer; }
  .flip-inner {
    position: relative; width: 100%; height: 100%;
    transform-style: preserve-3d;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .flip-card:hover .flip-inner { transform: rotateY(180deg); }
  .flip-front, .flip-back {
    position: absolute; inset: 0;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    overflow: hidden;
    border-radius: 12px;
  }
  .flip-front { background: #fff; }
  .flip-back {
    background: #002754;
    transform: rotateY(180deg);
    display: flex; flex-direction: column; justify-content: center;
    padding: 2rem;
  }
</style>'''
content = content.replace('</style>', css_to_add)

# Update grid
content = content.replace('<div class="grid gap-5" id="mentor-list">', '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="mentor-list">')

# Regex to match each mentor card
# Current mentor card HTML structure:
# <div class="mentor-item card-hover bg-white border border-outline-variant p-6 flex flex-col md:flex-row gap-6 reveal" data-domains="ai deep-tech">
#   <div class="flex flex-col items-center md:items-start gap-3 md:w-56 shrink-0">
#     <div class="w-16 h-16 rounded-full bg-surface-container text-primary font-display font-extrabold text-xl flex items-center justify-center">AK</div>
#     <div class="text-center md:text-left">
#       <div class="font-display font-bold text-base text-primary leading-tight">Ajay Kamalvanshi</div>
#       <div class="text-on-surface-variant text-xs mt-0.5">AI Infrastructure, NVIDIA</div>
#     </div>
#     <div class="flex flex-wrap gap-1.5 justify-center md:justify-start"><span class="section-label bg-surface-container px-2 py-1 text-primary">GPU / HPC</span>...</div>
#   </div>
#   <div class="flex-1 flex flex-col gap-3">
#     <div class="flex items-center gap-3"><hr class="flex-1 border-outline-variant"/></div>
#     <p class="text-on-surface-variant text-sm leading-relaxed">Drives next-generation AI infrastructure at NVIDIA...</p>
#     <div class="flex gap-2 flex-wrap mt-1"><span class="font-mono text-xs text-on-surface-variant border border-outline-variant px-2 py-1">NVIDIA</span>...</div>
#   </div>
# </div>

pattern = re.compile(
    r'<div class="mentor-item [^"]+" data-domains="([^"]+)">\s*'
    r'<div class="[^"]+">\s*'
    r'<div class="[^"]+">(.*?)</div>\s*' # Initials
    r'<div class="[^"]+">\s*'
    r'<div class="[^"]+">(.*?)</div>\s*' # Name
    r'<div class="[^"]+">(.*?)</div>\s*' # Subtitle
    r'</div>\s*'
    r'<div class="[^"]+">(.*?)</div>\s*' # Tags front
    r'</div>\s*'
    r'<div class="[^"]+">\s*'
    r'<div class="[^"]+">.*?</div>\s*' # HR line
    r'<p class="[^"]+">(.*?)</p>\s*' # Bio
    r'<div class="[^"]+">(.*?)</div>\s*' # Tags back (mono)
    r'</div>\s*'
    r'</div>',
    re.DOTALL
)

def repl(m):
    domains = m.group(1)
    initials = m.group(2)
    name = m.group(3)
    subtitle = m.group(4)
    tags_front = m.group(5)
    bio = m.group(6)
    tags_back = m.group(7)
    
    # Clean tags_front outer div if it was captured
    if '<span' in tags_front:
        # Just extract all spans
        spans = re.findall(r'<span[^>]*>.*?</span>', tags_front)
        tags_front_clean = ''.join(spans)
    else:
        tags_front_clean = tags_front
        
    # fix tags back (convert to section-label style)
    spans_back = re.findall(r'<span[^>]*>(.*?)</span>', tags_back)
    tags_back_clean = ''.join([f'<span class="section-label bg-white/10 px-2 py-1 text-white/70">{t}</span>' for t in spans_back])

    return f'''<div class="mentor-item flip-card reveal" data-domains="{domains}" style="height:420px;">
        <div class="flip-inner">
          <div class="flip-front border border-outline-variant flex flex-col items-center text-center">
            <div class="pt-8 pb-4 w-full flex justify-center">
              <div class="w-40 h-40 rounded-xl border-4 border-surface-container bg-surface-container text-primary font-display font-extrabold text-5xl flex items-center justify-center">
                {initials}
              </div>
            </div>
            <div class="px-6 pb-6 flex flex-col items-center flex-1 w-full">
              <h3 class="font-display font-bold text-xl text-primary mb-1">{name}</h3>
              <p class="text-on-surface-variant text-sm mb-3">{subtitle}</p>
              <div class="flex flex-wrap justify-center gap-2 mt-auto">{tags_front_clean}</div>
            </div>
          </div>
          <div class="flip-back">
            <h3 class="font-display font-bold text-xl text-white mb-4">{name}</h3>
            <p class="text-white/80 text-sm leading-relaxed mb-6">{bio}</p>
            <div class="flex flex-wrap justify-center gap-2 mt-auto">{tags_back_clean}</div>
          </div>
        </div>
      </div>'''

new_content = pattern.sub(repl, content)

with open('v3f_ventures_venture_foundation/mentors.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
