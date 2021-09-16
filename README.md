# 基于Python的定时关机自律脚本

#### 介绍
一个Python脚本，用于限制电脑使用时间，君子の自律辅助

#### 软件架构
软件架构说明


#### 安装教程

1.  在源码中设置"目标.txt"的绝对路径
2.  在命令提示符同一目录下，将shutdown.py用"pyinstaller -F shutdown.py"命令转化为shutdown.exe可执行文件
3.  将shutdown.exe放入开机自启动文件夹%programdata%\Microsoft\Windows\Start Menu\Programs\Startup下

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  判定当前时刻距离午饭/晚饭/入睡剩余多长时间，限制晚23点-次日早6点为应处于睡眠时间。
2.  记录和显示当次开机目标，并可随时覆盖
3.  设置关机时间，限制单次计算机使用时长，以达到提高效率的目的
4.  漂亮的文字显示和即时计时
