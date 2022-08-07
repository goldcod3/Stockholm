# Stockholm
Ransomware developed in 42Madrid.

<img src='https://media.giphy.com/media/damUMYvgrroqw2hxSu/giphy.gif' width=330 heigth= 330/>
Encrypt and decrypt multiple files and directories.

***WARNING:***
- This program was written for educational purposes. The responsibility for the use and distribution of the tool lies with the user. Use it at your own risk and enjoy! 
- This program was designed to affect only files located in the current user's '~/infection' directory.Use caution with files located in that directory.
- When the files are encrypted, a 'totem.key' file is generated, which contains the encryption password. To encrypt several times different files with the same key, do not move this file from its location.
- It is recommended to run the program in a docker container or a virtual machine.
- goldcod3 - [Don't lose the totem.key]

# Run - Options
```
# Default mode - Encrypt files
- ./stockholm 
# Reverse mode - Decrypt files
- ./stockholm -r + 'pass_key'
# Silent mode
- ./stockholm -s | ./stockholm -r + 'pass_key' -s
# Print version
- ./stockholm -v
# Print help
- ./stockholm -h
```
# Run Docker Test
- Install '[Docker Desktop](https://www.docker.com/products/docker-desktop/)' and run the app.
- Install 'make' and use the Makefile for buid a container and get a bash:
```
make && make exec
```
```
# Build image and container
->> make
# Get a bash from container
->> make exec
# Build a new container
->> make dock
# Build image
->> make image
# Remove image and container
->> make fclean
```
- In the container, run **run_test.sh**
```
cd; cd test; ./run_test.sh
```
- Unzip the **out.zip** and run **stockholm**
```
unzip out.zip 
cd out; ./stockholm
```

For more information about the project click [here](https://goldcod3.github.io/project/proyect-stockholm)

---
Finished proyect.

![lgomes-o's 42 stockholm Score](https://badge42.vercel.app/api/v2/cl4osmqtg006109jvtxcd7k3u/project/2669379)
