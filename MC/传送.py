from mcpi_e import minecraft
import time
mc = minecraft.Minecraft.create()
mc.postToChat("ok")
time.sleep(5)
mc.player.setDirection()