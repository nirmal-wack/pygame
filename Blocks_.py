#/usr/local/opt/python/bin/python3.7 /Users/sandipshah/Desktop/bootstrap/Blocks_.py
import pygame
import random
import os



x = pygame.init()
# Window Width And Height
screen_width=1000
screen_height=550
gameWindow=pygame.display.set_mode((screen_width,screen_height))
#Title
pygame.display.set_caption("Colour Blocks")
#to update screen with recent modifications
pygame.display.update()
# first we will consider exit_game & game_over as false .
exit_game= False
game_over=False
#colour white , black is just variable we can define any colour as per rgb form.
white = (0,0,0)
black=(137, 136, 140)
modif=(0,0,0)
#its for random colour selection.
c1=random.randint(10,245)
c2=random.randint(10,245)
c3=random.randint(10,245)

orange=(c1,c2,c3)
#to fill colour in backgound.
gameWindow.fill(modif)
# again update to show white backgound.
pygame.display.update()
# main charactors.
# block_x= direction at x factor. 
block_x=100
block_y=100
#size of the block
size_x=30
size_y=30
white=(255,255,255)
#clock is for to conider time at how code has to move when.
clock=pygame.time.Clock()
font=pygame.font.SysFont("comicsanms",100)
snk_length=1
snk_list=[]
color=(0,10,10)
block_size=30
text=pygame.font.SysFont('arial',20)
life=3
#to update and show Score
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	gameWindow.blit(screen_text,[5,450])
#to display point block on screen
def plot_block(gameWindow, color, snk_list, block_size):
    for x,y in snk_list:
	    pygame.draw.rect(gameWindow,color,[x,y,block_size,block_size])
		
#fps speed of particular elemenent that how fast or slow it has to move on second step.
fps=30
velo_x=0
velo_y=0
point_x=random.randint(20,screen_width/2)
point_y=random.randint(20,screen_height/2)
score=0

#Begining Progaram
while not exit_game:

		if game_over:
			gameWindow.fill(white)
			print("Your Score is",score)
			quit()
			
		else:
			for event in pygame.event.get():
				
			
				
				if(event.type==pygame.QUIT):
					exit_game = True
				if event.type==pygame.KEYDOWN:
					
                    
#which key is now pressing.				
					if event.key == pygame.K_RIGHT:
						block_x=block_x+10
						velo_x=5
						velo_y=0
					elif event.key == pygame.K_LEFT:
						block_x=block_x-10
						velo_x=-5
						velo_y=0
					elif event.key == pygame.K_UP:
						block_y=block_y-10
						velo_y=-5
						velo_x=0
					elif event.key == pygame.K_DOWN:
						block_y=block_y+10
						velo_y=5
						velo_x=0
			block_x=block_x+velo_x
			block_y=block_y+velo_y
			# main logic behind how point block get disappear and how score increase.
			if abs(block_x - point_x)<25 and abs(block_y-point_y)<25:
				score=score+10
				print("score :",score)
			
				# block_size=block_size+0.5
				
				point_x=random.randint(20,screen_width/2)
				point_y=random.randint(20,screen_height/2)
				snk_length+=5
				fps=fps+4
				head = []
				head.append(block_x)
				head.append(block_y)
				snk_list.append(head)
				black=orange
				c1=random.randint(1,255)
				c2=random.randint(1,255)
				c3=random.randint(1,255)
				orange=(c1,c2,c3)
				



			gameWindow.fill(modif)
			text_screen(" "+ str(score),orange,5,450)
			# text_screen1(life,orange,5,10)
			plot_block(gameWindow,black, snk_list, block_size)
			pygame.draw.rect(gameWindow,orange,(point_x,point_y,30,30))
			
			head = []
			head.append(block_x)
			head.append(block_y)
			snk_list.append(head)
			
			if len(snk_list)>snk_length:
				del(snk_list[0])
			if head in snk_list[:-7]:
				game_over=True

			
			if(block_x<0 or block_x>screen_width or block_y<0 or block_y>screen_height ):
			 	game_over=True;print("Game Over.")
			


				  
			pygame.display.update();clock.tick(fps)

pygame.quit()
quit()
