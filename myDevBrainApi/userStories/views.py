from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Status, UserStory
# Create your views here.


def index(request):

    return HttpResponse("Welcome to user stories!")


def detail(request, user_story_id):
    user_story = get_object_or_404(UserStory, pk=user_story_id)
    return render(request, 'userStories/detail.html', {'user_story': user_story})


def createForm(request):
    return render(request, 'userStories/createForm.html', {'form_field_set': UserStory.FORM_FIELDS})


def createStory(request):
    validation_feedback = validate_intput(request.POST)
    if len(validation_feedback) > 0:
        user_story = UserStory(
            short_name=request.POST['short_name'],
            full_name=request.POST['full_name'],
            status=Status.objects.get(pk=1),
            parent_feature=request.POST['parent_feature'],
            git_branch=request.POST['git_branch'],
        )
        print(request.POST)
        user_story.save()
        return HttpResponseRedirect(reverse('detail', args=(user_story.id,)))
    else:
        return render(request, 'userStories/createForm.html', {
            'error_message': "Invalid data!" + validation_feedback
        })

def change_status(request, user_story_id):
    user_story = get_object_or_404(UserStory, pk=user_story_id)
    next_status = user_story.status__next_status
    user_story.status = next_status
    user_story.save()


def validate_intput(input_map):
    feedback = ''
    if not type(input_map['short_name']) is str and len(input_map['short_name']) < 100:
        feedback = feedback + " | " + "short_name"
    if not type(input_map['full_name']) is str and len(input_map['full_name']) < 500:
        feedback = feedback + " | " + "full_name"
    if not type(input_map['parent_feature']) is int:
        feedback = feedback + " | " + "parent_feature"
    if not type(input_map['git_branch']) is str and len(input_map['git_branch']) < 50:
        feedback = feedback + " | " + "git_branch"
    return feedback
