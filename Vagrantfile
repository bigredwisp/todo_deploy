# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"

  config.vm.define "server", primary: true do |web|
    web.vm.hostname = "todo-server"
    if FileTest::directory?("../java_todo_server/build/libs")
      web.vm.synced_folder "../java_todo_server/build/libs/", "/home/vagrant/todo_server/"
    end
    if FileTest::directory?("../../js/js_todo_app/dist")
      web.vm.synced_folder "../../js/js_todo_app/dist/", "/home/vagrant/todo-webapp/"
    end
  end

  config.vm.define "db" do |db|
    db.vm.hostname = "todo-db"
    config.vm.provision "ansible" do |ansible|
      ansible.sudo = true
      ansible.playbook = "master.yml"
      ansible.groups = {
        "webserver" => ["server"],
        "dbserver" => ["db"],
        "all_groups:children" => ["webserver", "dbserver"]
      }
      ansible.limit = 'all'
    end
  end
end
