from mcpi import minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("OK")
pos = mc.player.getPos()
start_pos = pos.x - 10,pos.y,pos.z + 20
end_pos = pos.x + 10,pos.y,pos.z + 10
mc.setBlocks(start_pos[0],start_pos[1],start_pos[2],end_pos[0],end_pos[1],end_pos[2],4)
mc.setBlocks(start_pos[0],start_pos[1] + 1,start_pos[2],start_pos[0],start_pos[1] + 5,start_pos[2],17)
start_pos = start_pos[0] + 20,start_pos[1],start_pos[2]
mc.setBlocks(start_pos[0],start_pos[1] + 1,start_pos[2],start_pos[0],start_pos[1] + 5,start_pos[2],17)
start_pos = start_pos[0],start_pos[1],start_pos[2] - 10
mc.setBlocks(start_pos[0],start_pos[1] + 1,start_pos[2],start_pos[0],start_pos[1] + 5,start_pos[2],17)
start_pos = start_pos[0] - 20,start_pos[1],start_pos[2]
mc.setBlocks(start_pos[0],start_pos[1] + 1,start_pos[2],start_pos[0],start_pos[1] + 5,start_pos[2],17)


