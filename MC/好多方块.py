from mcpi_e import minecraft
import time
mc = minecraft.Minecraft.create()
mc.postToChat("ok")
#pos.x -= 10
#pos.z -= 10
#pos.y += 100
mc.postToChat("!")
#mc.setBlocks(pos.x,pos.y,pos.z,pos.x + 20,pos.y,pos.z + 20,145)
time.sleep(1)
while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x,pos.y + 10,pos.z,145)
