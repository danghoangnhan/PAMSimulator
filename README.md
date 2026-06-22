# PAMSimulator

[![Build Status](https://github.com/danghoangnhan/PAMSimulator/actions/workflows/linux-app.yml/badge.svg)](https://github.com/danghoangnhan/PAMSimulator/actions/workflows/linux-app.yml)

[![Build Status](https://github.com/danghoangnhan/PAMSimulator/actions/workflows/window-app.yml/badge.svg)](https://github.com/danghoangnhan/PAMSimulator/actions/workflows/window-app.yml)

The PAMSimulator is a tool designed to conduct experiments based on the Perceptual Assimilation Model (PAM). This application allows researchers and linguists to create and administer PAM experiments for the study of speech sound perception and categorization.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) — the Python package & project manager used by this repo.
- [FFmpeg](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/) — required by `pydub` for audio playback; it must be available on your `PATH`.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. Runtime dependencies are declared in `pyproject.toml` and pinned in `uv.lock` (commit both).

```bash
# 1. Install uv (if you don't have it yet)
#    macOS / Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
#    Windows (PowerShell):
#    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. From the project directory, create the virtual environment and install
#    the locked dependencies. uv manages a local .venv/ for you — no manual
#    virtualenv creation or activation needed.
uv sync

# Managing dependencies (these update pyproject.toml and uv.lock automatically):
uv add <package>        # add a runtime dependency
uv remove <package>     # remove a dependency
uv lock --upgrade       # refresh the lockfile to the latest allowed versions
```

## Usage

Run the application with uv (it resolves and uses the project environment automatically):

```bash
uv run python main.py
```

## Build Executable

PyInstaller lives in the optional `build` dependency group so it is not installed for normal use.

```bash
# Install the build toolchain
uv sync --group build

# Build a standalone executable with PyInstaller (output in dist/)
uv run pyinstaller main.spec
```

## Dependency updates

Automated dependency updates are handled by [Dependabot](.github/dependabot.yml), which opens weekly pull requests for both the Python (`uv`) dependencies and the GitHub Actions used in CI.

## Citation

```
@misc{PAMSimulator,
    author={Tu-Hung Jen},
    title={PAMSimulator - experiments based on the Perceptual Assimilation Model},
    year={2023},
    url={https://github.com/danghoangnhan/PAMSimulator},
}
```
