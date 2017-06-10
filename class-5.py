#类定义：类定义了一组属性，这些属性与一组叫做实例的对象相关且由其共享。类通常由函数（称为方法），变量（称为类变量）和计算出的属性（称为特性）组成的集合。
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0 #类变量，是可在类的所有实例之间共享的值（也就是说，他们不是单独分配给每个实例的）
    #定义构造方法
    def __init__(self,n,a,w): #类中定义的函数称为实例方法。实例方法是一种在类的实例上进行操作的函数，作为第一个参数传递。根据约定，这个参数称为self.
        self.name = n #表示将name属性保存在实例中。在新创建的实例返回到用户之后，使用点（.）运算符即可访问这些属性以及类的属性。
        self.age = a
        self.__weight = w
    def speak(self): # speak()为实例方法的例子
        print("%s 说: 我 %d 岁。" %(self.name,self.age))



#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))



s = student('ken',10,60,3)
s.speak()
