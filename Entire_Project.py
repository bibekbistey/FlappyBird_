from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

#Creating Window

root = Tk()
root.title('Flappy Bird!!! Login and Signup Page')
root.geometry('700x500')
root.iconbitmap('bird.ico')
root.resizable(False, False)

# Importing and resizing image for background in SignUp window

photo = Image.open("database_bg.jpg")
resize_pic = photo.resize((700, 500), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize_pic)
label = Label(root, image=new_pic)
label.place(x=-3, y=0)

label1 = Label(root, text="WELCOME", font='Ubuntu', fg='red')
label1.place(x=300, y=10)

# Creating database
conn = sqlite3.connect('Login and Registration.db')

c = conn.cursor()

'''
c.execute("""CREATE TABLE addressA(
                FirstName text,
        Username text,
        Password text,
        Country text
)""")
print("Table created successfully")'''



# Creating database for SIGNUP

def Signin():
    def signUp():

        conn = sqlite3.connect("Login and Registration.db")
        c = conn.cursor()

        c.execute("INSERT INTO addressA VALUES(:Name_label, :Username_label, :Password_label,:Country_label)", {
            'Name_label': Name_entry.get(),
            'Username_label': Username_entry.get(),
            'Password_label': Password_entry.get(),
            'Country_label': Region_entry.get()
        })

        print('SIGN IN SUCCESSFUL')
        roe = c.fetchall()
        print(roe)

        conn.commit()
        conn.close()

        Name_entry.delete(0, END)
        Username_entry.delete(0, END)
        Password_entry.delete(0, END)
        Region_entry.delete(0, END)

        # Creating new window

        signupwindow = Toplevel()
        signupwindow.geometry('650x400')
        signupwindow.configure(bg="Light Yellow")
        signupwindow.title(' SIGNUP FAST!')
        signupwindow.resizable(False, False)
        signupwindow.iconbitmap('bird.ico')

        # Designing Frames

        Frame1 = Frame(signupwindow, bd=10, bg='black', relief=RIDGE)
        Frame1.place(x=15, y=0)

        Frame2 = Label(Frame1, font=('Ubuntu', 20, 'bold'), fg="red", bg='White', text='Create Your Account ', padx=150)
        Frame2.grid()

        Details_entry = Frame(signupwindow, bd=10, bg='orange', width=810, height=690, padx=180, relief=RIDGE)
        Details_entry.place(x=15, y=100)

        # Building and designing Labels, Entries and Buttons for SignUp Window
        Name = Label(Details_entry, text='Name', fg="blue", bg="orange", font='Helvetica')
        Name.grid(row=1, column=0)

        Name_entry = Entry(Details_entry, font='Times', bd=3, relief=SUNKEN)
        Name_entry.grid(row=1, column=1)

        Username = Label(Details_entry, text="Username", fg="blue", bg="orange", font='Helvetica')
        Username.grid(row=2, column=0)

        Username_entry = Entry(Details_entry, font='Times', bd=3, relief=SUNKEN)
        Username_entry.grid(row=2, column=1)

        Password = Label(Details_entry, text="Password", fg="blue", bg="orange", font='Helvetica')
        Password.grid(row=3, column=0)

        Password_entry = Entry(Details_entry, show="*", font='Times', bd=3, relief=SUNKEN)
        Password_entry.grid(row=3, column=1)

        Region = Label(Details_entry, text="Region", fg="blue", bg="orange", font='Helvetica')
        Region.grid(row=4, column=0)

        Region_entry = Entry(Details_entry, font='Times', bd=3, relief=SUNKEN)
        Region_entry.grid(row=4, column=1)

        Submit = Button(Details_entry, text="Submit", font='Times ', bg="Light Green", command=signUp)
        Submit.grid(row=5, column=1)

def logdata():
    conn = sqlite3.connect("Login and Registration.db")
    c = conn.cursor()

    name = Username_entry.get()
    password = Password_entry.get()

    c.execute("SELECT * FROM addressA")
    record = c.fetchall()
    print(record)
    user = []
    passw = []

    for records in record:
        user += [records[1]]
        passw += [records[2]]
    print(user)
    print(passw)

    if name in user and password in passw:
        if user.index(name) == passw.index(password):
            print("sucess")
            import main


        else:
            messagebox.showinfo("FAILED", "Invalid Username or Password")

    else:
        messagebox.showinfo("FAILED", "Invalid Username or Password")

    Username_entry.delete(0, END)
    Password_entry.delete(0, END)

    conn.commit()
    conn.close()


# Making and Designing labels, entries and buttons for LogIn Window

Username = Label(root, text="Username",fg="blue", bg="Light Green", font='Times')
Username.place(x=170, y=70)

Username_entry = Entry(root,  bd=3,font='Helvetica', relief=SUNKEN)
Username_entry.place(x=270, y=70)

Password = Label(root, text="Password", fg="blue", bg="light green",font='Times')
Password.place(x=170, y=150)

Password_entry = Entry(root,show="*",  bd=3,font='Helvetica', relief=SUNKEN)
Password_entry.place(x=270, y=150)

login_button = Button(root, text="LogIn",fg="blue", bg="Light Green", font='Cambria 15 italic',command=logdata)
login_button.place(x=295, y=240)

signup_button = Button(root, text="SignUp", fg="blue", bg="Light Green",font='Cambria 15 italic', command=Signin)
signup_button.place(x=295, y=350)

NewAccount = Label(root, text="First Time?",  fg='white', bg="red",font='Cambria 15 italic', width=10)
NewAccount.place(x=270, y=300)

conn.commit()

conn.close()

mainloop()

import pygame
import sys
from pygame.locals import *
import random



#initializing pygame
pygame.init()

#For fps
clock = pygame.time.Clock()
fps = 40

width=664
height=636
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Defining function for obstacles

def obstacles():
    pipex=random.randint(250,550)
    top_pipe=pipe_img.get_rect(midtop=(660,pipex))
    bottom_pipe = pipe_img.get_rect(midbottom=(660, pipex-200))
    return top_pipe,bottom_pipe

#Defining function for collision

def collision():
    global game_over,score_time
    for pipe in pipes:
        if pipe.bottom>636:
            screen.blit(pipe_img,pipe)
        else:

            flip_pipe=pygame.transform.flip(pipe_img,False,True)
            screen.blit(flip_pipe,pipe)
        pipe.centerx-=pipe_speed
        if bird_rect.colliderect(pipe):
            game_over=True
            score_time=True
            hit_sound.play()

#Defining function to display Score

def score_display(game_state):
    if game_state == "game on":
        display = SCORE_FONT.render(str(score), True, (255, 0, 0))
        score_rect = display.get_rect(center=(350, 60))
        screen.blit(display, score_rect)
    elif game_state=="game over":
        display = SCORE_FONT.render(f" Score:{score}", True, ( 255,255, 0))
        score_rect = display.get_rect(center=(350, 100))
        screen.blit(display, score_rect)

        high_score_display = SCORE_FONT.render(f"High Score:{high_score}", True, ( 255,255, 0))
        high_score_rect = high_score_display.get_rect(center=(350, 225))
        screen.blit(high_score_display, high_score_rect)




#Defining function to update score
def score_update():
    global score, score_time, high_score
    if pipes:
        for pipe in pipes:
            if 65 < pipe.centerx < 69 and score_time:
                score += 1
                score_sound.play()

                score_time = False

            if pipe.left <= 0:
                score_time = True


    if score > high_score:
        high_score = score

#Defining function for text object
def text_object(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()


font = pygame.font.Font('freesansbold.ttf', 20)


#Game variables
gravity=0.60

#For ground

moving_ground = 0
ground_speed = 4

# Creating pipes

pipe_height=[350,400,533,490]
pipe_speed=4
pipes=[]
create_pipes=pygame.USEREVENT+1
pygame.time.set_timer(create_pipes,1800)

# For Score

score=0
high_score=0
score_time=True

#Score card font
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

#Game over Variables

game_over=False
game_over_rect=game_over_image.get_rect(center=(width//2,height//2))

#for bird
bird_movement=0

#Bir images

bird_up = pygame.image.load("up.png")
bird_mid = pygame.image.load("mid.png")
bird_down = pygame.image.load("down.png")

# To flap bird
BIRDS = [bird_up, bird_mid, bird_down]
bird_index = 0
BIRD_FLAP = pygame.USEREVENT
pygame.time.set_timer(BIRD_FLAP, 200)
bird_img = BIRDS[bird_index]
bird_rect = bird_img.get_rect(center=(67, 622//2))

#Loading  images

bg = pygame.image.load("bacground4.jpg")
ground_img = pygame.image.load("ground.png")
pipe_img=pygame.image.load("../FlappyBird_/pipe.1.png")
game_over_image=pygame.image.load("gameover2.png")


#Game sound

score_sound = pygame.mixer.Sound("score.wav")
flap_sound = pygame.mixer.Sound("flap_sound.wav")
fall_sound = pygame.mixer.Sound("Fall.wav")
hit_sound = pygame.mixer.Sound("Hit_sound.wav")

#Game Loop
run = True
while run:

    clock.tick(fps)

    #drawing background
    screen.blit(bg, (0,0))

    #Adding bird
    screen.blit(bird_img,bird_rect)

    #draw and move the ground
    screen.blit(ground_img, (moving_ground, 568))
    moving_ground -= ground_speed
    if abs(moving_ground) > 35:
        moving_ground = 0

    #moving bird
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==pygame.K_SPACE and not game_over  :
                bird_movement=0
                bird_movement=-7
                flap_sound.play()

                if event.key == pygame.K_SPACE and game_over :
                bird_rect=bird_img.get_rect(center=(67,622/2))
                bird_movement=0
                pipes=[]
                game_over=False
                score=0
                score_time=True
        if event.type == BIRD_FLAP:
            bird_index += 1

            if bird_index > 2:
                bird_index = 0

            bird_img = BIRDS[bird_index]
            bird_rect = bird_img.get_rect(center=bird_rect.center)

            if event.type == create_pipes:
                pipes.extend(obstacles())


    if not game_over:

        bird_movement += gravity

        bird_rect.centery += bird_movement

        if bird_rect.top <= 5:
            game_over = True
            fall_sound.play()

        if bird_rect.bottom >= 550:
            game_over = True

        collision()
        score_display("game on")
        score_update()

     elif game_over:
            screen.blit(game_over_image, game_over_rect)
            score_display("game over")

    # Creating Pause button

    pygame.draw.rect(screen, (0, 150, 0), (50, 0, 50, 50))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if mouse[0] > 50 and mouse[0] < 100 and mouse[1] > 0 and mouse[1] < 50:
        pygame.draw.rect(screen, (0, 80, 0), (50, 0, 50, 50))
        if click == (True, 0, 0):
            paused()
    else:
        pygame.draw.rect(screen, (0, 250, 0), (50, 0, 50, 50))
    smallText = pygame.font.Font('freesansbold.ttf', 25)
    textSurface, textRect = text_object("II", smallText)
    textRect.center = ((50 + 50 / 2)), (0 + 50 / 2)
    screen.blit(textSurface, textRect)
    pygame.display.update()

pygame.quit()