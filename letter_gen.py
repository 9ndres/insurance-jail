from docxtpl import DocxTemplate


def multi_risk_gen(current_path, l_d, date):
    doc = DocxTemplate('./templates/letters/Carta INS Remision MR.docx')
    project = {'dd_mm_yy': date, 'project_name': l_d[0], 'project_code': l_d[1]}
    doc.render(project)
    doc.save(current_path + 'carta mr.docx')
    return


def civil_risk_gen(current_path, l_d, date):
    doc = DocxTemplate('./templates/letters/RCG Carta INS -Inclusión - RCG.docx')
    project = {'dd_mm_yy': date,
               'project_name': l_d[0],
               'project_code': l_d[1],
               'constm': l_d[2],
               'panel_quantity': l_d[3],
               'panel_brand': l_d[4],
               'panel_potency': l_d[5],
               'inverter_quantity': l_d[6],
               'inverter_brand': l_d[7]
               }
    doc.render(project)
    doc.save(current_path + 'carta rcg.docx')
    return
