import sys
import winsound
import tkinter #FOR GRAPHICS
import random #TO RANDOMLY PLACE THE FOOD

ROWS=25
COLUMNS=25
TILE_SIZE=25#THIS MAKES IT MOVE PER TILE INSTEAD OF PER PIXEL

WINDOW_WIDTH=TILE_SIZE*COLUMNS
WINDOW_HEIGHT=TILE_SIZE*ROWS

class Tile:#STORING X AND Y POSITIONS FOR THE SNAKE AND THE FOOD
    def __init__(self,x,y):
        self.x=x
        self.y=y


#ACTUAL GAME WINDOW
window=tkinter.Tk()
window.title("SUPERMAN")
window.resizable(False, False)#THE USER CANNOT RESIZE THE WINDOW BY EXPANDING OR MINIMIZING

canvas=tkinter.Canvas(window,bg="Black",width=WINDOW_WIDTH,height=WINDOW_HEIGHT,borderwidth=0,highlightthickness=0)#BACKGROUND
canvas.pack()
window.update()

#TO MAKE THE WINDOW ALWAYS OPEN AT THE CENTRE OF THE SCREEN
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width)/2-(window_width/2))
window_y=int((screen_height)/2-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#Initialize the game
def start():
    global GAME_OVER,snake,food,snake_body,SCORE,velocityX,velocityY
    snake=Tile(12*TILE_SIZE,12*TILE_SIZE)#Single tile for snake head
    food=Tile(5*TILE_SIZE,5*TILE_SIZE)
    snake_body=[]#multiple snake tiles
    velocityX=0
    velocityY=0 #AT THIS POINT THE SNAKE WON'T MOVE BECAUSE BOTH VELOCITY OF X AND VELOCITY OF Y IS ZERO
    GAME_OVER=False
    SCORE=0

start()

def change_direction(e):#e=event
#print(e.keysym)#Tells us which key has been pressed on the keyboard
    global velocityX,velocityY,GAME_OVER,play,frequency,duration
    frequency=500
    duration=100
    if(GAME_OVER):
        start()
        return#STOPS THE USER FROM PLAYING
    if(e.keysym=="Up" and velocityY!=1):#MAKES THE SNAKE UNABLE TO MOVE UP AND DOWN SIMULTANEOUSLY
        velocityY=-1#When up is pressed y coordinate reduces as it approaches the (0,0) coordinate at top left of screen
        velocityX=0#When up is pressed x coordinate doesn't change

    elif(e.keysym=="Down" and velocityY!=-1):
        velocityY=1#When down is pressed y coordinate increases as it moves further from the (0,0) coordinate at top left of screen
        velocityX=0#When down is pressed x coordinate doesn't change

    elif(e.keysym=="Left" and velocityX!=1):
        velocityX=-1
        velocityY=0

    elif(e.keysym=="Right" and velocityX!=-1):
        velocityX=1
        velocityY=0


    #MOVING THE SNAKE
def move():
    global snake,GAME_OVER,snake_body,food,SCORE
    if(GAME_OVER):
        return

    if(snake.x<0 or snake.x>=WINDOW_WIDTH or snake.y<0 or snake.y>=WINDOW_HEIGHT):
        GAME_OVER=True
        return

    for tile in snake_body:
        if(snake.x==tile.x and snake.y==tile.y):
            GAME_OVER=True
            return
    #collision between snake and food
    if(snake.x==food.x and snake.y==food.y):#x and y position of the snake is equal to to x and y position of the food
        play = winsound.Beep(frequency, duration)
        snake_body.append(Tile(food.x,food.y))#if the condition above is satisfied the snake eats the food
        food.x=random.randint(0,COLUMNS-1)*TILE_SIZE#THE FOOD THEN SPAWNS TO ANOTHER RANDOM X POSITION ON THE SCREEN
        food.y=random.randint(0,ROWS-1)*TILE_SIZE#THE FOOD THEN SPAWNS TO ANOTHER RANDOM X POSITION ON THE SCREEN
        SCORE+=10
        #updating the snake body,making it follow the head
    for i in range(len(snake_body) - 1, -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i - 1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x+=velocityX*TILE_SIZE
    snake.y+=velocityY*TILE_SIZE

#Drawing the snake head
def draw():
    global snake,food,snake_body,GAME_OVER,SCORE
    move()

    canvas.delete("all")#MAKES IT SUCH THAT THE SNAKE DOESN'T GET ANY LONGER FROM  SIMPLY MOVING
    #draw the food before the snake
    canvas.create_oval(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")#SNAKE FOOD

    canvas.create_oval(snake.x, snake.y, snake.x+TILE_SIZE, snake.y+TILE_SIZE, fill="purple")#SNAKE HEAD
    for tile in snake_body:
        canvas.create_oval(tile.x,tile.y,tile.x+TILE_SIZE,tile.y+TILE_SIZE,fill="blue")#MAKING THE SNAKE BODY

    if (GAME_OVER):
        if (SCORE<100):
            canvas.create_text(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,font="Arial 20 bold",text=f"JUST WATCH MOVIES INSTEAD:\ \nYOUR SCORE IS {SCORE}",fill="red")
        else:
            canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, font="Arial 20 bold",text=f"NICE TRY, YOU CAN GO HIGHER:\ \nYOUR SCORE IS {SCORE}", fill="red")

    else:
        canvas.create_text(30,20,font="Arial 10 bold",text=f"SCORE:{SCORE}",fill="white")

    window.after(100,draw)#10 frames per second
draw()#ACTUALLY DRAWS THE SNAKE AND FOOD

window.bind("<KeyRelease>",change_direction)



window.mainloop()#KEEPS WINDOW OPEN