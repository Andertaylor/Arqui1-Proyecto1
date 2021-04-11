# Arqui1-Proyecto1

EL siguiente es el desarrollo de una aplicación para mejorar el contraste de una imagen en escala de grises, utilizando el lenguaje de programación Python y la arquitectura ARM. A continuación se presentan las generalidades que se requieren para la ejecución del proyecto.

# Características del sistema operativo, lenguajes y ambiente de programación:
  1. Versión de Ubuntu: Ubuntu 20.04.2 LTS, Release:	20.04
  2. Versión de Python: Python 3.8.5
  3. Versión de pip3: pip 21.0.1 
  4. Ambiente de programación en Python: Pycharm Community Edition

# Instalación de dependencias para Python:

  1. Abrimos una terminal con la combinación de teclas: 
    
    ctrl+alt+T
  
  2. Podemos revisar la versión actual que Python que se tiene con el comando:     
    
    $python --version
  
  3. Si la versión que se tiene es menor a 3.8.x, nos preparamos a instalar la nueva versión con el comando: 
    
    $sudo apt update
  
  4. Se procede a instalar la versión:
  
    $sudo apt install python3.8

# Instalación de pip3:
  
  1. Se prepara la instalación con el comando:
    $sudo apt update

  3. Se procede a instalar:
    $sudo apt install python3-pip 

# Instalación de dependencias para Pycharm

Desde el centro de Software de Ubuntu, se busca el programa Pycharm Community Edition y se procede a instalar. Una vez instalado, hay que configurar los ajustes de Pycharm e instalar las bibliotecas a utulizar en Python:

  1. Abrimos la pestaña de File -> Settings -> Project: <nombre del proyecto> -> Python Interpreter
  
  2. Una vez en esta última sección, se pueden ver las bibliotecas preinstaladas en el ambiente de programación. Se debe verificar que se encuentre las siguientes: matpltlib, numpy, opencv-python, pip, pygame, pyparsing, python-dateutil.
     
  3. De no encontrarse alguna instalada, solo es cuestión de buscar el ícono de "+" que permite agregar una nueva biblioteca, al presionarlo aparecerá un buscador donde se debe escribir el nombre de la biblioteca deseada, presionar el botón de instalar y plaicar los cambios realizados.

# Instalación de las herramientas cruzadas de ARM:

La siguiente sección fue tomada del curso de Arquitectura de Computadores 1, donde la instalación de estas herramientas se basó en el siguiente enlace: https://mynewt.apache.org/latest/get_started/native_install/cross_tools.html

  1. Abrimos una terminal con la combinación de teclas: 
    ctrl+alt+T
  
  2. Abrimos con el comando cd la ruta de la carpeta donde se va a ejecutar el código de ARM, luego se ejecuta el siguiente comando:
    $sudo apt-get install gcc-arm-linux-gnueabi gcc-arm-none-eabi
   
  3. Para enlazar y compilar el código de ARM, se ejecutan los siguientes comandos:
    $arm-linux-gnueabi-as <nombre del archivo>.s -o <nombre del archivo>.o
    $arm-linux-gnueabi-ld <nombre del archivo>.o -o <nombre del archivo>
  
  3. En este cas de va a utilizar QEMU para ejecutar el programa:
    $sudo apt get install qemu
    $qemu-arm <nombre del archivo>
  
  Ojo, para este paso se solicita que la ejecución se haga desde Python directamente, sin recurrir a la terminal de ubuntu.
  

    
  
  

