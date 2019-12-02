import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='sem_cloud',
     version='0.1',
     scripts=['sem_cloud'] ,
     author="Kerla Raju",
     author_email="kerlarajumca@gmail.com",
     description="Semiotics Cloud Application utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/kerlarajumca/sem_cloud",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )