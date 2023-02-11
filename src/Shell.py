import os
import openai
import datetime
import tiktoken

openai.api_key = os.environ.get('OPENAI_API_KEY')
model_engine = "text-davinci-003" #"text-ada-001"

tokens_used_per_session = 0
max_tokens=1024
session = ""


def make_a_completion_call(prompt, stream=False):
    global tokens_used_per_session
    response = "testing"
    try:
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
            stream=stream
        )
        if stream:
            # collected_events = []
            completion_text = ''
            print(f"\n")
            for event in completion:
                # collected_events.append(event)
                event_text = event['choices'][0]['text']
                completion_text += event_text
                print(f"{event_text}",end="")
            print(f"\n")
            response = f"{completion_text}"
            tokens_used_per_session += num_tokens_from_string(response)
        else:
            response = f"{completion.choices[0].text}"
            print(f"{response}")
            tokens_used_per_session += completion.usage.total_tokens
    except Exception as e:
        response = f"{e}"    
    return response

def do_a_prompt(prompt,log):
    global session
    global tokens_used_per_session
    session_prompt = f"\n{datetime.datetime.now()} Prompt:\n {prompt}\n"    
    session += session_prompt
    response_text = make_a_completion_call(session,stream=True)#.encode('utf-8', 'replace').decode()
    response_text = f"\n{datetime.datetime.now()} [{tokens_used_per_session}] Answer:\n {response_text}\n"
    session += response_text
    log.write(session_prompt)
    log.write(response_text)
    return tokens_used_per_session

def reset_session():
    global session
    session = ""

def list_models():
    try:
        response = []
        for model in openai.Model.list().data:
            response.append(model.id)
        response = f"\n".join(response)
    except Exception as e:
        response = f"{e}"
    return response

def current_model():
    return model_engine

def set_model(model):
    global model_engine
    model_engine = model

def num_tokens_from_string(string: str, encoding_name: str = "gpt2") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens