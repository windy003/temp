from get_required_data_two_page import  *

# 读取两个文本文件,并合并
with open("./1","r",encoding="utf-8") as f:
    content1= f.read()
content_list_1= eval(content1)


with open("./2","r",encoding="utf-8") as f:
    content2= f.read()
content_list_2= eval(content2)



merged_list=content_list_1 + content_list_2
print(merged_list)
print(type(merged_list))

sorted_merged_list=sort_tuple_list(merged_list)
# ---------------------------------

# 单行显示查看,并写入文件data_Source中
single_lined=single_lined(sorted_merged_list)
print(single_lined)  

with open("./data_Source.txt","w",encoding="utf-8") as f:
    f.write(str(sorted_merged_list))



