from django.shortcuts import render, get_object_or_404

# Create your views here.
def chat_group(request):
    group_name = get_object_or_404(group_name)
    return render(request, 'realtimechat/chat_group.html', {'group_name': group_name})