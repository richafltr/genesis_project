# Genesis Project Sandbox

This project demonstrates how to use [Modal](https://modal.com) sandboxes to run simulation code in a fully isolated Python environment, with all dependencies managed in the cloud.

## Contents
- `modal_sb.py`: Script to build a Modal sandbox image, install dependencies, and run simulation code (e.g., `run_genesis_sim.py`) inside the sandbox.
- `run_genesis_sim.py`: Your simulation script (customize as needed).
- `requirements.txt`: Python dependencies for local development and reference.

## Quick Start

### 1. Install requirements locally (for Modal CLI and development)
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Authenticate with Modal
```sh
pip install modal
modal token new
```

### 3. Run the Modal sandbox script
```sh
python modal_sb.py
```

This will:
- Build a Modal image with Python 3.10, `taichi`, and `genesis-world`.
- Mount your project directory into the sandbox.
- Run your simulation script inside the sandbox.

## Notes
- You can modify `modal_sb.py` to run different scripts or pass arguments.
- Modal sandboxes are ephemeral: you cannot SSH into them, but you can execute commands via the Modal SDK.

## License
Specify your license here.
