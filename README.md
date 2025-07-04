![20250705_050206](https://github.com/user-attachments/assets/378e22e6-e71c-4b9b-9a55-332ab1076f49)# how to run example
## PC
1. Install ethernet_communication library
   
        pip install git+https://github.com/25hanium/ethernet_communication.git


2. 이더넷 IP 확인.

이더넷을 wifi에 연결 공유 설정.

  ![image](https://github.com/user-attachments/assets/636f9b33-bf04-464b-8029-4ec926c2c560)
  

3. 이더넷 IP 확인

CMD에서 아래 명령어로 새로 추가된 IP 192.168.xxx.yyy 확인.

      ipconfig


4. main_accelerator.py의 'IP' 변수 수정

         IP = 192.168.xxx.1:5000

5. Run main_accelerator.py


## 라즈베리파이 
1. Install ethernet_communication library

         # git
         sudo apt install git
         git clone https://github.com/25hanium/ethernet_communication.git
         # lib
         sudo apt install python3-venv
         . .venv-3.7.3/bin/activate
         pip install numpy Pillow


2. pytorch 설치에 에로사항 있음으로 'ethernet_communication/ethernet_communication/__init__.py' 수정
 
         from .host import Host
         
         __all__ = ['Host']

3. main_host.py의 'IP'를 PC와 동일하게 수정. 
4. Run main_host.py

## Result

- PC

추가 예정 사실 별거 었으니 일단 패스.

- 라즈베리파이

![20250705_050206](https://github.com/user-attachments/assets/2d9a8534-9867-4a62-85e0-38ea86f83fb8)
    

  
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
