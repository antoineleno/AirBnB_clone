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


class TestReview(unittest.TestCase):
    """Class to test review class"""
    def test_review(self):
        """Test if review is a sub class of base_model"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_instance_and_attribute(self):
        """
        Test if review can create an instance
        Test review class attribute
        """
        my_instance = Review()
        self.assertIsInstance(my_instance, Review)
        my_instance.place_id = "ab55"
        my_instance.user_id = "ab22"
        my_instance.text = "This is review"
        self.assertEqual(my_instance.place_id, "ab55")
        self.assertEqual(my_instance.user_id, "ab22")
        self.assertEqual(my_instance.text, "This is review")

    def test_kwargs(self):
        """
        Test if we can pass attribute to class
        """
        my_review = Review(place_name="Kuala Lumpur", state_id="kl234")
        self.assertEqual(my_review.place_name, "Kuala Lumpur")
        self.assertEqual(my_review.state_id, "kl234")

    def test_id_attriubte(self):
        """
        Test id attriubte
        """
        my_new_review = Review()
        uuid_obj = uuid.UUID(my_new_review.id)
        self.assertTrue(uuid.UUID(my_new_review.id, version=4))
        self.assertIsInstance(uuid_obj, uuid.UUID)

    def test_created_updated_at(self):
        """
        Test created at and updated at attributes
        """
        my_review = Review()
        self.assertIsInstance(my_review.created_at, datetime)
        self.assertIsInstance(my_review.updated_at, datetime)

    def test_str_representation(self):
        """
        Test string representation for review
        """
        my_r = Review()
        ex_op = f"[{my_r.__class__.__name__}] ({my_r.id}) {my_r.__dict__}"
        self.assertEqual(str(my_r), ex_op)

    def test_str_rpr_with_attribute(self):
        """
        Test case where kwarg is provided
        """
        with self.assertRaises(AttributeError):
            m_rw = Review(name="New York")
            ex_op = f"[{m_rw.__class__.__name__}] ({m_rw.id}) {m_rw.__dict__}"
            self.assertEqual(str(m_rw), ex_op)

    def test_str_rpr_with_attribute_not_kwarg(self):
        """
        Test str rpr case where attriube is assign
        not using kwarg
        """
        my_rw = Review()
        my_rw.text = "This is review"
        ex_op = f"[{my_rw.__class__.__name__}] ({my_rw.id}) {my_rw.__dict__}"
        self.assertEqual(str(my_rw), ex_op)

    def test_review_attribute_name(self):
        """
        Test rewiew attribute type
        """
        my_review = Review()
        self.assertEqual(type(my_review.place_id), str)
        self.assertEqual(type(my_review.user_id), str)
        self.assertEqual(type(my_review.text), str)

    def test_str_representation_with_attributes(self):
        """
        Test review with attributes all type
        """
        my_A = Review()
        my_A.my_list = [1, 2, 4]
        my_A.dict = {"A": 2, "B": 5, "C": 6}
        output = f"[{my_A.__class__.__name__}] ({my_A.id}) {my_A.__dict__}"
        self.assertEqual(str(my_A), output)

    def test_to_dict_with_attriube(self):
        """
        Test to dict method on rewiew class
        with not attribute and with attributes
        """
        my_rewiew = Review()
        my_rewiew.name = "kL case"
        my_rewiew.my_list = [1, 2, 4]
        my_rewiew.my_tuple = (1, 2, 4)
        my_rewiew.my_dict = {"A": 1, "B": 2, "C": 4}
        my_model_dict_repr = my_rewiew.to_dict()
        class_name = f"{my_rewiew.__class__.__name__}"
        dictionary = my_rewiew.__dict__
        expected_dict = {"__class__": class_name}
        expected_dict.update(dictionary)
        self.assertDictEqual(my_model_dict_repr, expected_dict)

    def test_save_method_without_storage(self):
        """Test save method without storage"""
        my_rewiew = Review()
        my_rewiew.save()
        self.assertIsInstance(my_rewiew.updated_at, datetime)

    def test_update_at_created_at_assignemt(self):
        """test update_at and created_at"""
        with self.assertRaises(ValueError):
            my_model = Review(created_at="12pm", updated_at="12pm")
            self.assertEqual(my_model.created_at, "12pm")

    def test_attribute_error(self):
        """Test case where attribue does not exit"""
        with self.assertRaises(AttributeError):
            my_review = Review()
            my_review.calculate()
