class Head():
    def __init__(self):
        pass


class Torso():
    def __init__(self,head,rigth_arm,left_arm,rigth_leg,left_leg):
        self.head=head
        self.right_arm=rigth_arm
        self.left_arm=left_arm
        self.right_leg=rigth_leg
        self.left_leg=left_leg


class Arm():
    def __init__(self,hand):
        self.hand=hand


class Hand():
    def __init__(self):
        pass


class Leg():
    def __init__(self,feet):
        self.feet=feet


class Feet():
    def __init__(self):
        pass


class Human():
    def __init__(self):
        self.right_hand=Hand()
        self.left_hand=Hand()

        self.right_arm=Arm(self.right_hand)
        self.left_arm=Arm(self.left_hand)

        self.right_feet=Feet()
        self.left_feet=Feet()

        self.right_leg=Leg(self.right_feet)
        self.left_leg=Leg(self.left_feet)

        self.head=Head()

        self.torso=Torso(self.head,self.right_arm,self.left_arm,self.right_leg, self.left_leg)

        print("Hello. I'm a Human!!!")

