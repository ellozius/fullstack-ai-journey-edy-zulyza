from setuptools import setup, find_packages

setup(
    name="scientific-calculator",
    version="0.1.0",
    description="A scientific calculator for Milestone 1 Foundation - Fullstack AI",
    author="Edy Zulyza",
    author_email="your-email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "scicalc=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
