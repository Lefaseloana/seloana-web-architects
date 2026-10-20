from pathlib import Path
import re,json
p=Path('dist/index.html');s=p.read_text()
s=s.replace('Good ideas.<br>Thoughtfully<br><em>built.</em>','Ideas into<br>experiences.<br><em>Beautifully.</em>')
s=s.replace('I turn ambitious ideas into purposeful digital experiences. Beautiful on the surface. Considered in every detail.','I’m Lefa Seloana. I bring mathematical thinking, creative detail and hands-on development to the web — building things you can actually use.')
s=s.replace('Independent digital craft · South Africa','Seloana Web Architects · South Africa')
s=s.replace('Human-centred design.<br>Analytical foundations.','Six working applications.<br>One curious problem-solver.')
s=s.replace('<a href="#services">Expertise</a>','<a href="#services">Expertise</a><a href="https://github.com/Lefaseloana" target="_blank" rel="noopener noreferrer">GitHub ↗</a>')
s=s.replace('A selection of academic and web projects exploring how technology can solve everyday problems.','Six interactive applications. Open a demo, test the details, and explore the source. Built to show how I think — and how I build.')
s=s.replace('Ideas made tangible.','Don’t just read.<br><em>Try the work.</em>')
start=s.index('<article class="featured">');end=s.index('</div></div></section>',start)
old=s[start:end]
# Preserve the academic project as a separate research feature beneath the six projects.
academic=old[:old.index('<div class="projects">')]
projects=json.loads(Path('scripts/projects.json').read_text())
info={
'flowboard':('01','From to-do<br>to done.','Productivity','A local-first task board with priority filters, search, stage changes and portable JSON exports.','The challenge: keep a small workflow understandable without a complex account setup.','The implementation: explicit task state, safe text rendering, native controls and browser persistence.','The next step: user accounts, permissions and shared team workspaces.'),
'data-lens':('02','Your data.<br>A clearer story.','Data','Drop in a CSV to explore means, medians, value distributions and a searchable-by-column data view.','The challenge: make a raw spreadsheet understandable without sending it to a server.','The implementation: quoted-field parsing, numeric validation, descriptive statistics and browser-rendered charts.','The next step: streaming larger datasets and richer chart controls.'),
'route-lab':('03','Make the<br>invisible visible.','Algorithms','Draw obstacles and watch BFS and DFS search for a route. Compare exploration and path length.','The challenge: explain the difference between finding a route and finding a shortest route.','The implementation: graph traversal, parent reconstruction, cancellable animation and keyboard-operable cells.','The next step: weighted terrain and Dijkstra’s algorithm.'),
'contrast-studio':('04','Designed to<br>be readable.','Design tools','Live colour previews, contrast measurements, AA / AAA checks and ready-to-use CSS tokens.','The challenge: give visual colour decisions a measurable readability check.','The implementation: sRGB luminance calculations, contrast thresholds and downloadable CSS variables.','The next step: multi-colour palette checks and automated page audits.'),
'focus-studio':('05','Less distraction.<br>More intention.','Productivity','A focus timer with pause/resume, completion history and downloadable session records.','The challenge: keep a session clock accurate when browser callbacks are delayed.','The implementation: wall-clock deadlines, explicit timer states and locally stored completed sessions.','The next step: optional notifications and cross-device history.'),
'slotwise':('06','A little order.<br>A lot of clarity.','Productivity','A personal appointment planner with collision detection, date filters and calendar-file export.','The challenge: prevent overlapping appointments while keeping planning lightweight.','The implementation: interval comparison, date and time validation, and escaped iCalendar exports.','The next step: time-zone-aware scheduling and shared availability.')}
visuals={
'flowboard':'<div class="mini-board">'+''.join('<div><span>'+label+'</span>'+''.join('<i style="width:'+str(w)+'%"></i>' for w in widths)+'</div>' for label,widths in [('TO DO',[90,65,80]),('BUILDING',[80,55]),('SHIPPED',[90,70,85])])+'</div>',
'data-lens':'<div class="mini-data"><div><span>VISITORS / SAMPLE DATA</span><strong>2,810 <small>↗</small></strong></div><div class="mini-chart">'+''.join('<i style="height:'+str(v)+'%"></i>' for v in [30,47,40,60,73,91])+'</div></div>',
'route-lab':'<div class="mini-grid">'+''.join('<i class="'+('route' if n in [16,17,18,19,31,43,55,56,57,58,70,82] else 'wall' if n in [22,34,46,50,62,74,75,76] else '')+'"></i>' for n in range(96))+'</div>',
'contrast-studio':'<div class="mini-type"><span>Aa</span><div><strong>READABILITY, BY DESIGN.</strong><small>Forest ink / warm lime</small><b>AA ✓ &nbsp; AAA ✓</b></div></div>',
'focus-studio':'<div class="mini-clock"><span>IN THE ZONE</span><strong>25:00</strong><small>One thing at a time.</small></div>',
'slotwise':'<div class="mini-calendar"><div>09:00 <span>Discovery call</span></div><div>10:00 <span>Design review</span></div><div>11:00 <span>Build something good.</span></div></div>'}
cards=''
for slug,name,cat,desc,skills,limit in projects:
 number,title,category,copy,challenge,implementation,nextstep=info[slug]
 if slug=='data-lens':copy='Drop in a CSV to explore means, medians, value distributions and a column-by-column statistical view.'
 cards+=f'''<article class="lab-card reveal" data-category="{category}"><a class="project-art {slug}" href="projects/{slug}/index.html" aria-label="Open {name}"><div class="art-top"><span>SW/A — LAB {number}</span><span>INTERACTIVE ↗</span></div><h3>{title}</h3>{visuals[slug]}<span class="art-caption">{name.upper()} / WORKING BROWSER APPLICATION</span></a><div class="lab-copy"><div class="lab-meta"><span>{category}</span><span>0{int(number)} / 06</span></div><h3>{name}</h3><p>{copy}</p><div class="project-links"><a class="btn" href="projects/{slug}/index.html">Launch project ↗</a><a class="textlink" href="source/{slug}.zip" download>Source ↓</a></div><details><summary>Behind the build</summary><p>{challenge}</p><p>{implementation}</p><p>{limit}</p><p>{nextstep}</p></details></div></article>'''
new='''<div class="filterbar" role="group" aria-label="Filter projects"><button class="filter active" aria-pressed="true" data-filter="All">All projects <span>06</span></button><button class="filter" aria-pressed="false" data-filter="Productivity">Productivity</button><button class="filter" aria-pressed="false" data-filter="Data">Data</button><button class="filter" aria-pressed="false" data-filter="Algorithms">Algorithms</button><button class="filter" aria-pressed="false" data-filter="Design tools">Design tools</button></div><div class="lab-grid">'''+cards+'''</div><p id="filter-status" class="sr-only" aria-live="polite"></p><div class="academic-heading"><span class="eyebrow">Beyond the browser / Academic work</span><h2>Technology with<br>a human purpose.</h2></div>'''+academic
s=s[:start]+new+s[end:]
# The replaced segment included a closing wrapper for the old pair of cards.
s=s.replace('</article></div></div></section>\n<section id="services"','</article></div></section>\n<section id="services"')
s=s.replace('I enjoy the space where structured problem-solving meets thoughtful design. My work spans business websites, digital product concepts and an AI-focused final-year project in student success.','I enjoy the space where structured problem-solving meets thoughtful design. This portfolio brings that approach to life through six browser applications, business website work and an AI-focused final-year project in student success.')
s=s.replace('<a class="textlink" href="https://wa.me/27797837388"','<div class="contact-links"><a class="textlink" href="mailto:lefaseloana16@gmail.com">lefaseloana16@gmail.com ↗</a><br><a class="textlink" href="https://wa.me/27797837388"')
s=s.replace('Chat with Lefa on WhatsApp ↗</a></div>','Chat with Lefa on WhatsApp ↗</a></div></div>')
s=s.replace('<span>© <span id="year">','<span>© <span id="year">')
s=s.replace('<a href="#main">Back to top ↑</a>','<a href="source/seloana-web-architects.zip" download>Full source ↓</a><a href="https://github.com/Lefaseloana" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="#main">Back to top ↑</a>')
s=s.replace('</head>','<link rel="stylesheet" href="experience.css"></head>')
s=s.replace('<body>','<body><div class="reading-progress" aria-hidden="true"></div>')
s=s.replace('</body>','<script src="experience.js" defer></script></body>')
p.write_text(s)
