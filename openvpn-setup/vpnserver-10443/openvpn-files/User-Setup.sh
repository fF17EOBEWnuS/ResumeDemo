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

echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDZ130ce5541D+r6t9McKcrAlJxZ81CGZTsMCHRl5bS5276T9DO0L072iggqKvIGS4R3plm6cnTk+9cwpo9Q+8rirfKSiYA/vw+mFMa0fHJKYDrTVfdrVt0F7s8/gr7AEUJlgeWh3ZnOP5EqoFBWdkZsE4kuj0wBe+ABBVJfvG4V1M6+by72d6jj5vNQqWyI2cUGdR5O34AXyI7jd0oUdjnNF+TOVD0u8W8Zc8537vrESQIXoTHCsb+8jgUW+TDznJ97uPwMH1FEnXUX1DB0isHSk1lW3KR03zqMVnWacICcum1B98VwW9K/+E2XRrEE31BGkIPkXVAKQUK3zb/cPQn syeung@raspberrypi' >> /home/syeung/.ssh/authorized_keys
#sshd adjustment
sed -i 's/#Port 22/Port 3022/g' /etc/ssh/sshd_config
sed -i 's/Port 22/Port 3022/g' /etc/ssh/sshd_config
sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config

systemctl restart sshd

apt-get install ufw
ufw allow 3022/tcp
#ufw -force enable #Might not be necessary

echo '/bin/bash' | chsh syeung



