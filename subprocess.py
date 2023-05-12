import subprocess
import os
import json

class TerraformClient:
    def __init__(self, working_dir):
        self.working_dir = working_dir

    def init(self):
        self._run_terraform_cmd(['terraform', 'init'])

    def apply(self, auto_approve=True):
        cmd = ['terraform', 'apply']
        if auto_approve:
            cmd.append('-auto-approve')
        self._run_terraform_cmd(cmd)

    def destroy(self, auto_approve=True):
        cmd = ['terraform', 'destroy']
        if auto_approve:
            cmd.append('-auto-approve')
        self._run_terraform_cmd(cmd)

    def _run_terraform_cmd(self, cmd):
        process = subprocess.Popen(cmd, cwd=self.working_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f'Error running terraform command: {stderr.decode()}')
            return None

        return stdout.decode()

# Usage
tf = TerraformClient('/path/to/your/terraform/files')
tf.init()
tf.apply()
