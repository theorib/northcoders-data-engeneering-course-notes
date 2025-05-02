# 2025-04-28 - Day 29 | AWS Console and EC2
## DevOps
The practice of integrating operational deployment with software development is called DevOps.
- Continuous Integration
- Continuous Deployment
- Infrastructure as Code
- Monitoring and alerting

## 
```bash
mv Downloads/march-2025-cohort.pem ~/.ssh
chmod 400 ~/.ssh/de-sample-server_2025_04_28.pem
```


### SSH Login
```bash
ssh -i "/Users/theorib/.ssh/de-sample-server_2025_04_28.pem"  ubuntu@ec2-13-40-107-82.eu-west-2.compute.amazonaws.com

# advanced a
ssh -i "/Users/theorib/.ssh/de-sample-server_2025_04_28.pem"  ubuntu@ec2-18-171-243-220.eu-west-2.compute.amazonaws.com

# advanced b
ssh -i "/Users/theorib/.ssh/de-sample-server_2025_04_28.pem"  ubuntu@ec2-18-134-74-107.eu-west-2.compute.amazonaws.com


```
### Set a user password for the ubuntu user
```bash
sudo passwd
```

### Upgrade Apt
```bash
sudo apt update
sudo apt upgrade
```

### Install ZSH
```bash
sudo apt update
sudo apt install zsh

# change default shell to ZSH
chsh -s $(which zsh)
```
### Install Oh My ZSH!
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Oh My ZSH Plugins:
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/jirutka/zsh-shift-select.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-shift-select

```

### Install pyenv
```bash
# https://github.com/pyenv/pyenv?tab=readme-ov-file#linuxunix
curl -fsSL https://pyenv.run | bash

# https://github.com/pyenv/pyenv?tab=readme-ov-file#bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init - bash)"' >> ~/.profile

# https://github.com/pyenv/pyenv?tab=readme-ov-file#c-restart-your-shell
exec "$SHELL"

# https://github.com/pyenv/pyenv?tab=readme-ov-file#d-install-python-build-dependencies
# https://github.com/pyenv/pyenv/wiki#suggested-build-environment
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

pyenv install 3.13.3
pyenv global 3.13.3
```

### Install Postgres
```bash
sudo apt install postgresql
```

### Optionally Install Apache
```bash
apt update
sudo apt install apache2
sudo service apache2 start
# sudo service apache2 stop
```


### Restarting your shell
```bash
exec "$SHELL"
```

### Clone Git Repo
```bash
git clone https://github.com/theorib/de-sample-server.git
```

### Add .env file
```bash
DB_PORT=5432
DB_DB=postgres
DB_PASSWORD=cunwyF-tysrer-picgo7
DB_HOST=de-advanced-db.ctecqawm2mra.eu-west-2.rds.amazonaws.com
DB_USER=postgres
LOG_LEVEL=debug
```

### Install Git CLI
```bash
sudo apt install gh
```



```bash
# sudo psql --host=de-sample-server-db-1.ctecqawm2mra.eu-west-2.rds.amazonaws.com --port=5432 --dbname=postgres --username=postgres
sudo psql --host=de-sample-server-db-1.ctecqawm2mra.eu-west-2.rds.amazonaws.com --port=5432 --dbname=postgres --username=postgres -f ./seed.sql


# on the advanced
sudo psql --host=de-advanced-db.ctecqawm2mra.eu-west-2.rds.amazonaws.com --port=5432 --dbname=postgres --username=postgres -f ./src/data/seed.sql

```

```bash
psql \l
-w # asks for password
```


### Port Forwarding
```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000
```

### Starting the server
```bash
make start-server


$(call execute_in_env, PYTHONPATH=${PYTHONPATH} uvicorn src.api.app:app --reload --host 0.0.0.0 --port 80)
```


### See all process

### Check system status
```bash
top
```
`q`: Quit top.   
`h`: Display help.   
`k`: Kill a process (you'll be prompted for the PID).   
`M`: Sort processes by memory usage.
`P`: Sort processes by CPU usage.   
`1`: Show individual CPU cores.

Alternatively for a slightly more visual solution install htop
```bash
sudo apt update
sudo apt install htop
```
And run `htop`




On VPS Routes tables
- create a `0.0.0.0/0` connection to the corresponding Internet gateway ID `igw-0794b7f1742d0a496`