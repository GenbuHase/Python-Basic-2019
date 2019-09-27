#%%
# 練習1
for i in range(11): print(i)

#%%
# 練習2
for i in range(5, 11): print(i)

#%%
# 練習3
for i in range(1, 11, 2): print(i)

#%%
# 練習4
for i in range(1, 11):
  if (i % 2): print(i)

#%%
# 練習5
for i in range(1, 21):
  if (not i % 3): print(i)

#%%
# 練習6
for i in range(1, 21):
  if (not i % 3):
    print(i)
    if (not i % 2): print("6の倍数！")

#%%
# 最終課題 v1
# Q. 3以上9999以下の奇数aで a^2 - a が10000で割り切れるものをすべて求めよ。
for a in range(3, 10000, 2):
  if not (a**2 - a) % 10000: print(a)

#%%
# 最終課題 v2
# Q. 3以上9999以下の奇数aで a^2 - a が10000で割り切れるものをすべて求めよ。
for a in range(3, 10000):
  if (a % 2):
    if not (a**2 - a) % 10000: print(a)
