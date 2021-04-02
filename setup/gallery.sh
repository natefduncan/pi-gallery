cp ./gallery.service /etc/systemd/system/gallery.service
sudo systemctl daemon-reload
sudo systemctl enable gallery.service
sudo systemctl start gallery.service