"""
    A script to sort downloaded files

    What it does:
    - moves .jpg, .png and .gif files from Downloads to Pictures/Downloads
    - moves pdfs from Downloads to Documents/PDFs
    - moves .docx files from Downloads to Documents/docs
    - moves .exe and .msi files from Downloads to Downloads/Installers
    - moves .mp4 files from Downloads to Videos 
"""
import os, shutil

home = os.environ['USERPROFILE']
# home = os.environ['HOME']
images, pdfs, docs, installers, vids =[], [], [], [], []

for file in os.listdir(f"{home}/Downloads"):
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.gif'):
        images.append(file)
    if file.endswith('.pdf'):
        pdfs.append(file)
    if file.endswith('.docx'):
        docs.append(file)
    if file.endswith('.exe') or file.endswith('.msi'):
        installers.append(file)
    if file.endswith('.mp4'):
        vids.append(file)

dl_pic, dl_pdf, dl_doc, dl_inst, dl_vids = f"{home}/Pictures/Downloads", f"{home}/Documents/PDFs", f"{home}/Documents/Docs", f"{home}/Downloads/Installers", f"{home}/Videos"

if not os.path.exists(dl_pic):
    os.mkdir(dl_pic)
if not os.path.exists(dl_pdf):
    os.mkdir(dl_pdf)
if not os.path.exists(dl_doc):
    os.mkdir(dl_doc)
if not os.path.exists(dl_inst):
    os.mkdir(dl_inst)
if not os.path.exists(dl_vids):
    os.mkdir(dl_vids)

for file in images:
    shutil.move(f"{home}/Downloads/{file}", f"{dl_pic}/{file}")
for file in pdfs:
    shutil.move(f"{home}/Downloads/{file}", f"{dl_pdf}/{file}")
for file in docs:
    shutil.move(f"{home}/Downloads/{file}", f"{dl_doc}/{file}")
for file in installers:
    shutil.move(f"{home}/Downloads/{file}", f"{dl_inst}/{file}")
for file in vids:
    shutil.move(f"{home}/Downloads/{file}", f"{dl_vids}/{file}")

# Move Screenshots
images = [i for i in os.listdir(f"{home}/Documents") if i.endswith('.png') or i.endswith('.jpg')]
if not os.path.exists(f"{home}/Pictures/Screenshots"):
    os.mkdir(f"{home}/Pictures/Screenshots")
for file in images:
    shutil.move(f"{home}/Documents/{file}", f"{home}/Pictures/Screenshots/{file}")
