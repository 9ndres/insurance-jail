from docxtpl import DocxTemplate
# https://pypi.org/project/docxtpl/

def multi_risk_gen(current_path, l_d, date):
    path_multi_risk = '.\\templates\carta mr.docx'
    doc = DocxTemplate(path_multi_risk)
    project = {'dd_mm_yy': date,
                'project_name': l_d['project_name'], 
                'project_code': l_d['project_code']}
    doc.render(project)
    doc.save(current_path + 'Carta de Inclusión {project}.docx'.format(project=l_d['project_name']))
    return


def civil_risk_gen(current_path, l_d, date):
    path_civil_risk = '.\\templates\carta rcg.docx'
    doc = DocxTemplate(path_civil_risk)
    project = {'dd_mm_yy': date,
               'project_name': l_d['project_name'],
               'project_code': l_d['project_code'],
               'constm': l_d['constm'],
               'panel_quantity': l_d['panel_quantity'],
               'panel_brand': l_d['panel_brand'],
               'panel_potency': l_d['panel_potency'],
               'inverter_quantity': l_d['inverter_quantity'],
               'inverter_brand': l_d['inverter_brand'],
               'constt': l_d['constt']
               }
    doc.render(project)
    doc.save(current_path + 'Carta de Inclusión RCG {project}.docx'.format(project=l_d['project_name']))
    return
