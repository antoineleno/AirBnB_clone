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


class Teststate(unittest.TestCase):
    """Class to test stae class"""
    def test_state(self):
        """Test if state is a sub class of base_model"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_instance_and_attribute(self):
        """
        Test if state can create an instance
        Test state class attribute
        """
        my_instance = State()
        self.assertIsInstance(my_instance, State)
        my_instance.name = "Kedah"
        self.assertEqual(my_instance.name, "Kedah")

    def test_kwargs(self):
        """
        Test if we can pass attribute to class
        """
        my_state = State(name="kedah")
        self.assertEqual(my_state.name, "kedah")

    def test_id_attriubte(self):
        """
        Test id attriubte
        """
        my_new_state = State()
        uuid_obj = uuid.UUID(my_new_state.id)
        self.assertTrue(uuid.UUID(my_new_state.id, version=4))
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
        my_A = Place()
        ex_op = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), ex_op)

    def test_str_rpr_with_attribute(self):
        """
        Test case where kwarg is provided
        """
        with self.assertRaises(AttributeError):
            my_A = State(name="Swimming pool")
            ex_op = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
            self.assertEqual(str(my_A), ex_op)

    def test_str_rpr_with_attribute_not_kwarg(self):
        """
        Test str rpr case where attriube is assign
        not using kwarg
        """
        my_A = State()
        my_A.quality = "Good"
        ex_op = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), ex_op)

    def test_state_attribute_name(self):
        """
        Test Amanity type
        """
        my_A = State()
        self.assertEqual(type(my_A.name), str)

    def test_str_representation_with_attributes(self):
        """
        Test state with attributes all type
        """
        my_A = State()
        my_A.my_list = [1, 2, 4]
        my_A.dict = {"A": 2, "B": 5, "C": 6}
        output = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), output)

    def test_to_dict_with_attriube(self):
        """
        Test to dict method on amenity class
        with not attribute and with attributes
        """
        my_state = Amenity()
        my_state.name = "Penang"
        my_state.my_list = [1, 2, 4]
        my_state.my_tuple = (1, 2, 4)
        my_state.my_dict = {"A": 1, "B": 2, "C": 4}
        my_model_dict_repr = my_state.to_dict()
        class_name = f"{my_state.__class__.__name__}"
        dictionary = my_state.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_save_method_without_storage(self):
        """Test save method without storage"""
        my_state = State()
        my_state.save()
        self.assertIsInstance(my_state.updated_at, datetime)

    def test_update_at_created_at_assignemt(self):
        """test update_at and created_at"""
        with self.assertRaises(ValueError):
            my_state = State(created_at="12pm", updated_at="12pm")
            self.assertEqual(my_state.created_at, "12pm")

    def test_attribute_error(self):
        """Test case where attribue does not exit"""
        with self.assertRaises(AttributeError):
            my_state = State()
            my_state.calculate()
