from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw,ImageOps
import re

def doWithBoardingPass(name,flight,flightDate,fromP,toP):

	#img = Image.open('static/image/boardingpass/photo8jpg.jpg')
	
	
	# font = ImageFont.truetype(<font-file>, <font-size>)
	# font = ImageFont.truetype("georgia.ttf", 16)
	
	# # draw.text((x, y),"Sample Text",(r,g,b))
	# draw = ImageDraw.Draw(img)
	# draw.text((0,0),name,(0,0,0),font=font)
	# #draw.text((50, 50),"hellwo Text",(0,0,0),font=font)
	
	
	# img.save('static/image/boardingpass/sample-out.jpg')


	im=Image.open("static/image/boardingpass/photo8jpg.jpg")

	# f = ImageFont.truetype("georgia.ttf", 16)
	# txt=Image.new('L', (50,50))
	# d = ImageDraw.Draw(txt)
	# d.text( (0, 0), name,  font=f, fill=255)
	f20 = ImageFont.truetype("simhei.ttf", 16)
	f11 = ImageFont.truetype("simhei.ttf", 11)

	txtName=newWord(name,f20)
	txtFlight=newWord(flight,f11)
	txtFlightDate=newWord(flightDate,f11)
	txtFromP=newWord(fromP,f11)
	txtToP=newWord(toP,f11)


	wName=txtName.rotate(1,  expand=1)
	wFlight=txtFlight.rotate(-1,  expand=1)
	wFlightDate=txtFlightDate.rotate(-5,  expand=1)
	wFromP=txtFromP.rotate(-1,  expand=1)
	wToP=txtToP.rotate(-1,  expand=1)


	im.paste( ImageOps.colorize(wName, (0,0,0), (0,0,0)), (77,133),  wName)
	im.paste( ImageOps.colorize(wFlight, (0,0,0), (0,0,0)), (77,162),  wFlight)
	im.paste( ImageOps.colorize(wFlightDate, (0,0,0), (0,0,0)), (130,163),  wFlightDate)
	im.paste( ImageOps.colorize(wFromP, (0,0,0), (0,0,0)), (68,190),  wFromP)
	im.paste( ImageOps.colorize(wToP, (0,0,0), (0,0,0)), (235,205),  wToP)


	im.save('static/image/boardingpass/sample-out.jpg')


def doWithTrumpSign(page1,page2):

	im=Image.open("static/image/trump/trumpEdit.jpg")

	# f = ImageFont.truetype("georgia.ttf", 16)
	# txt=Image.new('L', (50,50))
	# d = ImageDraw.Draw(txt)
	# d.text( (0, 0), name,  font=f, fill=255)
	f20 = ImageFont.truetype("Lucida Bright Demibold.ttf", 20)
	#f11 = ImageFont.truetype("simhei.ttf", 20)
	print ('THE　LENGTH OF PAGE1 IS %s'%len(page1))
	length1=len(page1)
	length2=len(page2)
	positionPage1=(500,400)
	positionPage2=(860,430)
	anglePage1=-10
	anglePage2=-1
	
	if length1>20:
		huanhang(length1,page1,positionPage1,anglePage1,im)


	else:

		txtPage1=newWord(page1,f20)
		wPage1=txtPage1.rotate(-10,  expand=1)
		im.paste( ImageOps.colorize(wPage1, (0,0,0), (0,0,0)), (500,400),  wPage1)


	
	if length2>20:
		huanhang(length2,page2,positionPage2,anglePage2,im)
	else:
		txtPage2=newWord(page2,f11)
		wPage2=txtPage2.rotate(-1,  expand=1)
		im.paste( ImageOps.colorize(wPage2, (0,0,0), (0,0,0)), (860,430),  wPage2)		


	


	im.save('static/image/trump/sample-out.jpg')


def newWord(words,f):
	
	txt=Image.new('L', (500,500))
	d = ImageDraw.Draw(txt)
	d.text( (0, 0), words,  font=f, fill=255)
	

	return txt


def huanhang(length,page,position,angle,im):
	f20 = ImageFont.truetype("Lucida Bright Demibold", 20)
	lines=re.findall('.{20}',page)
	positionX,positionY=position
	
	words={}
	if length%20==0:			
		for num,line in enumerate(lines):
			words['txt'+str(num)]=newWord(line,f20)
			wPage=words['txt'+str(num)].rotate(angle,  expand=1)
			im.paste( ImageOps.colorize(wPage, (0,0,0), (0,0,0)), (positionX,positionY),  wPage)
			positionY+=30

	else:
		for num,line in enumerate(lines):
			words['txt'+str(num)]=newWord(line,f20)
			wPage=words['txt'+str(num)].rotate(angle,  expand=1)
			im.paste( ImageOps.colorize(wPage, (0,0,0), (0,0,0)), (positionX,positionY),  wPage)
			positionY+=30
		txt=newWord(page[-(length%20):],f20)
		wPage=txt.rotate(angle,  expand=1)
		im.paste( ImageOps.colorize(wPage, (0,0,0), (0,0,0)), (positionX,positionY),  wPage)


if __name__=="__main__":
	doWithBoardingPass('yoyoyo','fc103','30jun','Beijing','LA')