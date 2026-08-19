import subprocess

agent = subprocess.Popen(["python", "agent/main.py"])
web = subprocess.Popen(["python", "web/app.py"])
remote = subprocess.Popen(["python" ,"agent/remote_agent.py"])

agent.wait()
web.wait()
remote.wait()