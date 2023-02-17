# 声明：一切自动化操作都伴随封号的风险，请自行决定是否使用。

# 次项目主要以学习为主。
# 准备工作：

## 1：安装
  pet battle scripts
  https://www.curseforge.com/wow/addons/pet-battle-scripts
  
  rematch
  https://www.curseforge.com/wow/addons/rematch

## 2:宠物组
  对战位置在霜火岭，主要目标是冰脊幼崽，后两只是飞行或者小动物所以需要一套配套阵容，很多人用的是灰猫+戴米多斯的仆从x2 但因为我只有一个戴米多斯外加上他身子板脆所以我放了一个吞噬者宝宝。
  三只都要是25级蓝色等级，如果灰猫能买到加速度的最好，他的技能先攻打两次。
  灰猫和戴米多斯可以拍卖行直接买，吞噬者宝宝是噬渊抓的，遍地是，取决于想不想折腾。
  
## 3：script

if [enemy.type = 小动物]

change(40)

change(3139) [ self(灰猫:40).dead]

endif


if [enemy.type = 飞行]

change(1601)

change(3139) [ self(1601).dead]

endif


if [self(40).active & enemy.type = 小动物]

use(#3) [enemy.hp<600]

use(#2) 

use(#1) [!ability(#2).usable]

endif


if [self(40).active & enemy.type != 小动物]

use(#3) [enemy.hp<480]

use(#2) 

use(#1) [!ability(#2).usable]

endif


if [self(3139).active & enemy.type = 飞行]

use(#3)

use(#1) [!ability(#3).usable]

use(#2) [!ability(#3).usable & !ability(#1).usable]

standby [!ability(#3).usable & !ability(#1).usable & !ability(#2).usable]

endif


if [self(3139).active & enemy.type != 飞行]

use(#1)

use(#2) [!ability(#1).usable]

use(#3) [!ability(#1).usable & !ability(#2).usable]

standby [!ability(#3).usable & !ability(#1).usable & !ability(#2).usable]

endif



if [self(1601).active]

use(#3) 

use(#2) [!ability(#3).usable]

use(#1) [!ability(#2).usable & !ability(#3).usable]

endif


## 4.导入script
![image](https://user-images.githubusercontent.com/72532532/209479875-72bea96c-89ae-4107-8b3c-b401fced1b86.png)

队伍位置放好之后选中目标点击保存，技能按照图中选择。

![image](https://user-images.githubusercontent.com/72532532/209479885-abfa3be8-cae4-49e4-86bf-9fb7fe7044c7.png)

右键保存的组然后选择write script粘贴上3中的script然后保存

## 5.准备宏以及快捷键

准备一个宏：

/cast 复活战斗宠物

/target 冰脊幼崽

并且绑定为 '[' 键位

设置与目标互动为 ']'键位

打开插件设置

![image](https://user-images.githubusercontent.com/72532532/209479950-ee97435d-b6ea-47b4-a406-2e45e5289a78.png)

设置自动攻击为上面两个键位中随便一个

## 6.地图以及位置
如果从头升级，直接选择德拉诺时间线，主城接任务直接走进黑暗之门，不要跟卡德加交任务，可以跳过前置任务，直接去开启要塞。

已经有要塞了的直接要塞炉石

具体位置在

![image](https://user-images.githubusercontent.com/72532532/209480053-ed0f344e-74d2-47c2-899c-39c1f3e51838.png)
![image](https://user-images.githubusercontent.com/72532532/209480065-b1012753-de2a-4210-91fd-e7097c84495e.png)

这两只是几乎死了无限刷的，主要靠这两只劳模，有时候会有人同样方法抢怪，但是这个位置一般站两个人也不太影响效率

## 7.下载

需要一个python3以及pycharm（或别的环境）

为了一些lib的稳定性python可以选择 3.7

下载整个文件

![image](https://user-images.githubusercontent.com/72532532/209480421-b013efcb-0653-4183-aecd-c616361843e9.png)

解压这个zip到一个你想保留的位置

提前安装各个lib

![image](https://user-images.githubusercontent.com/72532532/209480567-366e83e4-4838-4eed-a398-564d1485a18e.png)

![image](https://user-images.githubusercontent.com/72532532/209480575-4bd1d60d-c384-4d35-a456-27d119db1e29.png)

需要安装：

mss
pyautogui
cv2
numpy




## script双仆人

if [enemy.type = 小动物]

change(40)

quit [ self(40).dead]

endif

if [enemy.type = 飞行]

change(One)

change(Two) [ self(One).dead]

quit [ self(Two).dead]

endif

if [self(40).active & enemy.type = 小动物]

use(#3) [enemy.hp<600]

use(#2)

use(#1) [!ability(#2).usable]

endif

if [self(40).active & enemy.type != 小动物]

use(#3) [enemy.hp<480]

use(#2)

use(#1) [!ability(#2).usable]

endif


if [self(1601).active]

use(#3)

use(#2) [!ability(#3).usable]

use(#1) [!ability(#2).usable & !ability(#3).usable]

endif

