#!/usr/bin/python3
"""
console module
    1 - Class to test Amenity
    2 - Class to test
"""

import unittest
import uuid
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Class to test Amenity class"""
    def test_Amenity(self):
        """Test if Amenity is a sub class of base_model"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_Amenity_instance_and_attribute(self):
        """
        Test if Amenity can create an instance
        Test amenity class attribute
        """
        my_instance = Amenity()
        self.assertIsInstance(my_instance, Amenity)
        my_instance.name = "swimming Pool"
        self.assertEqual(my_instance.name, "swimming Pool")

    def test_kwargs(self):
        """
        Test if we can pass attribute to class
        """
        my_Amenity = Amenity(name="swimming Pool", quality="Good")
        self.assertEqual(my_Amenity.name, "swimming Pool")
        self.assertEqual(my_Amenity.quality, "Good")

    def test_id_attriubte(self):
        """
        Test id attriubte
        """
        my_new_Amenity = Amenity()
        uuid_obj = uuid.UUID(my_new_Amenity.id)
        self.assertTrue(uuid.UUID(my_new_Amenity.id, version=4))
        self.assertIsInstance(uuid_obj, uuid.UUID)

    def test_created_updated_at(self):
        """
        Test created at and updated at attributes
        """
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity.created_at, datetime)
        self.assertIsInstance(my_amenity.updated_at, datetime)

    def test_str_representation(self):
        """
        Test string representation for Amenity
        """
        my_A = Amenity()
        ex_op = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), ex_op)

    def test_str_rpr_with_attribute(self):
        """
        Test case where kwarg is provided
        """
        with self.assertRaises(AttributeError):
            my_A = Amenity(name="Swimming pool")
            ex_op = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
            self.assertEqual(str(my_A), ex_op)

    def test_str_rpr_with_attribute_not_kwarg(self):
        """
        Test str rpr case where attriube is assign
        not using kwarg
        """
        my_A = Amenity()
        my_A.quality = "Good"
        ex_op = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), ex_op)

    def test_Amenity_attribute_name(self):
        """
        Test Amanity type
        """
        my_A = Amenity()
        self.assertEqual(type(my_A.name), str)

    def test_str_representation_with_attributes(self):
        """
        Test Amenity with attributes all type
        """
        my_A = Amenity()
        my_A.my_list = [1, 2, 4]
        my_A.dict = {"A": 2, "B": 5, "C": 6}
        output = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), output)

    def test_to_dict_with_attriube(self):
        """
        Test to dict method on amenity class
        with not attribute and with attributes
        """
        my_Amenity = Amenity()
        my_Amenity.name = "Swimming Pool"
        my_Amenity.my_list = [1, 2, 4]
        my_Amenity.my_tuple = (1, 2, 4)
        my_Amenity.my_dict = {"A": 1, "B": 2, "C": 4}
        my_model_dict_repr = my_Amenity.to_dict()
        class_name = f"{my_Amenity.__class__.__name__}"
        dictionary = my_Amenity.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_save_method_without_storage(self):
        """Test save method without storage"""
        my_model = Amenity()
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_update_at_created_at_assignemt(self):
        """test update_at and created_at"""
        with self.assertRaises(ValueError):
            my_model = Amenity(created_at="12pm", updated_at="12pm")
            self.assertEqual(my_model.created_at, "12pm")

    def test_attribute_error(self):
        """Test case where attribue does not exit"""
        with self.assertRaises(AttributeError):
            my_review = Amenity()
            my_review.calculate()


class TestCity(unittest.TestCase):
    """Class to test city class"""
    def test_City(self):
        """Test if City is a sub class of base_model"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_instance_and_attribute(self):
        """
        Test if City can create an instance
        Test city class attribute
        """
        my_instance = City()
        self.assertIsInstance(my_instance, City)
        my_instance.name = "Conakry"
        my_instance.state_id = "ab22"
        self.assertEqual(my_instance.name, "Conakry")
        self.assertEqual(my_instance.state_id, "ab22")

    def test_kwargs(self):
        """
        Test if we can pass attribute to class
        """
        my_city = City(name="Kuala Lumpur", state_id="kl234")
        self.assertEqual(my_city.name, "Kuala Lumpur")
        self.assertEqual(my_city.state_id, "kl234")

    def test_id_attriubte(self):
        """
        Test id attriubte
        """
        my_new_City = City()
        uuid_obj = uuid.UUID(my_new_City.id)
        self.assertTrue(uuid.UUID(my_new_City.id, version=4))
        self.assertIsInstance(uuid_obj, uuid.UUID)

    def test_created_updated_at(self):
        """
        Test created at and updated at attributes
        """
        my_ciy = City()
        self.assertIsInstance(my_ciy.created_at, datetime)
        self.assertIsInstance(my_ciy.updated_at, datetime)

    def test_str_representation(self):
        """
        Test string representation for Amenity
        """
        city = City()
        ex_op = f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), ex_op)

    def test_str_rpr_with_attribute(self):
        """
        Test case where kwarg is provided
        """
        with self.assertRaises(AttributeError):
            city = City(name="New York")
            ex_op = f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}"
            self.assertEqual(str(city), ex_op)

    def test_str_rpr_with_attribute_not_kwarg(self):
        """
        Test str rpr case where attriube is assign
        not using kwarg
        """
        city = City()
        city.name = "Kissidougou"
        ex_op = f"[{city.__class__.__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), ex_op)

    def test_city_attribute_name(self):
        """
        Test city attribute type
        """
        my_city = City()
        self.assertEqual(type(my_city.name), str)
        self.assertEqual(type(my_city.state_id), str)

    def test_str_representation_with_attributes(self):
        """
        Test City with attributes all type
        """
        my_A = City()
        my_A.my_list = [1, 2, 4]
        my_A.dict = {"A": 2, "B": 5, "C": 6}
        output = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), output)

    def test_to_dict_with_attriube(self):
        """
        Test to dict method on City class
        with not attribute and with attributes
        """
        my_City = City()
        my_City.name = "Swimming Pool"
        my_City.my_list = [1, 2, 4]
        my_City.my_tuple = (1, 2, 4)
        my_City.my_dict = {"A": 1, "B": 2, "C": 4}
        my_model_dict_repr = my_City.to_dict()
        class_name = f"{my_City.__class__.__name__}"
        dictionary = my_City.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_save_method_without_storage(self):
        """Test save method without storage"""
        my_city = City()
        my_city.save()
        self.assertIsInstance(my_city.updated_at, datetime)

    def test_update_at_created_at_assignemt(self):
        """test update_at and created_at"""
        with self.assertRaises(ValueError):
            my_model = City(created_at="12pm", updated_at="12pm")
            self.assertEqual(my_model.created_at, "12pm")
