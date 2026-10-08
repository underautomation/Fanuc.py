import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version_file = os.path.realpath(os.path.join(os.path.dirname(__file__), "underautomation", "fanuc", "lib", "version.txt"))

with open(version_file, "r", encoding="utf-8") as fh:
    version = fh.read().strip()

setuptools.setup(
    name="UnderAutomation.Fanuc",
    version=version,
    author="UnderAutomation",
    author_email="support@underautomation.com",
    description="Communicate with Fanuc robot controllers and ROBOGUIDE over Telnet KCL, FTP, SNPX, CGTP, RMI and Stream Motion: registers, variables, I/O, programs, alarms, motion, kinematics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://underautomation.com/fanuc",
    project_urls={
        "Documentation": "https://underautomation.com/fanuc/documentation/get-started-python",
        "Source": "https://github.com/underautomation/Fanuc.py",
        "Changelog": "https://github.com/underautomation/Fanuc.py/releases",
        "Issues": "https://github.com/underautomation/Fanuc.py/issues",
    },
    license="Commercial",
    keywords=["robot", "industrial robot", "fanuc", "roboguide", "telnet", "kcl", "ftp", "snpx", "srtp", "rmi", "stream motion", "j519"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    packages=setuptools.find_packages(include=["underautomation", "underautomation.*"]),
    python_requires="<3.14,>=3.7",
    install_requires=[
        "pythonnet==3.0.5",
    ],
    include_package_data=True,
    package_data={
        "underautomation": [
            "py.typed",
            "fanuc/lib/*.dll",
            "fanuc/lib/*.txt",
        ],
    },
)