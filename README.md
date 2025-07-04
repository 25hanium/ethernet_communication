# Ethernet Commnunication
이 프로젝트는 CNN 가속을 위해 가속기(PC)와 호스트(라즈베리 파이)를 직렬 LAN로 연결해 구동하기 위한 파이썬 라이브러리입니다.
구별률 최대 75%의 CatFaceNet CNN 모델이 디폴트 모델로 삽입되어 있습니다. 
한장의 이미지를 전송하고 CNN 결과를 반환받는 간단한 예제를 위해 [how_to_run_example.md](https://github.com/25hanium/ethernet_communication/blob/main/how_to_run_example.md)를 참고하세요.

- 연산 결과. (라즈베리파이)

 <img src="https://github.com/user-attachments/assets/2d9a8534-9867-4a62-85e0-38ea86f83fb8"  width="500"/>


  
# troubleshooting
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
