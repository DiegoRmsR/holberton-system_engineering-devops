#Featuring Nginx, change ULIMIT = "- n 15" for ULIMIT = "- n 4096"6" n 4096"6"

exec {'change':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/i" /etc/default/nginx',
  before   => Exec['restart'],
}
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
