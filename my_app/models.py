from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

CUser = get_user_model()  # Custom User


class Room_type(models.Model):
    description = models.CharField(max_length=250)
    rate = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.description


class Room(models.Model):
    class Status(models.TextChoices):
        VACANT = 'ว่าง', 'ว่าง'  # (VACANT: Name, vacant: value, VA: label[admin])
        RESERVED = 'จอง', 'จอง'

    room_type = models.ForeignKey(Room_type, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=4)
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.VACANT)
    exmovein_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.room_no

    def get_absolute_url(self):
        return reverse('update_room_status', args=[str(self.room_no)])


class Extra(models.Model):
    description = models.CharField(max_length=100)
    cpu = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.description


class Billing(models.Model):
    STATUS_CHOICE = (('open', 'OPEN'), ('close', 'CLOSE'),)

    bill_ref = models.CharField(max_length=6)
    bill_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICE, default='open')
    tenant_name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=4)
    room_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    room_acc_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    electricity_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    water_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    common_ser_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    other_ser_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    overdue_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    adjust = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    bill_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    payment_date = models.DateField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    cf_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    late_fee = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    maint_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    class Meta:
        ordering = ('-bill_date',)

    def __str__(self):
        return 'Bill for room number: {} Status: {}'.format(self.room_no, self.status)

    def get_absolute_url(self):
        return reverse('pay_bill', args=[str(self.bill_ref)])


class TenantProfile(models.Model):
    # tenant = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tenant = models.OneToOneField(CUser, on_delete=models.CASCADE)
    pin = models.CharField(max_length=13, unique=True)
    phone = models.CharField(max_length=10)
    # room_no = models.OneToOneField(Room, on_delete=models.CASCADE, unique=True)
    room_no = models.OneToOneField(Room, on_delete=models.CASCADE, unique=True)
    term = models.PositiveSmallIntegerField(default=12)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    deposit = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    deduct = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    cum_ovd = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0)
    adjust = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    extra = models.ManyToManyField(Extra)
    # bill_date = models.DateField(auto_now=True, blank=True) # DELETED 24Jan23
    bill_ref = models.CharField(max_length=6, blank=True)  # ADDED 24Jan23, each tpf carries during billing cycle
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    # USE PLACEHOLDER (NO DEFAULT VALUE) INITIAL VALUE TO BE PROVIDED WHEN SAVE TO DB
    elec_unit = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    water_unit = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    late_fee = models.DecimalField(max_digits=7, decimal_places=2, default=0)  # no need to use placeholder
    maint_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return 'Profile for user {}'.format(self.tenant.first_name)

    def get_absolute_url(self):
        return reverse('fill_bill', args=[self.room_no])

    #
    # def get_absolute_url(self):
    #     return reverse('fill_bill', args=[self.room_no])

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #                    args=[self.publish.year,
    #                          self.publish.month,
    #                          self.publish.day,
    #                          self.slug])


class MaintenanceService(models.Model):
    job_ref = models.CharField(max_length=6)
    job_date = models.DateField(auto_now_add=True)

    room_no = models.CharField(max_length=4)
    description = models.CharField(max_length=100, default='Maintenance Charge')
    job_cost = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ('-job_date',)

    def __str__(self):
        return 'Job_Ref.: {}'.format(self.job_ref)
