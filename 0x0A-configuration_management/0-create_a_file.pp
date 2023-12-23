# Creates a file 'school'
file {'/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
}
