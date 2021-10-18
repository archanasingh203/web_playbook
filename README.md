# web_playbook


Pre-requisites
--------------
- Inventory file : This file contains the address of your host machines and exists at /etc/ansible/hosts on Ansible controller.

Sample /etc/ansible/hosts

[webserver]
<Host IP> ansible_user=<user> ansible_ssh_pass=<pwd>

- Host machines are accessible to Ansible controller via ssh.

$ ansible all -m ping

172.17.0.2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "ping": "pong"
}
- Make sure HTTP is allowed on the port 8080 otherwise UFW module can be used to manage firewall.

Playbook description
---------------------

** Variables: http_port, index_filepath, http_host, download_topath

** Playbook comprises of two plays and is supported on Ubuntu/Debian/Centos/Fedora hosts:
- Play 1: Create webpage, install webserver and publish some server facts on the webpage
 
  + Create customize webpage for http server
  + Collect kernel, datetime, disk info for the hosts and include on webpage
  + Install and Configure webserver
  + Publish the generated webpage on port 8080 instead of default port 80

- Play 2: Test the configuration of the webserver

  + Install wget on remote host if the package is not already present.
  + Compare the webserver hosted webpage with created index file. 

Playbook Execution
------------------

[etc/ansible/playbooks]$ ansible-playbook -i ../hosts webserver.yaml 

Sample command execution on ubuntu host :-

PLAY [Create webpage, install webserver and publish some server facts on the webpage] *****************************************

TASK [Gathering Facts] ********************************************************************************************************
ok: [172.17.0.2]

TASK [Create a index file] ****************************************************************************************************
changed: [172.17.0.2]

TASK [Gather server facts] ****************************************************************************************************
changed: [172.17.0.2]

TASK [apt] ********************************************************************************************************************
[WARNING]: Updating cache and auto-installing missing dependency: python3-apt

[WARNING]: Could not find aptitude. Using apt-get instead

changed: [172.17.0.2]

TASK [Create document root for web domain] ************************************************************************************
changed: [172.17.0.2]

TASK [Copy created index page to web domain directory] ************************************************************************
changed: [172.17.0.2]

TASK [Add port in apache ports config file] ***********************************************************************************
changed: [172.17.0.2]

TASK [Set up virtuahHost] *****************************************************************************************************
changed: [172.17.0.2]

TASK [Restart apache2] ********************************************************************************************************
changed: [172.17.0.2]

TASK [yum] ********************************************************************************************************************
skipping: [172.17.0.2]

TASK [Copy created index page to default web directory] ***********************************************************************
skipping: [172.17.0.2]

TASK [Add port in httpd ports config file] ************************************************************************************
skipping: [172.17.0.2]

TASK [Restart httpd] **********************************************************************************************************
skipping: [172.17.0.2]

TASK [Publish the web page on new http port] **********************************************************************************
ok: [172.17.0.2]

TASK [debug] ******************************************************************************************************************
ok: [172.17.0.2] => {
    "web_content": {
        "accept_ranges": "bytes", 
        "changed": false, 
        "connection": "close", 
        "content_length": "635", 
        "content_type": "text/html", 
        "cookies": {}, 
        "cookies_string": "", 
        "date": "Sun, 17 Oct 2021 19:09:42 GMT", 
        "elapsed": 0, 
        "etag": "\"27b-5ce912b846ddf\"", 
        "failed": false, 
        "last_modified": "Sun, 17 Oct 2021 19:09:39 GMT", 
        "msg": "OK (635 bytes)", 
        "redirected": false, 
        "server": "Apache/2.4.18 (Ubuntu)", 
        "status": 200, 
        "url": "http://localhost:8080", 
        "vary": "Accept-Encoding"
    }
}

PLAY [Test the configuration of a webserver] ***********************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************
ok: [172.17.0.2]

TASK [Check if wget package is installed on Ubuntu/Debian server] ***************************************************************************
ok: [172.17.0.2]

TASK [Install wget on Ubuntu/Debian server if not already present] **************************************************************************
skipping: [172.17.0.2]

TASK [Check if wget package is installed on Centos/Fedora server] ***************************************************************************
skipping: [172.17.0.2]

TASK [Install wget on Centos/Fedora server if not already present] **************************************************************************
skipping: [172.17.0.2]

TASK [Download the default index file] ******************************************************************************************************
changed: [172.17.0.2]

TASK [compare the generated and downloaded index files] *************************************************************************************
changed: [172.17.0.2]

TASK [Display an error message if the two index files are not identical] ********************************************************************
skipping: [172.17.0.2]

PLAY RECAP **********************************************************************************************************************************
172.17.0.2                 : ok=14   changed=6    unreachable=0    failed=0    skipped=8    rescued=0    ignored=0
