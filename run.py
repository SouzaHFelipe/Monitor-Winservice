import subprocess
import sys


processes = [
	subprocess.Popen([sys.executable, "-m", "agent.main"]),
	subprocess.Popen([sys.executable, "-m", "web.app"]),
]

try:
	for process in processes:
		process.wait()
except KeyboardInterrupt:
	for process in processes:
		process.terminate()