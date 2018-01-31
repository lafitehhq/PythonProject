from django.db import models
from django.contrib.auth.models import User # Django的用户认证模块
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

# Create your models here.

"""客户信息表"""


class Customer(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, help_text="用户报名后请改为真实姓名")
    qq = models.CharField(max_length=64, unique=True)
    qq_name = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    id_num = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(verbose_name="常用邮箱", blank=True, null=True)
    source_choices = ((0, '转介绍'),
                      (1, 'QQ群'),
                      (2, '官网'),
                      (3, '百度推广'),
                      (4, '51CTO'),
                      (5, '知乎'),
                      (6, '市场推广')
                      )

    source = models.SmallIntegerField(choices=source_choices)
    referral_from = models.CharField(verbose_name="转介绍人qq",max_length=64,blank=True,null=True)

    consult_course = models.ForeignKey("Course",verbose_name="咨询课程")
    content = models.TextField(verbose_name="咨询详情")
    tags = models.ManyToManyField("Tag", blank=True,null=True)  # 标签信息
    status_choices = ((0, '已报名'),
                      (1, '未报名'),
                      )
    status = models.SmallIntegerField(choices=status_choices,default=1)
    consultant = models.ForeignKey("UserProfile")
    memo = models.TextField(blank=True, null=True)  # 备注
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<%s %s>" %(self.qq,self.name)

    class Meta:
        verbose_name ="客户表"
        verbose_name_plural ="客户表"

"""标签表"""


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=32)  # 唯一

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

"""客户跟进表"""


class CustomerFollowUp(models.Model):
    customer = models.ForeignKey("Customer")  # 跟进客户信息：关联客户信息表
    content = models.TextField(verbose_name="跟进内容")  # 跟进内容：字数不限制
    consultant = models.ForeignKey("UserProfile")  # 跟进的销售信息：关联销售账户表

    intention_choices = ((0, '2周内报名'),  # 客户意向信息
                        (1, '1个月内报名'),
                        (2, '近期无报名计划'),
                        (3, '已在其它机构报名'),
                        (4, '已报名'),
                        (5, '已拉黑'),
                         )
    intention = models.SmallIntegerField(choices=intention_choices)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<%s : %s>" %(self.customer.qq,self.intention)


    class Meta:
        verbose_name = "客户跟进记录"
        verbose_name_plural = "客户跟进记录"

"""课程表"""


class Course(models.Model):
    name = models.CharField(max_length=64, unique=True)  # 课程名称：字符类型;唯一;64字节
    price = models.PositiveSmallIntegerField()  # 课程价格：正小整数类型
    period = models.PositiveSmallIntegerField(verbose_name="周期(月)")  # 课程周期：显示的字段名称;正小整数类型
    outline = models.TextField()  # 课程大纲：文本类型

    def __str__(self):
        return self.name

    class Meta:  # 内嵌类
        verbose_name = "课程表"  # 定义课程表字段名
        verbose_name_plural = "课程表"

"""校区表"""


class Branch(models.Model):
    name = models.CharField(max_length=128, unique=True)  # 校区名称：字符类型；128字节；唯一
    addr = models.CharField(max_length=128)  # 校区地址

    def __str__(self):
        return self.name

    class Meta:  # 内嵌类
        verbose_name = "校区"  # 定义校区字段名
        verbose_name_plural = "校区"

"""班级表"""


class ClassList(models.Model):
    branch = models.ForeignKey("Branch", verbose_name="校区")  # 校区信息：关联校区表
    course = models.ForeignKey("Course")  # 课程信息：关联课程表（一对多）
    class_type_choices = ((0, '面授(脱产)'),
                          (1, '面授(周末)'),
                          (2, '网络班')
                          )
    class_type = models.SmallIntegerField(choices=class_type_choices, verbose_name="班级类型")  # 班级类型信息：小整数类型
    contract = models.ForeignKey("ContractTemplate", blank=True, null=True)
    semester = models.PositiveSmallIntegerField(verbose_name="学期")  # 学期信息：正小整数类型
    teachers = models.ManyToManyField("UserProfile")  # 教师信息：关联教师表（多对多）
    start_date = models.DateField(verbose_name="开班日期")   # 开班时间信息：日期格式类型
    end_date = models.DateField(verbose_name="结业日期", blank=True, null=True)  # 结业时间信息：可以不写

    def __str__(self):
        return "%s %s %s" % (self.branch, self.course, self.semester)  # 返回校区，课程，第几期作为返回值

    class Meta:
        unique_together = ('branch', 'course', 'semester')  # 联合唯一：校区，课程，第几期需要做联合唯一
        verbose_name_plural = "班级"
        verbose_name = "班级"

"""上课记录表"""


class CourseRecord(models.Model):
    from_class = models.ForeignKey("ClassList", verbose_name="班级")  # 课程信息：关联班级表
    day_num = models.PositiveSmallIntegerField(verbose_name="第几节(天)")  # 上课的天数进度信息：正小整数类型
    teacher = models.ForeignKey("UserProfile")  # 老师信息：关联教师表
    has_homework = models.BooleanField(default=True)  # 是否有作业信息：布尔值类型
    homework_title = models.CharField(max_length=128, blank=True, null=True)  # 作业标题信息：字符类型；128字节；可以为空
    homework_content = models.TextField(blank=True, null=True)  # 作业内容信息：文本类型；可以为空
    outline = models.TextField(verbose_name="本节课程大纲")
    date = models.DateField(auto_now_add=True)  # 上课时间信息：日期格式；auto_now_add表示添加时的时间，更新对象时不会有变动

    def __str__(self):
        return "%s %s" % (self.from_class, self.day_num)  # 返回班级名称和班级的上课天数进度

    class Meta:
        unique_together = ("from_class", "day_num")  # 创建联合唯一：班级和上课天数进度联合唯一
        verbose_name_plural = "上课记录"

"""学习记录表"""


class StudyRecord(models.Model):
    student = models.ForeignKey("Enrollment")   # 已报名学生信息：关联客户报名表
    course_record = models.ForeignKey("CourseRecord")  # 上课记录信息：关联上课记录表
    attendance_choices = ((0, '已签到'),
                          (1, '迟到'),
                          (2, '缺勤'),
                          (3, '早退'),
                          )
    attendance = models.SmallIntegerField(choices=attendance_choices,default=0)  # 出勤记录信息：正小整数类型
    score_choices = ((100, "A+"),
                     (90, "A"),
                     (85, "B+"),
                     (80, "B"),
                     (75, "B-"),
                     (70, "C+"),
                     (60, "C"),
                     (40, "C-"),
                     (-50, "D"),
                     (-100, "COPY"),
                     (0, "N/A"),  # N/A表示不可用
                     )
    score = models.SmallIntegerField(choices=score_choices, default=0)  # 成绩信息：小整数类型，默认为0
    memo = models.TextField(blank=True, null=True)  # 作业备注信息：文本类型；可以为空
    date = models.DateField(auto_now_add=True)  # 学习记录时间信息：日期类型；auto_now_add添加时的时间，更新对象时不会有变动

    def __str__(self):
        return "%s %s %s" % (self.student, self.course_record, self.score)  # 返回学生信息,上课记录信息和上课成绩

    class Meta:
        unique_together = ('student', 'course_record')
        verbose_name_plural = "学习记录"

"""客户报名表"""


class Enrollment(models.Model):
    customer = models.ForeignKey("Customer")  # 报名的学生信息：关联客户表
    enrolled_class = models.ForeignKey("ClassList", verbose_name="所报班级")  # 所报班级的信息：关联班级表
    consultant = models.ForeignKey("UserProfile", verbose_name="课程顾问")  # 对应跟进的顾问信息：关联客户顾问表
    contract_agreed = models.BooleanField(default=False, verbose_name="学员已同意合同条款")  # 学生意向信息：布尔类型
    contract_approved = models.BooleanField(default=False, verbose_name="合同已审核")  # 合同状态信息：布尔类型
    date = models.DateTimeField(auto_now_add=True)  # 客户报名时间信息：日期类型

    def __str__(self):
        return "%s %s" %(self.customer, self.enrolled_class)

    class Meta:
        unique_together = ("customer", "enrolled_class")  # 创建报名学生与所报班级的联合唯一
        verbose_name_plural = "报名表"

"""缴费记录表"""


class Payment(models.Model):

    customer = models.ForeignKey("Customer")  # 缴费客户：关联客户表，先交钱后报名
    course = models.ForeignKey("Course", verbose_name="所报课程")  # 缴费的课程：关联课程表
    amount = models.PositiveIntegerField(verbose_name="数额", default=500)  # 缴费金额：正整数；默认是500元订金
    consultant = models.ForeignKey("UserProfile")  # 缴费的员工：关联系统账户表
    date = models.DateTimeField(auto_now_add=True)  # 缴费的时间：时间类型

    def __str__(self):
        return "%s %s" % (self.customer, self.amount)

    class Meta:
        verbose_name_plural = "缴费记录"

# class UserProfile(models.Model):
#     '''账号表'''
#     user = models.OneToOneField(User)
#     name = models.CharField(max_length=32)
#     roles = models.ManyToManyField("Role",blank=True,null=True)
#
#     def __str__(self):
#         return self.name

"""合同模版表"""


class ContractTemplate(models.Model):
    name = models.CharField("合同名称",max_length=64,unique=True)
    template = models.TextField()

    def __str__(self):
        return self.name

"""客户顾问表"""


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        self.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self,email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user

'''账号表'''


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # user = models.OneToOneField(User)  # 继承Django 的账户认证模块

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )
    password = models.CharField(_('password'), max_length=128,
                                help_text=mark_safe('''<a href='password/'>修改密码</a>'''))
    name = models.CharField(max_length=32)  # 账户名称
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    roles = models.ManyToManyField("Role", blank=True)
    objects = UserProfileManager()

    stu_account = models.ForeignKey("Customer", verbose_name="关联学员账号", blank=True, null=True,
                                    help_text="只有学员报名后方可为其创建账号")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_active


    class Meta:
        permissions = (('can_fuck_him_to_death','弄死小虎逼'),
                       ('can_access_my_course','可以访问我的课程'),
                       ('can_access_customer_list','可以访问客户列表'),
                       ('can_access_customer_detail','可以访问客户详细'),
                       ('can_access_studyrecords','可以访问学习记录页面'),
                       ('can_access_homework_detail','可以访问作业详情页面'),
                       ('can_upload_homework','可以交作业'),
                       ('access_kingadmin_table_obj_detail','可以访问kingadmin每个表的对象'),
                       ('change_kingadmin_table_obj_detail','可以修改kingadmin每个表的对象'),
                       )


'''角色表'''


class Role(models.Model):
    name = models.CharField(max_length=32, unique=True)  # 角色的名称：字符类型，唯一，32字节
    menus = models.ManyToManyField("Menu", blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "角色"


'''菜单表'''


class Menu(models.Model):
    name = models.CharField(max_length=32)
    url_type_choices = ((0,'alias'),(1,'absolute_url'))
    url_type = models.SmallIntegerField(choices=url_type_choices,default=0)
    url_name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
