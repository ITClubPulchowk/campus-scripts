# Useful Commands For Lab/Report Submissions

## Contents
1) [Converting ppt/docx to pdf](www.link1) 
2) [Merging multiple pdf files](www.link2)
3) [Extracting from pdf](www.link3)
4) [Images to pdf conversion](www.link4)

---

## Convert ppt/docx into pdf

To convert documents into pdf formats for portability/compatibility with pdf 
readers, also to convert the class materials provided as powerpoint slides into pdf.

---

**Package required:** libreoffice

**Description:** 
This is just making use of command line features of a powerful software that
most linux users have installed by default for their general use. 

**Usage:**

```bash
 $ libreoffice --headless --invisible --convert-to pdf file1.odt
 $ libreoffice --headless --invisible --convert-to pdf *.pptx
```

Additionally, you can also use the GUI itself.

---

## Merging multiple PDFs

Unite small snippets of pages together for convenient printing (eg, cover pages, 
table of contents) and for merging hand-written photos with typed text.
 
---

**Package required:** pdfunite (linux)

**Description:** 

Merge PDFs quickly from the command line (wildcard characters allowed).

**Usage:**

```bash
$ pdfunite file1.pdf file2.pdf file3.pdf output.pdf
$ pdfunite *.pdf output.pdf
```

---

## To extract specific pages from a pdf

**Package required:** pdfseparate (linux)

**Description:** 

Command (below) extracts pages 2-4 from the pdf and 
gives three files of names `page-2.pdf`, `page-3.pdf` and `page-4.pdf`, 
each individual page in a separate file.

**Usage:**

```bash
 $ pdfseparate -f 2 -l 4 file1.pdf page-%d.pdf
```

---

## To convert images to pdf

**Package required:** img2pdf (pip3-python package)

**Description:** 

Convert images to pdf, install from your repository or as a python package using pip3.

**Usage:**

```bash
 $ img2pdf *.jpg -o output.pdf
```



