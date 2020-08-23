def make_readable(seconds):
    real_sec = str(seconds%60)
    real_min = str((seconds//60)%60)
    real_hou = str((seconds//60)//60)
    if len(real_sec) == 1: real_sec = "0" + real_sec 
    if len(real_min) == 1: real_min = "0" + real_min 
    if len(real_hou) == 1: real_hou = "0" + real_hou 
    return "%s:%s:%s"%(real_hou, real_min, real_sec)
