from pdfjinja import PdfJinja
import get_date

# -*- start: globals -*-
date_sl = dict(dd_mm_yy=get_date.slash_date, hora=get_date.str_date)
# -*- end: globals -*-

def __rcg_pod(rcg_letter_path):
    riesgocivil = PdfJinja(rcg_letter_path)
    pdfout2 = riesgocivil(date_sl)
    pdfout2.write(open('pod rcg.pdf', 'wb'))
    return
def __mr_pod(mr_letter_path):
    multiriesgo = PdfJinja(mr_letter_path)
    pdfout = multiriesgo(date_sl)
    pdfout.write(open('pod mr.pdf', 'wb'))
    return

def pods(mr_letter_path, rcg_letter_path):
    __mr_pod(mr_letter_path)
    __rcg_pod(rcg_letter_path)
    return