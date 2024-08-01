clear
clear
apt update -y && apt upgrade -y
apt install python3 python3-pip git -y
apt-get install libjpeg-dev zlib1g-dev -y
cd /etc/
git clone https://github.com/LunaticTunnel/dobot.git
pip3 install -r /etc/dobot/requirements.txt

clear
read -e -p "[*] Input Name   : " name
read -e -p "[*] Input Bot Token   : " bottoken
read -e -p "[*] Input Id Telegram : " admin

sed -i "s/Store Name/$name/g" /etc/dobot/config.json &> /dev/null
sed -i "s/BOT TOKEN/$bottoken/g" /etc/dobot/config.json &> /dev/null
sed -i "s/ID TELEGRAM/$admin/g" /etc/dobot/config.json &> /dev/null
 
cat > /etc/systemd/system/dobot.service << END
[Unit]
Description=SGDO
After=network.target

[Service]
WorkingDirectory=/etc/dobot
ExecStart=/usr/bin/python3 -m main
Restart=always

[Install]
WantedBy=multi-user.target
END

systemctl enable dobot
systemctl start dobot

cd
rm install.sh
echo -e "Successfully create the Digital Ocean/Start bot panel in the bot to start"
