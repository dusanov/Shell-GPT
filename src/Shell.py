import os
import openai
import datetime

openai.api_key = os.environ.get('OPENAI_API_KEY')
model_engine = "text-davinci-003"

tokens_used = 0
max_tokens=1024
session = ""


def make_a_call(prompt):
    global tokens_used
    response = "testing"
    try:
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = f"{completion.choices[0].text}"
        tokens_used += completion.usage.total_tokens
    except Exception as e:
        response = f"{e}"    
    return response

def do_a_prompt(prompt,log):
    global session
    global tokens_used
    session_prompt = f"\n{datetime.datetime.now()} Prompt:\n {prompt}\n"    
    session += session_prompt
    response = make_a_call(session).encode('utf-8', 'replace').decode()
    response = f"\n{datetime.datetime.now()} [{tokens_used}] Answer:\n {response}\n"
    print(f"{response}")
    session += response
    log.write(session_prompt)
    log.write(response)
    return tokens_used

def reset_session():
    global session
    session = ""