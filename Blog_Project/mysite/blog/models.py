from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    
      def __str__(self):
          return "@{}".format(self.username)

class Post(models.Model):
      author = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
      title = models.CharField(max_length=200)
      text = models.TextField()
      created_date = models.DateTimeField(default=timezone.now)
      published_date = models.DateTimeField(blank=True,null=True)

      def publish(self):
	      self.published_date = timezone.now()
	      self.save()
   
      def approve_comments(self):    
	      return self.comments.filter(approved_comment=True)

      def approve_likes(self):
	      return self.likepost.filter(liked_post=True) 
         	
      def get_absolute_url(self): 
	      return reverse("post_detail",kwargs={'pk':self.pk})
	
      def __str__(self): 
	      return self.title



class Comment(models.Model):
      post = models.ForeignKey('blog.Post',related_name='comments')
      author = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
      text = models.TextField()
      created_date = models.DateTimeField(default=timezone.now)
      approved_comment = models.BooleanField(default=False)

      def approve(self):
	      self.approved_comment = True
	      self.save()
         
      def approve_like(self):
          return self.likecomment.filter(liked_comment=True)

      def get_absoulte_url(self):
	      return reverse('post_list')

      def __str__(self):
	      return self.text

      class Meta:
	      ordering = ["-created_date"]	



class Post_Like(models.Model):
      post = models.ForeignKey('blog.Post',related_name='likepost')
      author = models.ForeignKey('auth.User')
      liked_post = models.BooleanField(default=False)

      def like_post(self):
	      self.liked_post = True
	      self.save()

      def get_absolute_url(self): 
	      return reverse("post_detail",kwargs={'pk':self.pk})
		
      def __unicode__(self): 
	      return self.post		


class Comment_Like(models.Model):
      comment = models.ForeignKey('blog.Comment',related_name='likecomment')
      author = models.ForeignKey('auth.User')
      liked_comment = models.BooleanField(default=False)

      def like_comment(self):
	      self.liked_comment = True
	      self.save()

      def get_absolute_url(self): 
	      return reverse("post_detail",kwargs={'pk':self.pk})
		
      def __unicode__(self): 
	      return self.comment
