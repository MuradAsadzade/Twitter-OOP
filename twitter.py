from datetime import datetime


class Profile:
    def __init__(self, nickname, bio, email, password):
        self.__nickname = nickname
        self.__bio = bio
        self.__email = email
        self.__password = password
        self.__tweet_list = []

    @property
    def nickname(self):
       return self.__nickname

    @nickname.setter
    def nickname(self, new_nickname):
        self.nickname = new_nickname

    @property
    def bio(self):
       return self.__bio

    @bio.setter
    def bio(self, new_bio):
        self.bio = new_bio

    @property
    def email(self):
       return self.__email

    @email.setter
    def email(self, new_email):
        self.email = new_email

    @property
    def password(self):
       return self.__password

    @password.setter
    def password(self, new_password):
        self.password = new_password

    @property
    def tweet_list(self):
        return self.__tweet_list

    def post_tweet(self, tweet):
        current_time=datetime.now()
        current_time=current_time.strftime("%H:%M:%S")
        self.tweet_list.append({
            'content': tweet,
            'date':current_time,
        })

    def delete_tweet(self, index):
        if index >= len(self.tweet_list) or index < 0:
            raise ValueError(f'Bu indeksde tweet yoxdur')
        else:
            self.tweet_list.pop(index)

    def get_info(self):
        return self.tweet_list

    def __str__(self):
        return self.nickname


class Twitter:
    def __init__(self) -> None:
        self.user_list = []

    def add_user(self, user):
        self.user_list.append({"nickname": user.nickname, "bio": user.bio,
                              "email": user.email, "password": user.password})



    def get_user_info_by_nick(self, nickname):
        for user in self.user_list:
            if nickname==user["nickname"]:
                return user
        return "This username was not found"
    
    def show_users(self):
        for user in self.user_list:
            print(user)


twitter = Twitter()
user1=Profile("Murad","I am developer","muradesedzade2004@gmail.com","murad123")
user2=Profile("Ayxan","I am a student","ayxan2010@gmail.com","ayxan123")
user1.post_tweet("Hi everyone")
# print(user1.tweet_list)
# print(user1)

twitter.add_user(user1)
twitter.add_user(user2)

# print(twitter.get_user_info_by_nick('Ayxan'))
# print(twitter.user_list)
twitter.show_users()