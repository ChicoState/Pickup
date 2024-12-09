from django.test import TestCase
from Pickup import models
from django.db import models as DBM

# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.date=DBM.DateTimeField(auto_now_add=True)      #store test date/time
        self.post=models.Post(
            post_text="text field", 
            post_title="title field",
            post_loc="location field",
            post_date=self.date,
            event_time=self.date,
            )
    def test_post_fields_correct(self):     #test that all fields store correct data    SHOULD PASS
        self.assertEqual(self.post.post_loc, "location field")
        self.assertEqual(self.post.post_text, "text field")
        self.assertEqual(self.post.post_title, "title field")
        self.assertEqual(self.post.post_date, self.date)
        self.assertEqual(self.post.event_time, self.date)
    def test_post_loc_false(self):          #test each field with false data    SHOULD ALL FAIL
        self.assertEqual(self.post.post_loc, "location fard")
    def test_post_text_false(self):
        self.assertEqual(self.post.post_text, "text fan")
    def test_post_title_false(self):
        self.assertEqual(self.post.post_title, "title lane")

class TagTest(TestCase):
    def setUp(self):
        self.tag=models.Tag(tag_name="name field")
    def test_name_correct(self):            #test with correct name field       SHOULD PASS
        self.assertEqual(self.tag.tag_name,"name field")
    def test_name_case(self):               #test case sensitivity              SHOULD FAIL
        self.assertEqual(self.tag.tag_name,"Name Field")
    def test_name_false(self):            #test with incorrect name field       SHOULD FAIL
        self.assertEqual(self.tag.tag_name,"false name")