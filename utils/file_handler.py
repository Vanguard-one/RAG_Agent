import os
import hashlib
from utils.logger_handler import logger

def get_file_md5(filepath: str):  #获取文件的MD5的十六进制字符串

    if not os.path.exists(filepath):
        logger.error(f"[md5计算]文件{filepath}不存在")
        return

    if not os.path.isfile(filepath):
        logger.error(f"[md5计算]路径{filepath}不是一个文件")

    md5_obj = hashlib.md5()  #通过hashlib函数获取一个MD5对象为md5_obj

    chunk_size = 4096  #4KB分片，避免文件过大爆内存
    try:
        with open(filepath, 'rb') as f:  # 必须二进制读取
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)

            '''
            上面代码等同于
            chunk = f.read(chunk_size)
            while chunk:
                md5_obj.update(chunk)
                chunk = f.read(chunk_size)
            '''
            md5_hex = md5_obj.hexdigest()  #转成十六进制
            return md5_hex
    except Exception as e:
        logger.error(f"计算文件{filepath}md5失败，{str(e)}")
        return None




