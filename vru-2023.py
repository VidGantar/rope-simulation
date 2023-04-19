import pygame as pg
from math import sqrt
from random import shuffle,randint
import tkinter as tk

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (0,0,0)

Gfont = 'Geometr212 BkCn BT',10

def za_slike():

	a = Pika(400,90,False)
	vse_pike.append(a)
	all_sprites.add(a)

	b = Pika(500,120,True)
	vse_pike.append(b)
	all_sprites.add(b)

	l1 = Palcka(b,a)
	all_sprites.add(l1)
	vse_palcke.append(l1)


def nihalo1():
	nihalo1_gumb.configure(state=tk.DISABLED)

	a = Pika(400,90,False)
	vse_pike.append(a)
	all_sprites.add(a)

	b = Pika(600,90,True)
	vse_pike.append(b)
	all_sprites.add(b)

	l1 = Palcka(b,a)
	all_sprites.add(l1)
	vse_palcke.append(l1)

def nihalo2():
	nihalo2_gumb.configure(state=tk.DISABLED)

	a = Pika(400,90,False)
	vse_pike.append(a)
	all_sprites.add(a)

	b = Pika(600,90,True)
	vse_pike.append(b)
	all_sprites.add(b)

	l1 = Palcka(b,a)
	all_sprites.add(l1)
	vse_palcke.append(l1)

	c = Pika(630,70,True)
	vse_pike.append(c)
	all_sprites.add(c)

	d = Pika(630,110,True)
	vse_pike.append(d)
	all_sprites.add(d)

	l2 = Palcka(b,c)
	all_sprites.add(l2)
	vse_palcke.append(l2)

	l3 = Palcka(b,d)
	all_sprites.add(l3)
	vse_palcke.append(l3)

	l4 = Palcka(c,d)
	all_sprites.add(l4)
	vse_palcke.append(l4)

	e = Pika(660,90,True)
	vse_pike.append(e)
	all_sprites.add(e)

	l5 = Palcka(e,d)
	all_sprites.add(l5)
	vse_palcke.append(l5)

	l6 = Palcka(c,e)
	all_sprites.add(l6)
	vse_palcke.append(l6)


def vrv1():
	vrv1_gumb.configure(state=tk.DISABLED)

	a = Pika(280,90,False)
	vse_pike.append(a)
	all_sprites.add(a)

	b = Pika(320,90,True)
	vse_pike.append(b)
	all_sprites.add(b)

	l1 = Palcka(b,a)
	all_sprites.add(l1)
	vse_palcke.append(l1)

	c = Pika(390,110,True)
	vse_pike.append(c)
	all_sprites.add(c)

	l2 = Palcka(b,c)
	all_sprites.add(l2)
	vse_palcke.append(l2)

	d = Pika(460,140,False)
	vse_pike.append(d)
	all_sprites.add(d)

	l3 = Palcka(d,c)
	all_sprites.add(l3)
	vse_palcke.append(l3)


	d = Pika(460,140,False)
	vse_pike.append(d)
	all_sprites.add(d)

	l3 = Palcka(d,c)
	all_sprites.add(l3)
	vse_palcke.append(l3)

	a2 = Pika(330,110,True)
	vse_pike.append(a2)
	all_sprites.add(a2)

	l22 = Palcka(b,a2)
	all_sprites.add(l22)
	vse_palcke.append(l22)

	b2= Pika(370,130,True)
	vse_pike.append(b2)
	all_sprites.add(b2)

	l12 = Palcka(b2,a2)
	all_sprites.add(l12)
	vse_palcke.append(l12)

	c2 = Pika(390,160,True)
	vse_pike.append(c2)
	all_sprites.add(c2)

	c2.sledi_miski = True

	l32 = Palcka(b2,c2)
	all_sprites.add(l32)
	vse_palcke.append(l32)

def mreza():
	mreza_gumb.configure(state=tk.DISABLED)

	prejsen_stolpec = False
	for s in range(1,14):
		stolpec = []
		prejsnja = False
		for v in range(1,7):
			mov = True
			if v == 1 and s % 4 == 1:
				mov = False
			p = Pika(50*s+50,50*v,mov)
			vse_pike.append(p)
			all_sprites.add(p)
			if prejsnja != False:
				l = Palcka(p,prejsnja)
				all_sprites.add(l)
				vse_palcke.append(l)
			prejsnja = p
			stolpec.append(p)
		if prejsen_stolpec != False:
			for i in range(len(stolpec)):
				l = Palcka(prejsen_stolpec[i],stolpec[i])
				all_sprites.add(l)
				vse_palcke.append(l)
		prejsen_stolpec = stolpec

def mreza2():
	mreza_gumb.configure(state=tk.DISABLED)

	prejsen_stolpec = False
	for s in range(1,42):
		stolpec = []
		prejsnja = False
		for v in range(1,20):
			mov = True
			if v == 1 and s % 4 == 1:
				mov = False
			p = Pika(10*s+150,10*v+10,mov)
			vse_pike.append(p)
			all_sprites.add(p)
			if prejsnja != False:
				l = Palcka(p,prejsnja)
				all_sprites.add(l)
				vse_palcke.append(l)
			prejsnja = p
			stolpec.append(p)
		if prejsen_stolpec != False:
			for i in range(len(stolpec)):
				l = Palcka(prejsen_stolpec[i],stolpec[i])
				all_sprites.add(l)
				vse_palcke.append(l)
		prejsen_stolpec = stolpec


class Pika(pg.sprite.Sprite):
	def __init__(self,x,y,movable):
		pg.sprite.Sprite.__init__(self)
		self.x = x 
		self.y = y	
		self.movable = movable
		if self.movable:
			self.color = (50,200,50)#WHITE
			self.width = 12
		else:
			self.width = 16
			self.color = (255,100,100)

		self.image = pg.Surface((self.width,self.width))
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		if not self.movable:
				pg.draw.circle(self.image,self.color,(self.width//2,self.width//2),self.width//2)
		self.rect.center = (self.x,self.y)
		self.pospesek = 1
		self.prejsnja_pozicija = (self.x,self.y)

		self.sledi_miski = False
		self.vpliv_miske = 0.2

	def update(self):
		if self.movable:
			self.pozicija_pred_p = (self.x,self.y)
			self.x += self.x - self.prejsnja_pozicija[0]
			self.y += self.y - self.prejsnja_pozicija[1] 
			self.y += self.pospesek
			self.rect.x = self.x 
			self.rect.y = self.y

			self.prejsnja_pozicija = self.pozicija_pred_p

			if self.sledi_miski:
				pos = pg.mouse.get_pos()
				self.x += (pos[0]-self.x)*self.vpliv_miske
				self.y += (pos[1]-self.y)*self.vpliv_miske

		if self.rect.top > HEIGHT:
			self.kill()
			vse_pike.remove(self)


class Palcka(pg.sprite.Sprite):
	def __init__(self,pika1,pika2): 
		pg.sprite.Sprite.__init__(self)
		self.pika1 = pika1
		self.pika2 = pika2
		self.dolzina = sqrt(abs(self.pika1.rect.center[0]-self.pika2.rect.center[0])**2+abs(self.pika1.rect.center[1]-self.pika2.rect.center[1])**2)
		self.color = (100,200,100)
	
	def update(self):
		if self.pika1 not in vse_pike or self.pika2 not in vse_pike:
			self.kill()
			vse_palcke.remove(self)
			return

		self.x1 = self.pika1.x
		self.x2 = self.pika2.x
		self.y1 = self.pika1.y
		self.y2 = self.pika2.y
		self.absx = abs(self.x1-self.x2) #dolzine
		self.absy = abs(self.y1-self.y2)

		self.sredinax = self.absx/2 + min(self.x1,self.x2)
		self.sredinay = self.absy/2 + min(self.y1,self.y2)
		self.dl_nova = sqrt(self.absx**2+self.absy**2)
		self.smer = ((self.x1-self.x2)/self.dl_nova,(self.y1-self.y2)/self.dl_nova)

		#premakne pike tako da se ohrani razdalja med njima
		if self.pika1.movable:
			self.pika1.x = self.sredinax + self.smer[0]*self.dolzina/2
			self.pika1.y = self.sredinay + self.smer[1]*self.dolzina/2
			self.pika1.rect.center = (self.pika1.x,self.pika1.y)

		if self.pika2.movable:
			self.pika2.x = self.sredinax - self.smer[0]*self.dolzina/2
			self.pika2.y = self.sredinay - self.smer[1]*self.dolzina/2
			self.pika2.rect.center = (self.pika2.x,self.pika2.y)

		#strga

		if self.dl_nova > self.dolzina * 15:
			self.kill()
			vse_palcke.remove(self)


		
	def narisi(self):
		self.image = pg.Surface((self.absx+2,self.absy+2))
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)

		if self.x1 >= self.x2 and self.y1 >= self.y2 or self.x2 >= self.x1 and self.y2 >= self.y1:
			self.rect = pg.draw.line(self.image,(WHITE),(0,0),((self.absx,self.absy)),2)
			self.rect.x = min(self.x1 -1,self.x2 -1)
			self.rect.y = min(self.y1 -1,self.y2 -1)
			pg.draw.line(self.image,self.color,(0,0),((self.absx,self.absy)),2)

		else:
			self.rect = pg.draw.line(self.image,(WHITE),(0,0),((self.absx,self.absy)),2)
			self.rect.x = min(self.x1 -1,self.x2 -1)
			self.rect.y = min(self.y1 -1,self.y2 -1)	
			pg.draw.line(self.image,self.color,(0,self.absy),(self.absx,0),2)

		#pg.draw.circle(self.image,((200,255,0)),[int(self.absx/2),int(self.absy/2)],5,0) # prikaze sredino

		
		
all_sprites = pg.sprite.Group()
vse_pike = []
vse_palcke = []



shuffle(vse_palcke)
running = True



#za_slike()

#GUI
root = tk.Tk()
root.title("Simulacija vrvi")
canvas = tk.Canvas(root,height=200,width=300)
canvas.pack()



napis = tk.Label(canvas, text="FPS",font=Gfont)
napis.place(x=15, y=50)

fps_vrednost = tk.IntVar()
frame_sl1 = tk.Frame(canvas)
frame_sl1.place(x=50, y=10 )
sl1 = tk.Scale(frame_sl1, from_=1, to=120,variable=fps_vrednost)
sl1.pack()
sl1.set(30)

napis = tk.Label(canvas, text="posodobitve",font=Gfont)
napis.place(x=130, y=50)

posodobitve_vrednost = tk.IntVar()
frame_sl2 = tk.Frame(canvas)
frame_sl2.place(x=220, y=10 )
sl2 = tk.Scale(frame_sl2, from_=1, to=50,variable=posodobitve_vrednost)
sl2.pack()
sl2.set(7)


vrv1_gumb = tk.Button(canvas,text="vrv1",command=vrv1,bg="white",bd =2,padx=4,pady=4,font=Gfont)
vrv1_gumb.place(x=15, y=120)

nihalo1_gumb = tk.Button(canvas,text="nihalo1",command=nihalo1,bg="white",bd =2,padx=4,pady=4,font=Gfont)
nihalo1_gumb.place(x=75, y=120)

nihalo2_gumb = tk.Button(canvas,text="nihalo2",command=nihalo2,bg="white",bd =2,padx=4,pady=4,font=Gfont)
nihalo2_gumb.place(x=155, y=120)

mreza_gumb = tk.Button(canvas,text="mreza",command=mreza2,bg="white",bd =2,padx=4,pady=4,font=Gfont)
mreza_gumb.place(x=235, y=120)


izhod = tk.Button(canvas,text="pojdi v simulacijo", command=root.destroy,bg="white",bd =2,padx=4,pady=4,font=Gfont)
izhod.place(x=85, y=160)

root.resizable(False, False)
root.mainloop()


FPS = fps_vrednost.get()
posodobitve = posodobitve_vrednost.get()

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SIMULACIJA VRVI")
clock = pg.time.Clock()


while running:
	clock.tick(FPS)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			pos = pg.mouse.get_pos()

			najblizja = vse_pike[0]
			razdalja_najblizje = 1000
			for pika in vse_pike:
				razdalja_sedanje = sqrt(abs(pika.x-pos[0])**2+abs(pika.y-pos[1])**2)
				if pika.movable and razdalja_sedanje < razdalja_najblizje:
					najblizja = pika
					razdalja_najblizje = razdalja_sedanje

			if najblizja.movable:
				najblizja.sledi_miski = True

		if event.type == pg.MOUSEBUTTONUP and event.button == 1:
			najblizja.sledi_miski = False



	#update	
	#all_sprites.update()
	
	
	for i in range(posodobitve):
		for p in vse_palcke:
			p.update()

	for p in vse_pike:
		p.update()	

	for p in vse_palcke:
		p.narisi()

	mouse_buttons = pg.mouse.get_pressed()
	
	if mouse_buttons[2]:
		pos = pg.mouse.get_pos()
		clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
		for s in clicked_sprites:
			if s in vse_palcke:
				s.kill()
				vse_palcke.remove(s)			

	#draw/render
	screen.fill((200,200,200))
	all_sprites.draw(screen)
	pg.display.flip()

pg.quit()