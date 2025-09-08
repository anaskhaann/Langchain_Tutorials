from langchain_community.tools import ShellTool

# create a command to run in shell
shell_command = ShellTool()

result = shell_command.invoke("git status")

print(result)
