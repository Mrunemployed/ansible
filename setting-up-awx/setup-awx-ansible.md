# Setup AWX-ANSIBLE

- Guidelines on how to setup ansibleAWX quick and easy.

## Setup the server

- Any linux server with 4 CPUs and 4 GB of RAM preferred for optimal performance.

1. Make sure Ansible is installed
    <sudo apt update>
    <sudo apt install software-properties-common>
    <sudo add-apt-repository --yes --update ppa:ansible/ansible>
    <sudo apt install ansible>
> Note: this is for Ubuntu server 20.0.4 and above.

2. Generate a secret key : <pwgen -N 1 -s 30 > /home/user/directory-name/pwgen.txt>
3. view the Secret key
4. Create a ansible.cfg file with the following contents.
    <mkdir DirectoryProject>
    <cd DirectoryProject/>
    <vim ansible.cfg>
    <# Configure>
    <[defaults]>
    <inventory = ./inventory>
5. Navigate to the <DirectoryProject> dir and save the "setup-awx-ansible.yml" file.
6. run the Playbook with <ansible-playbook setup-awx-ansible.yml>
7. Download and unzip the awx package from :
    <wget https://codeload.github.com/ansible/awx/zip/refs/tags/17.1.0 -O awx-17.1.0.zip>
    <unzip awx-17.1.0.zip>

## Install Ansible AWX

8. Edit the Inventory file located in <awx-17.1.0/installer/inventory> and modify the following section:
    <This will create or update a default admin (superuser) account in AWX, if not provided>
    <then these default values are used>
    <admin_user=<your-admin-user>>
    <admin_password=<your-password>>
    <secret_key=<your-secret-key-from-pwgen.txt>>
9. Navigate to the <awx-17.1.0/installer/> directory and run the installation playbook.
    <ansible-playbook -i inventory install.yml>
10. Verify if the Ansible AWX Containers are running or not - <docker ps>
11. if its a server vm enable portforwarding and send a <http//127.0.0.1> get request to this IP or the loopback IP Address of your host.
    > in case of virtualbox server make sure the network is NAT and add a port forwarding rule of Guest port: 80 to client port:80.
12. Login with the credentials saved in the inventory file of the installation dir on awx installer.
