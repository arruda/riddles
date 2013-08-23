group { 'puppet': ensure => present }
Exec { path => [ '/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/', '/usr/local/bin/' ] }
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


# PostgreSQL
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
} ->

postgresql::db { 'riddlesdb':
  user     => 'riddles_u',
  password => 'riddles_u'
} ->


# Python
class { 'python':
  version    => 'system',
  pip        => true,
  dev        => true,
  virtualenv => true,
  gunicorn   => false,
} ->

python::virtualenv { '/home/vagrant/.venvs/riddles':
  ensure       => present,
  version      => 'system',
  requirements => '/vagrant/requirements.txt',
  # proxy        => 'http://proxy.domain.com:3128',
  systempkgs   => true,
  distribute   => false,
  owner        => 'vagrant',
  group        => 'vagrant',
} ->


# Preparing ruby
class { 'ruby':

  # version         => '1.9.3',
  ruby_package     => 'ruby1.9.3',
  # gems_version    => '1.8.25',
  rubygems_update => false
} ->
class { bundler:
    provider => 'gem',
    ensure => 'present'
}->
bundler::install { '/vagrant/':
  user       => 'root',
  group      => 'root',
}
->

# django run stuff
class { 'run_django':
}


