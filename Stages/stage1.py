from Entity.Platform import Platform
from Entity.KillPlatform import KillPlatform
from Entity.CheckPoint import CheckPoint
from Entity.Cannon import Cannon
from Item.JumpItem import JumpItem
from Stages.parser import parse_stage
from constants import SCREEN
import pygame as pg


stage1 = parse_stage("""
................................
...............c................
............ppppppp.............
......c.....p.....p.......pppppp
.....ppppkkkp.....p.......p.....
.....p............p.......k.....
.s..jp............p.......k.....
pppppp............pkkkkkkkk.....
................................
""")


stage2 = parse_stage("""
................................
...............c................
............ppppppp.............
......c.....p.....p.......pppppp
.....ppppkkkp.....p.......p.....
.....p............p.......k.....
.s..jp............p.......k.....
pppppp............pkkkkkkkk.....
................................
""")