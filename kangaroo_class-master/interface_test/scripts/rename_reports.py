# -*- coding: utf-8 -*-
# @Time    : 2019-07-27 16:19
# @Author  : Gwen

import time
import os


class RenameReport:
    def __init__(self, file_dir, file_suffix):
        self.file_dir = file_dir
        self.file_suffix = file_suffix

    def get_file_name_list(self):
        """
        获取文件目录下的指定文件名称列表
        :param
            file_dir: 目标文件目录路径
            file_suffix: 指定文件后缀名
        :return: 目录下文件名称列表
        """
        file_name_list = []
        for root, dirs, files in os.walk(self.file_dir):
            for file in files:
                if os.path.splitext(file)[1] == self.file_suffix:
                    file_name_list.append(os.path.join(file))
        print(file_name_list)
        return file_name_list

    def get_last_file_name(self):
        """
        对目录下文件按时间排序，获取最新文件名
        :param
            file_dir: 目标文件目录路径
            file_suffix: 指定文件后缀名
        :return: 返回最新的文件名
        """
        file_list = RenameReport.get_file_name_list(self)
        file_list.sort(key=lambda fn: os.path.getmtime(file_dir + '/' + fn))
        print(file_list)
        last_file_name = file_list[-1]
        print(last_file_name)
        return last_file_name

    def transform_report_name(self):
        """
        将文件名中的时间戳改为时间作为文件名
        :param
            file_dir: 目标文件目录路径
            file_suffix: 指定文件后缀名
        :return: 转换完成的文件名
        """
        last_file_name = RenameReport.get_last_file_name(self)
        name_time_stamp = last_file_name.split('.')[0]
        transform_name = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(int(name_time_stamp)))
        report_name = transform_name + file_suffix
        return report_name

    def rename_report(self):
        """
        修改测试报告名称
        :param
            file_dir: 目标文件目录路径
            file_suffix: 指定文件后缀名
        :return: None
        """
        target_name = RenameReport.transform_report_name(self)
        target_file = RenameReport.get_last_file_name(self)
        os.rename(self.file_dir + '/' + target_file, self.file_dir + '/' + target_name)
        return None


if __name__ == '__main__':
    file_dir, file_suffix = "reports", '.html'
    rp = RenameReport(file_dir, file_suffix)
    time.sleep(3)
    rp.rename_report()
