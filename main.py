import libtcodpy as libtcod

#Assigns height and width. Also sets an fps limit (important for real-time)
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

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

#limits fps (real time game, because im the best)
libtcod.sys_set_fps(LIMIT_FPS)

#places player on screen
playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

#runs logic unless window is closed
while not libtcod.console_is_window_closed():

  #sets color of foreground(text)
  libtcod.console_set_default_foreground(0, libtcod.celadon)

  #places player
  libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)

  libtcod.console_flush()

  #makes it so the character does not have a line
  libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)

  #allows to exit game
  exit = handle_keys()
  if exit:
    break

  

