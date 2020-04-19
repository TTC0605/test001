
import re #正则
import tkinter as tk  #GUI
import requests #网络请求


url = 'http://www.qmaile.com/'

resp = requests.get(url)
#网页文本
#print(resp.text)
#二进制的网页源代码
#print(resp.content.decode("UTF-8"))

resp.encoding = resp.apparent_encoding
response = resp.text
#print(response)

#数据提取 re xpath bs4
res = re.compile('<option value="(.*?") selected')
#匹配 返回列表
reg = re.findall(res,response)
#print(reg)
one = reg[0]
two = reg[1]
three = reg[2]
four = reg[3]
five = reg[4]



#画板
root = tk.Tk()

root.title('VIP电影播放')
#长宽 及 起始位置
root.geometry('500x250+100+100')

l1 = tk.Label(root,text='播放接口',font=("Arial,12"))
l1.grid()
l2 = tk.Label(root,text='播放链接',font=("Arial,12"))
l2.grid(row =6,column =0)
t1 = tk.Entry(root , text='',width= 50)
t1.grid(row =6,column =1)

var = tk.StringVar()
r1 = tk.Radiobutton(root , text='播放接口1',variable = var,value = 'one')
r1.grid(row =0,column =1)
r2 = tk.Radiobutton(root , text='播放接口2',variable = var,value = 'two')
r2.grid(row =1,column =1)
r3 = tk.Radiobutton(root , text='播放接口3',variable = var,value = 'three')
r3.grid(row =2,column =1)
r4 = tk.Radiobutton(root , text='播放接口4',variable = var,value = 'four')
r4.grid(row =3,column =1)
r5 = tk.Radiobutton(root , text='播放接口5',variable = var,value = 'five')
r5.grid(row =4,column =1)

#播放按钮
b1 = tk.Button(root,text='播放',font=("Arial,12"),width =8,)
b1.grid(row =7,column =1)

def del_text():
    t1.delete(0,'end')

b2 = tk.Button(root,text='清楚',font=("Arial,12"),width =8,command=del_text)
b2.grid(row =8,column =1)

#消息循环
root.mainloop()