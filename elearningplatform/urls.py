from django.urls import path
from.import views
app_name="elearningplatform"
urlpatterns= [ path("",views.home, name="home"),
             path("Note/",views.Notes,name='Notes'),
             path('helpcipse/',views.helpcipse, name='helpcipse'),
             path("video/",views.Videos, name="video"),
             path('register/',views.registerPage,name='register'),
             path('About/',views.About ,name='About'),
             path('Article/',views.Article,name='Article'),
             path('certificatecourse/',views.certificatecourses,name='certificatecourses'),
             path('diplomacourses/',views.diplomacourses,name='diplomacourses'),
             path('undergraduatecourses/',views.undergraduatecourses,name='undergraduatecourses'),
             path('postgraduatecourses/',views.postgraduatecourses,name='postgraduatecourses'),
             path('professionalcourses/',views.professionalcourses,name='professionalcourses'),
             path('quizz/',views.quizz,name='quizz'),
             path('login/', views.loginPage,name='login'),
             path('logout/', views.logoutPage,name='logout'),
            # path('coursemenu/',views.coursemenu,name='coursemenu'),
             
             path('Learningmaterials/',views.Learning_materials,name='LearningMaterials'),
             path ('privacypolicy/',views.PrivacyPolicy,name='Privacy Policy'),
             ]