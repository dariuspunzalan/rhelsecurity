class rhelsecurity::admin_users {
  $admin_list.keys.each|String $id|{
    $groupid = $admin_list[$id][group]
    if ! defined(Group[$groupid]) {
      group { $groupid:
        ensure => present,
        name => $groupid,
      }
    }
    user { "$id" :
      ensure => present,
      gid    => $groupid,
      comment => $admin_list[$id][longname],
      home => "/home/$id",
      shell => "/bin/bash",
      managehome => true,
      require => Group[$groupid],
    }
  }
}
