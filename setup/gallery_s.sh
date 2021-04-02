cp ./gallery_s.service /etc/systemd/system/gallery_s.service
sudo systemctl daemon-reload
sudo systemctl enable gallery_s.service
sudo systemctl start gallery_s.service