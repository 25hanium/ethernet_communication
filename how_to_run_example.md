## PC
### 1. Install ethernet_communication library
   
         pip install "git+https://github.com/25hanium/ethernet_communication.git#egg=ethernet_communication[pytorch]"


### 2. 이더넷 IP 확인.

이더넷을 wifi에 연결 공유 설정. 

※이더넷2가 아닌 라즈베리 파이 연결로 추가된 이더넷으로 설정.

  ![image](https://github.com/user-attachments/assets/636f9b33-bf04-464b-8029-4ec926c2c560)
  

### 3. 이더넷 IP 확인

CMD에서 아래 명령어로 새로 추가된 IP 192.168.xxx.yyy 확인. 

※이때 192.168.xxx.xxx 양식이여야 합니다. 아닐 경우 ip 부여 실패입니다.

      ipconfig


### 4. main_accelerator.py의 'IP' 변수 수정

         IP = 192.168.xxx.1:5000

### 5. Run main_accelerator.py
<br><br>

## 라즈베리파이 
### 1. Install ethernet_communication library

         # git
         sudo apt install git
         # lib
         sudo apt install python3-venv
         python3 -m venv .venv
         pip install git+https://github.com/25hanium/ethernet_communication.git


### 3. main_host.py의 'IP'를 PC와 동일하게 수정. 
### 4. Run main_host.py
<br><br>
## Result

 <img src="https://github.com/user-attachments/assets/e553aa82-d91f-46ab-be18-77f183836b95"  width="500"/>
 <img src="https://github.com/user-attachments/assets/da150566-5c05-45bc-9bf6-f2d0e2dfde57"  width="500"/>
