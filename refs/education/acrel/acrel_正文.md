# 安科瑞 - KNX 医院方案

- 来源: https://www.eepw.com.cn/zhuanlan/202310/323834.html
- 采集时间: 2026-07-23 16:34
- 场景: education

---

"); //-->
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a4c46fa4&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [![img_01.php](images/img_01.php)] </a>
# 专栏中心
[EEPW首页](<https://www.eepw.com.cn>) > [专栏](<http://spaces.eepw.com.cn/>) > 浅谈KNX智能照明系统在福安中医院的应用
# 浅谈KNX智能照明系统在福安中医院的应用
发布人：[15052179967](<http://spaces.eepw.com.cn/space/1683205237>) 时间：2023-10-16 来源：工程师
  * [ [![img_02.png](images/img_02.png)] 加入技术交流群](<javascript:void\(0\);>)
    * [![img_03.jpg](images/img_03.jpg)]   
扫码加入  
和技术大咖面对面交流  
海量资料库查询


[发布文章](<http://spaces.eepw.com.cn/expert/publish/>)
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a635e61e&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_04.php — manual:图片缺失]] </a>
**【摘要】：** 本文介绍福安中医院智能照明的应用，采用Acrel-BUS智能照明控制系统对医院门急诊楼、妇幼楼、住院楼等公共部分照明回路的通断进行智能控制，系统组网为KNX总线通讯，设计采用就地触摸屏控制及通过IP网关接入Acrel-iLightControl智能照明控制系统，在计算机端集中控制与监控管理。
**【关键词】：** 医院；集中控制；医院智能照明控制。
0\. **前言：******
随着人们生活水平的不断提高，人们对工作和生活环境的要求越来越高，同时对照明系统的要求也越来越高。医院照明设计既要满足医护人员工作的需要，以及患者生理、心理健康恢复的要求，还要尽可能的节约用电，公共照明宜采用智能化的照明控制。
1\. **项目介绍：******
该项目位于坂中乡满春街北侧，富春大道西侧，总用地面积 49330.9㎡，建设用地面积39267.6㎡，按照三级综合性医院规划建设，一期总建筑面积88975.37㎡，编制床位600张，投资约7.5亿元。
**1.1 用户需求**
在医院各建筑物每层护士值班站、前台值班站或通道内安装触摸屏，前台值班人员可根据当前需求对该受控区实现集中控制，对该区的单回路开关控制、分区域控制等；远程与就地控制相互关联，照明回路可随时按需调整。
2\. **现场应用产品介绍：******
2.1 电源模块
[![img_05.png](images/img_05.png)]   

功能说明：
KNX/EIB系统标准供电电源，耦合总线信号，并且监测KNX/EIB系统的电流。另外本系列的电源提供一个30V的辅助直流电压，为其他的外设(如触摸屏幕、IP网关等)提供电源。该模块可以为64个设备供电，带总线复位、过流指示和短路保护。功能说明：
[![img_06.png](images/img_06.png)] 2.2 开关驱动器
**[![img_07.png](images/img_07.png)] **
[![img_08.png](images/img_08.png)] ** [![img_09.png](images/img_09.png)]  [![img_10.png](images/img_10.png)]   
**
功能说明：
开关驱动器，支持KNX总线协议，用于对设备进行开关控制的驱动器，具有逻辑、延时、预设、场景、阈值开关等功能。
**2.3****0-10V调光驱动器**
功能说明：
0-10V调光模块，支持KNX总线协议，用于控制调光回路，具有软开/关功能， 每一回路能同时被8个场景调用，能检测回路状态。尤其适合对白炽灯、LED灯和低压卤素灯进行调光，还具有开关、场景、状态反馈等功能。 而实现LED的调光功能。**  
**
**[![img_11.png](images/img_11.png)]  
**
**[![img_12.png](images/img_12.png)]  
**
**2.4****人体感应和光照度传感器**
功能说明**：**
智能照明传感器，支持KNX总线协议，可感受外界信号、物理条件（如光、红外、微波），并将感应的信息传递给其它KNX模块（如调光器、开关驱动器），实现其功能。主要用于智能照明控制系统中公共走道、门厅、车库等需要自动控制场所。
[![img_13.png](images/img_13.png)] 
[![img_14.png](images/img_14.png)]   

2.5 3.5寸触摸屏
功能描述：
触摸屏，支持KNX总线协议，用于接受控件触动信号，通过控件控制单控，群控，总控，调光等操作，以及定时功能，控制点位多达80个。
[![img_15.png](images/img_15.png)] [![img_16.png](images/img_16.png)]  [![img_17.png](images/img_17.png)]   

急诊楼，住院楼，妇幼楼采用3条支线（KNX总线线缆BUS EIB2*2*0.8）到消防控制值班室，通过IP网关接入到医院内网交换机，实时数据上传到Acrel-iLightControl（智能照明控制系统）。
3\. **现场应用：******
3.1 系统拓扑图
[![img_18.png](images/img_18.png)]   

图1
3.2 设备现场应用照片：
[![img_19.png](images/img_19.png)]  [![img_20.png](images/img_20.png)]   

图2
3.3 系统软件运行界面
[![img_21.png](images/img_21.png)] 
3.4 系统主要控制功能
3.4.1 定时控制
利用中控软件界面时钟管理器，实现整个系统的有关区域照明的定时和自动管理功能，实现公共通道、景观照明、车库照明等定时、分时控制、用户可按需设定平时照明、高峰照明、节假日模式定时关闭、定时通知等。
3.4.2 场景控制
智能照明控制系统根据各个部门的需求，设定不同种类的场景模式，进行各种照明灯光的组合，达到优化工作环境的效果；结合人体感应传感器，当人员离开时，关闭该区域照明。
3.4.3 人体感应控制
在办公走道和楼梯内，布置人体感应传感器。在有人员进入区域时，自动打开照明。当人员离开后，延迟一段时间再关闭。若延迟时间内有人进入，则重新进入打开模式，以达到节能目的。并且可以设置白天合理，晚上无效，根据需求设定。
3.4.4 光照度控制
在室内办公区域内，布置照度传感器，自然光采光良好的区域，自动调节室内照明的灯光亮度和开灯数量；既充分利用了自然光，又可以为室内人员创造一个舒畅闲适的工作环境。
3.4.5 实时监控
中心控制室，配置一台中控主机，所有照明控制设备，通过KNX网关，接入监控系统。操作管理人员，可以通过中控电脑，实时监视总线、区域、楼层、楼栋等照明状态，并可根据需求进行控制调整。系统绘图工具支持向量图和多层页面，图形页面缩放方便，切换简单，支持DXF、WMF、BMP、JPG、ICON等图形对象的嵌入、支持二维、三维图元的绘制，增加可视化的空间效果。
3.4.6 报警处理
系统提供了警报处理能力，用户可采用编程来完成不同的任务，当某种警报条件出现时应做什么，可由用户自行确定。
3.4.7 事件通报
系统提供了事件通报功能，支持邮件通报、文本输出以及事件驱动打印，可按照用户预先设置的条件，触发事件通报功能。
3.4.8 日照时间计算
按照用户当前所在的时区，计算日照时间，作为定时控制的时间基准。
3.4.9 数据交换
系统可以直接使用ETS3和ETS5项目的数据，方便的实现软件升级和替代；还可接受以CVS文件格式保存的模块及系统数据；系统支持OPC服务；通过KNX-MODBUS网关可以与其他建筑智能化系统（如BA系统）进行数据交换。
3.4.10 系统联动
系统可以开关量输入模块，接受其他系统或工作人员的强切信号；实现安防系统、广播系统、会议系统，甚至消防系统的联动控制，控制相应灯具点亮和设备启停。
4\. **结束语：**
Acrel-BUS智能照明控制系统，是基于KNX总线技术设计的控制系统。系统采用标准的2×2×0.8 EIB BUS总线（即KNX总线）作为总线线缆，将所有的智能照明控制模块连接到一起并组成一套完整的控制系统，即可实现照明灯具的远程集中控制，又可实现就近控制功能。该系统理论连接控制模块数量达58000多个。
安科瑞智能照明控制产品种类齐全，方案完善。用户可通过控制面板、人体感应、照度感应、微波感应、上位机系统、触摸屏、手机、平板端等多种控制终端实现灵活多样的智能化控制，特别适合于各类智能小区、医院、学校、酒店，以及体育场所、机场、隧道、车站等大型公建项目的照明系统。
参考文献
[1].安科瑞电气股份有限公司产品选型手册.2020.10
[2].周江. 基于单片机的调光控制器设置.成都学院 2010
安科瑞 缪阳扬  

专栏文章内容及配图由作者撰写发布，仅供工程师学习之用，如有侵权或者其他违规问题，请联系本站处理。 [联系我们](<https://www.eepw.com.cn/event/company/contact.html>)
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=ae6854a5&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_22.php — manual:图片缺失]] </a>
关键词： _智能照明_
### 相关推荐
[ [![img_23.gif](images/img_23.gif)] ](<https://www.eepw.com.cn/circuit/201504/123234.html>)
### [恩智浦智能照明应用方案](<https://www.eepw.com.cn/circuit/201504/123234.html>)
[设计方案](<https://diagram.eepw.com.cn>) [JN5168](<https://www.eepw.com.cn/tech/c/k/JN5168>) [无线微控制器](<https://www.eepw.com.cn/tech/c/k/%E6%97%A0%E7%BA%BF%E5%BE%AE%E6%8E%A7%E5%88%B6%E5%99%A8>) [温度传感器](<https://www.eepw.com.cn/tech/c/k/%E6%B8%A9%E5%BA%A6%E4%BC%A0%E6%84%9F%E5%99%A8>) [智能照明](<https://www.eepw.com.cn/tech/c/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2015-04-01
[ [![img_24.jpg](images/img_24.jpg)] ](<https://www.eepw.com.cn/circuit/201504/123227.html>)
### [智能照明平台解决方案](<https://www.eepw.com.cn/circuit/201504/123227.html>)
[设计方案](<https://diagram.eepw.com.cn>) [瑞萨电子](<https://www.eepw.com.cn/tech/c/k/%E7%91%9E%E8%90%A8%E7%94%B5%E5%AD%90>) [智能照明](<https://www.eepw.com.cn/tech/c/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [照明技术](<https://www.eepw.com.cn/tech/c/k/%E7%85%A7%E6%98%8E%E6%8A%80%E6%9C%AF>) 2015-04-01
### [基于热释电传感器楼宇智能照明控制系统](<https://share.eepw.com.cn/share/download/id/63826>)
分析了热释红外线传感器PIR输出信号特点，设计基于D203S高校楼宇智能照明控制系统，实现高校教室照明时间和空间控制。系统由传感器采集电路，OP07信号调理电路，ADC0832采样电路，DS1302时钟控制电路等部分构成...
[资源下载](<https://share.eepw.com.cn>) [电传感器](<https://www.eepw.com.cn/tech/s/k/%E7%94%B5%E4%BC%A0%E6%84%9F%E5%99%A8>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [DS1302](<https://www.eepw.com.cn/tech/s/k/DS1302>) 2012-04-10
### [芯科科技与涂鸦智能携手推出免编码AIoT智能照明创新开发平台](<http://www.eepw.com.cn/article/202601/477839.htm>)
对于许多消费者而言，智能照明帮助他们首次亲身体验到了互联技术所能创造的价值。如今，这类应用已远超简单的开关控制指令的范畴。该市场正向智能场景化系统演进，这些系统不仅能够提升能源效率，还可以改善用户生活及工作体验。从商业场...
[物联网与传感器](<https://www.eepw.com.cn/info/industry/special/iot>) [芯科科技](<https://www.eepw.com.cn/tech/s/k/%E8%8A%AF%E7%A7%91%E7%A7%91%E6%8A%80>) [涂鸦智能](<https://www.eepw.com.cn/tech/s/k/%E6%B6%82%E9%B8%A6%E6%99%BA%E8%83%BD>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2026-01-21
### [理想的GVS智能照明体验，就在汕头迎宾花园酒店](<https://forum.eepw.com.cn/thread/350382/1>)
[boring000](<https://passport.eepw.com.cn/profile/post/u/758527>) 2021-04-02
### [广州公寓这样做智能照明，简单舒适又高级](<https://forum.eepw.com.cn/thread/349736/1>)
[boring000](<https://passport.eepw.com.cn/profile/post/u/758527>) 2021-03-18
[ [![img_25.png](images/img_25.png)] ](<http://www.eepw.com.cn/article/202001/409333.htm>)
### [如何通过IP/以太网供电将智能照明引入到建设项目](<http://www.eepw.com.cn/article/202001/409333.htm>)
Molex 供稿摘 要：无论是新建项目、进行深度改造，还是从现有的设施迁移到物联网架构，第一步都是要摒弃掉当前那些在新的建设中阻碍技术采用的有机过程，或者是“用合适的同类产品替代”这种更新方式。不要去相信智能楼宇...
[202002](<https://www.eepw.com.cn/tech/s/k/202002>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [IP](<https://www.eepw.com.cn/tech/s/k/IP>) [以太网供电](<https://www.eepw.com.cn/tech/s/k/%E4%BB%A5%E5%A4%AA%E7%BD%91%E4%BE%9B%E7%94%B5>) [楼宇](<https://www.eepw.com.cn/tech/s/k/%E6%A5%BC%E5%AE%87>) [建设](<https://www.eepw.com.cn/tech/s/k/%E5%BB%BA%E8%AE%BE>) 2020-01-16
### [erabbit申请试用Dragonboard 410c](<https://forum.eepw.com.cn/thread/282929/1>)
[erabbit](<https://passport.eepw.com.cn/profile/post/u/601555>) 2016-09-27
[ [![img_26.jpg](images/img_26.jpg)] ](<https://www.eepw.com.cn/circuit/201508/124961.html>)
### [一种基于动态目标跟踪技术和PLC Bus的智能照明控制系统](<https://www.eepw.com.cn/circuit/201508/124961.html>)
[设计方案](<https://diagram.eepw.com.cn>) [PLC ](<https://www.eepw.com.cn/tech/c/k/PLC%20>) [Bus](<https://www.eepw.com.cn/tech/c/k/Bus>) [智能照明](<https://www.eepw.com.cn/tech/c/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2015-08-07
### [蓝牙mesh技术持续赋能台达电子智能照明系统创新](<http://www.eepw.com.cn/article/202304/446100.htm>)
蓝牙设备网络的解决方案主要是基于蓝牙mesh网络实现的多对多网络。根据《2023年蓝牙市场最新资讯》预估，到2027年，设备网络的年出货量将会达到16.3亿，复合年增长率将会达到21%。 作为蓝牙设备网络解决方...
[手机与无线通信](<https://www.eepw.com.cn/info/industry/special/wireless>) [蓝牙mesh](<https://www.eepw.com.cn/tech/s/k/%E8%93%9D%E7%89%99mesh>) [台达电子](<https://www.eepw.com.cn/tech/s/k/%E5%8F%B0%E8%BE%BE%E7%94%B5%E5%AD%90>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2023-04-28
[ [![img_27.jpg](images/img_27.jpg)] ](<https://www.eepw.com.cn/circuit/201508/125323.html>)
### [智能控制令照明更加节能](<https://www.eepw.com.cn/circuit/201508/125323.html>)
[设计方案](<https://diagram.eepw.com.cn>) [智能照明 ](<https://www.eepw.com.cn/tech/c/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%20>) [ 无线控制 ](<https://www.eepw.com.cn/tech/c/k/%20%20%E6%97%A0%E7%BA%BF%E6%8E%A7%E5%88%B6%20%20>) [ 节能](<https://www.eepw.com.cn/tech/c/k/%20%E8%8A%82%E8%83%BD>) 2015-08-17
[ [![img_28.jpg](images/img_28.jpg)] ](<http://v.eepw.com.cn/video/play/id/2479>)
### [智能照明控制系统](<http://v.eepw.com.cn/video/play/id/2479>)
开发背景： 当今时代，资源日益匮乏，发展节能行业已经逐渐成为一种必然的趋势，所以使用低能耗的产品也正逐渐为大众所青睐，随着经济与科学技术的发展，人们对产品的智能度要求更高，市场也开始关注产品的智能化和产品的人性化。 ...
[视频](<http://v.eepw.com.cn>) [信息技术大赛](<http://v.eepw.com.cn/video/search/key/%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%E5%A4%A7%E8%B5%9B>) [单片机](<http://v.eepw.com.cn/video/search/key/%E5%8D%95%E7%89%87%E6%9C%BA>) [STC15F2K61S2](<http://v.eepw.com.cn/video/search/key/STC15F2K61S2>) [智能照明](<http://v.eepw.com.cn/video/search/key/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [A/D转换器](<http://v.eepw.com.cn/video/search/key/A%2FD%E8%BD%AC%E6%8D%A2%E5%99%A8>) 2013-01-10
### [单灯控制器城市智能照明改造方案](<https://share.eepw.com.cn/share/download/id/389104>)
本项目采用单灯智能控制系统，每个路灯控制柜配置一套集中控制器，对应其控制的路灯均配有单灯终端控制器。路灯由路灯管理部分统一管理。道路照明采用智能化控制，通过计算机网络技术，利用有线或无线传输方式，对路灯的启闭、运行状态、...
[资源下载](<https://share.eepw.com.cn>) [单灯控制器](<https://www.eepw.com.cn/tech/s/k/%E5%8D%95%E7%81%AF%E6%8E%A7%E5%88%B6%E5%99%A8>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2021-10-27
[ [[image: img_29.gif — manual:图片缺失]] ](<https://www.eepw.com.cn/circuit/201412/122008.html>)
### [智能照明](<https://www.eepw.com.cn/circuit/201412/122008.html>)
[设计方案](<https://diagram.eepw.com.cn>) [智能照明](<https://www.eepw.com.cn/tech/c/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [JenNet-IP](<https://www.eepw.com.cn/tech/c/k/JenNet-IP>) 2014-12-31
[ [![img_30.jpg](images/img_30.jpg)] ](<http://www.eepw.com.cn/article/201912/408680.htm>)
### [基于共享公寓的智能电源管理系统设计](<http://www.eepw.com.cn/article/201912/408680.htm>)
樊习习 1 ，王 尧 2 ，陈铭轩 1 ，葛年明 1 （1.三江学院电子信息工程学院，江苏 南京，210012；2.南京富岛信息工程有限公司，江苏 南京，210000） 摘 要：提出了一种远程监控共享公寓智能电源...
[202001](<https://www.eepw.com.cn/tech/s/k/202001>) [电量监测](<https://www.eepw.com.cn/tech/s/k/%E7%94%B5%E9%87%8F%E7%9B%91%E6%B5%8B>) [无线通信](<https://www.eepw.com.cn/tech/s/k/%E6%97%A0%E7%BA%BF%E9%80%9A%E4%BF%A1>) [远程控制](<https://www.eepw.com.cn/tech/s/k/%E8%BF%9C%E7%A8%8B%E6%8E%A7%E5%88%B6>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2019-12-26
### [让能源成本降低80%！揭秘智能照明背后的关键技术](<http://www.eepw.com.cn/article/202403/456531.htm>)
现代建筑中最大的能源消耗主要来自照明系统。根据国际能源署的预测，除非采取具体行动提高效率，否则到2050年，建筑环境中的能源需求将增长50%。因此，智能照明系统迅速走到前台，成为现代建筑中能效战略的重要组成部分，其目标是...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [Mouser](<https://www.eepw.com.cn/tech/s/k/Mouser>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2024-03-19
### [赋能新基建！郑州地铁3号线的智能照明由GVS视声打造](<https://forum.eepw.com.cn/thread/347577/1>)
[boring000](<https://passport.eepw.com.cn/profile/post/u/758527>) 2021-01-22
### [R_10013](<https://share.eepw.com.cn/share/download/id/194875>)
智能照明,JenNet-IP...
[资源下载](<https://share.eepw.com.cn>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [JenNet-IP](<https://www.eepw.com.cn/tech/s/k/JenNet-IP>) 2014-12-30
### [浅谈智能照明控制系统应用在城市轨道交通](<https://share.eepw.com.cn/share/download/id/391235>)
在传统的城市轨道交通设计方面，照明设计方案具有一定的弊端。随着计算机技术的发展，智能化技术渐渐步入人们的生活并成为主流，故在城市轨道交通中应用新型的照明控制设计，即智能控制系统。本文主要对智能照明的具体应用进行了分析，并...
[资源下载](<https://share.eepw.com.cn>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [轨道交通](<https://www.eepw.com.cn/tech/s/k/%E8%BD%A8%E9%81%93%E4%BA%A4%E9%80%9A>) [应用研究](<https://www.eepw.com.cn/tech/s/k/%E5%BA%94%E7%94%A8%E7%A0%94%E7%A9%B6>) 2023-10-17
[ [![img_31.png](images/img_31.png)] ](<http://www.eepw.com.cn/article/202306/448178.htm>)
### [2023年智能照明市场增速领跑,无主灯概念加速智能化升级](<http://www.eepw.com.cn/article/202306/448178.htm>)
IDC《中国智能家居设备市场季度跟踪报告，2023年第一季度》显示，2023年中国智能照明市场出货量预计为3,379万台，同比增长20.7%，增速领跑中国智能家居设备市场。人机交互方式升级是市场增长的重要驱动力，同时无主...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [无主灯概念](<https://www.eepw.com.cn/tech/s/k/%E6%97%A0%E4%B8%BB%E7%81%AF%E6%A6%82%E5%BF%B5>) 2023-06-30
### [二合一的智能照明和联接方案](<http://www.eepw.com.cn/article/202309/450562.htm>)
在智能建筑应用中，照明是建筑物的基础功能，除了通过智能照明控制以达到节省能源、提高效率的目标外，通过可见光通信（VLC）技术，还可以实现室内定位与数据传输的功能，同时提供了二合一的智能照明和联接方案。本文将为您介绍VLC...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2023-09-14
[ [![img_32.png](images/img_32.png)] ](<http://www.eepw.com.cn/article/202206/435188.htm>)
### [大联大品佳集团推出基于MediaTek产品的Wi-Fi 6智能照明控制方案](<http://www.eepw.com.cn/article/202206/435188.htm>)
致力于亚太地区市场的领先半导体元器件分销商---大联大控股宣布，其旗下品佳推出基于联发科（MediaTek）Filogic 130A的Wi-Fi 6智能照明控制方案。 图示1-大联大品佳基于MediaTek产品...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [Wi-Fi 6](<https://www.eepw.com.cn/tech/s/k/Wi-Fi%206>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2022-06-15
### [协力INGY和 Wirepas以MG24多协议SoC提升智能照明控制](<http://www.eepw.com.cn/article/202312/453948.htm>)
Silicon Labs（亦称“芯科科技”）提供超低功耗且具备大容量存储和低延迟无线连接等行业领先性能的MG24多协议SoC，为INGY和Wirepas于智能照明控制系统的合作带来了极大助益，满足了新型照明系统对于尺寸限...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [INGY](<https://www.eepw.com.cn/tech/s/k/INGY>) [MG24](<https://www.eepw.com.cn/tech/s/k/MG24>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) 2023-12-15
### [中国智能照明竞争格局，智能照明将成为未来传统照明的升级趋势](<http://www.eepw.com.cn/article/202007/414978.htm>)
一、智能照明行业发展概况智能照明是智能家居范畴的重要组成部分，利用物联网技术、有线/无线通讯技术、电力载波通讯技术、嵌入式计算机智能化信息处理，以及节能控制等技术组成的分布式照明控制系统，来实现对照明设备的智能化控制。具...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [智能照明](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E>) [家居照明](<https://www.eepw.com.cn/tech/s/k/%E5%AE%B6%E5%B1%85%E7%85%A7%E6%98%8E>) [节能控制](<https://www.eepw.com.cn/tech/s/k/%E8%8A%82%E8%83%BD%E6%8E%A7%E5%88%B6>) 2020-07-01
  * [上一篇：浅谈电气火灾监控系统在某制药公司项目的应用](<https://www.eepw.com.cn/zhuanlan/202310/323833.html> "浅谈电气火灾监控系统在某制药公司项目的应用")
  * [下一篇：浅谈消防应急疏散指示系统在某学校项目上的应用](<https://www.eepw.com.cn/zhuanlan/202310/323831.html> "浅谈消防应急疏散指示系统在某学校项目上的应用")


<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a674caa6&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_33.php — manual:图片缺失]] </a>
[更多](<http://seminar.eepw.com.cn>) **培训课堂**
[更多](<https://www.eepw.com.cn/news>) **焦点**
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a50e4511&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_34.php — manual:图片缺失]] </a>
[更多](<http://v.eepw.com.cn>) **视频**
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=aaeb3436&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [![img_35.php](images/img_35.php)] </a>
## 技术专区
  * [FPGA](<https://www.eepw.com.cn/tech/s/k/FPGA> "FPGA")
  * [DSP](<https://www.eepw.com.cn/tech/s/k/DSP> "DSP")
  * [MCU](<https://www.eepw.com.cn/tech/s/k/MCU> "MCU")
  * [示波器](<https://www.eepw.com.cn/tech/s/k/%E7%A4%BA%E6%B3%A2%E5%99%A8> "示波器")
  * [步进电机](<https://www.eepw.com.cn/tech/s/k/%E6%AD%A5%E8%BF%9B%E7%94%B5%E6%9C%BA> "步进电机")
  * [Zigbee](<https://www.eepw.com.cn/tech/s/k/Zigbee> "Zigbee")
  * [LabVIEW](<https://www.eepw.com.cn/tech/s/k/LabVIEW> "LabVIEW")
  * [Arduino](<https://www.eepw.com.cn/tech/s/k/Arduino> "Arduino")
  * [RFID](<https://www.eepw.com.cn/tech/s/k/RFID> "RFID")
  * [NFC](<https://www.eepw.com.cn/tech/s/k/NFC> "NFC")
  * [STM32](<https://www.eepw.com.cn/tech/s/k/STM32> "STM32")
  * [Protel](<https://www.eepw.com.cn/tech/s/k/Protel> "Protel")
  * [GPS](<https://www.eepw.com.cn/tech/s/k/GPS> "GPS")
  * [MSP430](<https://www.eepw.com.cn/tech/s/k/MSP430> "MSP430")
  * [Multisim](<https://www.eepw.com.cn/tech/s/k/Multisim> "Multisim")
  * [滤波器](<https://www.eepw.com.cn/tech/s/k/%E6%BB%A4%E6%B3%A2%E5%99%A8> "滤波器")
  * [CAN总线](<https://www.eepw.com.cn/tech/s/k/CAN%E6%80%BB%E7%BA%BF> "CAN总线")
  * [开关电源](<https://www.eepw.com.cn/tech/s/k/%E5%BC%80%E5%85%B3%E7%94%B5%E6%BA%90> "开关电源")
  * [单片机](<https://www.eepw.com.cn/tech/s/k/%E5%8D%95%E7%89%87%E6%9C%BA> "单片机")
  * [PCB](<https://www.eepw.com.cn/tech/s/k/PCB> "PCB")
  * [USB](<https://www.eepw.com.cn/tech/s/k/USB> "USB")
  * [ARM](<https://www.eepw.com.cn/tech/s/k/ARM> "ARM")
  * [CPLD](<https://www.eepw.com.cn/tech/s/k/CPLD> "CPLD")
  * [连接器](<https://www.eepw.com.cn/tech/s/k/%E8%BF%9E%E6%8E%A5%E5%99%A8> "连接器")
  * [MEMS](<https://www.eepw.com.cn/tech/s/k/MEMS> "MEMS")
  * [CMOS](<https://www.eepw.com.cn/tech/s/k/CMOS> "CMOS")
  * [MIPS](<https://www.eepw.com.cn/tech/s/k/MIPS> "MIPS")
  * [EMC](<https://www.eepw.com.cn/tech/s/k/EMC> "EMC")
  * [EDA](<https://www.eepw.com.cn/tech/s/k/EDA> "EDA")
  * [ROM](<https://www.eepw.com.cn/tech/s/k/ROM> "ROM")
  * [陀螺仪](<https://www.eepw.com.cn/tech/s/k/%E9%99%80%E8%9E%BA%E4%BB%AA> "陀螺仪")
  * [VHDL](<https://www.eepw.com.cn/tech/s/k/VHDL> "VHDL")
  * [比较器](<https://www.eepw.com.cn/tech/s/k/%E6%AF%94%E8%BE%83%E5%99%A8> "比较器")
  * [Verilog](<https://www.eepw.com.cn/tech/s/k/Verilog> "Verilog")
  * [稳压电源](<https://www.eepw.com.cn/tech/s/k/%E7%A8%B3%E5%8E%8B%E7%94%B5%E6%BA%90> "稳压电源")
  * [RAM](<https://www.eepw.com.cn/tech/s/k/RAM> "RAM")
  * [AVR](<https://www.eepw.com.cn/tech/s/k/AVR> "AVR")
  * [传感器](<https://www.eepw.com.cn/tech/s/k/%E4%BC%A0%E6%84%9F%E5%99%A8> "传感器")
  * [可控硅](<https://www.eepw.com.cn/tech/s/k/%E5%8F%AF%E6%8E%A7%E7%A1%85> "可控硅")
  * [IGBT](<https://www.eepw.com.cn/tech/s/k/IGBT> "IGBT")
  * [嵌入式开发](<https://www.eepw.com.cn/tech/s/k/%E5%B5%8C%E5%85%A5%E5%BC%8F%E5%BC%80%E5%8F%91> "嵌入式开发")
  * [逆变器](<https://www.eepw.com.cn/tech/s/k/%E9%80%86%E5%8F%98%E5%99%A8> "逆变器")
  * [Quartus](<https://www.eepw.com.cn/tech/s/k/Quartus> "Quartus")
  * [RS-232](<https://www.eepw.com.cn/tech/s/k/RS-232> "RS-232")
  * [Cyclone](<https://www.eepw.com.cn/tech/s/k/Cyclone> "Cyclone")
  * [电位器](<https://www.eepw.com.cn/tech/s/k/%E7%94%B5%E4%BD%8D%E5%99%A8> "电位器")
  * [电机控制](<https://www.eepw.com.cn/tech/s/k/%E7%94%B5%E6%9C%BA%E6%8E%A7%E5%88%B6> "电机控制")
  * [蓝牙](<https://www.eepw.com.cn/tech/s/k/%E8%93%9D%E7%89%99> "蓝牙")
  * [PLC](<https://www.eepw.com.cn/tech/s/k/PLC> "PLC")
  * [PWM](<https://www.eepw.com.cn/tech/s/k/PWM> "PWM")
  * [汽车电子](<https://www.eepw.com.cn/tech/s/k/%E6%B1%BD%E8%BD%A6%E7%94%B5%E5%AD%90> "汽车电子")
  * [转换器](<https://www.eepw.com.cn/tech/s/k/%E8%BD%AC%E6%8D%A2%E5%99%A8> "转换器")
  * [电源管理](<https://www.eepw.com.cn/tech/s/k/%E7%94%B5%E6%BA%90%E7%AE%A1%E7%90%86> "电源管理")
  * [信号放大器](<https://www.eepw.com.cn/tech/s/k/%E4%BF%A1%E5%8F%B7%E6%94%BE%E5%A4%A7%E5%99%A8> "信号放大器")