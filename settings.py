import pygame

#GAMESIZE

columns = 10
rows = 20
cell_size = 30
game_width,game_height = columns * cell_size, rows * cell_size

#sidebar size

sidebar_width = 100
preview_height_fraction = 0.7
score_height_fraction = 1 - preview_height_fraction

#window

padding = 20
window_width = game_width + sidebar_width + padding * 3
window_height = game_height + padding * 2

#game_behaviour

update_start_speed = 800
move_wait_time = 200
rotate_wait_time = 200
block_offset = pygame.Vector2(columns // 2,-1)

#colors

black = (0,0,0)
white = (255,255,255)
grey = (128,128,128)
red = (255,0,0)
blue = (0,0,255)
line_color =(255,255,255)
yellow = (255,255,0)
purple = (128,0,128)
green = (0,255,0)
orange = (255,165,0)
cyan = (0,255,255)

# shapes
Tetrominoes = {
    'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': 'purple'},
    'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': 'green'},
    'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': 'yellow'},
    'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': 'blue'},
    'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': 'orange'},
    'S': {'shape': [(0,0), (0,-1), (0,-1), (1,-1)], 'color': 'cyan'},
    'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': 'red'}
}