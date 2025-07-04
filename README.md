update time: 202507051206
# Example
### Download clone
    git clone https://github.com/25hanium/ethernet_communication.git
    
### Check ip
- linux
  
      hostname -I
      admin@stiot:~/src/rs-232 $ python -m pip config set global.break-system-packages true
      Writing to /home/admin/.config/pip/pip.conf


  
- window
  
      ipconfig


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
  libbz2-devwget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
sudo tar xzf Python-3.8.7.tgz
cd Python.3.8.7
./configure
make
sudo make install
python3 -m pip install --upgrade pip

error legacy-install-failure
sudo apt install libgtk-3-dev
