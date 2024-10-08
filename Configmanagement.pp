Lab Work 1

init.pp

class profile {
        file { '/etc/profile.d/append-path.sh':
                owner   => 'root',
                group   => 'root',
                mode    => '0644',
                content => "PATH=\$PATH:/java/bin\n",
        }
}



Lab Work 2

modules/machine_info
init.pp

class machine_info {
    if $facts[kernel] == "windows" {
        $info_path = "C:\Windows\Temp\Machine_Info.txt"
}  else {
        $info_path = "/tmp/machine_info.txt"
}

    file { 'machine_info':
        path => $info_path,
        content => template('machine_info/info.erb'),
    }


}


modules/reboot/init.pp


class reboot {
    if $facts[kernel] == "windows" {
      $cmd = "shutdown /r"
} elsif $facts[kernel] == "Darwin" {
      $cmd = "shutdown -r now"
} else {
      $cmd = "reboot"
}


if $facts[uptime_days] > 30 {
    exec { 'reboot':
      command => $cmd,
    }
  }
}

}

