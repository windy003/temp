from cgi import print_environ_usage
import re
from unicodedata import name

def  main():
    # 导入文件
    with open('./source_Code_02.html','r',encoding='utf-8') as f:
        f_r=f.read()

    # 选出需要检索的代码块txt
    txt=re.findall(r'<table class="bought-table-mod(.*?)</td></tr></tbody></table>',f_r,re.S)

    # 初始化3个列表
    time_whole=[]
    title_whole=[]
    price_whole=[]

    # for循环弄出数据
    for t in txt:
        time=re.search('<span class="bought-wrapper-mod__create-time___yNWVS" data-reactid=".0.7:.*?">(.*?)</span>',t,re.S).group(1)
        time_whole.append(time)
        title=re.search('</span><span style="line-height:16px;" data-reactid=".0.7:.*?">(.*?)</span>',t,re.S).group(1)
        title_whole.append(title)
        price=re.search(r'￥(.*?)￥',"".join(re.findall('<span data-reactid=".0.7:.*?">(.*?)</span>',t,re.S)),re.S).group(1)
        price_whole.append(price)
        

    # 将3个列表zip一下
    zipped=zip(time_whole,title_whole,price_whole)
    listed_zip=list(zipped)
    sorted_list=sort_tuple_list(listed_zip)

    single_lined_list= single_lined(sorted_list)


    # 输入接口
    input_Value=input("请输入你要提取或查询的月份:(注:必须是两位数)")


    # for循环找出匹配的项目列表:list_Of_under_number
    list_Of_required=[]
    for i in sorted_list:
        j=(i[0].split("-")[1])
        # print(j)
        if  j==input_Value:
            list_Of_required.append(i)

    
    # 输入要存文件的文件名
    file_name=input("请输入要存文件的文件名")

    with open(file_name,"w",encoding="utf-8") as f:
        f.write(str(list_Of_required))



# 将元组列表排序函数
def  sort_tuple_list(tuple_list):
    return sorted(tuple_list)





# 单行显示函数single_lined()
def single_lined(list_of_tuple):
    single_lined_lists=("\n".join(repr(x) for x in list_of_tuple))
    return single_lined_lists








if __name__ == "__main__":
    main()