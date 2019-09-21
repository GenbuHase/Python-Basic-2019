#%%
# 練習1
x = 80

if (x >= 60):
  print("合格")
else:
  print("不合格")

#%%
# 練習2
x = int(input("Input x: "))

if (x >= 60):
  print("合格")
else:
  print("不合格")

#%%

# 練習3
x = int(input("Input x: "))

if (90 <= x):
  print("秀")
elif (80 <= x < 90):
  print("優")
elif (70 <= x < 80):
  print("良")
elif (60 <= x < 70):
  print("可")
else: print("不可")


#%%
# 最適化済み
x: int = input("Input x: ") or 0

try:
  x = int(x)
except ValueError as err:
  raise TypeError("A parameter, 'x' must be Integer.")

if (90 <= x):
  print("秀")
elif (80 <= x < 90):
  print("優")
elif (70 <= x < 80):
  print("良")
elif (60 <= x < 70):
  print("可")
else: print("不可")
