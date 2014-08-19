import libtcodpy as libtcod

#Assigns height and width. Also sets an fps limit (important for real-time)
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

class Object:
  #could be any object, NPC, item, player, etc, represented on screen
  
  def __init__(self, x, y, char, color):
    self.x = x
    self.y = y
    self.char = char
    self.color = color
  
  def move(self, dx, dy):
    #move by amount
    self.x += dx
    self.y += dy
  
  def draw(self):
    #set the color and then the character of object 
    libtcod.console_set_default_foreground(con, self.color)
    libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
  
  def clear(self):
    #erase character that represents object
    libtcod.console_put_char(con, self.x self.y ' ', libtcod.BKGND_NONE)
    

#checks for keypresses
def handle_keys():
  global playerx, playery

#fullscreen mode
  key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
  
  if key.vk == libtcod.KEY_ENTER and key.lalt:
    #alt + enter toggles fullscreen
    libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    
  #exit game
  elif key.vk == libtcod.KEY_ESCAPE:
    return True
  
#movement keys, WASD
  

  if key.vk == libtcod.KEY_CHAR:

    if key.c == ord('w'):
            playery -= 1
    elif key.c == ord('s'):
            playery += 1
    elif key.c == ord('a'):
            playerx -= 1
    elif key.c == ord('d'):
            playerx += 1

  
########################################
#STARTUP AND MAIN LOOP BROTHER
########################################

#Assigns custom font
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
#Initializes window and title, allows for fullscreen
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roguelike Project', False)
#creates new off-screen console
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
#limits fps (real time game, because im the best)
libtcod.sys_set_fps(LIMIT_FPS)

#create player
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.celadon)

#create NPC
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.lightGreen)

#list of objects
objects = [npc,player]

#runs logic unless window is closed
while not libtcod.console_is_window_closed():

  #sets color of foreground(text)
  libtcod.console_set_default_foreground(con, libtcod.celadon)
  #draws all objects
  for object in objects:
    object.draw()

  #blit contents of "con" to the root console and print it
  libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0) 
  libtcod.console_flush()

  #erase all objects before they move
  for object in objects:
    object.clear()
  #makes it so the character does not have a line
  libtcod.console_put_char(con, playerx, playery, ' ', libtcod.BKGND_NONE)

  #allows to exit game
  exit = handle_keys()
  if exit:
    break

  

