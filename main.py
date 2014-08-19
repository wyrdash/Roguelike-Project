import libtcodpy as libtcod

#Assigns height and width. Also sets an fps limit (important for real-time)
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

#Assigns custom font
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

#Initializes window and title, allows for fullscreen
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roguelike Project', False)

#limits fps (real time game, because im the best)
libtcod.sys_set_fps(LIMIT_FPS)

#runs logic unless window is closed
while not libtcod.console_is_window_closed():

#sets color of foreground(text)
  libtcod.console_set_default_foreground(0, libtcod.celadon)

#sets controllable character, @ for now(placeholder)
  libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)

  libtcod.console_flush

#space is free and adds readability for whomever is maintaing the code
