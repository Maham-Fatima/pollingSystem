from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question,Choice,Vote, Voter
from django.urls import reverse
from django.db.models import F

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "index.html", context)

def getQuestion(req, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(req, "question.html", {"question": question})
   
def giveVote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Validate Voter
    try:
        voter = Voter.objects.get(name=request.POST["name"], password=request.POST["password"])
    except Voter.DoesNotExist:
        return render(
            request,
            "question.html",
            {
                "question": question,
                "error_message": "Invalid voter credentials. Please try again.",
            },
        )

    # Validate Choice
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "question.html",
            {
                "question": question,
                "error_message": "You didn't select a valid choice.",
            },
        )
    
    # Check if the voter has already voted on this question
    if Vote.objects.filter(voter=voter, question=question).exists():
        return render(
            request,
            "question.html",
            {
                "question": question,
                "error_message": "You have already voted on this question.",
            },
        )

    # Save the vote
    vote = Vote(voter=voter, question=question, choice=selected_choice)
    vote.save()

    # Update the choice's vote count
    selected_choice.votes = F("votes") + 1
    selected_choice.save()

    # Redirect to results page after successful voting
    return HttpResponseRedirect(reverse("result", args=(question.id,)))

def getVoteCount(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "result.html", {"question": question})