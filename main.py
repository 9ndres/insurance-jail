# -*- coding: utf-8 -*-
import get_date
from letter_gen import multi_risk_gen, civil_risk_gen
from pdfjinja import PdfJinja
import batch_pdf

# -*- start: globals -*-
today = get_date.slash_date
path = './Deadline/Atesa/'
date_sl = dict(date_s=get_date.str_date())
# -*- end: globals -*-


letter_data = [
    input('Project name: '),
    input('Project code: '),
    input('Construction meters: '),
    input('Panel quantity:'),
    input('Panel brand: '),
    input('Panel potency: '),
    input('Inverter quantity: '),
    input('Inverter brand: ')
]


def voucher_gen():
    multiriesgo = PdfJinja('./templates/comprobante de entrega MR.pdf')
    pdfout = multiriesgo(date_sl)
    pdfout.write(open('comprobante multiriesgo.pdf', 'wb'))
    riesgocivil = PdfJinja('./templates/comprobante de entrega RCG.pdf')
    pdfout2 = riesgocivil(date_sl)
    pdfout2.write(open('comprobante rcg.pdf', 'wb'))
    return


multi_risk_gen(path, letter_data, today)
civil_risk_gen(path, letter_data, today)

# You should convert your files to pdf as the last step
batch_pdf.batch_convert(path)
