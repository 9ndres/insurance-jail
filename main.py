from docxtpl import DocxTemplate
import batch_pdf
doc = DocxTemplate('./templates/letters/Carta INS Remision MR.docx')
project = {'dd_mm_yy': '11/11/1111', 'project_name': 'foobar', 'project_code': '1111'}
doc.render(project)
doc.save('./templates/letters/new doc.docx')

batch_pdf.batch_convert()
