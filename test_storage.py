#!/usr/bin/python3
"""
file storage module
"""

import unittest
import uuid
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.city import City
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Class to test fileStorage"""

    def test_new_method_on_all_classes(self):
        """Test new method""on all the classes"""
        my_model = BaseModel()
        my_user = User()
        my_place = Place()
        my_amenity = Amenity()
        my_city = City()
        my_state = State()
        my_review = Review()

        all_objects = storage.all()
        self.assertTrue(my_model in all_objects.values())
        self.assertTrue(my_amenity in all_objects.values())
        self.assertTrue(my_city in all_objects.values())
        self.assertTrue(my_place in all_objects.values())
        self.assertTrue(my_review in all_objects.values())
        self.assertTrue(my_state in all_objects.values())
        self.assertTrue(my_user in all_objects.values())

    def test_all_methods(self):
        """
        Check if the value return by all is a dict
        chekc if the key of the dict if the name of class
        associated with id.
        overall check all and new method with all classes
        """

        all_objects = storage.all()
        self.assertEqual(type(all_objects), dict)
        for key, value in all_objects.items():
            class_name, obj_id = key.split(".")
            class_type = globals().get(class_name)
            my_key = uuid.UUID(obj_id)
            self.assertTrue(hasattr(globals().get(class_name), '__bases__') and
                            issubclass(globals().get(class_name), BaseModel))
            self.assertIsInstance(my_key, uuid.UUID)
            self.assertTrue(isinstance(value, class_type))

    def test_save_method_on_model(self):
        """
        Test save method on all the classses
        """
        my_model = BaseModel()
        my_model.name = "My first Model"
        my_model.save()
        all_objects = storage.all()
        model_key = "BaseModel." + my_model.id
        self.assertIn(model_key, all_objects.keys())
        self.assertEqual(all_objects[model_key].name, "My first Model")

    def test_save_method_on_amenety(self):
        """Test save method on amenety class"""
        my_amenity = Amenity()
        my_amenity.name = "Wifi"
        all_object = storage.all()
        my_amenity_key = "Amenity." + my_amenity.id
        self.assertIn(my_amenity_key, all_object.keys())
        self.assertEqual(all_object[my_amenity_key].name, "Wifi")

    def test_save_on_user(self):
        """Test save method on user class"""
        first_user = User()
        first_user.email = "lenomadeleineantoine@gmail.com"
        first_user.password = "ab123"
        first_user.first_name = "Amadou"
        first_user.last_name = "Bah"
        all_objects = storage.all()
        first_user_key = "User." + first_user.id
        self.assertIn(first_user_key, all_objects.keys())
        self.assertEqual(all_objects[first_user_key].password, "ab123")
        self.assertEqual(all_objects[first_user_key].first_name, "Amadou")

    def test_save_on_place(self):
        """Test save on place class"""
        my_place = Place()
        my_place.name = "Kuala Lumpur"
        all_objects = storage.all()
        my_place_key = "Place." + my_place.id
        self.assertIn(my_place_key, all_objects.keys())
        self.assertEqual(all_objects[my_place_key].name, "Kuala Lumpur")

    def test_save_on_state(self):
        """Test save on state"""
        my_state = State()
        my_state.name = "Kedah"
        all_objects = storage.all()
        my_state_id = "State." + my_state.id
        self.assertIn(my_state_id, all_objects.keys())
        self.assertEqual(all_objects[my_state_id].name, "Kedah")

    def test_save_on_city(self):
        """Test save on review class"""
        pass

    def test_save_on_review(self):
        """Test save method on city class"""
        my_review = Review()
        my_review.place_id = "ab22"
        my_review.user_id = "cd55"
        my_review.text = "Great review"
        my_review_key = "Review." + my_review.id
        all_objects = storage.all()
        self.assertIn(my_review_key, all_objects.keys())
        self.assertEqual(all_objects[my_review_key].place_id, "ab22")
        self.assertEqual(all_objects[my_review_key].user_id, "cd55")
        self.assertEqual(all_objects[my_review_key].text, "Great review")

    def test_reload_method(self):
        """Test reload method"""
        my_amenity = Amenity()
        my_amenity.name = "WiFi"

        my_user = User()
        my_user.email = "usr@ex.com"

        my_place = Place()
        my_place.name = "My Place"

        my_amenity.save()
        my_user.save()
        my_place.save()

        storage.reload()

        all_objects = storage.all()

        self.assertIn("Amenity." + my_amenity.id, all_objects)
        self.assertEqual(all_objects["Amenity." + my_amenity.id].name, "WiFi")

        self.assertIn("User." + my_user.id, all_objects)
        self.assertEqual(all_objects["User." + my_user.id].email, "usr@ex.com")

        self.assertIn("Place." + my_place.id, all_objects)
        self.assertEqual(all_objects["Place." + my_place.id].name, "My Place")

    def tearDown(self):
        """Clean up method after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
