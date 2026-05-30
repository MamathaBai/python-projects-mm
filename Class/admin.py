class admin:
    def __init__(self,name,add_post,delete_post):
        self.name =  name
        self.add_post = add_post
        self.delete_post = delete_post
    def post(self):
        print(f"Admin {self.name} added new post {self.add_post}")
    def delete(self):
        print(f"Admin {self.name} can delete post {self.delete_post}")
class privaleges(admin):
    def __init__(self,name,add_post,delete_post):
        self.show_message = "None"
        super().__init__(name,add_post,delete_post)
    def show(self):
        print(f"show no admin is {self.show_message}")
Admin1 = privaleges("Raj","Add post","Delete post")
Admin1.post()
Admin1.delete()
Admin1.show()
