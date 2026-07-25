'''
总结服务类：用户提问，搜索参考资料，将用户的提问和参考资料提交给模型，让模型总结回复
'''
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser

from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompts
from langchain_core.prompts import PromptTemplate
from model.factory import chat_model


def print_prompt(prompt):
    print("="*20, prompt.to_string(), "="*20)
    return prompt.to_string()

class RagSummarizeService(object):
    def __init__(self):
        self.vector_store = VectorStoreService()
        self.retriever = self.vector_store.get_retriver()   #检索器
        self.prompt_text = load_rag_prompts()   #RAG提示词
        self.prompt_template = PromptTemplate.from_template(self.prompt_text)  #将提示词放入模板
        self.model = chat_model
        self.chain = self._init_chain()

    def _init_chain(self):
        chain = self.prompt_template | print_prompt | self.model | StrOutputParser()
        return chain


    def retriever_docs(self, query: str) -> list[Document]:
        return self.retriever.invoke(query)

    #model总结后的内容
    def rag_summarize(self, query: str) -> str:

        context_docs = self.retriever_docs(query)  #检索出来的3条数据，因为k设置的值为3

        context = ""  #后续chain中要传入的参数之一
        counter = 0  #计数
        for doc in context_docs:
            counter += 1
            context += f"【参考资料{counter}】: 参考资料：{doc.page_content} | 参考元数据：{doc.metadata}\n"

        return self.chain.invoke(
            {
                "input": query,
                "context": context,
            }
        )

if __name__ == '__main__':
    rag = RagSummarizeService()

    print(rag.rag_summarize("小户型适合哪一种扫地机器人"))

