# -*- coding: utf-8 -*-
import get_date
from letter_gen import multi_risk_gen, civil_risk_gen
from pdfjinja import PdfJinja
from pods_gen import pods
import form_filler
import batch_pdf
# -*- start: globals -*-
today = get_date.slash_date
path = './gen/'
pods_path = './pods/'
pod_mr = pods_path + 'pod mr.pdf'
pod_rcg = pods_path + 'pod rcg.pdf'
forms_path = './forms/'
rcg_form_path = forms_path + 'civil risk form template.pdf'
multi_risk_form_path = forms_path + 'multi risk form template.pdf'
# -*- end: globals -*-


letter_data = {
    'project_name': input('Project name: '),
    'project_code': input('Project code: '),
    'constm': input('Construction meters: '),
    'panel_quantity' : input('Panel quantity: '),
    'panel_brand': input('Panel brand: '),
    'panel_potency': input('Panel potency: '),
    'inverter_quantity' : input('Inverter quantity: '),
    'inverter_brand' : input('Inverter brand: '),
    'latitud': input('latitud: '),
    'longitud': input('longitud: '),
    'provincia': input('Province: '),
    'canton': input('Canton: '),
    'distrit': input('Distrit: '),
    'full_location': input('Full location: '),
    'number_floors': input('Number of floors: '),
    'property': input('Property number: '),
    'activity': input('Fire activity: '),
    'flamables': input('Flamable liquis/NA: '),
    'adjacent': input('Adjacent properties: '),
    'credit': input('Credit:'),
    'observations': input('Observations: '),
    'constt': input('Total construction meters: ')
}


multi_risk_gen(path, letter_data, today)
civil_risk_gen(path, letter_data, today)
pods(pod_mr, pod_rcg)
form_filler.form_filler_both(rcg_form_path, multi_risk_form_path, letter_data)
# You should convert your files to pdf as the last step
batch_pdf.batch_convert(path)
