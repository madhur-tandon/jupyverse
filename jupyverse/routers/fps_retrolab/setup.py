from setuptools import setup

setup(
    name="fps_retrolab",
    install_requires=["fps", "retrolab", "fps-content"],
    entry_points={
        "fps": ["fps-retrolab = fps_retrolab.routes"]
    },
)
