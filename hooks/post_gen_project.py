import subprocess

subprocess.call(['pip', 'install','virtualenv'])
subprocess.call(['virtualenv','env'])


subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
