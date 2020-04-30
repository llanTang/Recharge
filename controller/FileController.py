from exception.CustomErrorCode import *
from exception.ControllerException import *


class fileController:
    # 静态方法
    def readFile(filePath):
        index = 0
        if (filePath is None):
            raise ControllerException(CustomErrorCode.PARAM_ERROR, "文件读取位置为空")
        result = []
        for line in open(filePath):
            index = index + 1
            result.append(list(map(float,line.strip('\n').split(','))))
        return result, index
