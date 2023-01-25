from pdfjinja import PdfJinja
from get_date import slash_date, str_date, day, month, year


def __multi_risk_filler(multi_risk_path, l_d):
    output = PdfJinja(multi_risk_path)
    pdfout = output(dict(
        dd=day,
        mm=month,
        yy=year,
        hora=str_date,
        latitud=l_d['latitud'],
        longitud=l_d['longitud'],
        pais='COSTA RICA',
        distrito=l_d['distrit'],
        canton=l_d['canton'],
        provincia=l_d['provincia'],
        full_location=l_d['full_location'],
        finca=l_d['property'],
        constm=l_d['constm'],
        actividad=l_d['activity'],
        inflamables=l_d['flamables'],
        colindantes=l_d['adjacent'],
        acreencia=l_d['credit'],
        observaciones=l_d['observations'],
        dd_mm_yy=slash_date,
        cantidad_pisos=l_d['number_floors'],
        corner_f=True
    ))
    pdfout.write(open('.\gen\Formulario MRM {project}.pdf'.format(project=l_d['project_name']), 'wb'))
    return


def __civil_risk_filler(civil_risk_path, l_d):
    output2 = PdfJinja(civil_risk_path)
    pdfout2 = output2(dict(
        distrito=l_d['distrit'],
        canton=l_d['canton'],
        provincia=l_d['provincia'],
        full_location=l_d['full_location'],
        constm=l_d['constm'],
        actividad=l_d['activity'],
        dd_mm_yy=slash_date,
        cantidad_pisos=l_d['number_floors'],
        constt=l_d['constt']
    ))
    pdfout2.write(open('.\gen\Formulario RCG {project}.pdf'.format(project=l_d['project_name']), 'wb'))
    return


def form_filler_both(civil_risk_path, multi_risk_path, l_d):
    __civil_risk_filler(civil_risk_path, l_d)
    __multi_risk_filler(multi_risk_path, l_d)
    return
