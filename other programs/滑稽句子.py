import random
p=["老师","你","同学们","二愣子","苹果","鼠标","手表"]
v=["坐着","站着","看着手机","呕吐","咳嗽"]
a=["在厕所里","在餐桌上","在卧室里","在台灯上"]
rp=random.choice(p)
rv=random.choice(v)
ra=random.choice(a)
ts=rp+ra+rv
print(ts)