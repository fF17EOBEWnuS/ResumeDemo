#!/bin/bash

useradd -m syeung
yes '4ppliedMath!' | passwd syeung
echo 'syeung  ALL=(ALL:ALL) ALL' >> /etc/sudoers

# Passwordless login

mkdir /home/syeung/.ssh
chown syeung.syeung /home/syeung/.ssh
touch /home/syeung/.ssh/authorized_keys
chown syeung.syeung /home/syeung/.ssh/authorized_keys

echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrMYKJIKaXW2q38KT1U+iLPb9Aivhh+XTS+zRc25eWORGn9X25zpzpp0L5HhIKluAs6BmkTfABI/2pbtzCVwQGD+XU58depER4pm/yCEaivPM3TW3UuXt4rRIrYccrjHvQXrOIE7Gvsjg3keZlfD4AMuAhR8wJsHhJHaSKCl8g/vKEL+JUYGvB1Qh32PkTcK5cJCdIiTZTxTlJ+91/gBrbKeYHMeide6maGacJp81CtYrHcQGADifo5DemJ1FJYyjTTUrtXrupc65zEqQ2GebPHPBNSsyEXaPfgoZsTpgRASazngFQg0L6wMV4+nH5w3R4NJ9DkCjQfh27kGkWW6mp syeung@M76Y75' >> /home/syeung/.ssh/authorized_keys

#sshd adjustment
sed -i 's/#Port 22/Port 3022/g' /etc/ssh/sshd_config
sed -i 's/Port 22/Port 3022/g' /etc/ssh/sshd_config
sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config

systemctl restart sshd

apt-get install ufw
ufw allow 3022/tcp
ufw -force enable 

echo '/bin/bash' | chsh syeung



