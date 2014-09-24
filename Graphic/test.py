data = [
	# Year   Month   Predicted   High   Low
	(2007, 12, 4.8, 5.0, 4.7),
	(2008, 1, 4.3, 4.4, 4.2)
]

from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100) 
s = String(50, 50, 'Hello, world!', textAnchor='middle')

d.add(s)
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file') 

pred = [row[2] for row in data]

#d.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
