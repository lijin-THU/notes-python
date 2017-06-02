
# coding: utf-8

# # 将笔记转化为不同的文件格式

# In[1]:

import os
import os.path
import nbconvert
import glob


# 检查路径是否存在，删除旧的文件：

# In[2]:

if not os.path.exists('static-files'):
    os.mkdir('static-files')
    
for n in glob.glob('static-files/*/*/*'):
    os.remove(n)


# 文件夹：

# In[3]:

folders = ['01-python-tools', 
           '02-python-essentials',
           '03-numpy',
           '04-scipy',
           '05-advanced-python',
           '06-matplotlib',
           '07-interfacing-with-other-languages',
           '08-object-oriented-programming',
           '09-theano',
           '10-something-interesting',
           '11-useful-tools',
           '12-pandas'
          ]


# 遍历文件夹得到所有的文件名：

# In[4]:

file_names = []

for folder in folders:
    files = sorted(os.listdir(folder))
    file_names += [os.path.join(folder, file_name) for file_name in files if file_name.endswith('.ipynb')]


# In[5]:

def convert_to_files(names, to_format):
    target_dir = os.path.join("static-files", to_format)
    for folder in folders:
        if not os.path.exists(os.path.join(target_dir, folder)):
            os.makedirs(os.path.join(target_dir, folder))
    converter = {
        "html": nbconvert.export_html,
        "python": nbconvert.export_python
        }
    
    for file_name in names:
        p = converter[to_format](file_name)
        with open(os.path.join(target_dir, file_name[:-6] + p[1]["output_extension"]), 'w') as f:
            f.write(p[0].encode("utf-8"))
        print file_name


# 转化 HTML 文件：

# In[6]:

convert_to_files(file_names, "html")


# 产生新目录：

# In[7]:

with open('index.md') as f:
    text = f.read()
    with open(os.path.join("static-files", "html", "README.md"), "w") as g:
        g.write(text.replace(".ipynb", ".html"))

