from django.db import models

# Create your models here.
class Ads(models.Model):
    adsID = models.AutoField(primary_key=True)
    advertiserID = models.CharField(max_length=32,)
    adsSpace = models.IntegerField()
    adsIMG = models.CharField(max_length=128)
    adsView = models.IntegerField()

class AppliedClubList(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    uSchoolID = models.ForeignKey('UserAccount', on_delete=models.CASCADE)
    memberState = models.IntegerField()
    applyDate = models.CharField(max_length = 128, null=True)

class Apply(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    uSchoolID = models.ForeignKey('UserAccount', on_delete=models.CASCADE,)
    additionalApplyContent = models.CharField(max_length= 1024)

class ClubMember(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    uSchoolID = models.ForeignKey('UserAccount', on_delete=models.CASCADE,)

class ClubStatistic(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    memberNumber = models.IntegerField()
    menNumber = models.IntegerField()
    womenNumber = models.IntegerField()
    overRatio12 = models.IntegerField()
    Ratio13 = models.IntegerField()
    Ratio14 = models.IntegerField()
    Ratio15 = models.IntegerField()
    Ratio16 = models.IntegerField()
    Ratio17 = models.IntegerField()
    Ratio18 = models.IntegerField()
    Ratio19 = models.IntegerField()
    Ratio20 = models.IntegerField()
    engineeringRatio = models.IntegerField()
    ITRatio = models.IntegerField()
    naturalscienceRatio = models.IntegerField()
    managementRatio = models.IntegerField()
    humanitiesRatio = models.IntegerField()
    socialscienceRatio = models.IntegerField()
    nurseRatio = models.IntegerField()
    InternationalRatio = models.IntegerField()#국제학부
    DasanRatio = models.IntegerField()#다산학부
    PharmacyRatio = models.IntegerField()#약대
    MedicalRatio = models.IntegerField()#의대


class Event(models.Model):
    eventID = models.AutoField( primary_key= True)
    eventName = models.CharField(max_length=32)
    eventDate = models.DateField()
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    eventInfo = models.CharField(max_length=1024)
    eventIMG = models.CharField(max_length=1024, null=True)

class MarkedClubList(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    uSchoolID = models.ForeignKey('UserAccount', on_delete=models.CASCADE,)


class Tag(models.Model):
    clubTag = models.CharField(max_length=64, primary_key=True)

class TaggedClubList(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    clubTag = models.ForeignKey('Tag', on_delete=models.CASCADE,)
    class Meta:
        unique_together = (('clubID', 'clubTag'),)

class UserAlarm(models.Model):
    uSchoolID = models.ForeignKey('UserAccount', on_delete=models.CASCADE,)
    newclubAlarm = models.BooleanField()
    stateAlarm = models.BooleanField()
    eventAlarm = models.BooleanField()
    autoLogin = models.BooleanField()
    unreadEvent = models.IntegerField()

class UserAccount(models.Model):
    uID = models.CharField(max_length=80,)
    uPW = models.CharField(max_length=20,)
    uIMG = models.CharField(max_length=128, null=True)
    uName = models.CharField(max_length=10, null=True)
    uJender = models.BooleanField(default=True)
    uSchoolID = models.IntegerField(primary_key=True, null=False, default = 1)
    uMajor = models.CharField(max_length=32, null=True)
    uPhoneNumber = models.IntegerField(null=True)
    uCollege = models.CharField(max_length=32, null=True)

class ManagerAccount(models.Model):
    mID = models.CharField(max_length=20, primary_key=True)
    mPW = models.CharField(max_length=20, null=True)
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    clubName = models.CharField(max_length=5,)
    clubIMG = models.CharField(max_length=128,)
    newbieAlarm = models.BooleanField(default=True)

class Club(models.Model):
    clubID = models.AutoField(primary_key=True)
    clubName = models.CharField(max_length=32)
    clubCategory = models.CharField(max_length=256)
    clubIMG = models.CharField(max_length=128, null=True)
    clubMajor = models.IntegerField(default=1)
    clubDues = models.FloatField(max_length=3)


class ClubPromotion(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,)
    promotionID = models.IntegerField(primary_key=True)
    posterIMG = models.CharField(max_length=128)
    clubInfo = models.CharField(max_length=4096)
    clubApply = models.CharField(max_length=1024)
    clubFAQ = models.CharField(max_length=2048)
    clubContact = models.CharField(max_length=1024)
    additionalApply = models.CharField(max_length=1024)
    recruitStartDate = models.DateField()
    recruitEndDate = models.DateField()

class ClubActivity(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE,null=True)
    clubActivityFile = models.CharField(max_length=128)
    clubActivityInfo = models.CharField(max_length=256)
    clubActivityID = models.AutoField(primary_key=True)
    clubActivityDetail = models.CharField(max_length=2048, null=True)

class Major_Affiliation(models.Model):
    majorName = models.CharField(max_length=20, primary_key=True)
    majorCollege = models.CharField(max_length=20,)

class FAQ(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE)
    userID = models.IntegerField()
    FAQID = models.AutoField(primary_key=True)
    FAQDate = models.DateTimeField()
    isAnonymous = models.BooleanField()
    FAQContent = models.CharField(max_length=1024)

class FAQComment(models.Model):
    clubID = models.ForeignKey('Club', on_delete=models.CASCADE)
    userID = models.IntegerField()
    FAQID = models.ForeignKey('FAQ', on_delete=models.CASCADE)
    FAQCommentID = models.AutoField(primary_key=True)
    FAQCommentDate = models.DateTimeField()
    isAnonymous = models.BooleanField()
    FAQCommentContent = models.CharField(max_length=1024)
