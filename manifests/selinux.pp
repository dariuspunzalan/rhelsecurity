class rhelsecurity::selinux {
  file { '/etc/selinux/config':
    ensure	=> file,
    path	=> '/etc/selinux/config',
  }
  file_line { 'Set SELINUX':
    path	=> '/etc/selinux/config',
    line	=> 'SELINUX=permissive',
    match	=> '^SELINUX=',
  }
  file_line { 'Set SELINUXTYPE':
    path	=> '/etc/selinux/config',
    line	=> 'SELINUXTYPE=taegeted',
    match	=> '^SELINUXTYPE=',
  }
}
