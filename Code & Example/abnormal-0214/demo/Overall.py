import json


def main(NUM):
    Jlabel = ['J17', 'J16', 'J15', 'J14', 'J13', 'J12', 'J11', 'J21', 'J22', 'J23', 'J24', 'J25', 'J26', 'J27']
    Tlabel = ['T17', 'T16', 'T15', 'T14', 'T13', 'T12', 'T11', 'T21', 'T22', 'T23', 'T24', 'T25', 'T26', 'T27']
    Rlabel = ['R17', 'R16', 'R15', 'R14', 'R13', 'R12', 'R11', 'R21', 'R22', 'R23', 'R24', 'R25', 'R26', 'R27']
    Clabel = ['C17', 'C16', 'C15', 'C14', 'C13', 'C12', 'C11', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27']
    Glabel = ['G1314', 'G1413', 'G1415', 'G1514', 'G1516', 'G1615', 'G1617', 'G1716', 'G1213', 'G1312', 'G1112',
              'G1211', 'G1121', 'G2111', 'G2122', 'G2221', 'G2223', 'G2322', 'G2324', 'G2423', 'G2324', 'G2423',
              'G2425', 'G2524', 'G2526', 'G2625', 'G2627', 'G2726']
    Olabel = ['O1314', 'O1413', 'O1415', 'O1514', 'O1516', 'O1615', 'O1617', 'O1716', 'O1213', 'O1312', 'O1112',
              'O1211', 'O1121', 'O2111', 'O2122', 'O2221', 'O2223', 'O2322', 'O2324', 'O2423', 'O2425', 'O2524',
              'O2526', 'O2625', 'O2627', 'O2726']

    Jlabel1 = ['J37', 'J36', 'J35', 'J34', 'J33', 'J32', 'J31', 'J41', 'J42', 'J43', 'J44', 'J45', 'J46', 'J47']
    Tlabel1 = ['T37', 'T36', 'T35', 'T34', 'T33', 'T32', 'T31', 'T41', 'T42', 'T43', 'T44', 'T45', 'T46', 'T47']
    Rlabel1 = ['R37', 'R36', 'R35', 'R34', 'R33', 'R32', 'R31', 'R41', 'R42', 'R43', 'R44', 'R45', 'R46', 'R47']
    Clabel1 = ['C37', 'C36', 'C35', 'C34', 'C33', 'C32', 'C31', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47']
    Glabel1 = ['G3334', 'G3433', 'G3435', 'G3534', 'G3536', 'G3635', 'G3637', 'G3736', 'G3233', 'G3332', 'G3132',
               'G3231', 'G3141', 'G4131', 'G4142', 'G4241', 'G4243', 'G4342', 'G4344', 'G4443', 'G4445', 'G4544',
               'G4546', 'G4645', 'G4647', 'G4746']
    Olabel1 = ['O3334', 'O3433', 'O3435', 'O3534', 'O3536', 'O3635', 'O3637', 'O3736', 'O3334', 'O3433', 'O3233',
               'O3332', 'O3132', 'O3231', 'O3141', 'O4131', 'O4142', 'O4241', 'O4243', 'O4342', 'O4344', 'O4443',
               'O4344', 'O4443', 'O4445', 'O4544', 'O4546', 'O4645', 'O4647', 'O4746']

    Xj, Yj = [], []
    Xt, Yt = [], []
    Xr, Yr = [], []
    Xc, Yc = [], []
    Xg, Yg = [], []
    Xo, Yo = [], []

    Xj1, Yj1 = [], []
    Xt1, Yt1 = [], []
    Xr1, Yr1 = [], []
    Xc1, Yc1 = [], []
    Xg1, Yg1 = [], []
    Xo1, Yo1 = [], []

    # 打开文件,r是读取,encoding是指定编码格式
    with open('../json/' + NUM + '.json', 'r', encoding='utf-8') as fp:
        print(type(fp))  # 输出结果是 <class '_io.TextIOWrapper'> 一个文件类对象

        # load()函数将fp(一个支持.read()的文件类对象，包含一个JSON文档)反序列化为一个Python对象
        data = json.load(fp)

        print(type(data))  # 输出结果是 <class 'dict'> 一个python对象,json模块会根据文件类对象自动转为最符合的数据类型,所以这里是dict
        fp.close()

    for i in data['shapes']:
        if i['label'][0:3] in Jlabel and i['label'][2:4] != '7D':
            Xj.append(i['points'][0][0])
            Yj.append(i['points'][0][1])
        elif i['label'][0:3] in Tlabel and i['label'][2:4] != '7D':
            Xt.append(i['points'][0][0])
            Yt.append(i['points'][0][1])
        elif i['label'][0:3] in Rlabel and i['label'][2:4] != '7D':
            Xr.append(i['points'][0][0])
            Yr.append(i['points'][0][1])
        elif i['label'][0:3] in Clabel and i['label'][2:4] != '7D':
            Xc.append(i['points'][0][0])
            Yc.append(i['points'][0][1])
        elif i['label'] in Glabel:
            Xg.append(i['points'][0][0])
            Yg.append(i['points'][0][1])
        elif i['label'] in Olabel:
            Xo.append(i['points'][0][0])
            Yo.append(i['points'][0][1])
        elif i['label'][0:3] in Jlabel1 and i['label'][2:4] != '7D':
            Xj1.append(i['points'][0][0])
            Yj1.append(i['points'][0][1])
        elif i['label'][0:3] in Tlabel1 and i['label'][2:4] != '7D':
            Xt1.append(i['points'][0][0])
            Yt1.append(i['points'][0][1])
        elif i['label'][0:3] in Rlabel1 and i['label'][2:4] != '7D':
            Xr1.append(i['points'][0][0])
            Yr1.append(i['points'][0][1])
        elif i['label'][0:3] in Clabel1 and i['label'][2:4] != '7D':
            Xc1.append(i['points'][0][0])
            Yc1.append(i['points'][0][1])
        elif i['label'] in Glabel1:
            Xg1.append(i['points'][0][0])
            Yg1.append(i['points'][0][1])
        elif i['label'] in Olabel1:
            Xo1.append(i['points'][0][0])
            Yo1.append(i['points'][0][1])

    # print("Xj:", Xj)
    # print("Yj:", Yj)
    # print("Xt:", Xt)
    # print("Yt:", Yt)
    # print("Xr:", Xr)
    # print("Yr:", Yr)
    # print("Xc:", Xc)
    # print("Yc:", Yc)
    # print("Xg:", Xg)
    # print("Yg:", Yg)
    # print("Xo:", Xo)
    # print("Yo:", Yo)

    import numpy as np
    from scipy.stats import pearsonr

    # J1+J2
    x1 = np.array(Xj)
    y1 = np.array(Yj)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z1 = np.polyfit(x1, y1, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p1 = np.poly1d(z1)
    # 在屏幕上打印拟合多项式
    print(p1)

    m1 = p1(x1)
    correlation_coefficient, p_value = pearsonr(y1, m1)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp1 = np.arange(x1.min(), x1.max(), 1)
    fx1 = p1(xp1)

    # T1+T2
    x2 = np.array(Xt)
    y2 = np.array(Yt)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z2 = np.polyfit(x2, y2, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p2 = np.poly1d(z2)
    # 在屏幕上打印拟合多项式
    print(p2)

    m2 = p2(x2)
    correlation_coefficient, p_value = pearsonr(y2, m2)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp2 = np.arange(x2.min(), x2.max(), 1)
    fx2 = p2(xp2)

    # R1+R2
    x3 = np.array(Xr)
    y3 = np.array(Yr)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z3 = np.polyfit(x3, y3, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p3 = np.poly1d(z3)
    # 在屏幕上打印拟合多项式
    print(p3)

    m3 = p3(x3)
    correlation_coefficient, p_value = pearsonr(y3, m3)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp3 = np.arange(x3.min(), x3.max(), 1)
    fx3 = p3(xp3)

    # C1+C2
    x4 = np.array(Xc)
    y4 = np.array(Yc)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z4 = np.polyfit(x4, y4, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p4 = np.poly1d(z4)
    # 在屏幕上打印拟合多项式
    print(p4)

    m4 = p4(x4)
    correlation_coefficient, p_value = pearsonr(y4, m4)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp4 = np.arange(x4.min(), x4.max(), 1)
    fx4 = p4(xp4)

    # G1+G2
    x5 = np.array(Xg)
    y5 = np.array(Yg)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z5 = np.polyfit(x5, y5, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p5 = np.poly1d(z5)
    # 在屏幕上打印拟合多项式
    print(p5)

    m5 = p5(x5)
    correlation_coefficient, p_value = pearsonr(y5, m5)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp5 = np.arange(x5.min(), x5.max(), 1)
    fx5 = p5(xp5)

    # O1+O2
    x6 = np.array(Xo)
    y6 = np.array(Yo)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z6 = np.polyfit(x6, y6, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p6 = np.poly1d(z6)
    # 在屏幕上打印拟合多项式
    print(p6)

    m6 = p6(x6)
    correlation_coefficient, p_value = pearsonr(y6, m6)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp6 = np.arange(x6.min(), x6.max(), 1)
    fx6 = p6(xp6)

    # J3+J4
    x11 = np.array(Xj1)
    y11 = np.array(Yj1)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z11 = np.polyfit(x11, y11, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p11 = np.poly1d(z11)
    # 在屏幕上打印拟合多项式
    print(p11)

    m11 = p11(x11)
    correlation_coefficient, p_value = pearsonr(y11, m11)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp11 = np.arange(x11.min(), x11.max(), 1)
    fx11 = p11(xp11)

    # T3+T4
    x21 = np.array(Xt1)
    y21 = np.array(Yt1)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z21 = np.polyfit(x21, y21, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p21 = np.poly1d(z21)
    # 在屏幕上打印拟合多项式
    print(p21)

    m21 = p21(x21)
    correlation_coefficient, p_value = pearsonr(y21, m21)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp21 = np.arange(x21.min(), x21.max(), 1)
    fx21 = p21(xp21)

    # R3+R4
    x31 = np.array(Xr1)
    y31 = np.array(Yr1)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z31 = np.polyfit(x31, y31, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p31 = np.poly1d(z31)
    # 在屏幕上打印拟合多项式
    print(p31)

    m31 = p31(x31)
    correlation_coefficient, p_value = pearsonr(y31, m31)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp31 = np.arange(x31.min(), x31.max(), 1)
    fx31 = p31(xp31)

    # C3+C4
    x41 = np.array(Xc1)
    y41 = np.array(Yc1)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z41 = np.polyfit(x41, y41, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p41 = np.poly1d(z41)
    # 在屏幕上打印拟合多项式
    print(p41)

    m41 = p41(x41)
    correlation_coefficient, p_value = pearsonr(y41, m41)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp41 = np.arange(x41.min(), x41.max(), 1)
    fx41 = p41(xp41)

    # G3+G4
    x51 = np.array(Xg1)
    y51 = np.array(Yg1)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z51 = np.polyfit(x51, y51, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p51 = np.poly1d(z51)
    # 在屏幕上打印拟合多项式
    print(p51)

    m51 = p51(x51)
    correlation_coefficient, p_value = pearsonr(y51, m51)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp51 = np.arange(x51.min(), x51.max(), 1)
    fx51 = p51(xp51)

    # O3+O4
    x61 = np.array(Xo1)
    y61 = np.array(Yo1)
    # 使用polyfit方法来拟合,并选择多项式,这里先使用2次方程
    z61 = np.polyfit(x61, y61, 2)
    # 使用poly1d方法获得多项式系数,按照阶数由高到低排列
    p61 = np.poly1d(z61)
    # 在屏幕上打印拟合多项式
    print(p61)

    m61 = p61(x61)
    correlation_coefficient, p_value = pearsonr(y61, m61)
    print("相关系数：", correlation_coefficient)

    # 求对应x的各项拟合函数值
    xp61 = np.arange(x61.min(), x61.max(), 1)
    fx61 = p61(xp61)

    # 绘制图像
    # import matplotlib.pyplot as plt
    # from PIL import Image
    #
    # plt.rc("font", family="Microsoft YaHei")
    # # 插入背景图片
    # img_path = '../img/' + NUM + ".jpg"
    # img = plt.imread(img_path)
    # img_info = Image.open(img_path)
    # fig, ax = plt.subplots()
    # # 指定图片的高度和宽度
    # # ax.imshow(img, extent=[0, 2904, 0, 1536])
    # ax.imshow(img, origin='lower', extent=[0, img_info.width, 0, img_info.height])
    #
    # # 绘制坐标系散点数据及拟合曲线图
    # plot1 = plt.plot(x1, y1, ".", markersize=1, color='blue', label='J')
    # plot3 = plt.plot(x2, y2, '.', markersize=1, color='orange', label='T')
    # plot5 = plt.plot(x3, y3, '.', markersize=1, color='green', label='R')
    # plot7 = plt.plot(x4, y4, '.', markersize=1, color='red', label='C')
    # # plot9 = plt.plot(x5, y5, '.', markersize=1, color='m', label='G')
    # # plot11 = plt.plot(x6, y6, '.', markersize=1, color='peru', label='O')
    #
    # plot13 = plt.plot(x11, y11, ".", markersize=1, color='blue')
    # plot15 = plt.plot(x21, y21, '.', markersize=1, color='orange')
    # plot17 = plt.plot(x31, y31, '.', markersize=1, color='green')
    # plot19 = plt.plot(x41, y41, '.', markersize=1, color='red')
    # # plot21 = plt.plot(x51, y51, '.', markersize=1, color='m')
    # # plot23 = plt.plot(x61, y61, '.', markersize=1, color='peru')
    #
    # plot2 = plt.plot(xp1, fx1, 'r', linewidth=0.6, label='polyfit J')
    # plot4 = plt.plot(xp2, fx2, 'b', linewidth=0.6, label='polyfit T')
    # plot6 = plt.plot(xp3, fx3, 'k', linewidth=0.6, label='polyfit R')
    # plot8 = plt.plot(xp4, fx4, 'y', linewidth=0.6, label='polyfit C')
    # # plot10 = plt.plot(xp5, fx5, 'c', linewidth=0.6, label='polyfit G')
    # # plot12 = plt.plot(xp6, fx6, 'm', linewidth=0.6, label='polyfit O')
    #
    # plot14 = plt.plot(xp11, fx11, 'r', linewidth=0.6)
    # plot16 = plt.plot(xp21, fx21, 'b', linewidth=0.6)
    # plot18 = plt.plot(xp31, fx31, 'k', linewidth=0.6)
    # plot20 = plt.plot(xp41, fx41, 'y', linewidth=0.6)
    # # plot22 = plt.plot(xp51, fx51, 'c', linewidth=0.6)
    # # plot24 = plt.plot(xp61, fx61, 'm', linewidth=0.6)
    #
    # plt.xlabel('x-price')
    # plt.ylabel('y-amount')
    #
    # # 隐藏刻度值
    # ax = plt.gca()
    # ax.axes.xaxis.set_ticklabels([])
    # ax.axes.yaxis.set_ticklabels([])
    #
    # # 显示图例
    # num1 = 1.01
    # num2 = 0
    # num3 = 3
    # num4 = 0
    # plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4)
    # # 右边距调整
    # plt.subplots_adjust(right=0.8)
    # # 坐标轴间距调整
    # plt.xticks(ticks=np.arange(0, img_info.width, 100))
    # plt.yticks(ticks=np.arange(0, img_info.height, 100))
    #
    # if y3.mean() < y2.mean():
    #     # y轴翻转
    #     plt.gca().invert_yaxis()
    #
    # import os
    # if not os.path.exists(NUM):
    #     os.mkdir(NUM)
    #
    # plt.title(NUM)
    # print(NUM + ": OK! ! !")
    # plt.savefig('img/quankou-' + NUM + '.png', dpi=400)
    # plt.savefig(NUM + '/quankou-' + NUM + '.png', dpi=400)
    # plt.show()


all = ['1-曾悦', '10-宋群英', '11-宋文', '12-唐嘉仪', '13-王柄权', '14-王玮璇', '15-谢川霞', '16-谢容', '17-徐玲玲',
       '18-杨红梅', '19-李茜颖子', '2-范凯筌', '20-刘娟', '21-刘雪梅', '22-唐平原', '23-陈华', '24-陈静', '25-陈露',
       '26-郭晓语', '27-黄曦之', '28-敬景怡', '29-邵懿阳', '30-袁杜', '31-赵韫莹', '32-钟明浩', '5-李欣珂',
       '6-林小婧', '7-罗鸿谕', '8-罗莲', '9-罗雯', '3-韩雨彤']

for i in all:
    main(i)