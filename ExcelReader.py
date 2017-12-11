#!/usr/bin/env python
#-*- coding: gb2312 -*-

__author__ = "Harry Wang"
__date__ = "2017/12/11"

import pandas
from formSubmitter import run

def main():
    df = pandas.read_excel('del.xlsx')
    # print the column names
    # print(df.columns)
    # get the values for a given column
    # for value in df.values:
    #     run(value[0].encode("gb2312"), str(value[1]), str(value[2]))

    for i in xrange(44, len(df.values)):
        value = df.values[i]
        run(value[0].encode("gb2312"), str(value[1]), str(value[2]))
    # print values[0], str(values[1]), str(values[2])

    # get a data frame with selected columns
    # FORMAT = ['Arm_id', 'DSPName', 'Pincode']
    # df_selected = df[FORMAT]


def test():
    temp = '最优化理论与算法(第2版)清华大学研究生公共课教材数学系列'
    print temp.encode("gb2312")

if __name__ == "__main__":
    main()
    # test()