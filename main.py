weigh = input("请输入要转换的重量）
if(weight[-1]=='g'):
              exweight = (int(weight[0:-2]))*2.2046
print("对应的英制重量为%.3f公斤“%(exweight))
      if(weight[-1] =='d'):
exweight1 =(int(weight[0:-2]))/2.2046
print("对应的硬质重量为%.3f公斤"%(exweight1))
