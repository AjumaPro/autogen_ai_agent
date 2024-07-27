import autogen

config_list =[{
    'model': 'gpt-3.5-turbo-16k',
    'api_key': 'sk-proj-tByhIkH3SY9SQ6zIAPX9T3BlbkFJfDHVTJLspguOG0vX6RI1'
}

]

llm_config={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply Terminate if the task has been completed, otherwise, reply CONTINUE, or for any reason"""
)

task = """Write about variables in java programming"""

user_proxy.initiate_chat(
    assistant,
    message=task
)