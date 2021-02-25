FROM ubuntu:bionic
LABEL   description="Nimble Streamer with SRT"

RUN     apt-get update -y
RUN     apt-get install wget gnupg sudo vim less -y

ENV     TZ=Asia/Vladivostok
RUN     ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN     wget -q -O - http://nimblestreamer.com/gpg.key | sudo apt-key add -
RUN     apt-get update -y
RUN     echo "deb http://nimblestreamer.com/ubuntu bionic/">>/etc/apt/sources.list \
        && apt-get update -y
RUN     apt-get install nimble nimble-srt -y

RUN     sudo echo "management_listen_interfaces = *" >> /etc/nimble/nimble.conf

RUN     rm /etc/nimble/rules.conf
COPY    ./start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
