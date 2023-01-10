from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Table
from reportlab.lib.units import mm
from reportlab.lib import colors
from datetime import datetime,date
import os
def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')


def makeReceipt(arg):
    #content
    fileName = arg[0]+'.pdf'
    documentTitle = 'Receipt'
    title = 'Ijaz and Sons'
    subTitle1 = '19F Wazir Ali Center, Badami Bagh, Lahore'
    subTitle2 = '0320-4332820'
    subTitle3 = '0320-4816860'

    date = str(datetime.now().date())
    billno = arg[0]
    name = arg[1]
    biltyno = arg[2]
    data = arg[3]

    folderName = os.path.dirname(os.path.abspath(__file__))+'\Bills'
    pathName = os.path.join(folderName,fileName)
    image = 'logo-whitebg.jpg'


    pdf = canvas.Canvas(pathName)
    pdf.setTitle(documentTitle)

    #drawMyRuler(pdf)

    pdf.drawInlineImage(image, 10,730, width=100, height=100)

    #pdf.saveState()
    #pdf.drawInlineImage(image,100,100,800,800)
    #pdf.rotate(45)
    #pdf.restoreState()

    pdf.setFont('Times-Roman', 22)
    pdf.drawCentredString(250,780,title)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(240,760,subTitle1)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(240,740,subTitle2)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(240, 720, subTitle2)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(420,780, 'Bill No:')
    pdf.line(450,780, 550,780)
    pdf.drawString(450,781,billno)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(420,740, 'Date:')
    pdf.line(450,740, 550,740)
    pdf.drawString(450,741,date)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(80,700, 'Receipient:')
    pdf.line(120,700, 550,700)
    pdf.drawString(120,701,name)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(80,650, 'Bilty No:')
    pdf.line(120,650, 550,650)
    pdf.drawString(120,651,biltyno)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(80,600, 'Qty')
    pdf.line(120,600, 120, 150)

    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(200,600, 'Description')
    pdf.line(370,600, 370, 150)


    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(400,600, 'Rate')
    pdf.line(470,600, 470, 150)


    pdf.setFont('Times-Roman', 14)
    pdf.drawCentredString(500,600, 'Total')

    pdf.line(50,590, 550,590)

    pdf.drawString(400,100, "Final:")
    pdf.line(450,100,550,100)

    pdf.drawString(50,100, "Sign: ")
    pdf.line(100,100,200,100)



    #insert in Receipt
    wantedData = []

    for i in data:
        temp = []
        temp.append(i[3])
        temp.append(i[0]+' '+i[1])
        temp.append(i[2])
        temp.append(int(i[2])*int(i[3]))

        wantedData.append(temp)


    basex = 50
    basey = 570

    marginList= [80,250,100,0]
    count = 0
    pdf.setFont('Times-Roman', 14)
    for i in wantedData:
        for j in i:
            print(j)
            pdf.drawString(basex, basey, str(j))
            basex = basex+marginList[count]
            count+=1

        basey -= 40
        basex = 50
        count = 0

    final = 0
    for i in wantedData:
        final += i[3]

    pdf.drawString(450,101,str(final))

    print(wantedData)
    pdf.save()

"""
data = [['abd', '5', 200, '5'], ['abc', '5', 200, '1']]
arg = (str(201),"irsam",str(900),data)
makeReceipt(arg)
"""

























