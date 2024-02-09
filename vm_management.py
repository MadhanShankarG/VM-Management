
from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("localhost",27017)
    print("_______Connection Established Successfully_______")
    print()
    return client

def get_collection(client,database_name="vm_db",collection_name="vm_collection"):
    db=client.vm_db
    vm_db=client.vm_db

    vm_collection= vm_db["vm_collection"]
    return vm_collection
collection=get_collection(connect_mongo())

def add_vm(vm_collection, document):
    result = vm_collection.insert_one(document)
    print("Insert Result:", result)
    if result.inserted_id is not None:
        print("VM Created Successfully")
        return True
    else:
        print("VM Creation Unsuccessful")
        return False



def display_vm():
    count = collection.count_documents({})

    if count == 0:
        print("No VMs Found")
        return None
    else:
        print("The Existing VMs are:")
        results = collection.find()
        for r in results:
            print(r)
        return results



def remove_vm(vm_collection, document):
    result = vm_collection.delete_one(document)
    print("Delete Result:", result)
    if result.deleted_count == 1:
        print("VM Deleted Successfully")
        return True
    else:
        print("VM Deletion Unsuccessful")
        return False


    

def modify_vm(vm_collection, criteria, updation):
    result = vm_collection.update_one(criteria, updation)
    print("Modify Result:", result)
    if result.modified_count > 0:
        print("VM Modified Successfully")
        return result
    else:
        print("VM Modification Unsuccessful")
        return result



def for_add_vm():
    vm_name=input("VM Name:")
    cpu_model=input("CPU Model:")
    vm_ram=input("RAM (in GB):")
    vm_storage=input("Storage (in GB):")
    vm_os=input("OS:")
    print()
    print("Mention Disk Details:")
    disk_name=input("Disk Name:")
    disk_type=input("Disk Type:")
    disk_size=input("Disk Size (in GB):")
    vm_disks=[{"DISK NAME":disk_name,"DISK TYPE":disk_type,"DISK SIZE":disk_size}]
    print()
    print("Mention Network Details:")
    network_name=input("Network Name:")
    gateway_ip=input("Gateway IP:")
    cidr_=input("Network CIDR:")
    network_usage=input("Network Usage:")
    vm_network=[{"NETWORK NAME":network_name,"GATEWAY IP":gateway_ip,"CIDR":cidr_,"NETWORK USAGE":network_usage}]
    add_vm(collection,{"VM NAME":vm_name,"CPU MODEL":cpu_model,"RAM":vm_ram,"STORAGE":vm_storage,"OPERATING SYSTEM":vm_os,"DISK INFO":vm_disks,"NETWORK INFO":vm_network})


def for_remove_vm():
    vm_name=input("VM Name:")
    remove_vm(collection,{"VM NAME":vm_name})

def for_modify_vm(modify_input1, modify_input2, modified_value,str_):
    
    modify_vm(collection,{modify_input1:str_},{"$set":{modify_input2:modified_value}})


if __name__=='__main__':
    print("                           Virtual Machine Database Menu")
    print("--------------------------------------------------------------------------")
    print()
    print("1. Add a VirtualMachine")
    print()
    print("2. Display all VirtualMachines")
    print()
    print("3. Modify a VirtualMachine")
    print()
    print("4. Remove a VirtualMachine")
    print()
    print("__________________________________________________________________________")
    print()
    choice=int(input("Choice in integer:"))
    if choice==1:
        for_add_vm()
    elif choice==2:
        display_vm()
        if display_vm ==0:
            print("no")
        
    elif choice==3:
        print('''What do you want to Modify:
            1. Name
            2. CPU Model
            3. RAM
            4. STORAGE
            5. ADD DISK
            6. REMOVE DISK
            7. MODIFY DISK SIZE''')
        m_choice=int(input("Choice in integer:"))
        if m_choice==1:
            str_=input("VM Name:")
            modify_input1="VM NAME"
            modify_input2="VM NAME"
            modified_value=input("Value to be modified:")
            for_modify_vm(modify_input1, modify_input2, modified_value,str_)
        elif m_choice==2:
            str_=input("VM Name:")
            modify_input1="VM NAME"
            modify_input2="CPU MODEL"
            modified_value=input("Value to be modified:")
            for_modify_vm(modify_input1, modify_input2, modified_value,str_)
        elif m_choice==3:
            str_=input("VM Name:")
            modify_input1="VM NAME" 
            modify_input2="RAM"
            modified_value=input("Value to be modified:")
            for_modify_vm(modify_input1, modify_input2, modified_value,str_)
        elif m_choice==4:
            str_=input("VM Name:")
            modify_input1="VM NAME"
            modify_input2="STORAGE"
            modified_value=input("Value to be modified:")
            for_modify_vm(modify_input1, modify_input2, modified_value,str_)
        elif m_choice==5:
            vm_name=input("VM Name:")
            print("TO ADD DISK:")
            disk_name = input("Disk Name:")
            disk_type = input("Disk Type:")
            disk_size = input("Disk Size (in GB):")
            modify_input = "DISK INFO"
            modified_value = {"DISK NAME": disk_name, "DISK TYPE": disk_type, "DISK SIZE": disk_size}
            modify_vm(collection, {"VM NAME": vm_name}, {"$push": {modify_input: modified_value}})

        elif m_choice==6:
            vm_name=input("VM Name:")
            disk_name = input("Disk Name:")
            modify_input = "DISK INFO"
            modified_value = {"DISK NAME": disk_name}
            modify_vm(collection, {"VM NAME": vm_name}, {"$pull": {modify_input: modified_value}})
        
        elif m_choice==7:
            vm_name=input("VM Name:")
            disk_name = input("Disk Name:")
            new_size = input("New Disk Size (in GB):")
            modify_input = "DISK INFO"
            modified_value = {"DISK NAME": disk_name}
            update_query = {
                "$set": {
                    f"{modify_input}.$.DISK SIZE": new_size
            }
        }
            modify_vm(collection, {"VM NAME": vm_name, "DISK INFO.DISK NAME": disk_name}, update_query)

        else:
            print("Kindly enter a valid Input")
            
    elif choice==4:
        for_remove_vm()
    
    else:
        print("Kindly enter a valid number")
    

    
    

