from pdfjinja import PdfJinja
import get_date

# -*- start: globals -*-
date_sl = dict(dd_mm_yy=get_date.slash_date, hora=get_date.str_date)


# -*- end: globals -*-
def __mr_pod(mr_pod_location, l_d):
    multiriesgo = PdfJinja(mr_pod_location)
    pdfout = multiriesgo(date_sl)
    filename = ".\gen\Comprobante IMR {project}.pdf".format(project=l_d['project_name'])
    pdfout.write(open(filename, 'wb'))
    return


def __rcg_pod(rcg_pod_location, l_d):
    riesgocivil = PdfJinja(rcg_pod_location)
    pdfout2 = riesgocivil(date_sl)
    filename = ".\gen\Comprobante RCG {project}.pdf".format(project=l_d['project_name'])
    pdfout2.write(open(filename, 'wb'))
    return


def pods(mr_pod_location, rcg_pod_location, l_d):
    __mr_pod(mr_pod_location, l_d)
    __rcg_pod(rcg_pod_location, l_d)
    return
