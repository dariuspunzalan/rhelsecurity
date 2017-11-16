class rhelsecurity::sudoers {
  case $role {
    'management': {$sudo_file = 'sudoers_mgmt'}
    'production': {$sudo_file = 'sudoers_prod'}
    default: {$sudo_file = 'sudoers_default'}
  }
  file { 'sudoers' :
    path	=> '/etc/sudoers',
    ensure	=> file,
    owner	=> 'root',
    mode	=> '0440',
    source	=> "puppet:///modules/os_hardening/$sudo_file",
  }
}
