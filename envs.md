# learning

### Anaconda+OpenCV+tensorflow环境配置
https://blog.csdn.net/weixin_43264986/article/details/90206299

**硬件配置：** 
- Cpu i5-8300H  
- 显卡 1050Ti  
- WIN10 企业版 版本：2019LTSC
- python 3.5（win平台 建议使用3.5）
- Cuda 9.0（10系显卡官方建议11.0，但是不建议10。0以上，win10会BUG）
- Cudnn v7.4（适合Cuda 9.0）
 
 
 
#### 1.Anaconda的安装下载 
清华大学开源软件**镜像站**进行下载并配置镜像
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/  
 
**下载版本需要注意事项：**  

找到**3-4.2版本的Anaconda安装包**下载安装，这样获得的默认python就是3.5版本了 
**注意：3-4.2以上版本的python都是3.6以上，在WIN下与诸多插件不兼容，不建议使用**  
**注意：python3.7和tensoflow到目前为止仍然不兼容（2018.10.7）**

#### 2.安装
基本都是**下一步**。 
为了避免不必要的麻烦，**建议默认路径安装即可**（其实没必要）
**注意事项：**   
![image](https://upload-images.jianshu.io/upload_images/10099391-694a47c246b6fa4f.jpg)   
**两个都✔，建议，否则需要自己设置环境变量，自行百度**

#### 3.配置Anaconda(关键步骤)
##### 3.1下载镜像配置（linux下可以在设置软件与更新中更改，此方法主要是win）
清华TUNA镜像源有Anaconda仓库的镜像，我们将其加入conda的配置即可：  
安装Anaconda后会有Anaconda Prompt，打开Prompt输入下列：
 
```
#一条一条的输入，不要一次复制粘贴全部
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```   
##### 3.2 在配置完上面三行代码以后，会在user下找到.condarc文件 
 
![image](http://imglf3.nosdn0.126.net/img/SVpTdVRSZGRBY1M5eElNMFZjeWRHUlVSSnUyWmxqSTlVTkVkRVVQbE1rS3Z2SmQ1SHZ2OWtRPT0.png)    
 
打开.condarc文件（用TXT文档打开，修改后保存）  
**关键：在文件中添加添加了menpo**  
配置修改后的.condarc文件内容如下：
```
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - menpo
  - defaults
ssl_verify: true
show_channel_urls: true
```
配置完成之后，要关闭控制台再重新打开控制台，这样新配置的文件才会被加载进来  
##### 3.3下载安装配置环境
在Anaconda Prompt继续运行：
```
conda create --name python35 python=3.5
#新建一个3.5的下的环境
activate python35 # for Windows
python --version
conda install numpy   #可能需要这一行
```
 
**OpenCV安装**
```
conda install -c menpo opencv3
```  
**tensorflow安装**
```
conda install tensorflow-gpu
#GPU安装需要安装显卡CUDA驱动，不是显卡驱动，是NVIDIA提供的tensorflow驱动
deactivate python35 s#退出该环境
```
**问题解决：如果conda下安装出现问题，则用python的PIP工具安装**  
##### 3.4 PIP安装环境
**PIP安装关键：运行下面这行代码之前需要清华镜像，否则下载速度会特别慢，最后安装失败**   
 
​安装命令为：
pip install -i 网址 所需要安装的库名
​例如：
```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
#安装requests库
```
​就是利用清华的镜像源，下载安装requests库。 
 
**附录：部分安装指令**
```
python -m pip install --upgrade pip
 
conda install tensorflow-gpu==1.10.0  #conda方法
pip install tensorflow-gpu==1.10.0    #pip方法
#建议安装tensorflow 1.10.0版本 其他高版本适用于linux下
pip install tensorflow
#安装的是CPU版本的tensorflow，计算速度较慢
pip uninstall keras                   #卸载
pip install opencv-python             #opencv基础库
pip install numpy==1.14.5             #制定版本安装
```
##### 3.5 tensorflow-gpu 安装
- GPU 版本需要 CUDA 和 cuDNN 的支持，CPU 版本不需要。
 
- 安装cuda9.0  
 
下载地址：https://developer.nvidia.com/cuda-toolkit-archive 或 https://developer.nvidia.com/cuda-downloads
 
-安装cudnn：对应版本，v7.4
 
#### 4. 常见问题
##### 4.1 no model named 'xxxx'
百度xxxx是什么库的，就用pip安装什么库,比如：no model named keras  
在prompt下输入即可：
```
pip install keras #keras版本安装会自动对应tensorflow版本号
```
##### 4.2 问题如下
```python
mkl-random 1.0.1 requires cython, which is not installed.
#没安装什么，就装什么
tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.15.2 which is incompatible.
#需要numpy版本大于1.13.3，小于1.14.5，安装的是1.15.2
#需要卸载1.15.2
tensorflow 1.10.0 has requirement setuptools<=39.1.0, but you'll have setuptools 40.2.0 which is incompatible.
```
tensorflow和其他依赖库版本不兼容，卸载现版本，安装依赖版本  
指令如下：
```
pip uninstall numpy==1.15.2
pip install numpy==1.14.5
```
