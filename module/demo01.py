"""
    demo01
"""


def yearSalary(salary):
    """
    该模块计算年薪
    :param salary:月薪
    :return: 年薪
    """
    return salary * 12


def daySalary(salary):
    '''
    本模块计算日薪（工作日22.5）
    :param salary:月薪
    :return: 日薪
    '''
    return salary/22.5

if __name__ == "__main__":
    print(yearSalary(3000))