from django.db import models
from django.contrib.auth.models import User


from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver




class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=True)
    
    

    def __int__(self):
        return self.id

    def __str__(self):
        return self.user.username  + " - "+self.user.first_name  + " - "+ self.user.last_name + " - " + self.user.email

    def userName(self):
        return self.user.username  + " - "+self.user.first_name  + " - "+ self.user.last_name + " - " + self.user.email

@receiver(post_save, sender=User)
def create_user_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_person(sender, instance, **kwargs):
    instance.person.save()



class Team(models.Model):
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(Person, blank=True, through='Relation')
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail.url))
        return ""

    def __str__(self):
        return self.name

    def userName(self):
        return self.users.user.username  + " - "+self.users.user.first_name + " - "+ self.users.user.last_name + " - " + self.users.user.email

    def get_users(self):
        return "\n".join([p.user.username for p in self.users.all()])



class Relation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.person.user.username  + " - "+self.person.user.first_name + " - "+ self.person.user.last_name + " - " + self.person.user.email




@receiver(post_save, sender=Team)
def send_new_officer_notification_email(sender, instance, created, **kwargs):

    
    if created:

                
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = "johandanielcruz@outlook.com"
        receiver_email = "johandanielcruz@gmail.com"

        """

        import getpass
        x = getpass.getpass("Enter Password")

               
        password = x #str(input())  

        """
        password = "127127mnb."


        import os
        def clear(): 
            os.system('clear')
            os.system('cls')
        clear()
       

        message = MIMEMultipart("alternative")
        message["Subject"] = "Se agrego nuevo equipo con nombre: "+ instance.name
        message["From"] = sender_email
        message["To"] = receiver_email

        #User.objects.all()



        

        text = """\
        Hola,
        
        En la aplicación se creo el nuevo equipo"""
        
        html = """\
        <html>
          <body>
            <p>Hola,<br>
               <br>
               
               En la aplicación se creo el nuevo equipo: """+instance.name+ """.\
            </p>
          </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)


        mail = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email,password)
        mail.sendmail(sender_email , [receiver_email] , message.as_string())
        
        mail.quit()
        
        


