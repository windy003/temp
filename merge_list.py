from get_required_data_two_page import  single_lined

# 读取两个文本文件,并合并
with open("./1","r",encoding="utf-8") as f:
    content1= f.read()
content_list_1= eval(content1)


with open("./1","r",encoding="utf-8") as f:
    content2= f.read()
content_list_2= eval(content2)



merged_list=content_list_1+(content_list_2)
print(merged_list)
print(type(merged_list))

# ---------------------------------

single_lined=single_lined(merged_list)
print(single_lined)

