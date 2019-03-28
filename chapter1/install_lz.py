# 进入..\opencv文件夹，创建虚拟环境：virtualenv venv -p python3
# 打开cmd，进入虚拟环境..\opencv\env\Scripts
# activite 进入虚拟环境
# 下载numpy: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
# 下载opencv-python: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python

# 测试
import cv2 as cv
import numpy as np
import sys

print('cv:'+cv.__version__)
print('numpy:'+np.__version__)
print('python:'+sys.version)

'''
cv:4.0.0
numpy:1.16.2
python:3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)]
'''

'''
备注：
若在pip升级的时候：python -m pip install --upgrade pip
出现错误：AttributeError: 'NoneType' object has no attribute 'bytes'
解决方案：easy_install -U pip
'''

'''
github提交文件：
1.在github新建仓库
2.打开Git Bash ，进入../opencv
3.依次执行一下命令：
echo "# OpenCV3-note" >> README.md
git init
git add .
git commit -m "Install opencv numpy"
git remote add origin https://github.com/luozhengszj/OpenCV3-note.git
git config --global credential.helper store
git push -u origin master
4.完成推送，其中git config --global credential.helper store是为了避免下次还需要输入用户密码

以后每次推送命令如下：
git add .
--git status
git commit -m "备注"
git log
--git rebase -i b0aa963
--改pick 为 drop，保存退出
git push -u origin master

5.若出错：error: failed to push some refs to
先拉取到本地仓库（会自动同步合并）git pull origin master
再使用 git push -u origin master 推送
'''
