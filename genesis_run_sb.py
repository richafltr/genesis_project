import modal
import os

app = modal.App.lookup("genesis-sandbox-app", create_if_missing=True)

local_dir = os.path.abspath(".")
remote_dir = "/workspace"
script_name = "run_genesis_sim.py"

image = (
    modal.Image.debian_slim()
    .pip_install("taichi==1.7.3", "genesis-world==0.2.1")
    .add_local_dir(local_path=local_dir, remote_path=remote_dir)
)

with modal.enable_output():
    sb = modal.Sandbox.create(
        image=image,
        app=app,
        workdir=remote_dir,
    )

p = sb.exec("python", script_name)
print(p.stdout.read())

sb.terminate()
