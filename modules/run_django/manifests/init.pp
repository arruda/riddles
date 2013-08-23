class run_django {
    exec { 'run_django_bg':
        environment => "PY_PATH='/home/vagrant/.venvs/riddles/bin/python'",
        command => '/home/vagrant/.venvs/riddles/bin/python /vagrant/manage.py runserver 0.0.0.0:8000&',
        require => Exec["south_migrate"]
    }
    exec { 'south_migrate':
        command => '/home/vagrant/.venvs/riddles/bin/python /vagrant/manage.py migrate',
        require => Exec["syncdb"]
    }
    exec { 'syncdb':
        command => '/home/vagrant/.venvs/riddles/bin/python /vagrant/manage.py syncdb --noinput',
    }
}
