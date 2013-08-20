group { 'puppet': ensure => present }
Exec { path => [ '/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/' ] }
File { owner => 0, group => 0, mode => 0644 }

class {'apt':
  always_apt_update => true,
}

package { [
    'build-essential',
    'vim',
    'curl',
    'git-core',
    'libpq-dev'
  ]:
  ensure  => 'installed',
}

class { 'postgresql::server':
  config_hash => {
    'ip_mask_deny_postgres_user' => '0.0.0.0/32',
    'ip_mask_allow_all_users'    => '0.0.0.0/0',
    'listen_addresses'           => '*',
    'ipv4acls'                   => ['host all all 0.0.0.0/0 md5'],
    'manage_redhat_firewall'     => true,
    'manage_pg_hba_conf'         => true,
    'postgres_password'          => 'postgres',
  },
}

postgresql::db { 'riddles':
  user     => 'riddles_db_u',
  password => 'riddles_db_u'
}


class { 'python':
  version    => 'system',
  pip        => true,
  dev        => true,
  virtualenv => true,
  gunicorn   => false,
}

python::pip { 'virtualenvwrapper':
  ensure      => 'absent',
  # virtualenv  => '/var/www/project1',
  owner       => 'root',
  # environment => 'ORACLE_HOME=/usr/lib/oracle/11.2/client64',
}


python::virtualenv { '/home/vagrant/.venvs/riddles':
  ensure       => present,
  version      => 'system',
  requirements => '/vagrant/requirements.txt',
  # proxy        => 'http://proxy.domain.com:3128',
  systempkgs   => true,
  distribute   => false,
  owner        => 'vagrant',
  group        => 'vagrant',
}

class run_django {
    exec { 'run_django':
        command => '/home/vagrant/.venvs/riddles/bin/python /vagrant/manage.py runserver 0.0.0.0:8000&',
    }
}
class { 'run_django':
}
