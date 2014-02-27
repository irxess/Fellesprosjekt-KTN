from pygame import *

# canvas will be a surface that captures the entirety of the "action"
canvas = pygame.Surface((800, 600))
# the following are your "camera" objects
# right now they are taking up discrete and even portions of the canvas,
# but the idea is that they can move and possibly cover overlapping sections
# of the canvas
p1_camera = pygame.Rect(0,0,400,300)
p2_camera = pygame.Rect(400,0,400,300)
p3_camera = pygame.Rect(0,300,400,300)
p4_camera = pygame.Rect(400,300,400,300)