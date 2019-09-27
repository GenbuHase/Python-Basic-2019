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
