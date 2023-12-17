import numpy as np
import pandas as pd

path = "E://S.T.U.D.Y//S.T.U.D.Y【4.1】//毕设//000 曾钰琪//data_JD//原始数据_Big_JD_Data//"
f_user = path+'JD_user_data.csv'
data_user = pd.read_csv(f_user)
d_order = pd.read_csv(path+'JD_order_data.csv')
'''
print(data_user.head())
l1=len(np.unique(data_user.user_ID))
l2=len(data_user.user_ID)
print("unique num:{}\ntotal num:{}".format(l1,l2))

print(d_order.head())
l1=len(np.unique(d_order.order_ID))
l2=len(d_order.order_ID)
print("unique num:{}\ntotal num:{}".format(l1,l2))
unique_sku=np.unique(d_order.sku_ID)
print(unique_sku[:2])
print("\nsku_ID=000aa92b82的下单条目：\n",d_order[d_order['sku_ID']=='000aa92b82'])
l11=len(unique_sku)
l12=len(d_order.sku_ID)
print("\nunique sku num:{}\ntotal sku num:{}".format(l11,l12))
'''
#排序
d_order2=d_order.sort_values(by=['user_ID','order_date','order_time'],ascending=True)
#print(d_order2.iloc[:3,:5])

d_order2['rebuy_intention'] = '0'#增加一列表示 重购意图，初始值为0，即无重购意图
#print(d_order2.head())

#某次购买之后还有购买记录，则该次购买的rebuy_intention=1
#print("\n============ rebuy_intention setting ===========\n")
i_user = d_order2['user_ID'][0]
i_sku = d_order2['sku_ID'][0]
iii=1
for index,row in d_order2.iterrows():
    #print("\n### 1. for row:\n",row)
    i_user = row['user_ID']#取当前的user_ID
    i_sku = row['sku_ID']
    d_order3=d_order2.iloc[iii:,:]
    iii=iii+1
    #print(d_order2.iloc[:3,:5])
    #print(d_order3.iloc[:3,:5])
    for index2,row2 in d_order3.iterrows():
        #print("\n### 2. for row2:\n",row2)
        i_user2 = d_order3['user_ID'][index2]
        if i_user2==i_user:
            #print("\n### i_user2==i_user True:",i_user2)
            i_sku2 = d_order3['sku_ID'][index2]
            if i_sku2==i_sku:
                d_order2.at[index,'rebuy_intention']=1#运用at方法才能修改原始的数据集
                print("\n### i_sku2==i_sku True:",i_sku2)
                break
            else:
                #print("\n### i_sku2==i_sku False:",i_sku2)
                continue
        else:
            #print("\n### i_user2==i_user False:",i_user2)
            break
        
d_order2.to_csv("E://S.T.U.D.Y//S.T.U.D.Y【4.1】//毕设//000 曾钰琪//data_JD//原始数据_Big_JD_Data//d_rebuy_intention2.csv",encoding='utf-8',index=False)
