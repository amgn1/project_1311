from django.contrib.auth import models

class KeycloakUserOAuth2Manager(models.UserManager):

    def create_new_user(self, user):
        # discord_tag = '%s#%s' % (user['username'], user['discriminator'])
        new_user = self.create(
            sub=user['sub'],
            avatar=user['avatar'],
            full_name=user['full_name'],
            email=user['email'],
            email_verified=user['email_verified'],
            
        )
        return new_user
