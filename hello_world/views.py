from django.shortcuts import render
import csv
import json

def test_view(request):
    return render(request, "test.html", {})

def map_view(request): 
    data=[]
    with open('SkinCancerbyCountries.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(row)
            data.append({
                "name": row["Country"],
                "value": row["Melanoma Annual Incidence"]
            })
            
        return render(request, "map.html", {"data": json.dumps(data)})