import subprocess

def run_terraform_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f'Error running terraform command: {stderr.decode()}')
        return None

    return stdout.decode()

# Usage
print(run_terraform_cmd(['terraform', 'apply', '-auto-approve']))
