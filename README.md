update time: 202507051206
# how to run example
    git clone https://github.com/25hanium/ethernet_communication.git

- In host(Rasberry PI), run main_host.py
- In accelerator(PC), run main_accelerator.py
  
# troubleshooting
## Check ip
- linux
  
        hostname -I
- window
  
        ipconfig

## Rasberry PI, pip install error
    sudo apt install \
        build-essential \
        zlib1g-dev \
        libncursesw5-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        wget \
        tk-dev \
        libbz2-dev
    wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
    sudo tar xzf Python-3.8.7.tgz
    cd Python.3.8.7
    ./configure
    make
    sudo make install
    python3 -m pip install --upgrade pip

## Install pytorch
    sudo apt update
    sudo apt-get update
    sudo apt-get dist-upgrade
    
    # git
    sudo apt install git

    # download project
    git clone https://github.com/25hanium/ethernet_communication.git
    
    # pytorch
    sudo apt install libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools
    sudo apt-get install libavutil-dev libavcodec-dev libavformat-dev libswscale-dev
    git clone https://github.com/sungjuGit/PyTorch-and-Vision-for-Raspberry-Pi-4B.git
    cd PyTorch-and-Vision-for-Raspberry-Pi-4B
    sudo pip3 install torch-1.4.0a0+f43194e-cp37-cp37m-linux_armv7l.whl
    sudo pip3 install torchvision-0.5.0a0+9cdc814-cp37-cp37m-linux_armv7l.whl
