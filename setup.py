import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JenAssistant",
    version="0.0.5",
    author="Vishal Balakrishna Shenoy",
    author_email="vishal.bshenoy@gmail.com",
    description="A package which can be used for virtual assistants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VishalShenoy2002/JEN",
    project_urls={
        "Bug Tracker": "https://github.com/VishalShenoy2002/JEN/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["pyttsx3","SpeechRecognition",'pyautogui','werkzeug','pipwin'],
    keywords=['python', 'virtual assistant', 'assistant', 'Jen', 'Jen Assistant', 'JEN'],
    python_requires=">=3.6",
)