# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨
# 时间：2021/11/5 23:09
# 功能：读取yml文件 封装


import yaml
from string import Template
from utils.log_utils import LogUtils
from utils.path_utils import PathUtils


class YamlUtils:
    def __init__(self):
        self.logger = LogUtils().get_logger()

    def get_yml_data(self, data_path, value=None):
        """
        读取yml文件 设置动态变量
        :param data_path: yml文件相对路径
        :param value: 动态变量 如：$username
        :return:
        """

        try:
            # 项目根目录
            project_path = PathUtils().get_project_path()
            # 根目录 + 相对路径 = 绝对路径
            yml_path = project_path + "/" + data_path

            with open(yml_path, "r", encoding="UTF-8") as f:
                text = f.read()
                if value is not None:
                    re = Template(text).safe_substitute(value)
                    json_data = yaml.safe_load(re)
                else:
                    json_data = yaml.safe_load(text)
            return json_data
        except Exception as e:
            self.logger.error(e)

    def get_config(self):
        return self.get_yml_data("config/config.yml")
