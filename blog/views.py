from django.shortcuts import render
# Create your views here.

posts=[
    {
        'author':'user1',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 1 2024'
    },
    {
        'author':'user2',
        'title':'Blog Post 2',
        'content':'Post content',
        'date_posted':'August 2 2024'
    },
]

def home(req):
    context={
        'posts':posts,
    }
    return render(req,'blog/home.html',context=context)


def about(req):
    return render(req,'blog/about.html',{'title':'About'})
    