# -*- coding: utf-8 -*-
import get_date
from letter_gen import multi_risk_gen, civil_risk_gen
from pods_gen import pods
import form_filler
import batch_pdf
# -*- start: globals -*-
today = get_date.slash_date
path = './gen/'
pods_path = './templates/'
pod_mr = pods_path + 'pod mr.pdf'
pod_rcg = pods_path + 'pod rcg.pdf'
forms_path = './templates/'
rcg_form_path = forms_path + 'civil risk form template.pdf'
multi_risk_form_path = forms_path + 'multi risk form template.pdf'
# -*- end: globals -*-

# Functions that start with __ aren't meant to be called outside module
letter_data = {
    'project_name': input('Project Name: '),
    'project_code': input('Project Code: '),
    'constm': input('Construction Meters: '),
    'constt': input('Total Construction Meters: '),
    'panel_quantity' : input('Panel Quantity: '),
    'panel_brand': input('Panel Brand: '),
    'panel_potency': input('Panel Potency: '),
    'inverter_quantity' : input('Inverter Quantity: '),
    'inverter_brand' : input('Inverter Brand: '),
    'latitud': input('Latitude: '),
    'longitud': input('Length: '),
    'provincia': input('Province: '),
    'canton': input('Canton: '),
    'distrit': input('District: '),
    'full_location': input('Full Location: '),
    'number_floors': input('Number of Floors: '),
    'property': input('Property Number: '),
    'activity': input('Fire Activity: '),
    'flamables': input('Flamable Liquis/NA: '),
    'adjacent': input('Adjacent Properties: '),
    'credit': input('Credit:'),
    'observations': input('Observations: ')
}


multi_risk_gen(path, letter_data, today)
civil_risk_gen(path, letter_data, today)
pods(pod_mr, pod_rcg, letter_data)
form_filler.form_filler_both(rcg_form_path, multi_risk_form_path, letter_data)
# You should convert your files to pdf as the last step
batch_pdf.batch_convert(path)
