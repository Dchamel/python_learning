from docx import Document

document = Document()

document.add_heading('Hello World!', 0)

p = document.add_paragraph('Мама мыла раму')

document.save('word.docx')
