FROM ubuntu:latest

RUN apt update && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt update && \
    apt install google-chrome-stable -y && \
    apt install python3 python3-pip -y

COPY . /app
WORKDIR /app

RUN pip3 install DrissionPage

CMD ["python3", "scripts/auto_login.py"]
