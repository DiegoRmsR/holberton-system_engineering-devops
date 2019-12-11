# Change the authentication pass and the file

exec { 'auth':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" > /etc/ssh/ssh_config'
}
