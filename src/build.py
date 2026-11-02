import subprocess,os
os.makedirs('../admin',exist_ok=True)
logo=open(os.environ.get('LOGO_TXT','/workspace/est/logo.txt')).read().strip()
content=''.join(open(f'm{i}.js').read() for i in range(1,13))+'\nconst MODS=[M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12];\n'
import time
BUILD=time.strftime('%Y%m%d%H%M%S')
t=open('template.html').read().replace('__LOGO__',logo).replace('__CONTENT__',content).replace('__ENGINE__','window.__COURSE_BUILD__="'+BUILD+'";\n'+open('engine.js').read())
open('../index.html','w').write(t);print(len(t))
meta=subprocess.check_output(['node','meta.js']).decode().strip()
a=open('admin.html').read().replace('__LOGO__',logo).replace('__META__',meta)
open('../admin/index.html','w').write(a);print(len(a))
open('../course-meta.json','w').write(meta+'\n')
