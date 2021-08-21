from django.shortcuts import render, redirect
from app01_core.models import Tv_shows


def shows(request):
    contexto = {
        'all_shows': Tv_shows.objects.all(),
    }
    return render(request, 'all_shows.html', contexto)


def showid(request, id_solicitado):
    if request.method == "GET":
        show_context ={ 
        'show_name': Tv_shows.objects.get(id=id_solicitado).title,
        'bcast_network': Tv_shows.objects.get(id=id_solicitado).network,
        'show_desc': Tv_shows.objects.get(id=id_solicitado).description,
        'show_rel_date': (Tv_shows.objects.get(id=id_solicitado).release_date),
        'id_show': id_solicitado,
        'last_update': Tv_shows.objects.get(id=id_solicitado).updated_at,
        }
        return render(request, 'view_tv_show.html', show_context)


def showedit(request, id_solicitado):
    if request.method == "GET":
        show_context ={ 
        'show_name': Tv_shows.objects.get(id=id_solicitado).title,
        'bcast_network': Tv_shows.objects.get(id=id_solicitado).network,
        'show_desc': Tv_shows.objects.get(id=id_solicitado).description,
        'show_rel_date': (Tv_shows.objects.get(id=id_solicitado).release_date),
        'id_show': id_solicitado
        }
        print(show_context)
        return render(request, 'edit_show.html', show_context)
#
    if request.method == "POST":
        #print("a POST request is being made from Shows' Edit")
        #print(request.POST)
        valor_title = request.POST["title_in"]
        valor_network = request.POST["network_in"]
        valor_reldate = request.POST["rel_date_in"]
        valor_desc = request.POST["desc_in"]
#
        actualizar = Tv_shows.objects.get(id=id_solicitado)
        actualizar.title = valor_title
        actualizar.network = valor_network
        actualizar.release_date =valor_reldate
        actualizar.description = valor_desc
        actualizar.save()
        return redirect(f"/shows/{id_solicitado}")


def newshow(request):
    if request.method == "GET":
        return render(request, 'add_show.html')
    #
    if request.method == "POST":
        #print("A post request hecha desde autorid")
        tituloshow = request.POST["title_in"]
        transmite = request.POST["network_in"]
        estreno = request.POST["rel_date_in"]
        info = request.POST["desc_in"]
        Tv_shows.objects.create(title = tituloshow, network = transmite, description = info, release_date = estreno)
        new_show_id = Tv_shows.objects.last().id
        return redirect(f"/shows/{new_show_id}")


def showdelete(request, id_solicitado):
    borrar = Tv_shows.objects.get(id=id_solicitado)
    #print(borrar)
    borrar.delete()
    return redirect("/shows")





# return redirect(f"/libro/{id_solicitado}")
