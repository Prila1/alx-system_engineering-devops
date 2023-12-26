# kills a process

exec {'killmenow':
  command => '/bin/pkill -f "killmenow"'
}
