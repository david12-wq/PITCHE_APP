from app.models import Comment,User,Pitch
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_David = User(username = 'David',password = 'banana', email = 'davidkamau245@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_comment='This is a test pitch',category="interview",user = self.user_Dorcas,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_David,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_David)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)