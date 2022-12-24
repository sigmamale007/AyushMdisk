echo "Cloning Repo...."
git clone https://github.com/sigmamale007/AyushMdisk.git /AyushMdisk
cd /AyushMdisk
pip3 install -U -r requirements.txt
echo "⚡️⚡️ Starting AyushMdisk..."
python3 main.py
