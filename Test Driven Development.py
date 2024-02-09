import unittest      # python unit testing framework
from unittest.mock import patch #patch - for object testing 
import vm_management   #main py file
from vm_management import (connect_mongo, get_collection, add_vm,
                              display_vm, remove_vm, modify_vm,
                              for_add_vm, for_remove_vm, for_modify_vm)


class test_vm_function(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.client = connect_mongo()
            cls.collection = get_collection(cls.client)
        
        def test_1_add_vm(self):
            with patch('builtins.input', side_effect=['Test_VM', 'Test_CPU', '16', '512', 'Linux', 'Test_Disk', 'SSD', '128', 'Test_Network', '192.168.1.1', '192.168.1.0/24', 'Public']):
                result = for_add_vm()
            self.assertIsNone(result)

        
        def test_2_display_vm(self):
            result = display_vm()
            print("Results after displaying VM:",result)
            self.assertIsNotNone(result)
        
        def test_3_modify_vm(self):
            
            with patch('builtins.input', side_effect=['Test_VM','1', 'NewVMname']):
                for_modify_vm("VM NAME", "VM NAME",'MOD PLACE', "new_value")



            result = self.collection.find_one({'VM NAME': 'New_VM_Name'})
            print("Results after modifying VM:",result)
            self.assertIsNone(result)

        def test_4_remove_vm(self):
            with patch('builtins.input', side_effect=['Test_VM']):
                for_remove_vm()

            result = self.collection.find_one({'VM NAME': 'Test_VM'})
            print("Results after removing VM:",result)
            self.assertIsNotNone(result)
        
        
        
        @classmethod
        def tearDownClass(cls):
            cls.client.close()



 


if __name__ == '__main__':
    unittest.main()