from setuptools import setup

setup(
    name="fps_kernels",
    install_requires=["fps", "kernel_server"],
    entry_points={
        "fps": ["fps-kernels = fps_kernels.routes"]
    },
)
