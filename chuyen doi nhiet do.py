import math
#chuyển đổi nhiệt độ từ C sang F
def dof():
    try:
        c=float(input('nhập nhiệt độ C từ bàn phím:  '))
        f=(9*(int(c))/5)+32 #công thức chuyển đổi từ C sang F
        print ('nhiệt độ F có được sau khi chuyển đổi là: ',f,'F')
    except:
        print('nhập đầu vào không đúng định dạng')
if __name__=="__main__":
    dof()