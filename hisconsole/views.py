from django.shortcuts import render

# def index(request):
#     return render(request, 'chat/index.html', {})
#
# def room(request, room_name):
#     return render(request, 'chat/room.html', {
#         'room_name': room_name
#     })


def dotaskview(request, room_name="dotask"):
    return render(request, 'admin/room.html', {
        'room_name': room_name
    })