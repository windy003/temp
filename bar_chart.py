from  pyecharts.charts import Bar

# 打开文件并读取
with open("data_Source.txt","r",encoding="utf-8") as f:
    strs_of_data=f.read()


list_of_strs_of_data=  eval(strs_of_data)


time_list=[]
titles_list=[]
price_list=[]
for i in list_of_strs_of_data:
    time_list.append(i[0])
    titles_list.append(i[1])
    price_list.append(i[2])
print(len(time_list))



bar=Bar()
bar.add_xaxis(titles_list)
bar.add_yaxis("淘宝订单分析",price_list)
bar.render("1.html")