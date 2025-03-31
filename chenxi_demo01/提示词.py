# 导入依赖库
import dashscope
import os

# 从环境变量中获取 API Key
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')


# 基于 prompt 生成文本
# 使用 deepseek-v3 模型
def get_completion(prompt, model="deepseek-v3"):
    messages = [{"role": "user", "content": prompt}]  # 将 prompt 作为用户输入
    response = dashscope.Generation.call(
        model=model,
        messages=messages,
        result_format='message',  # 将输出设置为message形式
        temperature=0,  # 模型输出的随机性，0 表示随机性最小
    )
    return response.output.choices[0].message.content  # 返回模型生成的文本


# 任务描述
instruction = """
你的任务是识别用户对手机流量套餐产品的选择条件。
每种流量套餐产品包含三个属性：名称，月费价格，月流量。
根据用户输入，识别用户在上述三种属性上的需求是什么。
"""

# 用户输入
input_text = """
办个100G的套餐。
"""

# prompt 模版。instruction 和 input_text 会被替换为上面的内容
prompt = f"""
# 目标
{instruction}

# 用户输入
{input_text}
"""

print("==== Prompt ====")
print(prompt)
print("================")

# 调用大模型
response = get_completion(prompt)
print(response)
