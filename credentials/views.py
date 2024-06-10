from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned,ObjectDoesNotExist
import pyautogui as pag
from . models import Collection_Agent, Credentials, Municiplality, WasteBin
import geopy.distance
from django.contrib.sessions.models import Session
from django.db.models import Sum
import pyqrcode
#import png
from pyqrcode import QRCode
from datetime import date

# Create your views here.
def index(request):

    # cursor.execute("select az.review,usr.name,usr.photo from credentials_userreview az inner join credentials_user usr on az.uploaded_by=usr.username")
    # get_feedback = User_Feedback.objects.filter()
    # get_reviews = cursor.fetchall()
    # get_agents = Collection_Agent.objects.filter()

    return render(request,'basic/landing_page.html')

def myfunction(request):
    name='anu'
    phn='987654432'
    return render(request,'basic/myhomepage.html',{'n':name,'c':phn})
def method(request):
    methods='inceneration'
    return render(request,'basic/methods.html',{'m':methods})
def demo(request):
    return render(request,'basic/demo.html',{})




def signIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)
        try:
            verify = Credentials.objects.get(
                username=username, password=password)
           
            u_type = verify.user_type

            print(u_type)
            if verify.user_status == "block":
                    pag.alert(text="Your Request Waitimg For Admin Approvel",title="Pending.")

                    return redirect('credentials:index')
            
            else:

                if u_type == "municipality":

                    request.session["municipality"] = verify.username

                    return redirect('credentials:municipalityHome')
                elif u_type == "admin":
                    request.session["admin"] = verify.username

                    return redirect('credentials:AdminHome')
                
                elif u_type == "collection_agent":
                    request.session["agent"] = verify.username

                    return redirect('credentials:collectionAgent_home')

                elif u_type == "user":
                    request.session["user"] = verify.username
                    print("point0")
                    return redirect('credentials:userHome')
                
                else:
                    
                    pag.alert(text="login Failed",
                        title="failed")

        except(ObjectDoesNotExist, MultipleObjectsReturned):
            pag.alert(text="Incorrect UserName or Passwordt",
                        title="incorrect")
    return render(request,'basic/landing_page.html')

def logout(request):
    try:
        Session.objects.all().delete()
    except:
        return redirect('credentials:index')
    return redirect('credentials:index')



#Admin



def admin_index(request):
    if "admin" in request.session:
        get_admin = Credentials.objects.get(username=request.session["admin"])
    
    else:
        pag.alert(text="Verification Failed",title="Failed")
        return redirect('credentials:signIn')

   
    return render(request,'admin/admin_index.html',{'admin':get_admin})



def addMuninicipality(request):
    if "admin" in request.session:
        get_admin = Credentials.objects.get(username=request.session["admin"])
    
    else:
        pag.alert(text="Verification Failed",title="Failed")
        return redirect('credentials:signIn')
    
    if request.method =="POST":
        municipality = request.POST.get('municiplality')
        mayor = request.POST.get('mayor')
        photo = request.FILES['photo']
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
       
        
        save_detais = Municiplality(municipality=municipality,mayor=mayor,photo=photo,username=username)
        save_detais.save()
        
        if save_detais is not None:
            save_credentials = Credentials(username=username,password=password,user_type="municipality",user_status="active")
            save_credentials.save()
            pag.alert(text="Municipality added",title="Success")
    return render(request,'admin/addMuninicipality.html',{'admin':get_admin})


#Municipality
def municipalityHome(request):
    if "municipality" in request.session:
        try:
            get_municipality = Municiplality.objects.get(username=request.session["municipality"])
        except:
            pag.alert(text="Verification Failed",title="Failed")
            return redirect('credentials:signIn')
    else:
        pag.alert(text="Verification Failed",title="Failed")
        return redirect('credentials:signIn')

    
    return render(request,'municipality/municipality_index.html',{'municipality':get_municipality})

def AddWasteBin(request):
    if "municipality" in request.session:
        try:
            get_municipality = Municiplality.objects.get(username=request.session["municipality"])
        except:
            pag.alert(text="Verification Failed",title="Failed")
            return redirect('credentials:signIn')
    else:
        pag.alert(text="Verification Failed",title="Failed")
        return redirect('credentials:signIn')
    
    collection_agents = Collection_Agent.objects.filter(municipality=get_municipality.username)
    if request.method =="POST":
        name = request.POST.get('name')
        photo = request.FILES['photo']
        landmark = request.POST.get('address')
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        location = " "+(lat)+","+(lon)+" "
       
        
        add_details =WasteBin(identity=name,location=location,photo=photo, landmark=landmark,municipality=get_municipality.id)
        add_details.save()
        
        if add_details is not None:
        
            pag.alert(text="Wastebin Added",title="Success")
    
    return render(request,'municipality/AddWasteBin.html',{'municipality':get_municipality,'agents':collection_agents})




def AddCollectionAgent(request):
    if "municipality" in request.session:
        try:
            get_municipality = Municiplality.objects.get(username=request.session["municipality"])
        except:
            pag.alert(text="Verification Failed",title="Failed")
            return redirect('credentials:signIn')
    else:
        pag.alert(text="Verification Failed",title="Failed")
        return redirect('credentials:signIn')
    
    if request.method =="POST":
        name = request.POST.get('name')
        photo = request.FILES['photo']
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        v_number = request.POST.get('v_number')
        v_photo = request.FILES['v_image']
        username = request.POST.get('username')
        password = request.POST.get('password')

        add_details =Collection_Agent(name=name,phone=phone,photo=photo,
                                      address=address,vehicle_number=v_number,vehicle_image=v_photo,username=username,municipality=get_municipality.username)
        add_details.save()
        
        if add_details is not None:
            add_credentials =Credentials(username=username,password=password,user_type="collection_agent",user_status="active")
            add_credentials.save()
            pag.alert(text="Agent Added",title="Success")
    
    return render(request,'municipality/AddCollectionAgent.html',{'municipality':get_municipality,})



# Collection Agent

def collectionAgent_home(request):

    try:
        get_profile = Collection_Agent.objects.get(username=request.session["agent"])
        
    except: 
        pag.alert(text="Verification Faileds",title="Failed")
        return redirect('credentials:signIn')
 
    get_waste_bins = WasteBin.objects.filter(agent=get_profile.id)
    return render(request,'collection_agent/collectionAgent_home.html',{'collectionAgent':get_profile,'bins':get_waste_bins}) 

