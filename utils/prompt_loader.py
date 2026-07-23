from utils.config_handler import prompts_conf
from utils.path_tool import get_abs_path
from utils.logger_handler import logger

def load_system_prompts():
    try:
        # 获取prompt的绝对路径，yaml中有相对路径，所以需要调用path_tool中的get_abs_path方法来获取绝对路径
        system_prompt_path = get_abs_path(prompts_conf["main_prompt_path"])
    except KeyError as e:
        logger.error(f"[load_system_prompts]在yaml配置项中没有main_prompt_path配置项")
        raise e

    try:
        #传入获取到的prompt绝对路径来进行读文件操作，并返回数据
        return open(system_prompt_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[load_system_prompts]解析系统提示词出错，{str(e)}")
        raise e


def load_rag_prompts():
    try:
        # 获取prompt的绝对路径，yaml中有相对路径，所以需要调用path_tool中的get_abs_path方法来获取绝对路径
        system_rag_path = get_abs_path(prompts_conf["rag_summarize_prompt_path"])
    except KeyError as e:
        logger.error(f"[load_rag_prompts]在yaml配置项中没有rag_summarize_prompt_path配置项")
        raise e

    try:
        #传入获取到的prompt绝对路径来进行读文件操作，并返回数据
        return open(system_rag_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[load_rag_prompts]解析RAG提示词出错，{str(e)}")
        raise e


def load_report_prompts():
    try:
        # 获取prompt的绝对路径，yaml中有相对路径，所以需要调用path_tool中的get_abs_path方法来获取绝对路径
        system_report_path = get_abs_path(prompts_conf["report_prompt_path"])
    except KeyError as e:
        logger.error(f"[load_report_prompts]在yaml配置项中没有report_prompt_path配置项")
        raise e

    try:
        #传入获取到的prompt绝对路径来进行读文件操作，并返回数据
        return open(system_report_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[load_report_prompts]解析报告生成提示词出错，{str(e)}")
        raise e


if __name__ == '__main__':
    print(load_system_prompts())
