import subprocess
subprocess.call(["conda", 
"create","--name","{{cookiecutter.directory_name}}",
"python={{cookiecutter.python_version}}","--file","requirements.txt"])
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])