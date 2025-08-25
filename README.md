**Adding user from the Azure directory to aws**
```
 https://community.amazonquicksight.com/t/enable-federation-to-amazon-quicksight-with-automatic-provisioning-of-users-between-aws-iam-identity-center-and-microsoft-azure-ad/8234 
```


**Checkov Checks**
```
terraform plan -out tf.plan
terraform show -json tf.plan > tf.json
pip install checkov
checkov -f tf.json

```

**Install kvm using the commands**
```
sudo apt-get install qemu-kvm -> kernel virtual machine
sudo apt-get install libvirt-bin
sudo apt-get install bridge-utils -> bridge utils for transferring the network from one to another
sudo apt-get install cpu-checker -> this is used to check usage of cpu
Check the KVM installation test -> KVM-ok
```

**make a copy of network using network configuration -> using copy command**
*************************************************************************
```
Sudo cp /etc/network /backupconfig
sudo brctl show -> bridge control network shown
```


**create a library as boot space in variable**
```
/var/lib/libvirt/images/(iso file)
Note: \ is used to point the next line in cmd 
	-- is used to pass the content to continue the command
```
	
	
INSTALLATION COMMANDS:
**********************************************
```
sudo virt-install \	!its a kernel vm
--virt-type=kvm \
--name centos7 \	!os version
--ram 2048 \	!allocate ram
--vcpus=2 \	!no cores
--os-variant=centos7.0 \	!os variant
--virt-type=kvm \	
--hvm \
--cdrom=/var/lib/libvirt/boot/CentOS-7-x86_64-Everything-2009.iso \ 	!place the location of the file
--graphics vnc \
--disk path=/var/lib/libvirt/images/centos7.iso,size=11,bus=virtio,format=qcow2 \
 --check all=off ! it will not displays any issue
 
 (or)

 virt-install --network bridge:br0 --name centos --ram=2048 --vcpu=2 --os-variant=centos7.0 --disk path=/(userdefined),size=(userdefine) --graphics (none) or (vnc) --location=(define the place of the os file where it is located) --check all=off
 ```
 
************************************************************ 
**Installation will be done				    
Please make sure all the configuration done on the vm's**
************************************************************
``` 
To list the VM in KVM
************************
virsh list --all  //to display the vm in KVM

To shutdown the KVM
*********************
virsh shutdown <vm name>

To start the KVM
*******************
virsh start <vm name>

To autostart the KVM
***********************
virsh autostart <vm name>

To take the vm in console
***************************
virsh console <vm name>  // to make them console and making the operations

To delete the vm 
*******************
virsh shutdown <vm name> // to shut down the running os
virsh undefine <vm name> // to unregister the domain name
virsh destory <vm name> // to delete the os
```
Sat Aug 16 01:47:09 UTC 2025
Sun Aug 17 01:58:04 UTC 2025
Mon Aug 18 01:58:57 UTC 2025
Tue Aug 19 01:46:17 UTC 2025
Wed Aug 20 01:44:59 UTC 2025
Thu Aug 21 01:43:39 UTC 2025
Fri Aug 22 01:44:16 UTC 2025
Sat Aug 23 01:40:44 UTC 2025
Sun Aug 24 01:54:05 UTC 2025
Mon Aug 25 01:48:50 UTC 2025
