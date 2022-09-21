from docxtpl import DocxTemplate

doc = DocxTemplate('./templates/Carta INS Remision MR.docx')
project = {'dd_mm_yy': '11/11/1111', 'project_name': 'foobar', 'project_code': '1111'}
doc.render(project)
doc.save('new doc.docx')
