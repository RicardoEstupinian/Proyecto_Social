#Este archivo permite renderizar los pdf

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_pdf(url_template, contexto={}):
	#renderizando un template a un pdf
	template = get_template(url_template)
	html = template.render(contexto)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),content_type="application/pdf")
	return None

