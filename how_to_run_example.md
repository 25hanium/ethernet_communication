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
