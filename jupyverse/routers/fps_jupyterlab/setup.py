from setuptools import setup

setup(
    name="fps_jupyterlab",
    install_requires=["fps", "jupyterlab", "fps-content"],
    entry_points={
        "fps": ["fps-jupyterlab = fps_jupyterlab.routes"]
    },
)
