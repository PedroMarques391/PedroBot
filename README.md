
!width="150px" height="150px>

<div>Olá, eu sou o PedroBot </div>

Bot com funções básicas construído em python

<div>
Para usar você precisa executar os seguintes comandos: 

</div>

 # #
  ```
  pip install pyautogui
  ```
  ```
  pip install selenium
 ```
 ```
  pip install pyttsx3
 ```
 ```
  pip install pytube
  ```
  ```
  pip install colorama 
  ```
  ```
  pip install chatterbot==1.0.4
  ```
  ```
  pip install pytz
  ```
 
 **OBSERVAÇÃO AO INSTALAR CHATTERBOT:**
 <p>
  
  Se ocorrer algum erro de atribuição ao installar o chatterbot <p> (AttributeError: module 'time' has no attribute 'clock') <p>
   
 
   ```
   if win 32 or jython:
        time_func = time.clock
   else: 
        time_func = time.time
   ```
  <b> 
    Basta comentar o comando "time_func = time.clock e adicionar o comando 'pass', veja o exemplo: 
    
   ```
   if win 32 or jython:
        #time_func = time.clock
        pass
   else: 
        time_func = time.time
   ```
  
</p>
    
    Agora está prontinho para usar :)
