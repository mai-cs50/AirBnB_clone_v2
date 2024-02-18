#!/usr/bin/python3
'''Define unittests'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    ''' '''

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_attribute(self):
        amenity = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity))
        self.assertNotIn("name", amenity.__dict__)

    def test_two_amenitys_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_two_amenitys_different_created_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_two_amenitys_different_updated_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date.repr = repr(date)
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.created_at = date
        amenitystr = amenity.__str__()
        self.assertIn("[Amenity] (123456)", amenitystr)
        self.assertIn("'id': '123456'", amenitystr)
        self.assertIn("'created_at': " + date.repr, amenitystr)
        self.assertIn("'updated_at': " + date.repr, amenitystr)

    def test_args_unused(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        date_iso = data.isoformat()
        amenity = Amenity(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, date)
        self.assertEqual(amenity.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    ''' '''
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_two_saves(self):
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        second_updated_at = amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity.save()
        self.assertLess(second_updated_at, amenity.updated_at)

    def test_save_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amenityid = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amenityid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    ''' '''
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenity = Amenity()
        amenity.middle_name = "Holberton"
        amenity.my_number = 98
        self.assertEqual("Holberton", amenity.middle_dict())
        self.assertIn("my_number", amenity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.crested_at = amenity.updated_at = date
        tdict = {
                'id': '123456'
                '__class__': 'Amenity',
                'created_at': date.isoformat(),
                'updated_at': date.isoformat()
            }
        self.assertDictEqual(amenity.to_dict(), tdict)

    def test_contrast_to_dict_under_dict(self):
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_to_dict_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)


if __name__ == '__main__':
    unittest.main()
