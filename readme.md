Running Application without installation

Executable is located in directory: target/xamp_linux_launcher/xamp_linux_launcher

<h1>Installing</h1>

1. cd to target/
2. run 'sudo dpkg -i xamp_linux_launcher.deb'
3. installation is run on 'sudo' so you will need to enter your password

<h2>Install location</h2>
<ul>
    <li>By default, application is installed in the opt/ directory.</li>
    <li>If you have issues removing the application through dpkg, then you can uninstall from within opt/ with rm -rf or something else.</li>
</ul>

<h1>Uninstall</h1>

1. Open Terminal
2. run command: 'sudo dpkg --purge xamp_linux_launcher'


<h1>Setup</h1>
<p>When you first install this application, you will need to run a one time setup to configure the executable.  This includes: </p>
<ul>
    <li>Agree to license conditions (GNU AGPL v3)</li>
    <li>Configure xampp executable</li>
</ul>

<h2>Configuring xampp executable</h2>
<p>After agreeing to the terms and conditions, you will have to configure executable.  This program creates an executable icon by linking it to the xampp .run file in the application directory.</p>

<strong>Step 1: </strong> In hte setup utility, click on the browser button to open the file dialog.  Travel to the xampp install path.  Should be located in the opt/ folder if you installed to default location.  See picture below.

![Image description](s1.png)

<strong>Step 2:</strong>cd to lampp/ and find the .run file.  Should be something like <em>opt/lampp/manager-linux-x64.run</em>. See picture below.

![Image description](s2.png)

<strong>Step 3:</strong>Click <strong>finalize</strong> once you have the right executable. 

![Image description](s3.png)


<h2>NOTE</h2>
This application launches xampp under sudo.  A terminal session will open up asking you for your password before running it.  


