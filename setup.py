from setuptools import setup, find_packages

setup(
    name='hand-gesture-volume-control',
    version='0.1.0',
    description='A project for controlling system volume using hand gestures',
    author='Sushank Reddy',
    author_email='sushank979@gmail.com',
    url='https://github.com/sushank99/Real-Time-Hand-Gesture-Volume-Control-System', 
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
        'pycaw',
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
