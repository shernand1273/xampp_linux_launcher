Running Application without installation

Executable is located in directory: target/xamp_linux_launcher/xamp_linux_launcher

To Install Application

1. cd to target/
2. run 'sudo dpkg -i xamp_linux_launcher.deb'
3. installation is run on 'sudo' so you will need to enter your password


To uninstall

1. Open Terminal
2. run command: 'sudo dpkg --purge xamp_linux_launcher'

Installation location

-By default, application is installed in the opt/ directory.
-If you have issues removing the application through dpkg, then you can uninstall from within opt/ with rm -rf or something else.