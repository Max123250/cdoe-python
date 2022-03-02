from mcpi import minecraft
import random
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
d_x = random.randint(pos[0] - 50,pos[2] + 50)
d_y = random.randint(pos[1],pos[1] + 2)
d_z = random.randint(pos[2] - 50,pos[2] + 50)
mc.setBlock(d_x,d_y,d_z,56)
mc.postToChat("Find the diamond block!")
game_over = False
while not game_over:
    pos = mc.player.getPos()
    pos = [pos.x,pos.y - 1,pos.z]
    last_block = mc.getBlock(pos.x,pos.y,pos.z)
    if last_block == 56:
        mc.postToChat("You find it!you are the winnerrrrrrrr!")
        game_over = True