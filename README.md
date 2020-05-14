Solar Pi
===

Generate SSH Key for Raspberry Pi
---

```zsh
cd ~/.ssh
ssh-keygen -o -f solarpi
ssh-copy-id -i solarpi pi@192.168.1.231 #Raspberry Pi's IP
ssh-add solarpi
```



Install and configure Ansible on MacOS
---

1. `pip install -user ansible`

2. Setup host file in `/etc/ansible/hosts`

```ini
[solarpi]
192.168.1.231
```

3. Check connection with `ping`:

`ansible solarpi -m ping`

This may cause an error first, as SSH will need to be set up too.

Provision Raspberry Pi
---

Run the following command in the ansible directory to configure the Raspberry Pi:

`ansible-playbook solarpi.yml`
