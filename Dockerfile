FROM jenkins/jenkins:lts
USER root
RUN mkdir /my_app
WORKDIR /my_app
# Adding trusting keys to apt for repositories
RUN apt-get -y update && apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub |
apt-key add -
# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# Updating apt to see and install Google Chrome
RUN apt-get -y update
# Magic happens
RUN apt-get install -y google-chrome-stable
# Installing Unzip
RUN apt-get install -yqq unzip
# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip
http://chromedriver.storage.googleapis.com/`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zi
p
# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# set display port to avoid crash
ENV DISPLAY=:99
# Download and install allure
RUN curl -o allure-2.7.0.tgz -Ls
https://github.com/allure-framework/allure2/releases/download/2.7.0/allure-
2.7.0.tgz
RUN tar -zxvf allure-2.7.0.tgz -C /opt/
RUN ln -s /opt/allure-2.7.0/bin/allure /usr/bin/allure
RUN allure --version
COPY requirements.txt /my_app
RUN pwd
RUN ls -la
RUN apt-get update
RUN apt-get install -y --force-yes python3-pip