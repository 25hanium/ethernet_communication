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
