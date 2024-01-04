from docx import Document

document = Document()

heading1 = document.add_heading('Start of the doc!', 0)
heading1.alignment = 1

# heading2 = document.add_heading('Paragraph 1', level=1)
# heading2.alignment = 1


p = document.add_paragraph('Мама мыла раму!')
p.add_run(' New text').bold = True

document.save('word.docx')
