import easygui as e
like=e.buttonbox(msg="我是谁？",title="猜猜我是谁？",choices=["龙骨炮","龙头","Toby"],image="G:/py/龙骨炮.gif")
if like=="龙骨炮":
    e.msgbox(msg="老传说了",title="评分")
elif like=="龙头":
    e.msgbox(msg="传说之下玩过没？",title="评分")
else:
    e.msgbox(msg="…………",title="评分")