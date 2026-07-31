# EEPW - 地铁智能照明设计

- 来源: https://www.eepw.com.cn/zhuanlan/202307/317281.html
- 采集时间: 2026-07-23 16:35
- 场景: metro

---

"); //-->
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a4c46fa4&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [![img_01.php](images/img_01.php)] </a>
# 专栏中心
[EEPW首页](<https://www.eepw.com.cn>) > [专栏](<http://spaces.eepw.com.cn/>) > 浅谈地铁车站中智能照明系统的设计与应用
# 浅谈地铁车站中智能照明系统的设计与应用
发布人：[acrelhn](<http://spaces.eepw.com.cn/space/1685769016>) 时间：2023-07-21 来源：工程师
  * [ [![img_02.png](images/img_02.png)] 加入技术交流群](<javascript:void\(0\);>)
    * [![img_03.jpg](images/img_03.jpg)]   
扫码加入  
和技术大咖面对面交流  
海量资料库查询


[发布文章](<http://spaces.eepw.com.cn/expert/publish/>)
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a635e61e&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_04.php — manual:图片缺失]] </a>
安科瑞 华楠
**【摘要】** 地铁作为地下建筑，大量使用灯光照明，智能照明系统的应用有利于提高照明使用效率并兼顾照明舒服度。通过介绍智能照明系统的特点及地铁中智能照明系统的系统构成和控制方案，并结合智能照明系统在南京地铁中的设计与应用，阐述了智能照明系统在应用在地铁建设中的优越性及发展前景。
**【关键词】** 智能照明地铁模式控制
**1引言**
随着地铁线路里程数的不断增加，地铁系统俨然己经成为了城市中的能耗大户。由于地铁车站处于地下，自然采光难以实现，主要依靠人工照明来营造和保障内部光环境，照明时间长、能耗大是其特点，据调査地铁车站照明的用电量仅次于电梯和排风系统，占总用电量的30%左右，各照明系统中还存在大量低效率的光源、灯具等设备和低效的照明控制方式，所以照明系统在节能方面有很大的空间。
照明的基本功能是明视性，也就是我们一般常说的生理照明，它能帮助我们辨别周围环境和识别眼前物体,满足一般的社会活动需求。随着社会经济的发展和人民生活水平的提高，人们对照明的需求不再局限于基本的明视功能，而是对光环境提岀了更高的要求，也就是心理照明。恰当的照明氛围能够让人体感舒服、心情愉悦。如果光环境处理的不好,也会影响人们的生活，如高架桥、高层办公楼等公共建筑的晚间亮化照明，会影响附近居民楼内人们睡眠的效率，进而影响生活和工作;商业区建筑外立面上的大幅广告照明，虽然比较夺人眼球，但是可能会影响交通安全。
因此，如何根据地铁车站内部环境特点、人群特点和交通行为特征以及视觉特点平衡兼顾照明舒服度水平和照明质量要求，实现经济、节能的绿色照明是地下空间人工光环境控制追求的目标。
**2智能照明系统简介**
在照明控制的进程中主要经历了三个阶段，分别为人工控制阶段、时序控制阶段和自动调光控制阶段。在地铁建设发展初期，大多釆用人工控制的方式进行空间照明，因为在照明控制方面计算机技术还不成熟，所以只能根据不同时段和现场环境,由专人负责照明的控制和管理，区域照明亮度也是由专门人员主观决定的。由于控制的不及时很容易造成能耗过大，产生浪费。
随着计算机技术、网络通讯技术的发展，以及智能型楼宇、住宅的广泛推广，智能照明控制技术得到众多投资方、用户及设计师的重视，智能照明控制产品市场也日益被各专业企业所关注。目前智能照明技术已广泛应用于智能家居、宾馆酒店、商业广告、园林景观、体育场馆、汽车等诸多领域,在轨道交通领域也有部分应用，如上海、深圳、杭州地铁等部分线路，但其系统只是作为车站BAS系统控制功能的一个衍伸，并未发挥其根据光环境达到智能调光的功效。
通俗地说,智能照明控制系统是利用计算机、嵌入式系统和网络通信技术，将照明线路中的各种光源通过网络连接到一起进行控制的平台。利用照明智能化控制可以根据环境变化、客观需要、用户预定需求等条件而自动采集照明系统中的各种信息，对所釆集的信息进行相应的逻辑分析、推理、判断，并对分析结果按照要求的形式存储、显示、传输，进行相应的工作状态信息反馈，以达到预期的控制效果。
(1)智能照明控制系统的特点
a.系统集成性，是集计算机技术、网络通信技术、自动控制技术、微电子技术、数据库技术和系统集成技术于一体的现代控制系统;
b.智能化，具有信息采集、传输、逻辑分析、智能分析推理及反馈控制等智能特征的控制系统;
c.网络化，传统照明控制系统大都是独立的、本地的、局部的系统，无专门的网络连接，而智能照明控制系统可以是大范围的控制系统，需要包括硬件技术和软件技术的计算机网络通信支持，进行必要的控制信息交换和通信，并纳入物联网技术，可实现通过移动终端进行控制;
d.使用方便，采用图形化界面，显示直观，控制方便，可以通过编程的方法灵活改变照明效果，同时还能实时监测末端负载的运行情况，为运营检修提供了便利。
(2)智能照明控制系统的功能
a.回路电流、电压、功率因数、电量检测等;
b.单灯开关和调光;
c.单灯电流、电压、功率因素、电量和温度检测等;
d.根据天气情况和实际的光照强度，实现灯具的自动开、关和调光;
e.灵活的亮灯组合管理，控制每一盏灯;
f.现场管理功能;
g.预设管理功能;
h.每天可进行自动通、断电操作，保证工作日、节假日按不同的时间自动通、断电，可对用电设备进行分区、分线路管理或单独管理;
i.集成无线抄表功能，为能耗管理打下基础;
j.监控灯具的开、关和亮度，从而显著延长灯具的有效寿命，减少灯具更换次数，节约资源。
**  
**
**3智能照明系统设计方案**
3.1系统构成
智能照明控制系统一般由四个单元构成:输入设备、系统设备、输出设备、负载。输入设备包括终端控制器、照度传感器等将所接收到的指令和信号发送给系统设备主机，主机把调整后的数据送给输出设备开关模块或调光控制模块，控制模块对负载光源进行开关与调光动作。
智能照明控制系统设备主要由一台智能照明主机控制柜和多个智能照明配电箱以及被控设备(灯具)组成(图1)。智能照明主机控制柜内安放了智能照明系统的核心组成部分，包括主控制器、工控机及显示器、远程数据集中器等接口配件。智能照明配电箱则内置了分控制器和控制模块，分控制器和控制模块通过现场总线连接成网络，通过专用接口元件及软件，可在控制室的智能照明主机控制柜内的工控机上进行实时监控及操作。还可根据用户需求拓展，将现场控制器和照度控制器等组件连接至分控制器上,实现状态控制功能。
[[image: img_05.png — manual:图片缺失]] 
图1智能照明系统简图
3.2控制方案
以往地铁车站的照明灯具釆用交叉配线，由车站BAS系统分回路通过硬线集中控制，在运营的高峰时段，站厅、站台公共区的所有照明全部开启。高峰过后，关掉其中一半照明以节约能源。列车正常停运后，将公共区的正常电照明全部关掉，只保留公共区的应急照明，供内部人员通行和巡视使用。
这种控制方式虽然在一定程度上达到了节电的效果，但是在照明梯度上变化明显，工况单一，无法做到在亮度上线性实时控制，会让人心理上产生一定的不适应，也无法做到分区域单灯控制。同时，传统的荧光灯管反复的开关会影响灯管的使用寿命，对于出现故障的灯具无法在控制室査看，只能通过运营维护人员到现场逐个排查，如检查疏漏、更换不及时，不但影响照明效果，还可能会收到乘客的投诉，扩大了影响范围，浪费了人力物力财力。同时，荧光灯/节能灯的特性决定其无法实现单灯调光控制。
因此,基于以上原因，选用更加绿色环保的光源LEDoLED除了有着节能、环保、寿命长的特点，更重要的是LED有着不可比拟的调光优势，体现在可通过调整电流的大小或通过LED颗粒分组控制从而达到调整光照强度的目的，非常适合配合智能照明控制器实现分时、分组、分区域控制，每套灯具还可以内嵌地址，实现单灯调光控制，实时上传工作状态。
南京地铁工程釆用的智能照明控制系统是一个二线制的智能控制系统，由智能照明主机、智能控制模块、被控设备(灯具)和相关通讯网络组成。系统内所有的控制模块均内置微处理器和存储单元，由一对信号线连接成网络。总线上所有控制模块通过系统编程使控制开关与输出回路建立逻辑对应关系。智能照明控制系统在控制的同时，监控各回路灯具的运行情况，并将数据反馈至主机显示屏，同时上传至车站综合监控系统。
(1)分时、分区、分组控制
在主机中根据日客流、节假日、重大节日、大型集会或庆典等不同情况下的客流大小分别设定模式，实现分时、分区、分组调光控制。
(2)自然光补偿控制
南京地处长江下游中部富庶地区，属亚热带季风气候，雨量充沛，四季分明,年平均雷暴日为32.6d/a。因此其自然光的光照强度受气候、天气变化的影响较大。利用自然光釆光的出入口及浅埋式开天窗车站的公共区设置照度传感器，根据季节、天气、日照的变化单独对有自然光引入范围内的灯具进行自动调光，给乘客提供舒服的视觉感受。控制过程无需人工干预,运营管理方便，同时节约电能。
(3)事件控制
根据特殊事件采用预编程或手动控制,管理照明。特殊情况下,打开特定区域内的局部照明光源，以满足各种情况下的照明需求。
**4智能照明系统在南京地铁中的应用**
4.1南京地铁工程车辆段及停车场
南京地铁3号线工程秣周车辆段、林场停车场及南京地铁4号线工程青龙车辆段在检修大库内设置了车辆段的智能照明系统。通过将照明系统与检修列车列位、列车检修工艺以及列车运行计划相协调，达到对大库照明系统的智能控制。智能照明控制装置按行车计划实时调用列位灯具控制模式,要求白天库顶照明工作区域开启部分灯光照明，晚间等待地铁车辆入库的时间段开启全部库顶照明灯具，地铁车辆入库开始检修时自动开启全部检修坑内及检修平台照明灯具。工作结束时间时自动关闭全部灯具，只保留部分库顶长明灯至早晨天亮。当现场需要加班或其他临时需要时，可通过现场控制器开启或关闭灯具。
车辆段采用智能照明控制系统,根据车辆基地行车组织计划，结合车辆检修工艺要求对停车列位上方一般照明灯具进行分区、分时控制，控制方便,节电效果显著。根据分析结果，南京地铁3号线工程车辆场段釆用智能照明系统,可节省50%的照明电能损耗。预计一年可节省54万kWho图2为检修大库智能照明方案图。
[[image: img_06.png — manual:图片缺失]] 
4.2灵山控制中心
南京地铁4号线工程还在灵山控制中心大楼设置了智能照明控制系统，对控制中心地下停车场及运营办公用房普通照明、室外照明、景观照明进行智能化控制，以节约电能。智能照明系统控制地下停车场灯具开断,做到车来灯亮、车走(停)灯熄,亮灯区域为有车行径的区域。控制中心运营办公用房由智能照明系统根据照度自动控制室内灯具,且室内无人时自动熄灯;走廊及电梯厅照明做到有人灯亮、无人灯熄。室外照明由智能照明系统根据室外照度情况，自动开灯、熄灯，在凌晨之后，根据需要可将室外照明全部熄灭。景观照明由智能照明系统设置模式控制，平日为节能景观模式，可只开启部分景观照明，有庆祝活动或节假日为节假景观模式，开启全部景观照明，在凌晨之后，根据需要可将景观照明全部熄灭,节能效果非常明显。
**  
**
**5、安科瑞智能照明控制系统**
5.1系统简介
Acrel-BUS智能照明控制系统，是基于KNX总线技术设计的控制系统。KNX总线技术起源于欧洲，是在EIB，Batibus和EHS这三种住宅和楼宇的总线控制技术上发展起来的，其中EIB是该总线技术的主体。
Acrel-BUS智能照明控制系统采用标准的2*2*0.8EIBBUS总线（即KNX总线）作为总线线缆，将所有的智能照明控制模块连接到一起并组成一套完整的控制系统，既可实现照明灯具的远程集中控制，又可实现就近控制功能。该系统理论可连接控制模块数量达580000多个。
安科瑞智能照明产品种类齐全，方案完善。用户可通过控制面板、人体感应、照度感应、微波感应、上位机系统、触摸屏、手机、平板端等多种控制终端实现灵活多样的智能控制，特别适合于各类智能小区、医院、学校、酒店，以及体育场所、机场、隧道、车站等大型公建项目的照明系统。
5.2系统结构
系统一般采用分层结构，搭建项目时，划分成域、支线、域－支线这种分布式总线结构。一方面其布局清晰，布线简单，容量大，对各种类型的项目尤其是大型公建项目特别适用，另一方面有效提高了系统的可靠性。由于每个域和每条支路分别分配了总线电源，这种电气的隔离使得系统的某个部分出现故障时，其他部分仍能继续工作，一条线路或一个域内的数据通信不会影响到其它范围的数据通信。
[[image: img_07.png — manual:图片缺失]] 
5.3产品介绍及选型
[[image: img_08.png — manual:图片缺失]] 
**6 结语**
智能照明随着地铁的建设，不断得以应用。通过在南京地铁中的应用经验，智能照明不仅能营造较好的光环境，还可以提高照明使用效率，有效节约能源和降低运行费用。在“十三五”推行绿色发展理念的今天，智能照明控制系统在地铁建设中的应用有发展前景，也是大势所趋。
  

专栏文章内容及配图由作者撰写发布，仅供工程师学习之用，如有侵权或者其他违规问题，请联系本站处理。 [联系我们](<https://www.eepw.com.cn/event/company/contact.html>)
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=ae6854a5&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_09.php — manual:图片缺失]] </a>
关键词： _智能照明系统_
### 相关推荐
### [基于单片机的交流LED智能照明系统设计](<http://www.eepw.com.cn/article/218545.htm>)
摘要：以热释电红外探测器、光亮度及声控传感器做为照明区域的感知器件，进行信号采集，将采集信号通过转换电路转 ......
[嵌入式系统](<https://www.eepw.com.cn/info/industry/special/embedded>) [单片机](<https://www.eepw.com.cn/tech/s/k/%E5%8D%95%E7%89%87%E6%9C%BA>) [交流LED](<https://www.eepw.com.cn/tech/s/k/%E4%BA%A4%E6%B5%81LED>) [智能照明系统](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F>) [](<https://www.eepw.com.cn/tech/s/k/>) 2012-08-08
### [汽车自适应大灯技术简介](<http://www.eepw.com.cn/article/201706/350682.htm>)
对于目前名目繁多的主动大灯系统，业界有一个专有名词---Advanced front-lighting system。其剪成就是我们在新车配置表里经常见到的AFS自适应大灯。但实际上很多厂商所采用的大灯技术还算不上自适应...
[汽车电子](<https://www.eepw.com.cn/info/industry/special/auto>) [自适应大灯](<https://www.eepw.com.cn/tech/s/k/%E8%87%AA%E9%80%82%E5%BA%94%E5%A4%A7%E7%81%AF>) [自动光束控制](<https://www.eepw.com.cn/tech/s/k/%E8%87%AA%E5%8A%A8%E5%85%89%E6%9D%9F%E6%8E%A7%E5%88%B6>) [智能照明系统](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F>) 2017-06-07
### [厂区智能照明系统的设计与应用](<http://www.eepw.com.cn/article/199961.htm>)
普通照明控制系统是以照明配电箱通过手动开关来控制照明灯具的通断，或通过回路中串入接触器，实现远距离控制。而今出现的厂区自控系统，是以电气触点来实现区域控制，定时通断。中心监控等功能，由于照明系统在自控...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [智能照明系统](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F>) [](<https://www.eepw.com.cn/tech/s/k/>) 2012-10-29
### [基于无线网络控制的智能照明系统](<http://www.eepw.com.cn/article/200609.htm>)
摘要：根据节能环保、智能家居的需求，采用LED灯和TI的SoC芯片CC2431设计了一套基于ZigBee无线网络控制的智能照明系统。该系统可在兼容已有调光模式的基础上，利用照度值来精细调节局部照度，从而实现简单的照明定位...
[光电显示](<https://www.eepw.com.cn/info/industry/special/led>) [无线](<https://www.eepw.com.cn/tech/s/k/%E6%97%A0%E7%BA%BF>) [网络控制](<https://www.eepw.com.cn/tech/s/k/%E7%BD%91%E7%BB%9C%E6%8E%A7%E5%88%B6>) [智能照明系统](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F>) [](<https://www.eepw.com.cn/tech/s/k/>) 2012-03-02
### [智能照明控制系统的设计](<http://www.eepw.com.cn/article/201808/386546.htm>)
摘要：目前我国高校的教学楼和学生宿舍的照明系统大多采用定时方式控制，存在电能的大量浪费和照明模式不灵活等问题。本文基于51单片机，通过设置时间...
[消费电子](<https://www.eepw.com.cn/info/industry/special/consume>) [智能照明系统;单片机;感应;动态控制](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F%3B%E5%8D%95%E7%89%87%E6%9C%BA%3B%E6%84%9F%E5%BA%94%3B%E5%8A%A8%E6%80%81%E6%8E%A7%E5%88%B6>) 2018-08-13
### [汽车自适应大灯技术简介](<https://www.eepw.com.cn/circuit/201508/125300.html>)
[设计方案](<https://diagram.eepw.com.cn>) [自适应大灯 ](<https://www.eepw.com.cn/tech/c/k/%E8%87%AA%E9%80%82%E5%BA%94%E5%A4%A7%E7%81%AF%20%20%20>) [自动光束控制 ](<https://www.eepw.com.cn/tech/c/k/%E8%87%AA%E5%8A%A8%E5%85%89%E6%9D%9F%E6%8E%A7%E5%88%B6%20%20>) [ 智能照明系统](<https://www.eepw.com.cn/tech/c/k/%20%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F>) 2015-08-16
[ [[image: img_10.jpg — manual:图片缺失]] ](<https://www.eepw.com.cn/circuit/201412/121807.html>)
### [DALI智能LED电源驱动控制器解决方案](<https://www.eepw.com.cn/circuit/201412/121807.html>)
[设计方案](<https://diagram.eepw.com.cn>) [智能照明系统 ](<https://www.eepw.com.cn/tech/c/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F%20>) [ 数字化可寻址照明接口](<https://www.eepw.com.cn/tech/c/k/%20%E6%95%B0%E5%AD%97%E5%8C%96%E5%8F%AF%E5%AF%BB%E5%9D%80%E7%85%A7%E6%98%8E%E6%8E%A5%E5%8F%A3>) [ 恒流驱动](<https://www.eepw.com.cn/tech/c/k/%20%20%E6%81%92%E6%B5%81%E9%A9%B1%E5%8A%A8>) 2014-12-22
### [采用CAN/LIN总线的教学楼智能照明系统](<http://www.eepw.com.cn/article/240820.htm>)
智能照明系统在智能办公大厦、现代化建筑中的研究运用较多，而对于教学楼的研究运用却很少，导致传统的照明......
[嵌入式系统](<https://www.eepw.com.cn/info/industry/special/embedded>) [CAN](<https://www.eepw.com.cn/tech/s/k/CAN>) [LIN总线](<https://www.eepw.com.cn/tech/s/k/LIN%E6%80%BB%E7%BA%BF>) [智能照明系统](<https://www.eepw.com.cn/tech/s/k/%E6%99%BA%E8%83%BD%E7%85%A7%E6%98%8E%E7%B3%BB%E7%BB%9F>) 2011-08-23
  * [上一篇：振弦式表面应变计在岩土工程中应用](<https://www.eepw.com.cn/zhuanlan/202307/317273.html> "振弦式表面应变计在岩土工程中应用")
  * [下一篇：工业物联网网关是什么？具备什么功能？](<https://www.eepw.com.cn/zhuanlan/202307/317270.html> "工业物联网网关是什么？具备什么功能？")


<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a674caa6&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_11.php — manual:图片缺失]] </a>
[更多](<http://seminar.eepw.com.cn>) **培训课堂**
[更多](<https://www.eepw.com.cn/news>) **焦点**
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=a50e4511&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [[image: img_12.php — manual:图片缺失]] </a>
[更多](<http://v.eepw.com.cn>) **视频**
<a href="https://ad.eepw.com.cn/www/delivery/ck.php?n=aaeb3436&amp;cb=INSERT_RANDOM_NUMBER_HERE" target="_blank"> [![img_13.php](images/img_13.php)] </a>
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