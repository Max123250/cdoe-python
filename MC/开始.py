from mcpi import minecraft
import time
mc = minecraft.Minecraft.create()
mc.postToChat("OK")
time.sleep(2)
while True:
    pos = mc.player.getPos()
    last_block = mc.getBlock(pos.x,pos.y - 1,pos.z)
    if last_block != 56:
        mc.setBlock(pos.x,pos.y - 1,pos.z,56)
