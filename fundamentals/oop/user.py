class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Email address: {self.email}')
        print(f'Age: {self.age}')
        print(f'Membership status: {self.is_rewards_member}')
        print(f'Gold card points: {self.gold_card_points}')

    def enroll(self):
        if self.is_rewards_member:
            print ('User already a member.')
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self,amount):
        if self.gold_card_points < amount:
            return
        self.gold_card_points -= amount

my_user = User('Tiffany', 'Liang', 'tiffanyliang333@gmail.com', 27)
my_user.display_info()

my_user.enroll()
my_user.display_info()

my_user.spend_points(10)
my_user.display_info()
