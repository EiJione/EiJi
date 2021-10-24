from math import pi,asin#载入数学符号
import win32api,win32con,win32gui,win32ui#载入pywin32模块，pywin32有许多功能，是windows提供的接口，追求效率或追求控制更深层的系统功能的话，这是值得学习的
e=1#改变函数f的弯曲方向，f是一个指数函数（e小于1时是凸函数)
ke=(1*2000/303)**(1/e-1)#函数f的系数,（2000/33）决定了对于函数f当指针与目标相距50像素时f(x)=x，（这是一个指数函数，画张图就非常明白了）。2000/33前的系数（1）用于妥善增大或减小50这个值
f= lambda x:(ke*x)**e if x >=0 else -(-ke*x)**e#这是一个‘指数函数’，只是在x小于0时它的图像是对称于x大于0时的图像的。

hwnd=0#目标窗口的句柄，0是全屏
x=0
y=0#为x,y设置一个初始值
xs=1920#xs,ys代表窗口大小
ys=1080#由于代码多次修改，并没有做到只要修改xs、ys就能使程序匹配新的窗口大小，还需做很多调整
x0=xs/2
y0=ys/2#x0,y0是窗口的中点
nx=0
ny=0#为x0,y0设置一个初始值
while 1==1:
    ni=0
    flag=0
    ki=0#以上三个数据用于重启找色部

    #截图部
    hwndDC=win32gui.GetWindowDC(0)
    mfcDC=win32ui.CreateDCFromHandle(hwndDC)
    saveDC=mfcDC.CreateCompatibleDC()
    saveBitMap=win32ui.CreateBitmap()#以下几行均是在这个bitmap中作画的代码
    saveBitMap.CreateCompatibleBitmap(mfcDC,300,300)#检测范围可以再大点吗
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (300, 300), mfcDC, (810,390), win32con.SRCCOPY) #第一个二元数对是画作左上角在bitmap中的位置，第二个是画作与画作源的大小，第三个是画作源左上角在屏幕中的位置
    data=saveBitMap.GetBitmapBits() #获取bitmap中每个点的R.G.B.alpha值构成的一个元组（顺序是G.B.R.alpha）。已知的图像大小的情况下，这个有序元组结合二维空间中每一个点的色彩值信息



    #saveDC.DeleteDC()
    #mfcDC.DeleteDC()
    #win32gui.ReleaseDC(hwnd, hwndDC)
    #win32gui.DeleteObject(saveBitMap.GetHandle())
    #输出data后便可清空截图的缓存。由于未系统学习win32，原理不明。耗时极短。作为可选项
    #耗时小于0.0005s/100次






    #找色部
    while flag == 0:

        try:#其实这种遍历方式我也不是很喜欢，所以问：是否可以一次只取第一个19，不符合就直接返回未找到？←决定其，我可以在找到合适的函数后看一看这个遍历起到了多大的作用，共占用了多少的时间，最长占用多少时间。

    #目前的感受是，在测试中找色部没有影响程序的流畅感。
    #完成于凌晨4点，无法正常思考所以实现方式冗杂。尚未改进（便不作太多注释了），但似乎没有太大影响。
            ni=data[ki:].index(19) #
            ki=ki+ni

            if ki%4==0 and data[ki+1]==0 and data[ki+2]==-1: #此处的if也可以精简
                flag=1

                x=(ki/4)%300+810+50
                y=(ki/4)//300+390+75
            else:
                ki=ki+1

        except:
            x,y=960,540
            flag=1
    #此时，输出了x,y



    #计算部
    #将x,y转化为鼠标需要移动的像素数与方向
    #基本思想是在已知视角为90度且通过实验得到鼠标移动1像素在某灵敏度下[角度→像素]的关系的情况下，将目标在屏幕x轴上的比值转化为偏移角度，再将角度转化为鼠标需要移动的方向与像素数，y轴同理
    #可以简化，但本身用时极少
    ax=xs-x
    ay=xs-(y+0.5*(xs-ys))#
    b=xs/((2)**0.5)
    cx=(ax**2+b**2-((2)**0.5)*ax*b)**0.5
    xt=45-360*(asin(ax*(2)**0.5/(2*cx))/(2*pi))
    cy=(ay**2+b**2-((2)**0.5)*ay*b)**0.5
    yt=45-360*(asin(ay*(2)**0.5/(2*cy))/(2*pi))#OW 20灵敏度下，x一圈2727像素 y一圈2700像素
    nx=round(f(xt*2727/(360*2*3.51)))#round后误差仅在1像素即0.1度左右，是可以接受的误差
    #分母（小，大）→速度（快，慢），过头程度（高，较低）,建议y轴过头少x速度快
    ny=round(yt*2700/(360*2*3.51))#nx与ny的分母已经过调试（理论上2可减小到1.5），使得过头程度几乎为0，在这个基础上可以改变函数f或者分母的系数来调整nx与ny的大小

    #操作部
    #使用win32api的mouse event才能模拟鼠标拖动而不是重新设置鼠标位置。后一个方法是不能操作FPS游戏的。
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,nx,ny)

