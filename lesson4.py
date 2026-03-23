


class User:
    user_count =0
    default_password = '12345678'

    def __init__(self,username, phone_number):
        self.username = username
        self.phone_number = phone_number
        self.password =User.default_password
        User.user_count += 1

    def get_username(self):
        return self.username

    @classmethod
    def get_user_count(cls):
        return User.user_count

    @classmethod
    def create_users(cls, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError(f"неправильный формат {phone_number}")
        new_user = User(name,phone_number)
        return new_user



user_1 = User('Жоомарт',"996556080502")
user_2 = User('Курманбек',"996556365667")
print(user_1.username)
print(user_2.username)
print(user_1.default_password, user_2.default_password)
print("кол-во пользователей", User.user_count)
User.user_count +=1
user_3 = User("Рома", "996708920588")
User.user_count +=1
print("кол-во пользователей", User.user_count)
user_4 = User.create_users(name="кол-во пользователей", phone_number="996777036674")
print(user_4.username)