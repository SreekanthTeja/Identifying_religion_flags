from django.shortcuts import render
from Webapp import forms
from Webapp.models import Religion 
from django.http import HttpResponse


# Create your views here.
def religion_view(request):
    print(request.method)
    if request.method=="POST":
        form= forms.ReligionForm(request.POST,request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Data has been inserted")
        return render(request,'MyApp/base.html',{'form':form})
    form=forms.ReligionForm()

    return render(request,'MyApp/base.html',{'form':form})
def display_view(request):
    if request.method=="POST":

        form=forms.InputForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            bars= request.POST['bars']
            stripes= request.POST['stripes']
            colours= request.POST['colours']
            red= request.POST['red']
            green= request.POST['green']
            blue= request.POST['blue']
            gold= request.POST['gold']
            white= request.POST['white']
            black= request.POST['black']
            orange= request.POST['orange']
            circles= request.POST['circles']
            crosses= request.POST['crosses']
            saltires= request.POST['saltires']
            quarters= request.POST['quarters']
            sunstars= request.POST['sunstars']
            crescent= request.POST['crescent']
            triangle= request.POST['triangle']
            icon= request.POST['icon']
            animate= request.POST['animate']
            text= request.POST['text']
            import numpy as np
            pre_data = [bars,stripes,colours,red , green , blue, gold , white , black , orange ,circles,crosses,
                saltires,quarters,sunstars,crescent,triangle,icon,animate,text ]
            test_data = np.array([[int(i) for i in pre_data]])
            
            op=random_algorithm(test_data)
            var=Religion.objects.get(religion_id=1)
            print(op)
            return render(request,'MyApp/base.html',{'form':form, 'op':var})
    form=forms.InputForm()
    return render(request,'MyApp/base.html',{'form':form})



def random_algorithm(test1):
    print(test1)
    import numpy as np 
    
    import pandas as pd 
    url="http://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data"
    names = ['name','landmass','zone','area','population','language','religion', 'bars','stripes',
         'colours','red','green','blue','gold','white','black','orange','mainhue','circles','crosses','saltires','quarters',
        'sunstars','crescent','triangle','icon','animate','text','topleft','botright']
    dataset=pd.read_csv(url,names=names)
    # print(dataset.head(10))
    dataset.head(10)
    # X = dataset.drop(['name','landmass','zone','area','population','language','religion','mainhue','topleft','botright'],axis=1)
    # y = dataset[['religion']]
    feature_cols=['bars' , 'stripes',  'colours' , 'red' , 'green',  'blue' , 'gold' , 'white' , 'black' , 'orange' ,'circles',  'crosses' , 'saltires'  ,'quarters' , 'sunstars',  'crescent' , 'triangle' , 'icon','animate', 'text' ]
    X=dataset[feature_cols]
    y = dataset[['religion']]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.03 , random_state=0)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    from sklearn.ensemble import RandomForestClassifier

    clf = RandomForestClassifier(n_estimators=194, random_state=4)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(test1)
    # print(y_pred)
    # y_pred = clf.predict([[0,0,2,1,0,0,1,0,0,0,0,0,0,0,5,0,0,0,0,0]])
    # print(X_test.shape)
    # print(X_test)
    # print(y_pred.shape)
    # print(y_pred)
    return y_pred

