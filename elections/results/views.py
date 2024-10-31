from django.shortcuts import render, redirect
from django.db import connection
from .models import *
from .forms import ElectionResultForm
from collections import defaultdict
from django.contrib import messages

# Create your views here.
def homepage(request):

    return render(request,'homepage.html')

def polling_unit(request):
    with connection.cursor() as cursor:
        cursor.execute(
    
            "SELECT polling_unit.polling_unit_id,announced_pu_results.party_abbreviation,announced_pu_results.party_score,announced_pu_results.polling_unit_uniqueid FROM polling_unit INNER JOIN announced_pu_results ON polling_unit.polling_unit_id = announced_pu_results.polling_unit_uniqueid ORDER BY polling_unit.polling_unit_id"
        )
        results= cursor.fetchall()
        polling_details= [
            {'polling_unit_id':row[0],'party_abbreviation':row[1],'party_score':row[2]}
            for row in results
        ]
    return render(request,'polling_unit.html', {'polling_details':polling_details })

def lga(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT lga.lga_name,lga.lga_id, announced_lga_results.lga_name,announced_lga_results.party_abbreviation,announced_lga_results.party_score FROM lga INNER JOIN announced_lga_results ON lga.lga_id = announced_lga_results.lga_name"
        )
        results = cursor.fetchall()
        lga_results = [
            {'lga_name':row[0], 'party_abbreviation':row[3], 'party_score':row[4]}
            for row in results
        ]
       
        result = defaultdict(list)
        for row in lga_results:
            lga_name = row['lga_name']
            party_abbreviation= row['party_abbreviation']
            party_score = row['party_score']
            result[lga_name].append({'party_abbreviation':party_abbreviation,'party_score':party_score})
    
    return render(request,'lga.html', {'lga_results':dict(result)})

def store_election_result(request):
    form = None
    if request.method == 'POST':
        form = ElectionResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully posted')
            return render(request, 'store-election-result.html', {'messages':messages})
        else:
            form = ElectionResultForm()
    return render(request,'store-election-result.html', {'forms':form})
    ''