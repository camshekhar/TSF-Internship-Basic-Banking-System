from django.shortcuts import redirect, render
from .models import CustomerDetail, Transfer
from django.contrib import messages


# Landing Page...
def home(request):
    return render(request, 'index.html')

# View All Customers Details...
def viewAllCustomer(request):
    
    cust_details = CustomerDetail.objects.all() 
    return render(request, 'viewcustomers.html', {'cust_details':cust_details})

# Perform Transactions/ Transfer money from one Customer to other...
def transaction(request):
    customer = CustomerDetail.objects.all()
    j='null'
    if request.method=="POST":
        semail=request.POST['semail']
        amt=request.POST['amount']
        remail=request.POST['remail']
        amt=int(amt)
        
        if semail == 'select' or remail == 'select' or (semail=='select' and remail=='select') or remail == semail:
            messages.warning(request,"Email Id not selected or both Email Id's are same")  
        elif amt <= 0:
            messages.warning(request,'Please provide valid money amount!!')
        else:
            for c in customer:
                if c.email==semail:
                    j=semail
                    i=c.id
                    name = c.name
                    if amt > c.curr_balance:
                        messages.warning(request,"Insufficient Balance in Sender's Account!")   
                    break

        for x in customer:
            if x.email == remail:
                rec_id = x.id
                rec_name = x.name
                rec_bal = x.curr_balance
                break
 
        for c in customer: 
            if c.email == semail and remail != semail and remail != 'select' and amt <= c.curr_balance and amt > 0:
                q1= Transfer(sender_name = name , receiver_name = rec_name, amount=amt)
                accbal = c.curr_balance - amt
                q2 = CustomerDetail.objects.filter(id = i).update(curr_balance = accbal)
                q1.save()
                accbal = rec_bal + amt
                q3 = CustomerDetail.objects.filter(id = rec_id).update(curr_balance = accbal)
                messages.success(request,"Transaction Successfully Completed!")
                return redirect('transferdetails')
                
    return render(request,'transfer.html',{'customer':customer})

# See Transfer Details...
def transferDetails(request):
    
    tr_details = Transfer.objects.all()
    return render(request, 'transferdetails.html', {'tr_details':tr_details})
   
    
    
    
    
    
    