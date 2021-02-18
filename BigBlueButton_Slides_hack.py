import os
import urllib.request
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PyPDF2 import PdfFileMerger
from datetime import date,datetime
from urllib.error import URLError, HTTPError

def mergePdf():
	source_dir = os.getcwd()
	merger = PdfFileMerger()
	lecSlide='./output/'+str(date.today())+'.pdf'
	for item in os.listdir(source_dir):
		if item.endswith('pdf'):
			merger.append(item)
	merger.write(lecSlide)       
	merger.close()


url=input()
i=0
while True:
    i=i+1
    y=url+str(i)
    print(y)
    z='/Users/Abhishek Gunjan/Desktop/python code/'+str(i)+'.svg'
    try:
        urllib.request.urlretrieve(y,z)
        t=str(i)+'.svg'
        if i<10:
            pdf="0"+str(i)+".pdf"
        else:
            pdf=str(i)+'.pdf'
        drawing = svg2rlg(t)
        renderPDF.drawToFile(drawing, pdf)
        os.remove(z) 
    except HTTPError as e:
        print("No any further slides so i am merging")
        mergePdf()
        print("This python script is developed by Abhishek Gunjan")
        print("Thanks for using it. Your Merged pdf is ready to use.")
        break
    except URLError as e:
        print("url error")
        break
#    finally:
#        mergePdf()

i=0
while True:
    i=i+1
    if i<10:
        Delpdfstr='0'+str(i)+'.pdf'
    else:
        Delpdfstr=str(i)+'.pdf'
    try:
        os.remove(Delpdfstr)
        print("deleted pdf "+str(i)+".pdf")
    except FileNotFoundError as e:
        print("all deleted")
        break
