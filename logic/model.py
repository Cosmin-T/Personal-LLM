# model.py

from logic.util import *
from langchain_community.llms import Ollama
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(window_size=50)

def engine(prompt):
    temperature = 0.7
    top_p = 0.9
    llm = Ollama(model="codellama")
    response = llm(prompt, temperature=temperature, top_p=top_p)
    return response


def prompt_temp(history, human_input):
    unnecesary_prefixes = ['Assistant', 'Human', 'User', 'AI', 'Answer', 'Question']
    prefixes_str = '. '.join(unnecesary_prefixes)
    prompt_template = f"""
        As an AI, your responses should be factual, straightforward, and devoid of any conversational fillers or politeness conventions. Focus solely on providing the information requested.
        You should not use any of these prefixes: {prefixes_str}

        {history}
        Human: {human_input}
        Assistant:
    """
    print('Prompt Template Generated')
    return prompt_template


def query(human_input):
    memory_data = memory.load_memory_variables({})
    history = memory_data.get('history', '')
    memory.save_context({"input": human_input}, {"output": ""})

    if isinstance(history, list):
        history_str = "\n".join(f"Human: {msg['input']}\nAssistant: {msg['output']}" for msg in history)
    else:
        history_str = history

    prompt_template = prompt_temp(history_str, human_input)

    try:
        full_prompt = f'{prompt_template} \n\nQuestion: {human_input.lower()}'
        response = engine(full_prompt)
        memory.save_context({"input": human_input}, {"output": response})
        return response
    except Exception as e:
        print(f'Error during processing: {e}')
        return f'Error during processing: {e}'

