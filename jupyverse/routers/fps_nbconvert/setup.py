from setuptools import setup

setup(
    name="fps_nbconvert",
    install_requires=["fps", "nbconvert", "fps-content"],
    entry_points={
        "fps": ["fps-nbconvert = fps_nbconvert.routes"]
    },
)
