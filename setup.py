from setuptools import setup, find_packages
import os


directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='art-fid',
      version='0.0.2',
      url='https://github.com/matthias-wright/art-fid',
      author='Matthias Wright',
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['pycli = pycli.__main__:main']
      },
      install_requires=['numpy>=1.19.5,<2',
                        'Pillow>=7.1.2',
                        'tqdm>=4.60.0',
                        'scikit-learn',
                        'torch',
                        'lpips',
                        'torchvision>=0.9.0',
                        'scipy',
                        'requests>=2.27.0, <3'],
      python_requires='>=3.8',
      license='Apache License 2.0',
      description='ArtFID: Quantitative Evaluation of Neural Style Transfer',
      long_description=long_description,
      long_description_content_type='text/markdown')
