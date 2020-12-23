#Update
sudo apt-get update
#Upgrade
sudo apt-get upgrade
# Install repository configuration
curl -sSL https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/microsoft-prod.list
# Install Microsoft GPG public key
curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
# Update package index files
sudo apt-get update
#Install Brave Browser
snap install brave -y
#Install Teams
snap install teams -y
#Install Edge
sudo apt install microsoft-edge-dev -y
#Install Pip
sudo apt-get install python3-pip -y
#Install VSCode
#Install Unity-Tweak Tool
sudo apt-get install unity-tweak-tool -y
#Install Spotify
sudo apt-get install spotify -y
#Install Discord
sudo apt-get install discord -y
#Install VLC
sudo apt-get install vlc -y
#Install Hiri
snap install hiri
