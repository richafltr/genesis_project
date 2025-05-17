import modal

# Lookup or create the Modal app
app = modal.App.lookup("genesis-sandbox-app", create_if_missing=True)

# Define the image with genesis-world and taichi pinned to the required version
image = (
    modal.Image.debian_slim()
    .pip_install("taichi==1.7.3", "genesis-world==0.2.1")
)

with modal.enable_output():
    # Create the sandbox with the custom image
    sb = modal.Sandbox.create(image=image, app=app)

# Run a command in the sandbox to verify installation
p = sb.exec("python", "-c", "import genesis; print('genesis-world imported successfully!')")
print(p.stdout.read())

# (Optional) Terminate the sandbox when done
sb.terminate()