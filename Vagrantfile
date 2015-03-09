# -*- mode: ruby -*-
# # vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.vm.box = 'coreos-beta'
  config.vm.hostname = 'buildvm'
  config.vm.network :private_network, ip: '192.168.60.101'

  # Provider specific configuration
  config.vm.provider :virtualbox do |virtualbox, override|
    override.vm.box_url = 'http://storage.core-os.net/coreos/amd64-usr/beta/coreos_production_vagrant.json'
    virtualbox.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
    virtualbox.customize ['modifyvm', :id, '--natdnsproxy1', 'on']
    virtualbox.memory = 4098
    virtualbox.cpus = 2
  end

  config.vm.provider :vmware_fusion do |vmware_fusion, override|
    override.vm.box_url = 'http://storage.core-os.net/coreos/amd64-usr/beta/coreos_production_vagrant_vmware_fusion.json'
    vmware_fusion.vmx['memsize'] = 4098
    vmware_fusion.vmx['numvcpus'] = 2
  end

  # Plugin conflict resolution
  config.vbguest.auto_update = false if Vagrant.has_plugin?('vagrant-vbguest')

  # NFS shares
  config.vm.synced_folder 'bin',
                          '/home/core/bin',
                          id: 'bin', nfs: true, mount_options: ['nolock,vers=3,udp']

  config.vm.synced_folder '.',
                          '/mnt/dockerfiles',
                          id: 'dockerfiles', nfs: true, mount_options: ['nolock,vers=3,udp']

  # CoreOS startup
  config.vm.provision :file,
                      source: './cloud-config.yml',
                      destination: '/tmp/vagrantfile-user-data'
  config.vm.provision :shell,
                      inline: 'mv /tmp/vagrantfile-user-data /var/lib/coreos-vagrant/',
                      privileged: true
  config.vm.provision :shell,
                      inline: 'rm /home/core/.bashrc && cp /usr/share/skel/.bashrc /home/core/.bashrc && echo "export PATH=/home/core/bin:$PATH" >>/home/core/.bashrc',
                      privileged: true
end
