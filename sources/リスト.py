#%%
# 練習1
me = ["Genbu", "Hase", 3, 3, "Unknown"]

print("名前: {} {}".format(me[0], me[1]))
print("生年月日: {}月{}日".format(me[2], me[3]))
print("性別: {}".format(me[4]))

#%%
# 練習2
me = [ "Genbu", "Hase", 3, 3, "Unknown", ["https://itabashi.0j0.jp/@ProgrammerGenboo", "https://github.com/GenbuHase"] ]

print("名前: {} {}".format(me[0], me[1]))
print("生年月日: {}月{}日".format(me[2], me[3]))
print("性別: {}".format(me[4]))
print("リンク: {}".format(", ".join(me[5])))
