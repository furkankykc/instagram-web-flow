# Create your tests here.
from instagramApp.instaRest import InstagramClient

ic = InstagramClient("cubbelimehmedefendi", "8989323846q")
# print(ic.getFollowers()['username'])

list = ic.getPosts(('jenselter'))
print("this", *list[0])
ic.uploadPhotoList(list)

# print(list[2])
# deleteAllMedia(self,)
print(ic.get_userID('furkankykc'))

# if __name__ == "__main__":
#     api = InstagramClient("furkankykc", "fur3808535qQ@")
# print(api.getFollowers())
# print (api.getProfileInfo("cubbelimehmedefendi"))
#
# for i in (api.getPosts(api.api.username_id)):
#     print(i)

#     user_id = '1461295173'
#     user_id = self.api.username_id
#     # Alternatively, use the code below
#     # (self,check evaluation.evaluate_user_followers for further details).
#     # posts = getPosts(self,self.api,1461295173)
#     # info = getUsernameInfo(self,self.api,1461295173)
#     # list = getFeed(self,get_userID(self,'inonuitiraflar'))
#     # print (self,len(self,list))
#     # upload(self,list)
#     deleteAllMedia(self,)
#     print (self,get_userID(self,'furkankykc'))
