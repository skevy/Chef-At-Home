from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend
from social_auth.signals import pre_update

class CAHProfile(models.Model):
    user = models.ForeignKey(User)
    avatar = models.URLField(max_length=1000)
    service = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s - %s' % (self.user, self.service)


def associate_profile(sender, user, response, details, old_user, **kwargs):

    avatar = ""
    service = ""
    if sender == FacebookBackend: #facebook
        avatar = "http://graph.facebook.com/%s/picture" % response['username']
        service = "facebook"
    elif sender == TwitterBackend: #twitter
        avatar = response['profile_image_url']
        service = "twitter"

    try:
        cah_profile = user.get_profile()
    except:
        cah_profile = None

    if cah_profile is None:
        cah_profile = CAHProfile(
            user = user,
            avatar = avatar,
            service = service
        )
        cah_profile.save()
    else:
        cah_profile.avatar = avatar
        cah_profile.service = service
        cah_profile.save()

    return True

pre_update.connect(associate_profile)

class FavoriteItem(models.Model):
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u'Favorited Item'