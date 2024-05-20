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


class TestPlace(unittest.TestCase):
    """Class to test Place class"""
    def test_Place(self):
        """Test if place is a sub class of base_model"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_instance_and_attribute(self):
        """
        Test if City can create an instance
        Test city class attribute
        """
        my_instance = Place()
        self.assertIsInstance(my_instance, Place)
        my_instance.city_id = "ab22"
        my_instance.user_id = "ab23"
        my_instance.name = "Conakry"
        my_instance.number_rooms = 33
        my_instance.description = "Very Good place"
        my_instance.number_bathrooms = 54
        my_instance.max_guest = 5120
        my_instance.price_by_night = 2344
        my_instance.latitude = 22.5
        my_instance.longitude = 65.33
        my_instance.amenity_ids = ["ab22", "ab23"]
        self.assertEqual(my_instance.city_id, "ab22")
        self.assertEqual(my_instance.user_id, "ab23")
        self.assertEqual(my_instance.name, "Conakry")
        self.assertEqual(my_instance.description, "Very Good place")
        self.assertEqual(my_instance.number_rooms, 33)
        self.assertEqual(my_instance.number_bathrooms, 54)
        self.assertEqual(my_instance.max_guest, 5120)
        self.assertEqual(my_instance.price_by_night, 2344)
        self.assertEqual(my_instance.latitude, 22.5)
        self.assertEqual(my_instance.longitude, 65.33)
        self.assertEqual(my_instance.amenity_ids, ["ab22", "ab23"])

    def test_attribute_error(self):
        """Test case where attribue does not exit"""
        with self.assertRaises(AttributeError):
            my_review = City()
            my_review.calculate()

    def test_kwargs(self):
        """
        Test if we can pass attribute to class
        """
        my_place = Place(name="Kuala Lumpur", city_id="kl234")
        self.assertEqual(my_place.name, "Kuala Lumpur")
        self.assertEqual(my_place.city_id, "kl234")

    def test_id_attriubte(self):
        """
        Test id attriubte
        """
        my_new_place = Place()
        uuid_obj = uuid.UUID(my_new_place.id)
        self.assertTrue(uuid.UUID(my_new_place.id, version=4))
        self.assertIsInstance(uuid_obj, uuid.UUID)

    def test_created_updated_at(self):
        """
        Test created at and updated at attributes
        """
        my_place = Place()
        self.assertIsInstance(my_place.created_at, datetime)
        self.assertIsInstance(my_place.updated_at, datetime)

    def test_str_representation(self):
        """
        Test string representation for place
        """
        place = Place()
        ex_op = f"[{place.__class__.__name__}] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), ex_op)

    def test_str_rpr_with_attribute(self):
        """
        Test case where kwarg is provided
        """
        with self.assertRaises(AttributeError):
            place = Place(name="New York")
            rpr = f"[{place.__class__.__name__}] ({place.id}) {place.__dict__}"
            self.assertEqual(str(place), rpr)

    def test_str_rpr_with_attribute_not_kwarg(self):
        """
        Test str rpr case where attriube is assign
        not using kwarg
        """
        place = Place()
        place.name = "Kissidougou"
        ex_op = f"[{place.__class__.__name__}] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), ex_op)

    def test_city_attribute_name(self):
        """
        Test city attribute type
        """
        my_place = Place()
        self.assertEqual(type(my_place.name), str)
        self.assertEqual(type(my_place.city_id), str)
        self.assertEqual(type(my_place.user_id), str)
        self.assertEqual(type(my_place.description), str)
        self.assertEqual(type(my_place.number_rooms), int)
        self.assertEqual(type(my_place.number_bathrooms), int)
        self.assertEqual(type(my_place.max_guest), int)
        self.assertEqual(type(my_place.price_by_night), int)
        self.assertEqual(type(my_place.latitude), float)
        self.assertEqual(type(my_place.longitude), float)
        self.assertEqual(type(my_place.amenity_ids), list)

    def test_str_representation_with_attributes(self):
        """
        Test place with attributes all type
        """
        my_p = Place()
        my_p.my_list = [1, 2, 4]
        my_p.dict = {"A": 2, "B": 5, "C": 6}
        output = f"[{my_p.__class__.__name__}] ({my_p.id}) {my_p.__dict__}"
        self.assertEqual(str(my_p), output)

    def test_to_dict_with_attriube(self):
        """
        Test to dict method on City class
        with not attribute and with attributes
        """
        my_place = Place()
        my_place.name = "Conakry"
        my_place.my_list = [1, 2, 4]
        my_place.my_tuple = (1, 2, 4)
        my_place.my_dict = {"A": 1, "B": 2, "C": 4}
        my_model_dict_repr = my_place.to_dict()
        class_name = f"{my_place.__class__.__name__}"
        dictionary = my_place.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_save_method_without_storage(self):
        """Test save method without storage"""
        my_place = Place()
        my_place.save()
        self.assertIsInstance(my_place.updated_at, datetime)

    def test_update_at_created_at_assignemt(self):
        """test update_at and created_at"""
        with self.assertRaises(ValueError):
            my_model = Place(created_at="12pm", updated_at="12pm")
            self.assertEqual(my_model.created_at, "12pm")
