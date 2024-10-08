from gemini_llm import llm
from handle_system_files import update_search_list, open_file_or_dir, search_files, get_default_paths
from basic_tools import repl_tool, youtube_tool, get_brightness, change_brightness, settings_opener, download_image, brave_web_search, open_url
from pdf_writer import create_and_write_pdf_file
from display import run_command, github_push_instructions
from alter_files import alter_files, file_editor
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver


tools = [get_brightness, change_brightness, create_and_write_pdf_file, update_search_list, 
         open_file_or_dir, search_files, alter_files, settings_opener, run_command,  youtube_tool, open_url, download_image, 
         brave_web_search, file_editor, github_push_instructions, get_default_paths]


memory = MemorySaver()

system_prompt = '''You are a smart OS assistant with the ability to control and manage various operations on the user's operating system. Your capabilities include (but are not limited to) tasks like file manipulation, web search, and executing commands through PowerShell etc. When the user requests an action, you should always attempt to fulfill it using the tools and commands available to you. Only inform the user that a task cannot be completed if there is truly no way to achieve it with the tools or commands at your disposal. You have full access to PowerShell, so if a task can be accomplished using a command, execute it directly. Your primary goal is to maximize the user's experience by efficiently performing tasks and minimizing any instances where you inform the user of limitations.
Important: Ensure that all tasks are handled sequentially. Perform one function call at a time and only proceed to the next task after the current one has been completed. This prevents the system from executing multiple tools in parallel and ensures smooth and orderly task management.'''
agent_executor = create_react_agent(llm, tools, checkpointer=memory, state_modifier=system_prompt)