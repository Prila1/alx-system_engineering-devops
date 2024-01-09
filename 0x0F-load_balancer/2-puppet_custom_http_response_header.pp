# puppet config for nginx server
exec {'nginx_conf':
  require  => Exec['install_nginx'],
  command  => 'http {
        server {
                listen 80;
                root /var/www/data/;
                index index.html;
                error_page 404 /404.html;
								add_header X-Served-By \$hostname;
                location /redirect_me {
                        rewrite ^/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
                }
                location /404.html {
                        root /var/www/data/error;
                        internal;
                }
        }
}
events {}" | sudo tee /etc/nginx/nginx.conf >> /dev/null',
  provider => 'shell',
}


exec {'index_html':
  require  => Exec['nginx_conf'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'printf "Hello World!\n" | sudo tee /var/www/data/index.html >> /dev/null',
  provider => 'shell',
}

exec {'404_html':
  require  => Exec['index_html'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'printf "Ceci n\'est pas une page\n" | sudo tee /var/www/data/error/404.html >> /dev/null',
  provider => 'shell',
}

exec {'run_nginx':
  require  => Exec['404_html'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  provider => 'shell',
  command  => 'sudo service nginx start'
}

exec {'update':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo apt-get update -y',
  provider => 'shell',
  before   => Exec['install_nginx'],
}

exec { 'install_nginx':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo apt-get install nginx -y',
  provider => 'shell'
}
