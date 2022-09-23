# -*- coding: utf-8 -*-
import os
from docxtpl import DocxTemplate
from pdfjinja import PdfJinja
from datetime import date
import batch_pdf

doc = DocxTemplate('./templates/letters/Carta INS Remision MR.docx')
project = {'dd_mm_yy': '11/11/1111', 'project_name': 'foobar', 'project_code': '1111'}
doc.render(project)
doc.save('./templates/letters/new doc.docx')

# batch_pdf.batch_convert()
current_date = date.today()
slash_date = current_date.strftime("%d/%m/%Y")
date_sl = dict(date_s=slash_date)


def voucher_gen():
    multiriesgo = PdfJinja('./templates/comprobante de entrega MR.pdf')
    pdfout = multiriesgo(date_sl)
    pdfout.write(open('comprobante multiriesgo.pdf', 'wb'))
    riesgocivil = PdfJinja('./templates/comprobante de entrega RCG.pdf')
    pdfout2 = riesgocivil(date_sl)
    pdfout2.write(open('comprobante rcg.pdf', 'wb'))


return
