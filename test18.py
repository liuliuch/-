#等额本息
import os


def Month_Equal(贷款本金,还款月数,月利率):
    计划月还款额 = (贷款本金*月利率*pow((1+月利率),还款月数)) / (pow((1+月利率),还款月数)-1)
    月还款额=float_two(计划月还款额)
    还款总额=float_two(计划月还款额 * 还款月数)
    return 月还款额,还款总额

#等额本金
def Month_Decre(贷款本金,还款月数,月利率):
    # 已还款月数 month
    首页月供=float_two((贷款本金/还款月数)+贷款本金*月利率)
    每月月供递减额 =float_two(贷款本金/还款月数*月利率)
    总还款额 =float_two(((贷款本金/还款月数+贷款本金*月利率) + 贷款本金/还款月数*(1 + 月利率))/2*还款月数)
    return 首页月供,每月月供递减额,总还款额


def Month_Interest_Rate(type):
    商业贷款年利率 = 0.0490
    公积金贷款年利率 = 0.0325
    if type == '商业贷款' or type == 1:
        年利率 = 商业贷款年利率
    else:
        年利率 = 公积金贷款年利率
    月利率 = 年利率 / 12
    return 月利率

def float_two(a):
    a ='%.2f'% a
    return float(a)

def sum_float(a,b):
    return float_two(a+b)

def print_info(E_月还款额,E_还款总额,D_首页月供,D_每月月供递减额,D_总还款额):
    print("I 每月等额还款：")
    print("     计划月还款额：",E_月还款额)
    print("     计划还款总额",E_还款总额)
    print("II 逐月递减还款：")
    print("     首月还款:", D_首页月供)
    print('     每月月供递减额:',D_每月月供递减额)
    print("     总还款额", D_总还款额)

def Accu_Base(贷款本金,还款月数):
    # 公积金贷款
    月利率 =Month_Interest_Rate(2)
    E_月还款额,E_还款总额=Month_Equal(贷款本金,还款月数,月利率)
    D_首页月供,D_每月月供递减额,D_总还款额=Month_Decre(贷款本金,还款月数,月利率)
    return E_月还款额, E_还款总额, D_首页月供, D_每月月供递减额, D_总还款额

def Bus_Base(贷款本金,还款月数):
    # 商业贷款
    月利率 = Month_Interest_Rate(1)
    E_月还款额, E_还款总额 = Month_Equal(贷款本金, 还款月数, 月利率)
    D_首页月供, D_每月月供递减额, D_总还款额 = Month_Decre(贷款本金, 还款月数, 月利率)
    return E_月还款额, E_还款总额, D_首页月供, D_每月月供递减额, D_总还款额

def Accu_Loan():
    还款月数 = int(input("贷款年限："))*12
    贷款本金 = int(input("公积金贷款金额："))
    E_月还款额, E_还款总额, D_首页月供, D_每月月供递减额, D_总还款额=Accu_Base(贷款本金,还款月数)
    print_info(E_月还款额, E_还款总额, D_首页月供, D_每月月供递减额, D_总还款额)

def Bus_Loan():
    还款月数 = int(input("贷款年限："))*12
    贷款本金 = int(input("商业贷款金额："))
    E_月还款额, E_还款总额, D_首页月供, D_每月月供递减额, D_总还款额 = Bus_Base(贷款本金, 还款月数)
    print_info(E_月还款额, E_还款总额, D_首页月供, D_每月月供递减额, D_总还款额 )

def Port_Loan():
    贷款年限 = int(input("贷款年限："))
    还款月数 = 贷款年限 * 12
    公积金贷款本金 = int(input("公积金贷款金额："))
    商业贷款本金 = int(input("商业贷款金额："))
    E_月还款额_1, E_还款总额_1, D_首页月供_1, D_每月月供递减额_1, D_总还款额_1=Accu_Base(公积金贷款本金,还款月数)
    E_月还款额_2, E_还款总额_2, D_首页月供_2, D_每月月供递减额_2, D_总还款额_2=Bus_Base(商业贷款本金, 还款月数)
    print_info(sum_float(E_月还款额_1,E_月还款额_2),sum_float(E_还款总额_1,E_还款总额_2),
               sum_float(D_首页月供_1,D_首页月供_2), sum_float(D_每月月供递减额_1,D_每月月供递减额_2),
               sum_float(D_总还款额_1,D_总还款额_2))

def index_app():
    贷款计算方式 = str(input('''贷款计算方式：
    1、公积金贷款
    2、商业贷款
    3、组合贷款
    '''))
    if 贷款计算方式=='1':
        Accu_Loan()
    elif 贷款计算方式=='2':
        Bus_Loan()
    else:
        Port_Loan()
def type_ac(type):
    if  type == '1':
        房价=int(input("请输入房价(元）："))
        面积=int(input("请输入房子面积(m²):"))
        print("总房价为：",房价*面积)
        print("首付为：",int(房价*面积*0.3))
        print("需要贷款金额为：", 房价*面积-int(房价 * 面积 * 0.3))
    index_app()

if __name__ == '__main__':
    while True:
        type_ac(str(input('''
        选择计算方式：
            1、根据房价和面积
            2、直接按贷款金额
        ''')))
        if str(input("是否继续：1：No，2：Yes")) == '1':
            exit(0)