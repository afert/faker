from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw,ImageOps

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
	f16 = ImageFont.truetype("simhei.ttf", 16)
	f11 = ImageFont.truetype("simhei.ttf", 11)

	txtName=newWord(name,f16)
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
	f16 = ImageFont.truetype("simhei.ttf", 16)
	f11 = ImageFont.truetype("simhei.ttf", 11)

	txtPage1=newWord(page1,f16)
	txtPage2=newWord(page2,f11)



	wPage1=txtPage1.rotate(1,  expand=1)
	wPage2=txtPage2.rotate(-1,  expand=1)



	im.paste( ImageOps.colorize(wPage1, (0,0,0), (0,0,0)), (77,133),  wPage1)
	im.paste( ImageOps.colorize(wPage2, (0,0,0), (0,0,0)), (77,162),  wPage2)

	im.save('static/image/trump/sample-out.jpg')


def newWord(words,f):
	
	txt=Image.new('L', (100,200))
	d = ImageDraw.Draw(txt)
	d.text( (0, 0), words,  font=f, fill=255)
	

	return txt





if __name__=="__main__":
	doWithBoardingPass('yoyoyo','fc103','30jun','Beijing','LA')