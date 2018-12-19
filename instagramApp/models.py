import urllib.request

from django.core.files import File  # you need this somewhere
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.utils import timezone


# Create your models here.


class instagram(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    followers = models.IntegerField(null=True, blank=True)
    followings = models.IntegerField(null=True, blank=True)
    isPrivate = models.BooleanField(null=True, blank=True)
    fullName = models.CharField(max_length=20, null=True, blank=True)
    biograpy = models.CharField(max_length=200, null=True, blank=True)
    mediaCount = models.IntegerField(null=True, blank=True)
    profilePicture = models.ImageField(upload_to='img/profile', blank=True, default='img/temp.jpg')
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.username + ":" + self.password

    def updateData(self, api):
        try:
            info = api.getProfileInfo(self.username)
            print(info)
            self.followers = info['followerCount']
            self.followings = info['followingCount']
            self.mediaCount = info['mediaCount']
            self.isPrivate = info['isPrivate']
            self.fullName = info['fullName']
            self.biograpy = info['biography']
            profilePic = info['profilePicture']

            # pic = urllib.request.urlretrieve(profilePic)
            # img_temp = NamedTemporaryFile(delete=True)
            # img_temp.write(pic)
            # img_temp.flush()
            # img_filename = self.username+".jpg"
            # self.profilePicture.save(img_filename, pic, save=True)

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib.request.urlopen(profilePic).read())
            img_temp.flush()
            # self.profilePicture.delete()
            self.profilePicture.save(self.username + ".jpg", File(img_temp), save=True)
            self.save()
        except:
            return
