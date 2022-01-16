from  pyecharts.charts import Pie

# 打开文件并读取
with open("data_Source.txt","r",encoding="utf-8") as f:
    strs_of_data=f.read()


list_of_strs_of_data=  eval(strs_of_data)


time_list=[]
titles_list=[]
price_list=[]
number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in list_of_strs_of_data:
    time_list.append(i[0])
    titles_list.append(i[1])
    price_list.append(i[2])
print(len(time_list))



pie=Pie("淘宝交易数据")
pie.add(
    "",
    titles_list,
    price_list,
    is_labeled=True,
    is_more_utils=True
)
pie.render("1.html")