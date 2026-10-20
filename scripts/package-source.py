from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
root=Path('dist/source');root.mkdir(exist_ok=True)
for folder in Path('dist/projects').iterdir():
 if folder.is_dir():
  with ZipFile(root/(folder.name+'.zip'),'w',ZIP_DEFLATED) as z:
   for f in folder.rglob('*'):
    if f.is_file():
     if f.name=='index.html':
      html=f.read_text().replace('../../index.html#work','https://lefa-seloana-portfolio.pinesfaizo.chatgpt.site/#work').replace('../../source/','https://lefa-seloana-portfolio.pinesfaizo.chatgpt.site/source/')
      z.writestr('index.html',html)
     else:z.write(f,f.relative_to(folder))
with ZipFile(root/'seloana-web-architects.zip','w',ZIP_DEFLATED) as z:
 for name in ['dist','scripts','tests','.github','README.md','package.json','netlify.toml','.gitignore']:
  p=Path(name)
  for f in ([p] if p.is_file() else p.rglob('*')):
   if f.is_file() and f!=root/'seloana-web-architects.zip':z.write(f,f)
print('Packaged six projects and complete portfolio source.')
