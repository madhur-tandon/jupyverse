from setuptools import setup

setup(
    name="fps_content",
    install_requires=["fps", "aiofiles"],
    entry_points={
        "fps": ["fps-content = fps_content.routes"]
    },
)
