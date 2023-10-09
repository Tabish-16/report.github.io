from urllib import response
from django.http import HttpResponse, HttpResponseRedirect,FileResponse,JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import *
import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.template.loader import get_template
import pdfkit
import qrcode
from xhtml2pdf import pisa


def userlogin(request):
     if request.method == "POST":
          userName = request.POST['username']
          password = request.POST['password']

          user = authenticate(request,username=userName,password=password)
          if user is not None:
               login(request,user)
               return redirect('home')
               
          else:
               return HttpResponse("User Not Found")
     else:
          if request.user.is_authenticated:
               print(request.user)
               return redirect('home')
               
          
          else:
               return render(request,"LoginForm.html")

def logoutUser(request):
     logout(request)
     if request.user.is_authenticated:
          return redirect('home') 
     else:
          return redirect("login")


@login_required(login_url="/login")     
def home(request):
     return render(request,"index.html")

@login_required(login_url="/login",redirect_field_name="drinkingWaterForm")
def drinkingWaterForm(request):


     if request.method == 'POST':
          location = request.POST['location']
          lab_report_no = request.POST['lab_report_no']
          invoice_bill_no = request.POST['invoice_bill_no']
          reporting_date = request.POST['reporting_date']
          reporting_to = request.POST['reporting_to']
          address = request.POST['address']
          attention = request.POST['attention']
          email = request.POST['email']
          sample_id = request.POST['sample_id']
          collection_date = request.POST['collection_date']
          sample_description = request.POST['sample_description']
          sample_type = request.POST['sample_type']
          sample_collected_by = request.POST['sample_collected_by']
          date_of_analysis_from = request.POST['date_of_analysis_from']
          date_of_analysis_to = request.POST['date_of_analysis_to']
          test_description = request.POST['test_description']
          select = request.POST.get('water-select')
          water_sr1 = request.POST['water_sr1']
          water_sr2 = request.POST['water_sr2']
          water_sr3 = request.POST['water_sr3']
          water_sr4 = request.POST['water_sr4']
          water_sr5 = request.POST['water_sr5']
          water_sr6 = request.POST['water_sr6']
          water_sr7 = request.POST['water_sr7']
          water_sr8 = request.POST['water_sr8']
          water_sr9 = request.POST['water_sr9']
          water_sr10 = request.POST['water_sr10']
          water_sr11 = request.POST['water_sr11']
          water_sr12 = request.POST['water_sr12']
          water_sr13 = request.POST['water_sr13']
          water_sr14 = request.POST['water_sr14']
          water_sr15 = request.POST['water_sr15']
          water_sr16 = request.POST['water_sr16']
          water_sr17 = request.POST['water_sr17']
          water_sr18 = request.POST['water_sr18']
          water_sr19 = request.POST['water_sr19']
          water_sr20 = request.POST['water_sr20']
          water_sr21 = request.POST['water_sr21']
          water_sr22 = request.POST['water_sr22']
          water_sr23 = request.POST['water_sr23']
          water_sr24 = request.POST['water_sr24']
          water_sr25 = request.POST['water_sr25']
          water_sr26 = request.POST['water_sr26']
          water_sr27 = request.POST['water_sr27']
          water_sr28 = request.POST['water_sr28']
          water_sr29 = request.POST['water_sr29']
          water_sr30 = request.POST['water_sr30']
          water_sr31 = request.POST['water_sr31']
          water_sr32 = request.POST['water_sr32']
          legend_1 = request.POST['legend-1']
          legend_2 = request.POST['legend-2']
          legend_3 = request.POST['legend-3']
          legend_4 = request.POST['legend-4']
          legend_5 = request.POST['legend-5']
          legend_6 = request.POST['legend-6']
          legend_7 = request.POST['legend-7']
          legend_8 = request.POST['legend-8']
          legend_9 = request.POST['legend-9']
          legend_10 = request.POST['legend-10']
          legend_11 = request.POST['legend-11']
          edit_note = request.POST['edit-note']
          custom_legend = request.POST['custom-legend']
          doc_con_1 = request.POST['doc-con-1']
          doc_con_2 = request.POST['doc-con-2']
          doc_con_3 = request.POST['doc-con-3']
          analyzed_by_w = request.FILES["analyzedby" ]
          reviewd_by_w = request.FILES["reviewedby" ]
          approved_by_w = request.FILES["approvedby" ]
          approved_by_w1 = request.FILES["approvedby1" ]




          waterForm = DrinkingWaterForm(lab_report_no = lab_report_no, invoice_bill_no = invoice_bill_no,
                                        reporting_date = reporting_date,report_to = reporting_to, address =address,
                                        attention = attention, email = email, sample_id = sample_id,
                                        sample_collection_date=collection_date, sample_description = sample_description,
                                        sample_type = sample_type, sample_collected_by = sample_collected_by,
                                        date_of_analysis_from = date_of_analysis_from, date_of_analysis_to =  date_of_analysis_to,
                                        test_description=test_description,select=select, water_sr1 = water_sr1, water_sr2 = water_sr2, water_sr3 =  water_sr3,
                                        water_sr4 = water_sr4, water_sr5=water_sr5, water_sr6 = water_sr6, water_sr7 = water_sr7,
                                        water_sr8=water_sr8,water_sr9=water_sr9,water_sr10=water_sr10,water_sr11=water_sr11,water_sr12=water_sr12,
                                        water_sr13 = water_sr13,water_sr14=water_sr14,water_sr15=water_sr15,water_sr16=water_sr16,
                                        water_sr17=water_sr17,water_sr18=water_sr18,water_sr19=water_sr19,water_sr20=water_sr20,
                                        water_sr21=water_sr21,water_sr22=water_sr22,water_sr23=water_sr23,water_sr24=water_sr24,
                                        water_sr25=water_sr25,water_sr26=water_sr26,water_sr27=water_sr27,water_sr28=water_sr28,
                                        water_sr29=water_sr29,water_sr30=water_sr30,water_sr31=water_sr31,water_sr32=water_sr32,
                                         legend_1=legend_1,legend_2=legend_2, legend_3=legend_3,legend_4=legend_4,
                                        legend_5 = legend_5,legend_6=legend_6,legend_7=legend_7,legend_8=legend_8,legend_9=legend_9,
                                        legend_10=legend_10,legend_11=legend_11,edit_note = edit_note, custom_legend=custom_legend,
                                        doc_controll_1=doc_con_1,doc_controll_2=doc_con_2,doc_controll_3=doc_con_3,analyzed_by=analyzed_by_w,
                                        reviewed_by=reviewd_by_w,approved_by=approved_by_w,approved_by1=approved_by_w1,location = location)


          waterForm.save()
          messages.success(request, 'Operation was successful!')
          id = (DrinkingWaterForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/view-form/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               
               return render(request, "drinkingWaterForm.html")
     else:
          return render(request, "drinkingWaterForm.html")

@login_required(login_url="/login")
def gaseousEmission(request):
    if request.method == 'POST':
        location = request.POST['location']
        GasEm_lab_report_no1 = request.POST['GasEm-lab_report_no']
        GasEm_invoice_bill_no = request.POST['GasEm-invoice-bill-no']
        GaseEm_reporting_date = request.POST['GasEm-reporting-date']
        GaseEm_reporting_to = request.POST['GasEm-report-to']
        GaseEm_address = request.POST['GasEm-address']
        GaseEm_attention = request.POST['GasEm-attention']
        GaseEm_email = request.POST['GasEm-email']
        GaseEm_test_id = request.POST['GasEm-test-id']
        GaseEm_test_perf_date = request.POST['GasEm-test-perf-date']
        GaseEm_test_type = request.POST['GasEm-test-type']
        GaseEm_test_perf_by = request.POST['GasEm-test-perf-by']
        GasEm_test_desc = request.POST['GasEm-test-desc']
        GaseEm_types = request.POST.get('GasEm-type')
        GaseEm_select = request.POST.get('select')
        GaseEm_sr1 = request.POST['GasEm-sr1']
        GaseEm_sr2 = request.POST['GasEm-sr2']
        GaseEm_sr3 = request.POST['GasEm-sr3']
        GaseEm_sr4 = request.POST['GasEm-sr4']
        GaseEm_sr5 = request.POST['GasEm-sr5']
        GaseEm_sr6 = request.POST['GasEm-sr6']
        GaseEm_sr7 = request.POST['GasEm-sr7']
        GaseEm_sr8 = request.POST['GasEm-sr8']
        GaseEm_sr9 = request.POST['GasEm-sr9']
        GaseEm_sr10 = request.POST['GasEm-sr10']
        GaseEm_sr11 = request.POST['GasEm-sr11']
        GaseEm_sr12 = request.POST['GasEm-sr12']
        GaseEm_sr13 = request.POST['GasEm-sr13']
        GaseEm_sr14 = request.POST['GasEm-sr14']
        GaseEm_sr15 = request.POST['GasEm-sr15']
        GaseEm_sr16 = request.POST['GasEm-sr16']
        GaseEm_sr17 = request.POST['GasEm-sr17']
        GaseEm_sr18 = request.POST['GasEm-sr18']
        GaseEm_sr19 = request.POST['GasEm-sr19']
        GaseEm_sr20 = request.POST['GasEm-sr20']
        GaseEm_sr21 = request.POST['GasEm-sr21']
        GaseEm_sr22 = request.POST['GasEm-sr22']
        GaseEm_legend_1 = request.POST['GasEm-legend-1']
        GaseEm_legend_2 = request.POST['GasEm-legend-2']
        GaseEm_legend_3 = request.POST['GasEm-legend-3']
        GaseEm_legend_4 = request.POST['GasEm-legend-4']
        GaseEm_legend_5 = request.POST['GasEm-legend-5']
        GaseEm_legend_6 = request.POST['GasEm-legend-6']
        GaseEm_legend_7 = request.POST['GasEm-legend-7']
        GaseEm_legend_8 = request.POST['GasEm-legend-8']
        GaseEm_legend_9 = request.POST['GasEm-legend-9']
        GaseEm_legend_10 = request.POST['GasEm-legend-10']
        GaseEm_legend_11 = request.POST['GasEm-legend-11']
        GaseEm_edit_note = request.POST['GasEm-editnote']
        GaseEm_custom_legend = request.POST['GasEm-custom-legend']
        GaseEm_doc_con_1 = request.POST['GasEm-doc1']
        GaseEm_doc_con_2 = request.POST['GasEm-doc2']
        GaseEm_doc_con_3 = request.POST['GasEm-doc3']
        GaseEm_analyzed_by = request.FILES["GasEm-analyzedby" ]
        GaseEm_reviewd_by = request.FILES["GasEm-reviewedby" ]
        GaseEm_approved_by = request.FILES["GasEm-approvedby" ]
        GaseEm_approved_by1 = request.FILES["GasEm-approvedby1" ]


        gaseousForm = GaseousEmissionForm(GasEm_lab_report_no1 = GasEm_lab_report_no1,GasEm_invoice_bill_no = GasEm_invoice_bill_no,
                                          GaseEm_reporting_date=GaseEm_reporting_date,GaseEm_reporting_to=GaseEm_reporting_to,
                                          GaseEm_address=GaseEm_address,GaseEm_attention=GaseEm_attention,GaseEm_email=GaseEm_email,
                                          GaseEm_test_id=GaseEm_test_id,GaseEm_test_perf_date =GaseEm_test_perf_date,GaseEm_test_type=GaseEm_test_type,GaseEm_test_perf_by=GaseEm_test_perf_by,
                                          GasEm_test_desc = GasEm_test_desc,GaseEm_types=GaseEm_types,GaseEm_select=GaseEm_select,GaseEm_sr1=GaseEm_sr1,
                                          GaseEm_sr2=GaseEm_sr2,GaseEm_sr3=GaseEm_sr3,GaseEm_sr4=GaseEm_sr4,GaseEm_sr5=GaseEm_sr5,GaseEm_sr6=GaseEm_sr6,
                                          GaseEm_sr7=GaseEm_sr7,GaseEm_sr8=GaseEm_sr8,GaseEm_sr9=GaseEm_sr9,GaseEm_sr10=GaseEm_sr10,GaseEm_sr11=GaseEm_sr11,
                                          GaseEm_sr12=GaseEm_sr12,GaseEm_sr13=GaseEm_sr13,GaseEm_sr14=GaseEm_sr14,GaseEm_sr15=GaseEm_sr15,GaseEm_sr16=GaseEm_sr16,
                                          GaseEm_sr17=GaseEm_sr17,GaseEm_sr18=GaseEm_sr18,GaseEm_sr19=GaseEm_sr19,GaseEm_sr20=GaseEm_sr20,
                                          GaseEm_sr21=GaseEm_sr21,GaseEm_sr22=GaseEm_sr22,GaseEm_legend_1=GaseEm_legend_1,GaseEm_legend_2=GaseEm_legend_2,
                                          GaseEm_legend_3=GaseEm_legend_3,GaseEm_legend_4=GaseEm_legend_4,GaseEm_legend_5=GaseEm_legend_5,
                                          GaseEm_legend_6=GaseEm_legend_6,GaseEm_legend_7=GaseEm_legend_7,GaseEm_legend_8=GaseEm_legend_8,
                                          GaseEm_legend_9=GaseEm_legend_9,GaseEm_legend_10=GaseEm_legend_10,GaseEm_legend_11=GaseEm_legend_11,
                                          GaseEm_edit_note=GaseEm_edit_note,location=location,
                                          GaseEm_custom_legend=GaseEm_custom_legend,GaseEm_doc_con_1=GaseEm_doc_con_1,GaseEm_doc_con_2=GaseEm_doc_con_2,
                                          GaseEm_doc_con_3=GaseEm_doc_con_3,GaseEm_analyzed_by=GaseEm_analyzed_by,GaseEm_reviewd_by=GaseEm_reviewd_by,
                                          GaseEm_approved_by=GaseEm_approved_by,GaseEm_approved_by1=GaseEm_approved_by1)

        gaseousForm.save()
        id = (GaseousEmissionForm.objects.last()).id
        if "submit_and_view" in request.POST:
               url = f"/GaseousForm-view-form/{str(id)}/"
               return redirect(to=url)
        if "submit_and_new" in request.POST:
               return render(request, "gaseousEmission.html")

    else:
         return render(request,"gaseousEmission.html")

@login_required(login_url="/login")
def ambientAirForm(request):
        if request.method == 'POST':
            location = request.POST['location']
            ambientAir_lab_report_no1 = request.POST['ambient_Air_lab_report_no']
            ambientAir_invoice_bill_no = request.POST['ambientAir_invoice_no']
            ambientAir_reporting_date = request.POST['ambientAir_rep_date']
            ambientAir_reporting_to = request.POST['ambientAir_rep_to']
            ambientAir_address = request.POST['ambientAir_address']
            ambientAir_attention = request.POST['ambientAir_attention']
            ambientAir_email = request.POST['ambientAir_email']
            ambientAir_test_id = request.POST['ambientAir_testid']
            ambientAir_test_perf_date = request.POST['ambientAir_test_perf_date']
            ambientAir_test_type_location = request.POST['ambientAir_testtype_location']
            ambientAir_test_perf_by = request.POST['ambientAir_test_perf_by']
            ambientAir_test_desc = request.POST['ambientAir_test_desc']
            ambienAir_select = request.POST['select']
            ambientAir_sr1 = request.POST['ambientAir_sr1']
            ambientAir_sr2 = request.POST['ambientAir_sr2']
            ambientAir_sr3 = request.POST['ambientAir_sr3']
            ambientAir_sr4 = request.POST['ambientAir_sr4']
            ambientAir_sr5 = request.POST['ambientAir_sr5']
            ambientAir_sr6 = request.POST['ambientAir_sr6']
            ambientAir_sr7 = request.POST['ambientAir_sr7']
            ambientAir_sr8 = request.POST['ambientAir_sr8']
            ambientAir_sr9 = request.POST['ambientAir_sr9']
            ambientAir_sr10 = request.POST['ambientAir_sr10']
            ambientAir_sr11 = request.POST['ambientAir_sr11']
            ambientAir_sr12 = request.POST['ambientAir_sr12']
            ambientAir_sr13 = request.POST['ambientAir_sr13']
            ambientAir_sr14 = request.POST['ambientAir_sr14']
            ambientAir_legend_1 = request.POST['ambientAir-legend-1']
            ambientAir_legend_2 = request.POST['ambientAir-legend-2']
            ambientAir_legend_3 = request.POST['ambientAir-legend-3']
            ambientAir_legend_4 = request.POST['ambientAir-legend-4']
            ambientAir_legend_5 = request.POST['ambientAir-legend-5']
            ambientAir_legend_6 = request.POST['ambientAir-legend-6']
            ambientAir_edit_note = request.POST['ambientAir_editNote']
            ambientAir_custom_legend = request.POST['ambientAir_customlegend']
            ambientAir_doc_con_1 = request.POST['ambientAir_doc1']
            ambientAir_doc_con_2 = request.POST['ambientAir_doc2']
            ambientAir_doc_con_3 = request.POST['ambientAir_doc3']
            ambientAir_analyzed_by = request.FILES["ambientAir_analyzedby" ]
            ambientAir_reviewd_by = request.FILES["ambientAir_reviewedby" ]
            ambientAir_approved_by = request.FILES["ambientAir_approvedby" ]
            ambientAir_approved_by1 = request.FILES["ambientAir_approvedby1" ]

            ambientAir = AmbientAirForm(ambienAir_lab_report_no1 = ambientAir_lab_report_no1,ambienAir_invoice_bill_no=ambientAir_invoice_bill_no,
                                        ambientAir_reporting_date = ambientAir_reporting_date,ambientAir_reporting_to=ambientAir_reporting_to,
                                        ambientAir_address=ambientAir_address,ambientAir_attention=ambientAir_attention,ambientAir_email=ambientAir_email,
                                        ambientAir_test_id=ambientAir_test_id,ambientAir_test_perf_date=ambientAir_test_perf_date,ambientAir_test_type_location =
                                        ambientAir_test_type_location,ambientAir_test_perf_by=ambientAir_test_perf_by,ambienAir_test_desc=ambientAir_test_desc,
                                        ambienAir_select=ambienAir_select,ambientAir_sr1 =ambientAir_sr1,ambientAir_sr2=ambientAir_sr2,ambientAir_sr3=ambientAir_sr3,ambientAir_sr4=ambientAir_sr4,
                                        ambientAir_sr5=ambientAir_sr5,ambientAir_sr6=ambientAir_sr6,ambientAir_sr7=ambientAir_sr7,ambientAir_sr8=ambientAir_sr8,
                                        ambientAir_sr9=ambientAir_sr9,ambientAir_sr10=ambientAir_sr10,ambientAir_sr11=ambientAir_sr11,ambientAir_sr12=ambientAir_sr12,
                                        ambientAir_sr13=ambientAir_sr13,ambientAir_sr14=ambientAir_sr14,ambientAir_legend_1=
                                        ambientAir_legend_1,ambientAir_legend_2=ambientAir_legend_2,ambientAir_legend_3=ambientAir_legend_3,ambientAir_legend_4=ambientAir_legend_4,
                                        ambientAir_legend_5=ambientAir_legend_5,ambientAir_legend_6=ambientAir_legend_6,
                                        ambientAir_edit_note=ambientAir_edit_note,ambientAir_custom_legend=ambientAir_custom_legend,ambientAir_doc_con_1=ambientAir_doc_con_1,ambientAir_doc_con_2=ambientAir_doc_con_2,
                                        ambientAir_doc_con_3=ambientAir_doc_con_3,ambientAir_analyzed_by=ambientAir_analyzed_by,ambientAir_reviewd_by=ambientAir_reviewd_by,
                                        ambientAir_approved_by=ambientAir_approved_by,location=location,ambientAir_approved_by1=ambientAir_approved_by1)
            ambientAir.save()
            id = (AmbientAirForm.objects.last()).id
            if "submit_and_view" in request.POST:
               url = f"/ambientAir-view/{str(id)}/"
               return redirect(to=url)
            if "submit_and_new" in request.POST:
               return render(request, "ambientAirForm.html")
        else:
          return render(request,"ambientAirForm.html")

@login_required(login_url="/login")
def wasteWaterSludge(request):
     if request.method == 'POST':
            location = request.POST['location']
            ww_lab_report_no = request.POST['ww_lab_report_no']
            ww_invoice_no = request.POST['ww_invoice_no']
            ww_report_date = request.POST['ww_report_date']
            ww_report_to = request.POST['ww_report_to']
            ww_address = request.POST['ww_address']
            ww_attention = request.POST['ww_attention']
            ww_email = request.POST['ww_email']
            ww_sampleid = request.POST['ww_sampleid']
            ww_sample_colec_Date = request.POST['ww_sample_colec_Date']
            ww_sample_desc = request.POST['ww_sample_desc']
            ww_sample_type = request.POST['ww_sample_type']
            ww_sample_colec_by = request.POST['ww_sample_colec_by']
            ww_date_of_analy = request.POST['ww_date_of_analy']
            ww_test_desc = request.POST['ww_test_desc']
            ww_sr1 = request.POST['ww_sr1']
            ww_sr2 = request.POST['ww_sr2']
            ww_sr3 = request.POST['ww_sr3']
            ww_sr4 = request.POST['ww_sr4']
            ww_sr5 = request.POST['ww_sr5']
            ww_sr6 = request.POST['ww_sr6']
            ww_sr7 = request.POST['ww_sr7']
            ww_sr8 = request.POST['ww_sr8']
            ww_sr9 = request.POST['ww_sr9']
            ww_sr10 = request.POST['ww_sr10']
            ww_sr11 = request.POST['ww_sr11']
            ww_sr12 = request.POST['ww_sr12']
            ww_sr13 = request.POST['ww_sr13']
            ww_legend_1 = request.POST['ww-legend-1']
            ww_legend_2 = request.POST['ww-legend-2']
            ww_legend_3 = request.POST['ww-legend-3']
            ww_legend_4 = request.POST['ww-legend-4']
            ww_legend_5 = request.POST['ww-legend-5']
            ww_legend_6 = request.POST['ww-legend-6']
            ww_legend_7 = request.POST['ww-legend-7']
            ww_legend_8 = request.POST['ww-legend-8']
            ww_legend_9 = request.POST['ww-legend-9']
            ww_legend_10 = request.POST['ww-legend-10']
            ww_legend_11 = request.POST['ww-legend-11']
            ww_editnote = request.POST['ww_editnote']
            ww_custom_legend = request.POST['ww_custom_legend']
            ww_doc_con_1 = request.POST['ww_doc1']
            ww_doc_con_2 = request.POST['ww_doc2']
            ww_doc_con_3 = request.POST['ww_doc3']
            ww_analyzed_by = request.FILES["ww_analyzedby" ]
            ww_reviewd_by = request.FILES["ww_reviewedby" ]
            ww_approved_by = request.FILES["ww_approvedby" ]
            ww_approved_by1 = request.FILES["ww_approvedby1" ]


            wasteWaterForm = WasteWaterSludge(ww_lab_report_no=ww_lab_report_no,ww_invoice_no=ww_invoice_no,ww_report_date=ww_report_date,
                                              ww_report_to=ww_report_to,ww_address=ww_address,ww_attention=ww_attention,ww_email=ww_email,
                                              ww_sampleid=ww_sampleid,ww_sample_colec_Date=ww_sample_colec_Date,ww_sample_desc=ww_sample_desc,
                                              ww_sample_type=ww_sample_type,ww_sample_colec_by=ww_sample_colec_by,ww_date_of_analy=ww_date_of_analy,
                                              ww_test_desc=ww_test_desc,ww_sr1=ww_sr1,ww_sr2=ww_sr2,ww_sr3=ww_sr3,ww_sr4=ww_sr4,ww_sr5=ww_sr5,
                                              ww_sr6=ww_sr6,ww_sr7=ww_sr7,ww_sr8=ww_sr8,ww_sr9=ww_sr9,ww_sr10=ww_sr10,ww_sr11=ww_sr11,ww_sr12=ww_sr12,
                                              ww_sr13=ww_sr13,ww_legend_1=ww_legend_1,ww_legend_2=ww_legend_2,location=location,
                                              ww_legend_3=ww_legend_3,ww_legend_4=ww_legend_4,ww_legend_5=ww_legend_5,ww_legend_6=ww_legend_6,ww_legend_7=ww_legend_7,
                                              ww_legend_8=ww_legend_8,ww_legend_9=ww_legend_9,ww_legend_10=ww_legend_10,ww_legend_11=ww_legend_11,ww_editnote=ww_editnote,ww_custom_legend=ww_custom_legend,
                                              ww_doc_con_1=ww_doc_con_1,ww_doc_con_2=ww_doc_con_2,ww_doc_con_3=ww_doc_con_3,ww_analyzed_by=ww_analyzed_by,ww_reviewd_by=ww_reviewd_by,
                                              ww_approved_by=ww_approved_by,ww_approved_by1=ww_approved_by1)


            wasteWaterForm.save()
            id = (WasteWaterSludge.objects.last()).id
            if "submit_and_view" in request.POST:
               url = f"/wasteWaterSludge-view/{str(id)}/"
               return redirect(to=url)
            if "submit_and_new" in request.POST:
               return redirect("wasteWaterSludge")
     return render(request,"wasteWaterSludge.html")


@login_required(login_url="/login")
def vehicularEmission(request):
     if request.method == "POST":
          location = request.POST['location']
          vehEm_lab_report_no = request.POST['vehEm_lab_report_no']
          vehEm_invoice_no = request.POST['vehEm_invoice_no']
          vehEm_report_date = request.POST['vehEm_report_date']
          vehEm_report_to = request.POST['vehEm_report_to']
          vehEm_address = request.POST['vehEm_address']
          vehEm_attention = request.POST['vehEm_attention']
          vehEm_email = request.POST['vehEm_email']
          vehEm_testId = request.POST['vehEm_testId']
          vehEm_test_perf_date = request.POST['vehEm_test_perf_date']
          vehEm_test_type = request.POST['vehEm_test_type']
          vehEm_test_perfBy = request.POST['vehEm_test_perfBy']
          vehEm_test_desc = request.POST['vehEm_test_desc']
          select = request.POST['select']
          vehEm_sr1 = request.POST['vehEm_sr1']
          vehEm_sr2 = request.POST['vehEm_sr2']
          vehEm_sr3 = request.POST['vehEm_sr3']
          vehEm_legend_1 = request.POST['vehEm-legend-1']
          vehEm_legend_2 = request.POST['vehEm-legend-2']
          vehEm_legend_3 = request.POST['vehEm-legend-3']
          vehEm_legend_4 = request.POST['vehEm-legend-4']
          vehEm_legend_5 = request.POST['vehEm-legend-5']
          vehEm_legend_6 = request.POST['vehEm-legend-6']
          vehEm_legend_7 = request.POST['vehEm-legend-7']
          vehEm_legend_8 = request.POST['vehEm-legend-8']
          vehEm_legend_9 = request.POST['vehEm-legend-9']
          vehEm_legend_10 = request.POST['vehEm-legend-10']
          vehEm_legend_11 = request.POST['vehEm-legend-11']
          vehEm_edit_note = request.POST['vehEm_edit_note']
          vehEm_custom_legend = request.POST['vehEm_custom_legend']
          vehEm_doc_con1 = request.POST['vehEm_doc-con1']
          vehEm_doc_con2 = request.POST['vehEm_doc-con2']
          vehEm_doc_con3 = request.POST['vehEm_doc-con3']
          vehEm_analyzedby = request.FILES['vehEm-analyzedby']
          vehEm_reviewedby = request.FILES['vehEm-reviewedby']
          vehEm_approvedby = request.FILES['vehEm-approvedby']
          vehEm_approvedby1 = request.FILES['vehEm-approvedby1']


          vehicularemissionForm = VehiculEmissionForm(vehEm_lab_report_no=vehEm_lab_report_no,vehEm_invoice_no=vehEm_invoice_no,
                                                      vehEm_report_date=vehEm_report_date,vehEm_report_to=vehEm_report_to,vehEm_address=vehEm_address,vehEm_attention=
                                                      vehEm_attention,vehEm_email=vehEm_email,vehEm_testId=vehEm_testId,vehEm_test_perf_date=vehEm_test_perf_date,
                                                      vehEm_test_type=vehEm_test_type,vehEm_test_perfBy=vehEm_test_perfBy,vehEm_test_desc=vehEm_test_desc,location=location,
                                                      select=select,vehEm_sr1=vehEm_sr1,vehEm_sr2=vehEm_sr2,vehEm_sr3=vehEm_sr3,vehEm_legend_1=
                                                      vehEm_legend_1,vehEm_legend_2=vehEm_legend_2,vehEm_legend_3=vehEm_legend_3,vehEm_legend_4=vehEm_legend_4,
                                                      vehEm_legend_5=vehEm_legend_5,vehEm_legend_6=vehEm_legend_6,vehEm_legend_7=vehEm_legend_7,vehEm_legend_8=vehEm_legend_8,
                                                      vehEm_legend_9=vehEm_legend_9,vehEm_legend_10=vehEm_legend_10,vehEm_legend_11=vehEm_legend_11,vehEm_edit_note=vehEm_edit_note,
                                                      vehEm_custom_legend=vehEm_custom_legend,vehEm_doc_con1=vehEm_doc_con1,vehEm_doc_con2=vehEm_doc_con2,vehEm_doc_con3=vehEm_doc_con3,
                                                      vehEm_analyzedby=vehEm_analyzedby,vehEm_reviewedby=vehEm_reviewedby,vehEm_approvedby=vehEm_approvedby,vehEm_approvedby1=vehEm_approvedby1)

          vehicularemissionForm.save()
          id = (VehiculEmissionForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/vehicularEmission-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect("vahicularEmission")


     return render(request,"vehicularEmission.html")

@login_required(login_url="/login")
def luxAnalysis(request):
     if request.method == 'POST':
          location = request.POST['location']
          lux_lab_report_no = request.POST['lux_lab_rep_no']
          lux_invoice_no = request.POST['lux_invoice_no']
          lux_report_date = request.POST['lux_report_date']
          lux_report_to = request.POST['lux_report_to']
          lux_address = request.POST['lux-address']
          lux_attention = request.POST['lux_attention']
          lux_email = request.POST['lux_email']
          lux_testId = request.POST['lux_testId']
          lux_test_perf_date = request.POST['lux_test_perf_date']
          lux_test_type = request.POST['lux_test_type']
          lux_test_perfBy = request.POST['lux_test_perf_by']
          lux_test_desc = request.POST['lux_test_desc']
          lux_parameters_1 = request.POST['lux_parameters_1']
          lux_result_1 = request.POST['lux_result_1']
          lux_parameters_2 = request.POST['lux_parameters_2']
          lux_result_2 = request.POST['lux_result_2']
          lux_parameters_3 = request.POST['lux_parameters_3']
          lux_result_3 = request.POST['lux_result_3']
          lux_parameters_4 = request.POST['lux_parameters_4']
          lux_result_4 = request.POST['lux_result_4']
          lux_parameters_5 = request.POST['lux_parameters_5']
          lux_result_5 = request.POST['lux_result_5']
          lux_parameters_6 = request.POST['lux_parameters_6']
          lux_result_6 = request.POST['lux_result_6']
          lux_parameters_7 = request.POST['lux_parameters_7']
          lux_result_7 = request.POST['lux_result_7']
          lux_parameters_8 = request.POST['lux_parameters_8']
          lux_result_8 = request.POST['lux_result_8']
          lux_parameters_9 = request.POST['lux_parameters_9']
          lux_result_9 = request.POST['lux_result_9']
          lux_parameters_10 = request.POST['lux_parameters_10']
          lux_result_10 = request.POST['lux_result_10']
          lux_parameters_11 = request.POST['lux_parameters_11']
          lux_result_11 = request.POST['lux_result_11']
          lux_parameters_12 = request.POST['lux_parameters_12']
          lux_result_12 = request.POST['lux_result_12']
          lux_parameters_13 = request.POST['lux_parameters_13']
          lux_result_13 = request.POST['lux_result_13']
          lux_legend_1 = request.POST['lux-legend-1']
          lux_legend_2 = request.POST['lux-legend-2']
          lux_legend_3 = request.POST['lux-legend-3']
          lux_legend_4 = request.POST['lux-legend-4']
          lux_legend_5 = request.POST['lux-legend-5']
          lux_legend_6 = request.POST['lux-legend-6']
          lux_legend_7 = request.POST['lux-legend-7']
          lux_legend_8 = request.POST['lux-legend-8']
          lux_legend_9 = request.POST['lux-legend-9']
          lux_legend_10 = request.POST['lux-legend-10']
          lux_legend_11 = request.POST['lux-legend-11']
          lux_edit_note = request.POST['lux_edit_note']
          lux_custom_legend = request.POST['lux_custom_legend']
          lux_doc_con1 = request.POST['lux_doc_con1']
          lux_doc_con2 = request.POST['lux_doc_con2']
          lux_doc_con3 = request.POST['lux_doc_con3']
          lux_analyzedby = request.FILES['lux-analyzedby']
          lux_reviewedby = request.FILES['lux-reviewedby']
          lux_approvedby = request.FILES['lux-approvedby']
          lux_approvedby1 = request.FILES['lux-approvedby1']


          luxForm = LuxAnalysisForm(lux_lab_report_no=lux_lab_report_no,lux_invoice_no=lux_invoice_no,lux_report_date=lux_report_date,
                                    lux_report_to=lux_report_to,lux_address=lux_address,lux_attention=lux_attention,lux_email=lux_email,
                                    lux_testId=lux_testId,lux_test_perf_date=lux_test_perf_date,lux_test_type=lux_test_type,lux_test_perfBy=lux_test_perfBy,
                                    lux_test_desc=lux_test_desc,lux_parameters_1=lux_parameters_1,lux_result_1=lux_result_1,lux_parameters_2=lux_parameters_2,
                                    lux_result_2=lux_result_2,lux_parameters_3=lux_parameters_3,lux_result_3=lux_result_3,lux_parameters_4=lux_parameters_4,
                                    lux_result_4=lux_result_4,lux_parameters_5=lux_parameters_5,lux_result_5=lux_result_5,lux_parameters_6=lux_parameters_6,
                                    lux_result_6=lux_result_6,lux_parameters_7=lux_parameters_7,lux_result_7=lux_result_7,lux_parameters_8=lux_parameters_8,
                                    lux_result_8=lux_result_8,lux_parameters_9=lux_parameters_9,lux_result_9=lux_result_9,lux_parameters_10=lux_parameters_10,
                                    lux_result_10=lux_result_10,lux_parameters_11=lux_parameters_11,lux_result_11=lux_result_11,lux_parameters_12=lux_parameters_12,
                                    lux_result_12=lux_result_12,lux_parameters_13=lux_parameters_13,lux_result_13=lux_result_13,lux_legend_1=lux_legend_1,
                                    lux_legend_2=lux_legend_2,lux_legend_3=lux_legend_3,lux_legend_4=lux_legend_4,lux_legend_5=lux_legend_5,
                                    lux_legend_6=lux_legend_6,lux_legend_7=lux_legend_7,lux_legend_8=lux_legend_8,lux_legend_9=lux_legend_9,lux_legend_10=lux_legend_10,
                                    lux_legend_11=lux_legend_11,lux_edit_note=lux_edit_note,location=location,
                                    lux_custom_legend=lux_custom_legend,lux_doc_con1=lux_doc_con1,lux_doc_con2=lux_doc_con2,lux_doc_con3=lux_doc_con3,lux_analyzedby=
                                    lux_analyzedby,lux_reviewedby=lux_reviewedby,lux_approvedby=lux_approvedby,lux_approvedby1=lux_approvedby1)

          luxForm.save()
          id = (LuxAnalysisForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f'/luxAnalysisReport/{str(id)}/'
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to='luxAnalysis')
     return render(request,"luxAnalysis.html")

@login_required(login_url="/login")
def packingPoly(request):
     if request.method == 'POST':
          location = request.POST['location']
          pack_lab_rep_no = request.POST['pack_lab_rep_no']
          pack_invoice = request.POST['pack_invoice']
          pack_rep_date = request.POST['pack_rep_date']
          pack_rep_to = request.POST['pack_rep_to']
          pack_address = request.POST['pack_address']
          pack_attention = request.POST['pack_attention']
          pack_email = request.POST['pack_email']
          pack_sampleId = request.POST['pack_sampleId']
          pack_sample_colc_date = request.POST['pack_sample_colc_date']
          pack_sample_desc = request.POST['pack_sample_desc']
          pack_sample_type = request.POST['pack_sample_type']
          pack_sample_colc_by = request.POST['pack_sample_colc_by']
          pack_test_desc = request.POST['pack_test_desc']
          pack_sr1 = request.POST['pack_sr1']
          pack_legend_1 = request.POST['pack-legend-1']
          pack_edit_note = request.POST['pack_edit_note']
          pack_custom_legend = request.POST['pack_custom_legend']
          doc_con1 = request.POST['doc_con1']
          doc_con2 = request.POST['doc_con2']
          doc_con3 = request.POST['doc_con3']
          pack_analyzed_by = request.FILES['pack-analyzedby']
          pack_reviewed_by = request.FILES['pack-reviewedby']
          pack_approved_by = request.FILES['pack-approvedby']
          pack_approved_by1 = request.FILES['pack-approvedby1']



          packingForm = PackingPolyBagForm(pack_lab_rep_no = pack_lab_rep_no ,pack_invoice=pack_invoice,pack_rep_date=pack_rep_date,
                                        pack_rep_to=pack_rep_to,pack_address=pack_address,pack_attention=pack_attention,pack_email=pack_email,
                                        pack_sampleId=pack_sampleId,pack_sample_colc_date=pack_sample_colc_date,pack_sample_desc=pack_sample_desc,location=location,
                                        pack_sample_type=pack_sample_type,pack_sample_colc_by=pack_sample_colc_by,pack_test_desc=
                                        pack_test_desc,pack_sr1=pack_sr1,pack_legend_1=pack_legend_1,pack_edit_note=pack_edit_note,pack_custom_legend=pack_custom_legend,doc_con1=doc_con1,doc_con2=doc_con2,doc_con3=doc_con3,
                                        pack_analyzed_by=pack_analyzed_by,pack_reviewed_by=pack_reviewed_by,pack_approved_by=pack_approved_by,pack_approved_by1=pack_approved_by1)

          packingForm.save()
          id = (PackingPolyBagForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/packingpolybag-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="packingPolyBag")
     return render(request,"packingPolyBag.html")



@login_required(login_url="/login")
def machineOil(request):
     if request.method == 'POST':
          location = request.POST['location']
          machine_lab_rep_no = request.POST['machine_lab_rep_no']
          machine_invoice_no = request.POST['machine_invoice_no']
          machine_rep_date = request.POST['machine_rep_date']
          machine_report_to = request.POST['machine_report_to']
          machine_address = request.POST['machine_address']
          machine_attention = request.POST['machine_attention']
          machine_email = request.POST['machine_email']
          machine_sampleId = request.POST['machine_sampleId']
          machine_sample_col_date = request.POST['machine_sample_col_date']
          machine_sample_desc = request.POST['machine_sample_desc']
          machine_sample_type = request.POST['machine_sample_type']
          machine_sample_col_by = request.POST['machine_sample_col_by']
          machine_test_desc = request.POST['machine_test_desc']
          machine_sr1 = request.POST['machine_sr1']
          machine_sr2 = request.POST['machine_sr2']
          machine_sr3 = request.POST['machine_sr3']
          machine_sr4 = request.POST['machine_sr4']
          machine_sr5 = request.POST['machine_sr5']
          machine_sr6 = request.POST['machine_sr6']
          machine_sr7 = request.POST['machine_sr7']
          machine_sr8 = request.POST['machine_sr8']
          machine_sr9 = request.POST['machine_sr9']
          machine_sr10 = request.POST['machine_sr10']
          machine_sr11 = request.POST['machine_sr11']
          machine_sr12 = request.POST['machine_sr12']
          machine_sr13 = request.POST['machine_sr13']
          machine_sr14 = request.POST['machine_sr14']
          machine_sr15 = request.POST['machine_sr15']
          machine_sr16 = request.POST['machine_sr16']
          machine_legend_1 = request.POST['machine_legend-1']
          machine_legend_2 = request.POST['machine_legend-2']
          custom_legend = request.POST['custom_legend']
          machine_edit_note = request.POST['machine_edit_note']
          machine_custom_legend = request.POST['machine_custom_legend']
          machine_doc1 = request.POST['machine_doc1']
          machine_doc2 = request.POST['machine_doc2']
          machine_doc3 = request.POST['machine_doc3']
          machine_analyzedby = request.FILES['machine_analyzedby']
          machine_reviewedby = request.FILES['machine_reviewedby']
          machine_approvedby = request.FILES['machine_approvedby']
          machine_approvedby1 = request.FILES['machine_approvedby']



          machineOil = MachineOilForm(machine_lab_rep_no=machine_lab_rep_no,machine_invoice_no=machine_invoice_no,
                                      machine_rep_date=machine_rep_date,machine_report_to=machine_report_to,
                                      machine_address=machine_address,machine_attention=machine_attention,
                                      machine_email=machine_email,machine_sampleId=machine_sampleId,
                                      machine_sample_col_date=machine_sample_col_date,machine_sample_desc=machine_sample_desc,
                                      machine_sample_type=machine_sample_type,machine_sample_col_by=machine_sample_col_by,
                                      machine_test_desc=machine_test_desc,machine_sr1=machine_sr1,machine_sr2=machine_sr2,
                                      machine_sr3=machine_sr3,machine_sr4=machine_sr4,machine_sr5=machine_sr5,
                                      machine_sr6=machine_sr6,machine_sr7=machine_sr7,machine_sr8=machine_sr8,location=location,
                                      machine_sr9=machine_sr9,machine_sr10=machine_sr10,machine_sr11=machine_sr11,machine_sr12=machine_sr12,
                                      machine_sr13=machine_sr13,machine_sr14=machine_sr14,machine_sr15=machine_sr15,machine_sr16=
                                      machine_sr16,machine_legend_1=machine_legend_1,machine_legend_2=machine_legend_2,custom_legend=custom_legend,
                                      machine_edit_note=machine_edit_note,machine_custom_legend=machine_custom_legend,machine_doc1=machine_doc1,machine_doc2=machine_doc2,machine_doc3=machine_doc3,
                                     machine_analyzedby=machine_analyzedby,machine_reviewedby=machine_reviewedby,machine_approvedby=machine_approvedby,machine_approvedby1=machine_approvedby1)
          machineOil.save()
          id = (MachineOilForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/machineOil-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="machineOil")


     return render(request,"machineOil.html")


@login_required(login_url="/login")
def microbialAnalysis(request):
     if request.method == 'POST':
          location = request.POST['location']
          micro_lab_report_no = request.POST['micro_lab_report_no']
          micro_invoice_bill = request.POST['micro_invoice_bill']
          micro_rep_date = request.POST['micro_rep_date']
          micro_rep_to = request.POST['micro_rep_to']
          micro_address = request.POST['micro_address']
          micro_attention = request.POST['micro_attention']
          micro_email = request.POST['micro_email']
          micro_sampleId = request.POST['micro_sampleId']
          micro_sample_col_date = request.POST['micro_sample_col_date']
          micro_sample_desc = request.POST['micro_sample_desc']
          micro_sample_type = request.POST['micro_sample_type']
          micro_sample_col_by = request.POST['micro_sample_col_date']
          micro_date_analysis = request.POST['micro_date_analysis']
          micro_test_desc = request.POST['micro_test_desc']
          micro_sr1 = request.POST['micro_sr1']
          micro_sr2 = request.POST['micro_sr2']
          micro_sr3 = request.POST['micro_sr3']
          micro_sr4 = request.POST['micro_sr4']
          micro_sr5 = request.POST['micro_sr5']
          micro_sr6 = request.POST['micro_sr6']
          micro_legend_1 = request.POST['micro_legend_1']
          micro_legend_2 = request.POST['micro_legend_2']
          micro_editnote = request.POST['micro_editnote']
          micro_custom_legend = request.POST['micro_custom_legend']
          micro_doc1 = request.POST['micro_doc1']
          micro_doc2 = request.POST['micro_doc2']
          micro_doc3 = request.POST['micro_doc3']
          micro_analyzedby = request.FILES['micro_analyzedby']
          micro_reviewedby = request.FILES['micro_reviewedby']
          micro_approvedby = request.FILES['micro_approvedby']
          micro_approvedby1 = request.FILES['micro_approvedby1']


          microbialForm = MicrobialAnalysis(micro_lab_report_no=micro_lab_report_no,micro_invoice_bill=micro_invoice_bill,micro_rep_date=micro_rep_date,
                                            micro_rep_to=micro_rep_to,micro_address=micro_address,micro_attention=micro_attention,micro_email=micro_email,
                                            micro_sampleId=micro_sampleId,micro_sample_col_date=micro_sample_col_date,micro_sample_desc=micro_sample_desc,
                                            micro_sample_type=micro_sample_type,micro_sample_col_by=micro_sample_col_by,micro_date_analysis=micro_date_analysis,
                                            micro_test_desc=micro_test_desc,micro_sr1=micro_sr1,micro_sr2=micro_sr2,micro_sr3=micro_sr3,micro_sr4=micro_sr4,
                                            micro_sr5=micro_sr5,micro_sr6=micro_sr6,micro_legend_1=micro_legend_1,micro_legend_2=micro_legend_2,location=location,
                                            micro_editnote=micro_editnote,micro_custom_legend=micro_custom_legend,micro_doc1=micro_doc1,micro_doc2=micro_doc2,micro_doc3=micro_doc3,
                                            micro_analyzedby=micro_analyzedby,micro_reviewedby=micro_reviewedby,micro_approvedby=micro_approvedby,micro_approvedby1=micro_approvedby1)
          microbialForm.save()
          id = (MachineOilForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/microbial-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="microBialAnalysis")
     return render(request,"microbialAnalysis.html")

@login_required(login_url="/login")
def viscousLiquid(request):
     if request.method == 'POST':
          location = request.POST['location']
          lab_rep_no = request.POST['lab_rep_no']
          invoice_no = request.POST['invoice_no']
          report_date = request.POST['report_date']
          report_to = request.POST['report_to']
          address = request.POST['address']
          Attention = request.POST['Attention']
          Email = request.POST['Email']
          sampleId = request.POST['sampleId']
          sample_Col_date = request.POST['sample_Col_date']
          sample_Desc = request.POST['sample_Desc']
          sample_type = request.POST['sample_type']
          sample_col_by = request.POST['sample_col_by']
          date_of_analysis = request.POST['date_of_analysis']
          test_desc = request.POST['test_desc']
          viscous_select = request.POST.get('select')
          sr1 = request.POST['sr1']
          legend_1 = request.POST['legend_1']
          legend_2 = request.POST['legend_2']
          edit_note = request.POST['edit_note']
          custom_legend = request.POST['custom_legend']
          doc1 = request.POST['doc1']
          doc2 = request.POST['doc2']
          doc3 = request.POST['doc3']
          analyzedby = request.FILES['analyzedby']
          reviewedby = request.FILES['reviewedby']
          approvedby = request.FILES['approvedby']
          approvedby1 = request.FILES['approvedby1']

          viscousForm = ViscousLiquid(lab_rep_no=lab_rep_no,invoice_no=invoice_no,report_date=report_date,report_to=report_to,
                                      address=address,Attention=Attention,Email=Email,sampleId=sampleId,sample_Col_date=sample_Col_date,
                                      sample_Desc=sample_Desc,sample_type=sample_type,sample_col_by=sample_col_by,date_of_analysis=date_of_analysis,
                                      test_desc=test_desc,viscous_select=viscous_select,sr1=sr1,legend_1=legend_1,legend_2=legend_2,
                                      edit_note=edit_note,custom_legend=custom_legend,doc1=doc1,location=location,
                                      doc2=doc2,doc3=doc3,analyzedby=analyzedby,reviewedby=reviewedby,approvedby=approvedby,approvedby1=approvedby1)
          viscousForm.save()
          id = (ViscousLiquid.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/viscousLiquid-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="viscousLiquid")
     return render(request,"viscousLiquid.html")


@login_required(login_url="/login")
def ambientAirQuality2(request):
     if request.method == 'POST':
          location = request.POST['location']
          lab_rep_no = request.POST['lab_rep_no']
          invoice_no = request.POST['invoice_no']
          report_date = request.POST['report_date']
          report_to = request.POST['report_to']
          address = request.POST['address']
          attention = request.POST['attention']
          email = request.POST['email']
          testId = request.POST['testId']
          test_perf_date = request.POST['test_perf_date']
          test_type = request.POST['test_type']
          test_desc = request.POST['test_desc']
          test_test_perf_by = request.POST['test_test_perf_by']
          sr1_1 = request.POST['sr1_1']
          sr1_2 = request.POST['sr1_2']
          sr1_3 = request.POST['sr1_3']
          sr1_4 = request.POST['sr1_4']
          sr1_5 = request.POST['sr1_5']
          sr1_6 = request.POST['sr1_6']
          sr1_7 = request.POST['sr1_7']
          sr1_8 = request.POST['sr1_8']
          sr1_9 = request.POST['sr1_9']
          sr1_10 = request.POST['sr1_10']
          sr2_0 = request.POST['sr2_0']
          sr2_1 = request.POST['sr2_1']
          sr2_2 = request.POST['sr2_2']
          sr2_3 = request.POST['sr2_3']
          sr2_4 = request.POST['sr2_4']
          sr2_5 = request.POST['sr2_5']
          sr2_6 = request.POST['sr2_6']
          sr2_7 = request.POST['sr2_7']
          sr2_8 = request.POST['sr2_8']
          sr2_9 = request.POST['sr2_9']
          sr3_0 = request.POST['sr3_0']
          sr3_1 = request.POST['sr3_1']
          sr3_2 = request.POST['sr3_2']
          sr3_3 = request.POST['sr3_3']
          sr3_4 = request.POST['sr3_4']
          sr3_5 = request.POST['sr3_5']
          sr3_6 = request.POST['sr3_6']
          sr3_7 = request.POST['sr3_7']
          sr3_8 = request.POST['sr3_8']
          sr3_9 = request.POST['sr3_9']
          sr4_0 = request.POST['sr4_0']
          sr4_1 = request.POST['sr4_1']
          sr4_2 = request.POST['sr4_2']
          sr4_3 = request.POST['sr4_3']
          sr4_4 = request.POST['sr4_4']
          sr4_5 = request.POST['sr4_5']
          sr4_6 = request.POST['sr4_6']
          sr4_7 = request.POST['sr4_7']
          sr4_8 = request.POST['sr4_8']
          sr4_9 = request.POST['sr4_9']
          sr5_0 = request.POST['sr5_0']
          sr5_1 = request.POST['sr5_1']
          sr5_2 = request.POST['sr5_2']
          sr5_3 = request.POST['sr5_3']
          sr5_4 = request.POST['sr5_4']
          sr5_5 = request.POST['sr5_5']
          sr5_6 = request.POST['sr5_6']
          sr5_7 = request.POST['sr5_7']
          sr5_8 = request.POST['sr5_8']
          sr5_9 = request.POST['sr5_9']
          sr6_0 = request.POST['sr6_0']
          sr6_1 = request.POST['sr6_1']
          sr6_2 = request.POST['sr6_2']
          sr6_3 = request.POST['sr6_3']
          sr6_4 = request.POST['sr6_4']
          sr6_5 = request.POST['sr6_5']
          sr6_6 = request.POST['sr6_6']
          sr6_7 = request.POST['sr6_7']
          sr6_8 = request.POST['sr6_8']
          sr6_9 = request.POST['sr6_9']
          sr7_0 = request.POST['sr7_0']
          sr7_1 = request.POST['sr7_1']
          sr7_2 = request.POST['sr7_2']
          sr7_3 = request.POST['sr7_3']
          sr7_4 = request.POST['sr7_4']
          sr7_5 = request.POST['sr7_5']
          sr7_6 = request.POST['sr7_6']
          sr7_7 = request.POST['sr7_7']
          sr7_8 = request.POST['sr7_8']
          sr7_9 = request.POST['sr7_9']
          sr8_0 = request.POST['sr8_0']
          sr8_1 = request.POST['sr8_1']
          sr8_2 = request.POST['sr8_2']
          sr8_3 = request.POST['sr8_3']
          sr8_4 = request.POST['sr8_4']
          sr8_5 = request.POST['sr8_5']
          sr8_6 = request.POST['sr8_6']
          sr8_7 = request.POST['sr8_7']
          sr8_8 = request.POST['sr8_8']
          sr8_9 = request.POST['sr8_9']
          sr9_0 = request.POST['sr9_0']
          sr9_1 = request.POST['sr9_1']
          sr9_2 = request.POST['sr9_2']
          sr9_3 = request.POST['sr9_3']
          sr9_4 = request.POST['sr9_4']
          sr9_5 = request.POST['sr9_5']
          sr9_6 = request.POST['sr9_6']
          sr9_7 = request.POST['sr9_7']
          sr9_8 = request.POST['sr9_8']
          sr9_9 = request.POST['sr9_9']
          sr10_0 = request.POST['sr10_0']
          sr10_1 = request.POST['sr10_1']
          sr10_2 = request.POST['sr10_2']
          sr10_3 = request.POST['sr10_3']
          sr10_4 = request.POST['sr10_4']
          sr10_5 = request.POST['sr10_5']
          sr10_6 = request.POST['sr10_6']
          sr10_7 = request.POST['sr10_7']
          sr10_8 = request.POST['sr10_8']
          sr10_9 = request.POST['sr10_9']
          sr11_0 = request.POST['sr11_0']
          sr11_1 = request.POST['sr11_1']
          sr11_2 = request.POST['sr11_2']
          sr11_3 = request.POST['sr11_3']
          sr11_4 = request.POST['sr11_4']
          sr11_5 = request.POST['sr11_5']
          sr11_6 = request.POST['sr11_6']
          sr11_7 = request.POST['sr11_7']
          sr11_8 = request.POST['sr11_8']
          sr11_9 = request.POST['sr11_9']
          sr12_0 = request.POST['sr12_0']
          sr12_1 = request.POST['sr12_1']
          sr12_2 = request.POST['sr12_2']
          sr12_3 = request.POST['sr12_3']
          sr12_4 = request.POST['sr12_4']
          sr12_5 = request.POST['sr12_5']
          sr12_6 = request.POST['sr12_6']
          sr12_7 = request.POST['sr12_7']
          sr12_8 = request.POST['sr12_8']
          sr12_9 = request.POST['sr12_9']
          sr13_0 = request.POST['sr13_0']
          sr13_1 = request.POST['sr13_1']
          sr13_2 = request.POST['sr13_2']
          sr13_3 = request.POST['sr13_3']
          sr13_4 = request.POST['sr13_4']
          sr13_5 = request.POST['sr13_5']
          sr13_6 = request.POST['sr13_6']
          sr13_7 = request.POST['sr13_7']
          sr13_8 = request.POST['sr13_8']
          sr13_9 = request.POST['sr13_9']
          sr14_0 = request.POST['sr14_0']
          sr14_1 = request.POST['sr14_1']
          sr14_2 = request.POST['sr14_2']
          sr14_3 = request.POST['sr14_3']
          sr14_4 = request.POST['sr14_4']
          sr14_5 = request.POST['sr14_5']
          sr14_6 = request.POST['sr14_6']
          sr14_7 = request.POST['sr14_7']
          sr14_8 = request.POST['sr14_8']
          sr14_9 = request.POST['sr14_9']
          sr15_0 = request.POST['sr15_0']
          sr15_1 = request.POST['sr15_1']
          sr15_2 = request.POST['sr15_2']
          sr15_3 = request.POST['sr15_3']
          sr15_4 = request.POST['sr15_4']
          sr15_5 = request.POST['sr15_5']
          sr15_6 = request.POST['sr15_6']
          sr15_7 = request.POST['sr15_7']
          sr15_8 = request.POST['sr15_8']
          sr15_9 = request.POST['sr15_9']
          sr16_0 = request.POST['sr16_0']
          sr16_1 = request.POST['sr16_1']
          sr16_2 = request.POST['sr16_2']
          sr16_3 = request.POST['sr16_3']
          sr16_4 = request.POST['sr16_4']
          sr16_5 = request.POST['sr16_5']
          sr16_6 = request.POST['sr16_6']
          sr16_7 = request.POST['sr16_7']
          sr16_8 = request.POST['sr16_8']
          sr16_9 = request.POST['sr16_9']
          sr17_0 = request.POST['sr17_0']
          sr17_1 = request.POST['sr17_1']
          sr17_2 = request.POST['sr17_2']
          sr17_3 = request.POST['sr17_3']
          sr17_4 = request.POST['sr17_4']
          sr17_5 = request.POST['sr17_5']
          sr17_6 = request.POST['sr17_6']
          sr17_7 = request.POST['sr17_7']
          sr17_8 = request.POST['sr17_8']
          sr17_9 = request.POST['sr17_9']
          sr18_0 = request.POST['sr18_0']
          sr18_1 = request.POST['sr18_1']
          sr18_2 = request.POST['sr18_2']
          sr18_3 = request.POST['sr18_3']
          sr18_4 = request.POST['sr18_4']
          sr18_5 = request.POST['sr18_5']
          sr18_6 = request.POST['sr18_6']
          sr18_7 = request.POST['sr18_7']
          sr18_8 = request.POST['sr18_8']
          sr18_9 = request.POST['sr18_9']
          sr19_0 = request.POST['sr19_0']
          sr19_1 = request.POST['sr19_1']
          sr19_2 = request.POST['sr19_2']
          sr19_3 = request.POST['sr19_3']
          sr19_4 = request.POST['sr19_4']
          sr19_5 = request.POST['sr19_5']
          sr19_6 = request.POST['sr19_6']
          sr19_7 = request.POST['sr19_7']
          sr19_8 = request.POST['sr19_8']
          sr19_9 = request.POST['sr19_9']
          sr20_0 = request.POST['sr20_0']
          sr20_1 = request.POST['sr20_1']
          sr20_2 = request.POST['sr20_2']
          sr20_3 = request.POST['sr20_3']
          sr20_4 = request.POST['sr20_4']
          sr20_5 = request.POST['sr20_5']
          sr20_6 = request.POST['sr20_6']
          sr20_7 = request.POST['sr20_7']
          sr20_8 = request.POST['sr20_8']
          sr20_9 = request.POST['sr20_9']
          sr21_0 = request.POST['sr21_0']
          sr21_1 = request.POST['sr21_1']
          sr21_2 = request.POST['sr21_2']
          sr21_3 = request.POST['sr21_3']
          sr21_4 = request.POST['sr21_4']
          sr21_5 = request.POST['sr21_5']
          sr21_6 = request.POST['sr21_6']
          sr21_7 = request.POST['sr21_7']
          sr21_8 = request.POST['sr21_8']
          sr21_9 = request.POST['sr21_9']
          sr22_0 = request.POST['sr22_0']
          sr22_1 = request.POST['sr22_1']
          sr21_2 = request.POST['sr21_2']
          sr21_3 = request.POST['sr21_3']
          sr21_4 = request.POST['sr21_4']
          sr21_5 = request.POST['sr21_5']
          sr21_6 = request.POST['sr21_6']
          sr21_7 = request.POST['sr21_7']
          sr21_8 = request.POST['sr21_8']
          sr21_9 = request.POST['sr21_9']
          sr22_0 = request.POST['sr22_0']
          sr22_1 = request.POST['sr22_1']
          sr22_2 = request.POST['sr22_2']
          sr22_3 = request.POST['sr22_3']
          sr22_4 = request.POST['sr22_4']
          sr22_5 = request.POST['sr22_5']
          sr22_6 = request.POST['sr22_6']
          sr22_7 = request.POST['sr22_7']
          sr22_8 = request.POST['sr22_8']
          sr22_9 = request.POST['sr22_9']
          sr23_0 = request.POST['sr23_0']
          sr23_1 = request.POST['sr23_1']
          sr23_2 = request.POST['sr23_2']
          sr23_3 = request.POST['sr23_3']
          sr23_4 = request.POST['sr23_4']
          sr23_5 = request.POST['sr23_5']
          sr23_6 = request.POST['sr23_6']
          sr23_7 = request.POST['sr23_7']
          sr23_8 = request.POST['sr23_8']
          sr23_9 = request.POST['sr23_9']
          sr24_0 = request.POST['sr24_0']
          sr24_1 = request.POST['sr24_1']
          sr24_2 = request.POST['sr24_2']
          sr24_3 = request.POST['sr24_3']
          sr24_4 = request.POST['sr24_4']
          sr24_5 = request.POST['sr24_5']
          sr24_6 = request.POST['sr24_6']
          sr24_7 = request.POST['sr24_7']
          sr24_8 = request.POST['sr24_8']
          sr24_9 = request.POST['sr24_9']
          sr25_0 = request.POST['sr25_0']
          sr25_1 = request.POST['sr25_1']
          sr25_2 = request.POST['sr25_2']
          sr25_3 = request.POST['sr25_3']
          sr25_4 = request.POST['sr25_4']
          sr25_5 = request.POST['sr25_5']
          sr25_6 = request.POST['sr25_6']
          sr25_7 = request.POST['sr25_7']
          sr25_8 = request.POST['sr25_8']
          select = request.POST.get('select')
          legend_1 = request.POST['legend_1']
          legend_2 = request.POST['legend_2']
          legend_3 = request.POST['legend_3']
          legend_4 = request.POST['legend_4']
          legend_5 = request.POST['legend_5']
          legend_6 = request.POST['legend_6']
          legend_7 = request.POST['legend_7']
          legend_8 = request.POST['legend_8']
          legend_9 = request.POST['legend_9']
          legend_10 = request.POST['legend_10']
          legend_11 = request.POST['legend_11']
          edit_note = request.POST['edit_note']
          custom_legend = request.POST['custom_legend']
          doc1 = request.POST['doc1']
          doc2 = request.POST['doc2']
          doc3 = request.POST['doc3']
          analyzedby = request.FILES['analyzedby']
          reviewedby = request.FILES['reviewedby']
          approvedby = request.FILES['approvedby']
          approvedby1 = request.FILES['approvedby1']


          ambientAirForm2 = AmbientAir2(lab_rep_no=lab_rep_no,invoice_no=invoice_no,report_date=report_date,report_to=report_to,address=address,
                                        attention=attention,email=email,testId=testId,test_perf_date=test_perf_date,test_type=test_type,
                                        test_desc=test_desc,test_test_perf_by=test_test_perf_by,sr1_1=sr1_1,sr1_2=sr1_2,sr1_3=sr1_3,sr1_4=sr1_4,
                                        sr1_5=sr1_5,sr1_6=sr1_6,sr1_7=sr1_7,sr1_8=sr1_8,sr1_9=sr1_9,sr1_10=sr1_10,sr2_0=sr2_0,sr2_1=sr2_1,sr2_2=sr2_2,sr2_3=sr2_3,
                                        sr2_4=sr2_4,sr2_5=sr2_5,sr2_6=sr2_6,sr2_7=sr2_7,sr2_8=sr2_8,sr2_9=sr2_9,sr3_0=sr3_0,sr3_1=sr3_1,sr3_2=sr3_2,
                                        sr3_3=sr3_3,sr3_4=sr3_4,sr3_5=sr3_5,sr3_6=sr3_6,sr3_7=sr3_7,sr3_8=sr3_8,sr3_9=sr3_9,sr4_0=sr4_0,sr4_1=sr4_1,sr4_2=sr4_2,
                                        sr4_3=sr4_3,sr4_4=sr4_4,sr4_5=sr4_5,sr4_6=sr4_6,sr4_7=sr4_7,sr4_8=sr4_8,sr4_9=sr4_9,sr5_0=sr5_0,sr5_1=sr5_1,sr5_2=sr5_2,
                                        sr5_3=sr5_3,sr5_4=sr5_4,sr5_5=sr5_5,sr5_6=sr5_6,sr5_7=sr5_7,sr5_8=sr5_8,sr5_9=sr5_9,sr6_0=sr6_0,sr6_1=sr6_1,sr6_2=sr6_2,
                                        sr6_3=sr6_3,sr6_4=sr6_4,sr6_5=sr6_5,sr6_6=sr6_6,sr6_7=sr6_7,sr6_8=sr6_8,sr6_9=sr6_9,sr7_0=sr7_0,sr7_1=sr7_1,sr7_2=sr7_2,
                                        sr7_3=sr7_3,sr7_4=sr7_4,sr7_5=sr7_5,sr7_6=sr7_6,sr7_7=sr7_7,sr7_8=sr7_8,sr7_9=sr7_9,sr8_0=sr8_0,sr8_1=sr8_1,sr8_2=sr8_2,
                                        sr8_3=sr8_3,sr8_4=sr8_4,sr8_5=sr8_5,sr8_6=sr8_6,sr8_7=sr8_7,sr8_8=sr8_8,sr8_9=sr8_9,sr9_0=sr9_0,sr9_1=sr9_1,sr9_2=sr9_2,
                                        sr9_3=sr9_3,sr9_4=sr9_4,sr9_5=sr9_5,sr9_6=sr9_6,sr9_7=sr9_7,sr9_8=sr9_8,sr9_9=sr9_9,sr10_0=sr10_0,sr10_1=sr10_1,sr10_2=sr10_2,
                                        sr10_3=sr10_3,sr10_4=sr10_4,sr10_5=sr10_5,sr10_6=sr10_6,sr10_7=sr10_7,sr10_8=sr10_8,sr10_9=sr10_9,sr11_0=sr11_0,
                                        sr11_1=sr11_1,sr11_2=sr11_2,sr11_3=sr11_3,sr11_4=sr11_4,sr11_5=sr11_5,sr11_6=sr11_6,sr11_7=sr11_7,sr11_8=sr11_8,sr11_9=sr11_9,
                                        sr12_0=sr12_0,sr12_1=sr12_1,sr12_2=sr12_2,sr12_3=sr12_3,sr12_4=sr12_4,sr12_5=sr12_5,sr12_6=sr12_6,sr12_7=sr12_7,sr12_8=sr12_8,
                                        sr12_9=sr12_9,sr13_0=sr13_0,sr13_1=sr13_1,sr13_2=sr13_2,sr13_3=sr13_3,sr13_4=sr13_4,sr13_5=sr13_5,sr13_6=sr13_6,sr13_7=sr13_7,
                                        sr13_8=sr13_8,sr13_9=sr13_9,sr14_0=sr14_0,sr14_1=sr14_1,sr14_2=sr14_2,sr14_3=sr14_3,sr14_4=sr14_4,sr14_5=sr14_5,sr14_6=sr14_6,
                                        sr14_7=sr14_7,sr14_8=sr14_8,sr14_9=sr14_9,sr15_0=sr15_0,sr15_1=sr15_1,sr15_2=sr15_2,sr15_3=sr15_3,sr15_4=sr15_4,sr15_5=sr15_5,
                                        sr15_6=sr15_6,sr15_7=sr15_7,sr15_8=sr15_8,sr15_9=sr15_9,sr16_0=sr16_0,sr16_1=sr16_1,sr16_2=sr16_2,sr16_3=sr16_3,sr16_4=sr16_4,
                                        sr16_5=sr16_5,sr16_6=sr16_6,sr16_7=sr16_7,sr16_8=sr16_8,sr16_9=sr16_9,sr17_0=sr17_0,sr17_1=sr17_1,sr17_2=sr17_2,sr17_3=sr17_3,sr17_4=sr17_4,
                                        sr17_5=sr17_5,sr17_6=sr17_6,sr17_7=sr17_7,sr17_8=sr17_8,sr17_9=sr17_9,sr18_0=sr18_0,sr18_1=sr18_1,sr18_2=sr18_2,sr18_3=sr18_3,
                                        sr18_4=sr18_4,sr18_5=sr18_5,sr18_6=sr18_6,sr18_7=sr18_7,sr18_8=sr18_8,sr18_9=sr18_9,sr19_0=sr19_0,sr19_1=sr19_1,sr19_2=sr19_2,
                                        sr19_3=sr19_3,sr19_4=sr19_4,sr19_5=sr19_5,sr19_6=sr19_6,sr19_7=sr19_7,sr19_8=sr19_8,sr19_9=sr19_9,sr20_0=sr20_0,sr20_1=sr20_1,
                                        sr20_2=sr20_2,sr20_3=sr20_3,sr20_4=sr20_4,sr20_5=sr20_5,sr20_6=sr20_6,sr20_7=sr20_7,sr20_8=sr20_8,sr20_9=sr20_9,sr21_0=sr21_0,
                                        sr21_1=sr21_1,sr21_2=sr21_2,sr21_3=sr21_3,sr21_4=sr21_4,sr21_5=sr21_5,sr21_6=sr21_6,sr21_7=sr21_7,sr21_8=sr21_8,sr21_9=sr21_9,
                                        sr22_0=sr22_0,sr22_1=sr22_1,sr22_2=sr22_2,sr22_3=sr22_3,sr22_4=sr22_4,sr22_5=sr22_5,sr22_6=sr22_6,sr22_7=sr22_7,sr22_8=sr22_8,
                                        sr22_9=sr22_9,sr23_0=sr23_0,sr23_1=sr23_1,sr23_2=sr23_2,sr23_3=sr23_3,sr23_4=sr23_4,sr23_5=sr23_5,sr23_6=sr23_6,sr23_7=sr23_7,
                                        sr23_8=sr23_8,sr23_9=sr23_9,sr24_0=sr24_0,sr24_1=sr24_1,sr24_2=sr24_2,sr24_3=sr24_3,sr24_4=sr24_4,sr24_5=sr24_5,sr24_6=sr24_6,
                                        sr24_7=sr24_7,sr24_8=sr24_8,sr24_9=sr24_9,sr25_0=sr25_0,sr25_1=sr25_1,sr25_2=sr25_2,sr25_3=sr25_3,sr25_4=sr25_4,sr25_5=sr25_5,
                                        sr25_6=sr25_6,sr25_7=sr25_7,sr25_8=sr25_8,select=select,legend_1=legend_1,legend_2=legend_2,legend_3=legend_3,
                                        legend_4=legend_4,legend_5=legend_5,legend_6=legend_6,legend_7=legend_7,legend_8=legend_8,legend_9=legend_9,legend_10=legend_10,
                                        legend_11=legend_11,edit_note=edit_note,custom_legend=custom_legend,location=location,
                                        doc1=doc1,doc2=doc2,doc3=doc3,analyzedby=analyzedby,reviewedby=reviewedby,approvedby=approvedby,approvedby1=approvedby1)
          ambientAirForm2.save()
          id = (AmbientAir2.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/ambientAir2-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="ambientAir2")


     return render(request,"ambientAir2.html")

@login_required(login_url="/login")
def wasteWater2(request):
     if request.method == 'POST':
          location = request.POST['location']
          lab_rep_no = request.POST['lab_rep_no']
          invoice_no = request.POST['invoice_no']
          repo_date = request.POST['repo_date']
          report_to = request.POST['report_to']
          address = request.POST['address']
          attention = request.POST['attention']
          email = request.POST['email']
          sampleId = request.POST['sampleId']
          sample_Col_date = request.POST['sample_Col_date']
          sample_desc = request.POST['sample_desc']
          sampling_method = request.POST['sampling_method']
          sample_type = request.POST['sample_type']
          sample_collected_by = request.POST['sample_collected_by']
          date_of_analysis = request.POST['date_of_analysis']
          test_description = request.POST['test_description']
          select = request.POST.get('select')
          result_1 = request.POST['result_1']
          result_1_1 = request.POST['result_1_1']
          result_2 = request.POST['result_2']
          result_2_2 = request.POST['result_2_2']
          result_3 = request.POST['result_3']
          result_3_3 = request.POST['result_3_3']
          result_4 = request.POST['result_4']
          result_4_4 = request.POST['result_4_4']
          result_5 = request.POST['result_5']
          result_5_5 = request.POST['result_5_5']
          result_6 = request.POST['result_6']
          result_6_6 = request.POST['result_6_6']
          result_7 = request.POST['result_7']
          result_7_7 = request.POST['result_7_7']
          metho_select = request.POST.get('metho_select')
          result_8 = request.POST['result_8']
          result_8_8 = request.POST['result_8_8']
          result_9 = request.POST['result_9']
          result_9_9 = request.POST['result_9_9']
          result_10 = request.POST['result_10']
          result_10_10 = request.POST['result_10_10']
          result_11 = request.POST['result_11']
          result_11_11= request.POST['result_11_11']
          result_12 = request.POST['result_12']
          result_12_12 = request.POST['result_12_12']
          result_13 = request.POST['result_13']
          result_13_13 = request.POST['result_13_13']
          result_14 = request.POST['result_14']
          result_14_14 = request.POST['result_14_14']
          result_15 = request.POST['result_15']
          result_15_15 = request.POST['result_15_15']
          result_16 = request.POST['result_16']
          result_16_16 = request.POST['result_16_16']
          result_17 = request.POST['result_17']
          result_17_17 = request.POST['result_17_17']
          result_18 = request.POST['result_18']
          result_18_18 = request.POST['result_18_18']
          result_19 = request.POST['result_19']
          result_19_19 = request.POST['result_19_19']
          result_20 = request.POST['result_20']
          result_20_20 = request.POST['result_20_20']
          result_21 = request.POST['result_21']
          result_21_21 = request.POST['result_21_21']
          result_22 = request.POST['result_22']
          result_22_22 = request.POST['result_22_22']
          result_23 = request.POST['result_23']
          result_23_23 = request.POST['result_23_23']
          result_24 = request.POST['result_24']
          result_24_24 = request.POST['result_24_24']
          result_25 = request.POST['result_25']
          result_25_25 = request.POST['result_25_25']
          result_26 = request.POST['result_26']
          result_26_26 = request.POST['result_26_26']
          result_27 = request.POST['result_27']
          result_27_27 = request.POST['result_27_27']
          result_28 = request.POST['result_28']
          result_28_28 = request.POST['result_28_28']
          result_29 = request.POST['result_29']
          result_29_29 = request.POST['result_29_29']
          result_30 = request.POST['result_30']
          result_30_30 = request.POST['result_30_30']
          result_31 = request.POST['result_31']
          result_31_31 = request.POST['result_31_31']
          result_32 = request.POST['result_32']
          result_32_32 = request.POST['result_32_32']
          legend_1 = request.POST['legend_1']
          legend_2 = request.POST['legend_2']
          legend_3 = request.POST['legend_3']
          legend_4 = request.POST['legend_4']
          legend_5 = request.POST['legend_5']
          legend_6 = request.POST['legend_6']
          legend_7 = request.POST['legend_7']
          legend_8 = request.POST['legend_8']
          legend_9 = request.POST['legend_9']
          legend_10 = request.POST['legend_10']
          legend_11 = request.POST['legend_11']
          editNote = request.POST['editNote']
          customlegend = request.POST['customlegend']
          doc1 = request.POST['doc1']
          doc2 = request.POST['doc2']
          doc3 = request.POST['doc3']
          analyzedby = request.FILES['analyzedby']
          reviewedby = request.FILES['reviewedby']
          approvedby = request.FILES['approvedby']
          approvedby1 = request.FILES['approvedby1']


          wasteWaterForm2 =  WasteWaterForm2(lab_rep_no=lab_rep_no,invoice_no=invoice_no,repo_date=repo_date,report_to=report_to,address=address,
                                             attention=attention,email=email,sampleId=sampleId,sample_Col_date=sample_Col_date,sample_desc=sample_desc,
                                             sampling_method=sampling_method,sample_type=sample_type,sample_collected_by=sample_collected_by,
                                             date_of_analysis=date_of_analysis,test_description=test_description,select=select,result_1=result_1,
                                             result_1_1=result_1_1,result_2=result_2,result_2_2=result_2_2,result_3=result_3,result_3_3=result_3_3,
                                             result_4=result_4,result_4_4=result_4_4,result_5=result_5,result_5_5=result_5_5,result_6=result_6,result_6_6 =result_6_6,result_7 = result_7,
                                             result_7_7=result_7_7,metho_select=metho_select,result_8=result_8,result_8_8=result_8_8,result_9=result_9,
                                             result_9_9=result_9_9,result_10=result_10,result_10_10=result_10_10,result_11=result_11,result_11_11=result_11_11,
                                             result_12=result_12,result_12_12=result_12_12,result_13=result_13,result_13_13=result_13_13,result_14=result_14,
                                             result_14_14=result_14_14,result_15=result_15,result_15_15=result_15_15,result_16=result_16,result_16_16=result_16_16,
                                             result_17=result_17,result_17_17=result_17_17,result_18=result_18,result_18_18=result_18_18,result_19=result_19,
                                             result_19_19=result_19_19,result_20=result_20,result_20_20=result_20_20,result_21=result_21,result_21_21=result_21_21,
                                             result_22=result_22,result_22_22=result_22_22,result_23=result_23,result_23_23=result_23_23,result_24=result_24,
                                             result_24_24=result_24_24,result_25=result_25,result_25_25=result_25_25,result_26=result_26,result_26_26=result_26_26,
                                             result_27=result_27,result_27_27=result_27_27,result_28=result_28,result_28_28=result_28_28,result_29=result_29,
                                             result_29_29=result_29_29,result_30=result_30,result_30_30=result_30_30,result_31=result_31,result_31_31=result_31_31,
                                             result_32=result_32,result_32_32=result_32_32,legend_1=legend_1,legend_2=legend_2,legend_3=legend_3,
                                             legend_4=legend_4,legend_5=legend_5,legend_6=legend_6,legend_7=legend_7,legend_8=legend_8,legend_9=legend_9,
                                             legend_10=legend_10,legend_11=legend_11,editNote=editNote,location=location,
                                             customlegend=customlegend,doc1=doc1,doc2=doc2,doc3=doc3,analyzedby=analyzedby,reviewedby=reviewedby,approvedby=approvedby,approvedby1=approvedby1)
          wasteWaterForm2.save()
          id = (WasteWaterForm2.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/wasteWater2-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="wasteWater2")
     return render(request,"wasteWater2.html")


@login_required(login_url="/login")
def noiseAnalysis(request):
     if request.method == 'POST':
          location = request.POST['location']
          lab_rep_no = request.POST['lab_rep_no']
          invoice_no = request.POST['invoice_no']
          rep_date = request.POST['rep_date']
          report_to = request.POST['report_to']
          address = request.POST['address']
          attention = request.POST['attention']
          email = request.POST['email']
          testId = request.POST['testId']
          test_perf_date = request.POST['test_perf_date']
          test_type = request.POST['test_type']
          test_perf_by = request.POST['test_perf_by']
          test_desc = request.POST['test_desc']
          select = request.POST.get('select')
          select1 = request.POST.get('select1')
          r1 = request.POST['r1']
          r1_1 = request.POST['r1_1']
          r2 = request.POST['r2']
          r2_2 = request.POST['r2_2']
          r3 = request.POST['r3']
          r3_3 = request.POST['r3_3']
          r4 = request.POST['r4']
          r4_4 = request.POST['r4_4']
          r5 = request.POST['r5']
          r5_5 = request.POST['r5_5']
          r6 = request.POST['r6']
          r6_6 = request.POST['r6_6']
          r7 = request.POST['r7']
          r7_7 = request.POST['r7_7']
          r8 = request.POST['r8']
          r8_8 = request.POST['r8_8']
          r9 = request.POST['r9']
          r9_9 = request.POST['r9_9']
          r10 = request.POST['r10']
          r10_10 = request.POST['r10_10']
          r11 = request.POST['r11']
          r11_11 = request.POST['r11_11']
          r12 = request.POST['r12']
          r12_12 = request.POST['r12_12']
          r13 = request.POST['r13']
          r13_13 = request.POST['r13_13']
          legend_1 = request.POST['legend_1']
          legend_2 = request.POST['legend_2']
          legend_3 = request.POST['legend_3']
          legend_4 = request.POST['legend_4']
          legend_5 = request.POST['legend_5']
          legend_6 = request.POST['legend_6']
          legend_7 = request.POST['legend_7']
          legend_8 = request.POST['legend_8']
          legend_9 = request.POST['legend_9']
          legend_10 = request.POST['legend_10']
          legend_11 = request.POST['legend_11']
          editNote = request.POST['editNote']
          customlegend = request.POST['customlegend']
          doc1 = request.POST['doc1']
          doc2 = request.POST['doc2']
          doc3 = request.POST['doc3']
          analyzedby = request.FILES['analyzedby']
          reviewedby = request.FILES['reviewedby']
          approvedby = request.FILES['approvedby']
          approvedby1 = request.FILES['approvedby1']


          noiseForm = NoiseAnalysis(lab_rep_no=lab_rep_no,invoice_no=invoice_no,rep_date=rep_date,report_to=report_to,
                                    address=address,attention=attention,email=email,testId=testId,test_perf_date=test_perf_date,
                                    test_type=test_type,test_perf_by=test_perf_by,test_desc=test_desc,select=select,select1=select1,r1=r1,r1_1=r1_1,
                                    r2=r2,r2_2=r2_2,r3=r3,r3_3=r3_3,r4=r4,r4_4=r4_4,r5=r5,r5_5=r5_5,r6=r6,r6_6=r6_6,r7=r7,r7_7=r7_7,
                                    r8=r8,r8_8=r8_8,r9=r9,r9_9=r9_9,r10=r10,r10_10=r10_10,r11=r11,r11_11=r11_11,r12=r12,r12_12=r12_12,
                                    r13=r13,r13_13=r13_13,legend_1=legend_1,legend_2=legend_2,legend_3=legend_3,legend_4=legend_4,
                                    legend_5=legend_5,legend_6=legend_6,legend_7=legend_7,legend_8=legend_8,legend_9=legend_9,legend_10=legend_10,
                                    legend_11=legend_11,editNote=editNote,customlegend=customlegend,location=location,
                                    doc1=doc1,doc2=doc2,doc3=doc3,analyzedby=analyzedby,reviewedby=reviewedby,approvedby=approvedby,approvedby1=approvedby1)


          noiseForm.save()
          id = (NoiseAnalysis.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/noiseAnalysis-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="noiseAnalysis")
     return render(request,"noiseAnalysis.html")

@login_required(login_url="/login")
def drinkingWaterList(request):
     drinkingWaterList = DrinkingWaterForm.objects.all()
     context = {'list':drinkingWaterList}

     return render(request,"drinkingWaterList.html",context)

@login_required(login_url="/login")
def deleteDrinkingWaterList(request,pk):
     drinkingWaterList = DrinkingWaterForm.objects.get(id=pk)
     drinkingWaterList.delete()
     return redirect("drinkWaterList")

@login_required(login_url="/login")
def editDrinkingWaterList(request,pk):
     drinkingWaterList = DrinkingWaterForm.objects.get(id=pk)
     context ={'list': drinkingWaterList}
     # print(editableForm.id)
     return render(request,"drinkingWaterEdit.html",context)

@login_required(login_url="/login")
def editDrinkingWaterListRecord(request,pk):
     if request.method == 'POST':
          updatedata = DrinkingWaterForm.objects.get(id=pk)
          updatedata.location = request.POST['location']
          updatedata.lab_report_no = request.POST['lab_report_no']
          updatedata.invoice_bill_no = request.POST['invoice_bill_no']
          updatedata.reporting_date = request.POST['reporting_date']
          updatedata.report_to = request.POST['reporting_to']
          updatedata.address = request.POST['address']
          updatedata.attention = request.POST['attention']
          updatedata.email = request.POST['email']
          updatedata.sample_id = request.POST['sample_id']
          updatedata.sample_collection_date = request.POST['collection_date']
          updatedata.sample_description = request.POST['sample_description']
          updatedata.sample_type = request.POST['sample_type']
          updatedata.sample_collected_by = request.POST['sample_collected_by']
          updatedata.date_of_analysis_from = request.POST['date_of_analysis_from']
          updatedata.date_of_analysis_to = request.POST['date_of_analysis_to']
          updatedata.test_description = request.POST['test_description']
          updatedata.water_sr1 = request.POST['water_sr1']
          updatedata.water_sr2 = request.POST['water_sr2']
          updatedata.water_sr3 = request.POST['water_sr3']
          updatedata.water_sr4 = request.POST['water_sr4']
          updatedata.water_sr5 = request.POST['water_sr5']
          updatedata.water_sr6 = request.POST['water_sr6']
          updatedata.water_sr7 = request.POST['water_sr7']
          updatedata.water_sr8 = request.POST['water_sr8']
          updatedata.water_sr9 = request.POST['water_sr9']
          updatedata.water_sr10 = request.POST['water_sr10']
          updatedata.water_sr11 = request.POST['water_sr11']
          updatedata.water_sr12 = request.POST['water_sr12']
          updatedata.water_sr13 = request.POST['water_sr13']
          updatedata.water_sr14 = request.POST['water_sr14']
          updatedata.water_sr15 = request.POST['water_sr15']
          updatedata.water_sr16 = request.POST['water_sr16']
          updatedata.water_sr17 = request.POST['water_sr17']
          updatedata.water_sr18 = request.POST['water_sr18']
          updatedata.water_sr19 = request.POST['water_sr19']
          updatedata.water_sr20 = request.POST['water_sr20']
          updatedata.water_sr21 = request.POST['water_sr21']
          updatedata.water_sr22 = request.POST['water_sr22']
          updatedata.water_sr23 = request.POST['water_sr23']
          updatedata.water_sr24 = request.POST['water_sr24']
          updatedata.water_sr25 = request.POST['water_sr25']
          updatedata.water_sr26 = request.POST['water_sr26']
          updatedata.water_sr27 = request.POST['water_sr27']
          updatedata.water_sr28 = request.POST['water_sr28']
          updatedata.water_sr29 = request.POST['water_sr29']
          updatedata.water_sr30 = request.POST['water_sr30']
          updatedata.water_sr31 = request.POST['water_sr31']
          updatedata.water_sr32 = request.POST['water_sr32']
          updatedata.legend_1 = request.POST['legend-1']
          updatedata.legend_2 = request.POST['legend-2']
          updatedata.legend_3 = request.POST['legend-3']
          updatedata.legend_4 = request.POST['legend-4']
          updatedata.legend_5 = request.POST['legend-5']
          updatedata.legend_6 = request.POST['legend-6']
          updatedata.legend_7 = request.POST['legend-7']
          updatedata.legend_8 = request.POST['legend-8']
          updatedata.legend_9 = request.POST['legend-9']
          updatedata.legend_10 = request.POST['legend-10']
          updatedata.legend_11 = request.POST['legend-11']
          updatedata.edit_note = request.POST['edit-note']
          updatedata.custom_legend = request.POST['custom-legend']
          updatedata.doc_controll_1 = request.POST['doc-con-1']
          updatedata.doc_controll_2 = request.POST['doc-con-2']
          updatedata.doc_controll_3 = request.POST['doc-con-3']
          updatedata.analyzed_by = request.FILES["analyzedby" ]
          updatedata.reviewed_by = request.FILES["reviewedby" ]
          updatedata.approved_by = request.FILES["approvedby" ]




          updatedata.save()
          id = (DrinkingWaterForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f'/DrinkingWaterform-view/{str(id)}/'
               return redirect(to=url)
          if "submit" in request.POST:
               return redirect('drinkWaterList')
          else:
               return HttpResponse('Invalid Request Method',status=400)
     return render(request,"drinkWaterList.html")
          

@login_required(login_url="/login")
def drinkWaterReport(request,pk):
     from django_pdfkit import PDFView
     waterReport = DrinkingWaterForm.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     context ={'list': waterReport,'qr':'media/qr.png'}


     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")




     return render(request,"drinkingWaterReport.html",context)


@login_required(login_url="/login")
def generatePDF(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,report_number,invoice,reporting_date,report_to,address,attention,email,sample_id,sample_collection_date,
                       sample_description,sample_type,sample_collected_by,date_of_analysis_from,date_of_analysis_to,test_description):
               super().__init__()
               self.report_number = report_number
               self.invoice_number = invoice
               self.reporting_date = reporting_date
               self.report_to = report_to
               self.address = address
               self.attention = attention
               self.email = email
               self.sample_id = sample_id
               self.sample_collection_Date = sample_collection_date
               self.sample_description = sample_description
               self.sample_type = sample_type
               self.sample_collected_by = sample_collected_by
               self.date_of_analysis = (date_of_analysis_from +"-"+ date_of_analysis_to)
               self.test_description = test_description


          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.report_number)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.invoice_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.reporting_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(85,82,txt="Sample ID:")
               self.text(110,82,txt=self.sample_id)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(67,88,txt="Sample Collection Date:")
               self.text(110,88,txt=self.sample_collection_Date)

               self.rect(10,90,190,6)
               self.set_font("Calibri","B", 10)
               self.text(73,94,txt="Sample Description:")
               self.text(110,94,txt=self.sample_description)

               self.rect(10,96.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(82,100,txt="Sample Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.sample_type)

               self.line(105,78,105,120)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(54,106,txt="Sample Collected / Submitted By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.sample_collected_by)

               self.rect(10,108,190,6)
               self.set_font("Calibri","B", 10)
               self.text(77,112,txt="Date Of Analysis:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.date_of_analysis)

               self.rect(10,114.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(77,118,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,118,txt=self.test_description)

               #table header
               self.rect(10,123.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,127.5,txt="Aanalytical Test Report")

               self.set_y(130)




     waterForm = DrinkingWaterForm.objects.get(id=pk)
     

     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Methods","Unit","Test Result",""],
     ]
     sr_no = 1
     if waterForm.water_sr1:
          a = [str(sr_no),"pH @ 25°C","*APHA 4500 H","-",waterForm.water_sr1,"6.5 - 8.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr2:
          a = [str(sr_no),"Total Dissolved Solids (TDS)","*APHA 2540-C","mg/L",waterForm.water_sr2,"<1000"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr3:
          a = [str(sr_no),"Total Hardness as CaCO3","ASTM D 1126","mg/L",waterForm.water_sr3,"< 500"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr4:
          a = [str(sr_no),"Color","HACH 8025","TCU",waterForm.water_sr4,"≤ 15"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr5:
          a = [str(sr_no),"Turbidity","*APHA 2130","NTU",waterForm.water_sr5,"≤ 5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr6:
          a = [str(sr_no),"Nitrite (NO₂)","HACH 8507","mg/L",waterForm.water_sr6,"≤ 3"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr7:
          a = [str(sr_no),"Nitrate (NO3)","HACH 8507","mg/L",waterForm.water_sr7,"≤ 0.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr8:
          a = [str(sr_no),"Taste","*APHA 2160","-",waterForm.water_sr8,"Non-Objectionable"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr9:
          a = [str(sr_no),"Odor","*APHA 2150","-",waterForm.water_sr9,"Non-Objectionable"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr10:
          a = [str(sr_no),"Chloride (Cl)","*APHA 4500 Cl","mg/L",waterForm.water_sr10,"≤ 250"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr11:
          a = [str(sr_no),"Fluoride (F)","HACH 8029","mg/L",waterForm.water_sr11,"≤ 1.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr12:
          a = [str(sr_no),"Aluminum (Al)","*APHA 3111-D","mg/L",waterForm.water_sr12,"≤ 0.2"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr13:
          a = [str(sr_no),"Nickel (Ni)","*APHA 3111-B","mg/L",waterForm.water_sr13,"≤ 0.02"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr14:
          a = [str(sr_no),"Lead (Pb)","*APHA 3111-B","mg/L",waterForm.water_sr14,"≤ 0.05"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr15:
          a = [str(sr_no),"Barium (Ba)","HACH 8014","mg/L",waterForm.water_sr15,"≤ 0.7"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr16:
          a = [str(sr_no),"Antimony (Sb)","*APHA 3111-B","mg/L",waterForm.water_sr16,"≤ 0.005"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr17:
          a = [str(sr_no),"Arsenic (As)","*APHA 3114-B","mg/L",waterForm.water_sr17,"≤ 0.05"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr18:
          a = [str(sr_no),"Boron (B)","HACH 8015","mg/L",waterForm.water_sr18,"0.3"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr19:
          a = [str(sr_no),"Cadmium (Cd)","*APHA 3111-B","mg/L",waterForm.water_sr19,"0.01"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr20:
          a = [str(sr_no),"Chromium (Cr)","*APHA 3111-B","mg/L",waterForm.water_sr20,"≤ 0.05"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr21:
          a = [str(sr_no),"Selenium (Se)","*APHA 3114-B","mg/L",waterForm.water_sr21,"0.01"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr22:
          a = [str(sr_no),"Copper (Cu)","*APHA 3111-B","mg/L",waterForm.water_sr22,"2"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr23:
          a = [str(sr_no),"HACH 8027","*APHA 3111-B","mg/L",waterForm.water_sr23,"≤ 0.05"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr24:
          a = [str(sr_no),"Mercury (Hg)","*APHA 3112-B","mg/L",waterForm.water_sr24,"≤ 0.001"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr25:
          a = [str(sr_no),"Manganese (Mn)","*APHA 3111-B","mg/L",waterForm.water_sr25,"≤ 0.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr26:
          a = [str(sr_no),"Zinc (Zn)","*APHA 3111-B","mg/L",waterForm.water_sr26,"≤ 5.0"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr27:
          a = [str(sr_no),"Residual Chlorine","HACH 10069","mg/L",waterForm.water_sr27,"0.2 - 0.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr28:
          a = [str(sr_no),"PhenolicCompounds as Phenols","ASTM-D-1783","mg/L",waterForm.water_sr28,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr29:
          a = [str(sr_no),"Fecal Coliform","USEPA 1604","CFU/100 ml",waterForm.water_sr29,"0 CFU/100 ml"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr30:
          a = [str(sr_no),"Total Coliform","*APHA 922 B","CFU/100 ml",waterForm.water_sr30,"0 CFU/100 ml"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr31:
          a = [str(sr_no),"E-Coli","USEPA 1604","CFU/100 ml",waterForm.water_sr31,"0 CFU/100 ml"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if waterForm.water_sr32:
          a = [str(sr_no),"Pesticides","USEPA-614.1","mg/L",waterForm.water_sr32,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     pdf = PDFWithPageNumbers(report_number=waterForm.lab_report_no,invoice=waterForm.invoice_bill_no,reporting_date=waterForm.reporting_date,report_to=waterForm.report_to,
                              address=waterForm.address,attention=waterForm.attention,email=waterForm.email,sample_id=waterForm.sample_id,sample_collection_date=waterForm.sample_collection_date,
                              sample_description=waterForm.sample_description,sample_type=waterForm.sample_type,sample_collected_by=waterForm.sample_collected_by,
                              date_of_analysis_to=waterForm.date_of_analysis_to, date_of_analysis_from=waterForm.date_of_analysis_from,test_description=waterForm.test_description,
                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True, margin=15)









     #report data table
     num_rows = 0
     with pdf.table(col_widths=(6, 35, 20, 15,18,18),line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               num_rows = num_rows + 1
               if k == 0:
                    data_row[5] = waterForm.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)
     print("Y",pdf.y + num_rows )
     # data after Table
     print("ROWS",num_rows)
     if num_rows == 22 :
          pdf.add_page()
     if waterForm.edit_note:
          pdf.set_font("Calibri","B", 10)
          if num_rows >= 22:
               pdf.text(10,188,txt="Note:")
          else:
               pdf.text(10,pdf.y+5,txt="Note:")
          pdf.set_font("Calibri","", 8)
          if num_rows >=22:
               pdf.set_y(185.5)
          else:
               pdf.set_y(pdf.y+2)

          pdf.set_x(20)
          pdf.multi_cell(182,txt=waterForm.edit_note)

     line_height = 4
     if num_rows >=22:
          y = 196
     else:
          y = pdf.y+5
     if waterForm.legend_1:
          pdf.text(10,y,txt=waterForm.legend_1)
          y = y+line_height
     if waterForm.legend_2:
          pdf.text(10,y,txt=waterForm.legend_2)
          y = y+line_height
     if waterForm.legend_3:
          pdf.text(10,y,txt=waterForm.legend_3)
          y = y+line_height
     if waterForm.legend_4:
          pdf.text(10,y,txt=waterForm.legend_4)
          y = y+line_height
     if waterForm.legend_5:
          pdf.text(10,y,txt=waterForm.legend_5)
          y = y+line_height
     if waterForm.legend_6:
          pdf.text(10,y,txt=waterForm.legend_6)
          y = y+line_height
     if waterForm.legend_7:
          pdf.text(10,y,txt=waterForm.legend_7)
          y = y+line_height
     if waterForm.legend_8:
          pdf.text(10,y,txt=waterForm.legend_8)
          y = y+line_height
     if waterForm.legend_9:
          pdf.text(10,y,txt=waterForm.legend_9)
          y = y+line_height
     if waterForm.legend_10:
          pdf.text(10,y,txt=waterForm.legend_10)
          y = y+line_height
     if waterForm.legend_11:
          pdf.text(10,y,txt=waterForm.legend_11)
          y = y+line_height


     pdf.image(waterForm.analyzed_by,30,238,12,12)
     pdf.line(19,250,36+pdf.get_string_width("Analyzed By (Analyst)"),250)
     pdf.text(26,253     ,"Analyzed By (Analyst)")
     pdf.image(waterForm.reviewed_by,100,238,12,12)
     pdf.line(126,250,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),250)
     pdf.text(87.5,253,"Reviewed By (Assistant Manager)")
     pdf.image(waterForm.approved_by,165,237,12,12)
     pdf.image(waterForm.approved_by1,178,237,12,12)
     pdf.line(155,250,165+pdf.get_string_width("Approved By (Lab Manager)"),250)
     pdf.text(160,253,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,257,-10+pdf.w,257)
     pdf.text(10,262,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,266,txt="• Report is valid for current batch (sample).")
     pdf.text(10,269,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(269.8)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(273)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,259,19,15)
     if waterForm.location == "SEQS":
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if waterForm.location == "PEQS":
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15)
     if waterForm.location == "NEQS":
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)          
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,259,19,15)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,276,txt="(Certificate # 20210131)")
     pdf.text(158,276,txt="(Certificate # 20210131)")
     pdf.text(182,276,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,277,25,5)
     pdf.text(132,280,txt=waterForm.doc_controll_1)
     pdf.rect(155,277,25,5)
     pdf.text(157,280,txt=waterForm.doc_controll_2)
     pdf.rect(180,277,25,5)
     pdf.text(186.5,280,txt=waterForm.doc_controll_3)







     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response

@login_required(login_url="/login")
def gaseousEmissionList(request):
     gaseous_Emission = GaseousEmissionForm.objects.all()
     context = {'data' : gaseous_Emission}

     return render(request,"gaseousEmissionList.html",context)

@login_required(login_url="/login")
def deleteGaseousList(request,pk):
     gaseous_Emission = GaseousEmissionForm.objects.get(id=pk)
     gaseous_Emission.delete()

     return redirect('gaseousEmissionList')

     
@login_required(login_url="/login")
def editGaseousList(request,pk):
     gaseous_Emission =  GaseousEmissionForm.objects.get(id=pk)
     context = {'data':gaseous_Emission}
     return render(request,"gaseousEmissionEditForm.html",context)


@login_required(login_url="/login")
def updateGaseousRecord(request,pk):
     if request.method=='POST':
          update_data = GaseousEmissionForm.objects.get(id=pk)
          update_data.location = request.POST['location']
          update_data.GasEm_lab_report_no1 = request.POST['GasEm-lab_report_no']
          update_data.GasEm_invoice_bill_no = request.POST['GasEm-invoice-bill-no']
          update_data.GaseEm_reporting_date = request.POST['GasEm-reporting-date']
          update_data.GaseEm_reporting_to = request.POST['GasEm-report-to']
          update_data.GaseEm_address = request.POST['GasEm-address']
          update_data.GaseEm_attention = request.POST['GasEm-attention']
          update_data.GaseEm_email = request.POST['GasEm-email']
          update_data.GaseEm_test_id = request.POST['GasEm-test-id']
          update_data.GaseEm_test_perf_date = request.POST['GasEm-test-perf-date']
          update_data.GaseEm_test_type = request.POST['GasEm-test-type']
          update_data.GaseEm_test_perf_by = request.POST['GasEm-test-perf-by']
          update_data.GasEm_test_desc = request.POST['GasEm-test-desc']
          update_data.GaseEm_types = request.POST.get('GasEm-type')
          update_data.GaseEm_select = request.POST.get('select')
          update_data.GaseEm_sr1 = request.POST['GasEm-sr1']
          update_data.GaseEm_sr2 = request.POST['GasEm-sr2']
          update_data.GaseEm_sr3 = request.POST['GasEm-sr3']
          update_data.GaseEm_sr4 = request.POST['GasEm-sr4']
          update_data.GaseEm_sr5 = request.POST['GasEm-sr5']
          update_data.GaseEm_sr6 = request.POST['GasEm-sr6']
          update_data.GaseEm_sr7 = request.POST['GasEm-sr7']
          update_data.GaseEm_sr8 = request.POST['GasEm-sr8']
          update_data.GaseEm_sr9 = request.POST['GasEm-sr9']
          update_data.GaseEm_sr10 = request.POST['GasEm-sr10']
          update_data.GaseEm_sr11 = request.POST['GasEm-sr11']
          update_data.GaseEm_sr12 = request.POST['GasEm-sr12']
          update_data.GaseEm_sr13 = request.POST['GasEm-sr13']
          update_data.GaseEm_sr14 = request.POST['GasEm-sr14']
          update_data.GaseEm_sr15 = request.POST['GasEm-sr15']
          update_data.GaseEm_sr16 = request.POST['GasEm-sr16']
          update_data.GaseEm_sr17 = request.POST['GasEm-sr17']
          update_data.GaseEm_sr18 = request.POST['GasEm-sr18']
          update_data.GaseEm_sr19 = request.POST['GasEm-sr19']
          update_data.GaseEm_sr20 = request.POST['GasEm-sr20']
          update_data.GaseEm_sr21 = request.POST['GasEm-sr21']
          update_data.GaseEm_sr22 = request.POST['GasEm-sr22']
          update_data.GaseEm_legend_1 = request.POST['GasEm-legend-1']
          update_data.GaseEm_legend_2 = request.POST['GasEm-legend-2']
          update_data.GaseEm_legend_3 = request.POST['GasEm-legend-3']
          update_data.GaseEm_legend_4 = request.POST['GasEm-legend-4']
          update_data.GaseEm_legend_5 = request.POST['GasEm-legend-5']
          update_data.GaseEm_legend_6 = request.POST['GasEm-legend-6']
          update_data.GaseEm_legend_7 = request.POST['GasEm-legend-7']
          update_data.GaseEm_legend_8 = request.POST['GasEm-legend-8']
          update_data.GaseEm_legend_9 = request.POST['GasEm-legend-9']
          update_data.GaseEm_legend_10 = request.POST['GasEm-legend-10']
          update_data.GaseEm_legend_11 = request.POST['GasEm-legend-11']
          update_data.GaseEm_edit_note = request.POST['GasEm-editnote']
          update_data.GaseEm_custom_legend = request.POST['GasEm-custom-legend']
          update_data.GaseEm_doc_con_1 = request.POST['GasEm-doc1']
          update_data.GaseEm_doc_con_2 = request.POST['GasEm-doc2']
          update_data.GaseEm_doc_con_3 = request.POST['GasEm-doc3']
          update_data.GaseEm_analyzed_by = request.FILES["GasEm-analyzedby" ]
          update_data.GaseEm_reviewd_by = request.FILES["GasEm-reviewedby" ]
          update_data.GaseEm_approved_by = request.FILES["GasEm-approvedby" ]

          update_data.save()
          id = (GaseousEmissionForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f'/GaseousForm-view-form/{str(id)}/'
               return redirect(to=url)
          if "submit" in request.POST:
               return redirect('gaseousEmissionList')
          else:
               return HttpResponse('Invalid Request Method',status=400)
     return redirect('gaseousEmissionList')



@login_required(login_url="/login")
def gaseousEmissionReport(request,pk):
     gaseousReport = GaseousEmissionForm.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     context ={'list': gaseousReport,'qr':'media/qr.png'}


     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")

     return render(request,"gaseousEmissionReport.html",context)


@login_required(login_url="/login")
def gaseousReportgeneratePDF(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,GasEm_lab_report_no1,GasEm_invoice_bill_no,GaseEm_reporting_date,GaseEm_reporting_to,GaseEm_address,GaseEm_attention,GaseEm_email,GaseEm_test_id,GaseEm_test_perf_date,
                       GasEm_test_desc,GaseEm_test_type,GaseEm_test_perf_by,GaseEm_types):
               super().__init__()
               self.GasEm_lab_report_no1 = GasEm_lab_report_no1
               self.GasEm_invoice_bill_no_number = GasEm_invoice_bill_no
               self.GaseEm_reporting_date = GaseEm_reporting_date
               self.GaseEm_reporting_to = GaseEm_reporting_to
               self.GaseEm_address = GaseEm_address
               self.GaseEm_attention = GaseEm_attention
               self.GaseEm_email = GaseEm_email
               self.GaseEm_test_id = GaseEm_test_id
               self.GaseEm_test_perf_date = GaseEm_test_perf_date
               self.GasEm_test_desc = GasEm_test_desc
               self.GaseEm_test_type = GaseEm_test_type
               self.GaseEm_test_perf_by = GaseEm_test_perf_by
               self.GaseEm_types = GaseEm_types


          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.GasEm_lab_report_no1)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.GasEm_invoice_bill_no_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.GaseEm_reporting_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.GaseEm_reporting_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.GaseEm_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.GaseEm_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.GaseEm_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(91,82,txt="Test ID:")
               self.text(110,82,txt=self.GaseEm_test_id)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(71,88,txt="Test Performed Date:")
               self.text(110,88,txt=self.GaseEm_test_perf_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(87.2,94,txt="Test Type:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.GaseEm_test_type)

               self.line(105,78,105,114)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(74.5,100,txt="Test Performed By:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.GaseEm_test_perf_by)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(78,106,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.GasEm_test_desc)

               self.rect(10,108.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(92.8,112,txt="Types:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.GaseEm_types)

               #table header
               self.rect(10,116.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,120.5,txt="Aanalytical Test Report")



               self.set_y(123)





     gaseousForm = GaseousEmissionForm.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Unit","Test Result",""],
     ]
     sr_no = 1
     if gaseousForm.GaseEm_sr1:
          a = [str(sr_no),"Smoke, Ringlemann Scale","-",gaseousForm.GaseEm_sr1,"2"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr2:
          a = [str(sr_no),"Particular matter","mg/Nm3",gaseousForm.GaseEm_sr2,"300"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr3:
          a = [str(sr_no),"Carobon Monoxide (CO)","mg/Nm3",gaseousForm.GaseEm_sr3,"800"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr4:
          a = [str(sr_no),"Nitrogen Dioxide (NO2)","mg/Nm3",gaseousForm.GaseEm_sr4,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr5:
          a = [str(sr_no),"Nitrogen Oxide (NO)","mg/Nm3",gaseousForm.GaseEm_sr5,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr6 and gaseousForm.GaseEm_types == 'gas fired':
          a = [str(sr_no),"NOx","mg/Nm3",gaseousForm.GaseEm_sr6,"400"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif gaseousForm.GaseEm_sr6 and gaseousForm.GaseEm_types == "oil fired":
          a = [str(sr_no),"NOx","mg/Nm3",gaseousForm.GaseEm_sr6,"600"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif gaseousForm.GaseEm_sr6 and gaseousForm.GaseEm_types == "coal fired":
          a = [str(sr_no),"NOx","mg/Nm3",gaseousForm.GaseEm_sr6,"1200"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     if gaseousForm.GaseEm_sr7:
          a = [str(sr_no),"Oxygen (O2)","%",gaseousForm.GaseEm_sr7,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr8:
          a = [str(sr_no),"Hydrogen Sulfide(H2S)","mg/Nm3",gaseousForm.GaseEm_sr8,"10"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr9:
          a = [str(sr_no),"Hydrogen Chloride","mg/Nm3",gaseousForm.GaseEm_sr9,"400"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr10:
          a = [str(sr_no),"Chlorine","mg/Nm3",gaseousForm.GaseEm_sr10,"150"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr11:
          a = [str(sr_no),"Hydrogen Fluoride","mg/Nm3",gaseousForm.GaseEm_sr11,"150"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr12:
          a = [str(sr_no),"Sulphur Dioxide (SO2)","mg/Nm3",gaseousForm.GaseEm_sr12,"1700"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr13:
          a = [str(sr_no),"Mercury","mg/Nm3",gaseousForm.GaseEm_sr13,"10"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr14:
          a = [str(sr_no),"Cadmium","mg/Nm3",gaseousForm.GaseEm_sr14,"20"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr15:
          a = [str(sr_no),"Arsenic","mg/Nm3",gaseousForm.GaseEm_sr15,"20"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr16:
          a = [str(sr_no),"Copper","mg/Nm3",gaseousForm.GaseEm_sr16,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr17:
          a = [str(sr_no),"Antimony","mg/Nm3",gaseousForm.GaseEm_sr17,"20"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr18:
          a = [str(sr_no),"Zinc","mg/Nm3",gaseousForm.GaseEm_sr18,"200"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr19:
          a = [str(sr_no),"Lead","mg/Nm3",gaseousForm.GaseEm_sr19,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr20:
          a = [str(sr_no),"Carbon dioxide (CO2)","%",gaseousForm.GaseEm_sr20,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr21:
          a = [str(sr_no),"Hydrocarbon","%",gaseousForm.GaseEm_sr21,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if gaseousForm.GaseEm_sr22:
          a = [str(sr_no),"Noise","db",gaseousForm.GaseEm_sr22,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     pdf = PDFWithPageNumbers(GasEm_lab_report_no1=gaseousForm.GasEm_lab_report_no1,GasEm_invoice_bill_no=gaseousForm.GasEm_invoice_bill_no,GaseEm_reporting_date=gaseousForm.GaseEm_reporting_date,GaseEm_reporting_to=gaseousForm.GaseEm_reporting_to,
                              GaseEm_address=gaseousForm.GaseEm_address,GaseEm_attention=gaseousForm.GaseEm_attention,GaseEm_email=gaseousForm.GaseEm_email,GaseEm_test_id=gaseousForm.GaseEm_test_id,GaseEm_test_perf_date=gaseousForm.GaseEm_test_perf_date,
                              GasEm_test_desc=gaseousForm.GasEm_test_desc,GaseEm_test_type=gaseousForm.GaseEm_test_type,GaseEm_test_perf_by=gaseousForm.GaseEm_test_perf_by,
                              GaseEm_types=gaseousForm.GaseEm_types,
                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True,margin=15)











     #report data table
     num_rows = 0
     with pdf.table(col_widths=(6, 45, 30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               num_rows = num_rows+1
               if k == 0:
                    data_row[4] = gaseousForm.GaseEm_select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)

     print("y",num_rows)
     if num_rows >=18 and num_rows <=23:
          pdf.add_page()
     Table_Data1 = [
          
     ]
     if gaseousForm.GaseEm_edit_note:
          a=["Note :"+gaseousForm.GaseEm_edit_note] 
          Table_Data1.append(a)
          
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if gaseousForm.GaseEm_legend_1:
          a = [gaseousForm.GaseEm_legend_1]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_2:
          a = [gaseousForm.GaseEm_legend_2]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_3:
          a = [gaseousForm.GaseEm_legend_3]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_4:
          a = [gaseousForm.GaseEm_legend_4]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_5:
          a = [gaseousForm.GaseEm_legend_5]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_6:
          a = [gaseousForm.GaseEm_legend_6]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_7:
          a = [gaseousForm.GaseEm_legend_7]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_8:
          a = [gaseousForm.GaseEm_legend_8]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_9:
          a = [gaseousForm.GaseEm_legend_9]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_10:
          a = [gaseousForm.GaseEm_legend_10]
          Table_data_legend.append(a)
          
     if gaseousForm.GaseEm_legend_11:
          a = [gaseousForm.GaseEm_legend_11]
          Table_data_legend.append(a)
          

     if gaseousForm.GaseEm_custom_legend:
          a = [gaseousForm.GaseEm_custom_legend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')


     # if num_rows >= 15:
     #      pdf.add_page()
     #      num_rows = 0



     # y = 196
     # print('y',pdf.y + num_rows)
     # print(num_rows)
     # # data after Table
     # if num_rows == 20:
     #      pdf.add_page()
     # if gaseousForm.GaseEm_edit_note:
     #      pdf.set_font("Calibri","B", 10)
     #      if num_rows >= 15:
     #           pdf.text(10,188,txt="Note:")
     #      else:
     #           pdf.text(10,y+5,txt="Note:")
     #           pdf.set_font("Calibri","", 8)
     #      if num_rows >= 15:
     #           pdf.set_y(185.5)
     #      else:
     #           pdf.set_y(pdf.y+2)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=gaseousForm.GaseEm_edit_note)
     # line_height = 4

     # if gaseousForm.GaseEm_legend_1:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_1)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_2:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_2)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_3:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_3)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_4:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_4)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_5:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_5)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_6:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_6)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_7:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_7)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_8:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_8)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_9:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_9)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_10:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_10)
     #      y = y+line_height
     # if gaseousForm.GaseEm_legend_11:
     #      pdf.text(10,y,txt=gaseousForm.GaseEm_legend_11)
     #      y = y+line_height


     pdf.image(gaseousForm.GaseEm_analyzed_by,30,238,12,12)
     pdf.line(19,250,36+pdf.get_string_width("Analyzed By (Analyst)"),250)
     pdf.text(26,253,"Analyzed By (Analyst)")
     pdf.image(gaseousForm.GaseEm_reviewd_by,100,238,12,12)
     pdf.line(126,250,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),250)
     pdf.text(87.5,253,"Reviewed By (Assistant Manager)")
     pdf.image(gaseousForm.GaseEm_approved_by,165,237,12,12)
     pdf.image(gaseousForm.GaseEm_approved_by1,178,237,12,12)
     pdf.line(155,250,165+pdf.get_string_width("Approved By (Lab Manager)"),250)
     pdf.text(160,253,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,257,-10+pdf.w,257)
     pdf.text(10,262,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,266,txt="• Report is valid for current batch (sample).")
     pdf.text(10,269,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(269.8)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(273)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,259,19,15)
     if gaseousForm.location == "SEQS":
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if gaseousForm.location == "PEQS":
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15)
     if gaseousForm.location == "NEQS":
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)     
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,259,19,15)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,276,txt="(Certificate # 20210131)")
     pdf.text(158,276,txt="(Certificate # 20210131)")
     pdf.text(182,276,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,277,25,5)
     pdf.text(132,280,txt=gaseousForm.GaseEm_doc_con_1)
     pdf.rect(155,277,25,5)
     pdf.text(157,280,txt=gaseousForm.GaseEm_doc_con_2)
     pdf.rect(180,277,25,5)
     pdf.text(186.5,280,txt=gaseousForm.GaseEm_doc_con_3)








     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response


@login_required(login_url="/login")
def ambientAirList(request):
     ambientAir = AmbientAirForm.objects.all()
     context = {'data':ambientAir}
     return render(request,"ambientAirList.html",context)


@login_required(login_url="/login")
def ambientAirDelete(request,pk):
     ambientDelete = AmbientAirForm.objects.get(id=pk)
     ambientDelete.delete()
     return redirect('ambientAirList')

@login_required(login_url="/login")
def ambientAirEdit(request,pk):
     ambientEdit = AmbientAirForm.objects.get(id=pk)
     context = {'data':ambientEdit}
     return render(request,"ambientAirEdit.html",context)


@login_required(login_url="/login")
def ambientAirUpdateRecord(request,pk):
     ambientUpdate = AmbientAirForm.objects.get(id=pk)
     if request.method == 'POST':
          # data = JsonResponse(request.POST)
          # return data
          ambientUpdate.location = request.POST['location']
          ambientUpdate.ambienAir_lab_report_no1 = request.POST['ambient_Air_lab_report_no']
          ambientUpdate.ambienAir_invoice_bill_no = request.POST['ambientAir_invoice_no']
          ambientUpdate.ambientAir_reporting_date = request.POST['ambientAir_rep_date']
          ambientUpdate.ambientAir_reporting_to = request.POST['ambientAir_rep_to']
          ambientUpdate.ambientAir_address = request.POST['ambientAir_address']
          ambientUpdate.ambientAir_attention = request.POST['ambientAir_attention']
          ambientUpdate.ambientAir_email = request.POST['ambientAir_email']
          ambientUpdate.ambientAir_test_id = request.POST['ambientAir_testid']
          ambientUpdate.ambientAir_test_perf_date = request.POST['ambientAir_test_perf_date']
          ambientUpdate.ambientAir_test_type_location = request.POST['ambientAir_testtype_location']
          ambientUpdate.ambientAir_test_perf_by = request.POST['ambientAir_test_perf_by']
          ambientUpdate.ambienAir_test_desc = request.POST['ambientAir_test_desc']
          ambientUpdate.ambientAir_sr1 = request.POST['ambientAir_sr1']
          ambientUpdate.ambientAir_sr2 = request.POST['ambientAir_sr2']
          ambientUpdate.ambientAir_sr3 = request.POST['ambientAir_sr3']
          ambientUpdate.ambientAir_sr4 = request.POST['ambientAir_sr4']
          ambientUpdate.ambientAir_sr5 = request.POST['ambientAir_sr5']
          ambientUpdate.ambientAir_sr6 = request.POST['ambientAir_sr6']
          ambientUpdate.ambientAir_sr7 = request.POST['ambientAir_sr7']
          ambientUpdate.ambientAir_sr8 = request.POST['ambientAir_sr8']
          ambientUpdate.ambientAir_sr9 = request.POST['ambientAir_sr9']
          ambientUpdate.ambientAir_sr10 = request.POST['ambientAir_sr10']
          ambientUpdate.ambientAir_sr11 = request.POST['ambientAir_sr11']
          ambientUpdate.ambientAir_sr12 = request.POST['ambientAir_sr12']
          ambientUpdate.ambientAir_sr13 = request.POST['ambientAir_sr13']
          ambientUpdate.ambientAir_sr14 = request.POST['ambientAir_sr14']
          ambientUpdate.ambientAir_legend_1 = request.POST['ambientAir-legend-1']
          ambientUpdate.ambientAir_legend_2 = request.POST['ambientAir-legend-2']
          ambientUpdate.ambientAir_legend_3 = request.POST['ambientAir-legend-3']
          ambientUpdate.ambientAir_legend_4 = request.POST['ambientAir-legend-4']
          ambientUpdate.ambientAir_legend_5 = request.POST['ambientAir-legend-5']
          ambientUpdate.ambientAir_legend_6 = request.POST['ambientAir-legend-6']
          ambientUpdate.ambientAir_edit_note = request.POST['ambientAir_editNote']
          ambientUpdate.ambientAir_custom_legend = request.POST['ambientAir_customlegend']
          ambientUpdate.ambientAir_doc_con_1 = request.POST['ambientAir_doc1']
          ambientUpdate.ambientAir_doc_con_2 = request.POST['ambientAir_doc2']
          ambientUpdate.ambientAir_doc_con_3 = request.POST['ambientAir_doc3']
          ambientUpdate.ambientAir_analyzed_by = request.FILES["ambientAir_analyzedby" ]
          ambientUpdate.ambientAir_reviewd_by = request.FILES["ambientAir_reviewedby" ]
          ambientUpdate.ambientAir_approved_by = request.FILES["ambientAir_approvedby" ]
          ambientUpdate.ambientAir_approved_by1 = request.FILES["ambientAir_approvedby1" ]

          ambientUpdate.save()

          id = (AmbientAirForm.objects.last()).id
          if "update_and_view" in request.POST:
               url = f"/ambientAir-view/{str(id)}/"
               return redirect(to=url)
          else:
               # url = f"/{str(id)}/"
               return redirect(to="ambientAirList")
     else:
          return redirect('ambientAirList')



@login_required(login_url="/login")
def ambientAirview(request,pk):
     ambientAir = AmbientAirForm.objects.get(id=pk)

     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':ambientAir,'qr':'media/qr.png'}
     return render(request,'ambientAirReport.html',context)

@login_required(login_url="/login")
def ambientAirGeneratePDF(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,ambienAir_lab_report_no1,ambienAir_invoice_bill_no,ambientAir_reporting_date,ambientAir_reporting_to,ambientAir_address,ambientAir_attention,ambientAir_email,ambientAir_test_id,ambientAir_test_perf_date,
                       ambientAir_test_perf_by,ambientAir_test_type_location,ambienAir_test_desc):
               super().__init__()
               self.ambienAir_lab_report_no1 = ambienAir_lab_report_no1
               self.ambienAir_invoice_bill_no_number = ambienAir_invoice_bill_no
               self.ambientAir_reporting_date = ambientAir_reporting_date
               self.ambientAir_reporting_to = ambientAir_reporting_to
               self.ambientAir_address = ambientAir_address
               self.ambientAir_attention = ambientAir_attention
               self.ambientAir_email = ambientAir_email
               self.ambientAir_test_id = ambientAir_test_id
               self.ambientAir_test_perf_date = ambientAir_test_perf_date
               self.ambientAir_test_perf_by = ambientAir_test_perf_by
               self.ambientAir_test_type_location = ambientAir_test_type_location
               self.ambientAir_test_perf_by = ambientAir_test_perf_by
               self.ambienAir_test_desc = ambienAir_test_desc



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.ambienAir_lab_report_no1)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.ambienAir_invoice_bill_no_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.ambientAir_reporting_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.ambientAir_reporting_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.ambientAir_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.ambientAir_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.ambientAir_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(91,82,txt="Test ID:")
               self.text(110,82,txt=self.ambientAir_test_id)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(71,88,txt="Test Performed Date:")
               self.text(110,88,txt=self.ambientAir_test_perf_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(77.8,94,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.ambienAir_test_desc)

               self.line(105,78,105,108)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(70.5,100,txt="Test Type & Location:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.ambientAir_test_type_location)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(74,106,txt="Test Performed By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.ambientAir_test_perf_by)

               #table header
               self.rect(10,110.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,114.5,txt="Aanalytical Test Report")

               self.set_y(117)




     ambientAirForm = AmbientAirForm.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Unit","Test Result",""],
     ]
     sr_no = 1
     if ambientAirForm.ambientAir_sr1:
          a = [str(sr_no),"Temperature","°C",ambientAirForm.ambientAir_sr1,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr2:
          a = [str(sr_no),"Humidity","%",ambientAirForm.ambientAir_sr2,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr3:
          a = [str(sr_no),"Particular matter (PM 1.0)","ug/m3",ambientAirForm.ambientAir_sr3,"500"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr4 and ambientAirForm.ambienAir_select == "SEQS":
          a = [str(sr_no),"Particular matter (PM 2.5)","ug/m3",ambientAirForm.ambientAir_sr4,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif ambientAirForm.ambientAir_sr4 and ambientAirForm.ambienAir_select == "PEQS":
          a = [str(sr_no),"Particular matter (PM 2.5)","ug/m3",ambientAirForm.ambientAir_sr4,"35"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif ambientAirForm.ambientAir_sr4 and ambientAirForm.ambienAir_select == "NEQS":
          a = [str(sr_no),"Particular matter (PM 2.5)","ug/m3",ambientAirForm.ambientAir_sr4,"35"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr5:
          a = [str(sr_no),"Particular matter (PM 10)","ug/m3",ambientAirForm.ambientAir_sr5,"150"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr6:
          a = [str(sr_no),"Carbon Monoxide (CO)","mg/m3",ambientAirForm.ambientAir_sr6,"10"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr7:
          a = [str(sr_no),"Sulphur Dioxide (SO2)","ug/m3",ambientAirForm.ambientAir_sr7,"120"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr8:
          a = [str(sr_no),"Nitrogen Dioxide (NO2)","ug/m3",ambientAirForm.ambientAir_sr8,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr9:
          a = [str(sr_no),"Nitrogen Oxide (NO)","ug/m3",ambientAirForm.ambientAir_sr9,"40"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr10:
          a = [str(sr_no),"Oxygen (O2)","%",ambientAirForm.ambientAir_sr10,"21"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr11:
          a = [str(sr_no),"Formaldehyde","mg/m3",ambientAirForm.ambientAir_sr11,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr12:
          a = [str(sr_no),"Total Volatile Organic Compounds (TVOC)","mg/m3",ambientAirForm.ambientAir_sr12,"-"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr13:
          a = [str(sr_no),"Ozone (O3)","ug/m3",ambientAirForm.ambientAir_sr13,"130"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if ambientAirForm.ambientAir_sr14:
          a = [str(sr_no),"Lead (Pb)","ug/m3",ambientAirForm.ambientAir_sr14,"1.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)



     pdf = PDFWithPageNumbers(ambienAir_lab_report_no1=ambientAirForm.ambienAir_lab_report_no1,ambienAir_invoice_bill_no=ambientAirForm.ambienAir_invoice_bill_no,ambientAir_reporting_date=ambientAirForm.ambientAir_reporting_date,ambientAir_reporting_to=ambientAirForm.ambientAir_reporting_to,
                              ambientAir_address=ambientAirForm.ambientAir_address,ambientAir_attention=ambientAirForm.ambientAir_attention,ambientAir_email=ambientAirForm.ambientAir_email,ambientAir_test_id=ambientAirForm.ambientAir_test_id,ambientAir_test_perf_date=ambientAirForm.ambientAir_test_perf_date,
                              ambienAir_test_desc=ambientAirForm.ambienAir_test_desc,ambientAir_test_type_location=ambientAirForm.ambientAir_test_type_location,ambientAir_test_perf_by=ambientAirForm.ambientAir_test_perf_by,

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     num_rows = 0
     with pdf.table(col_widths=(6, 45, 30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               num_rows+=1
               if k == 0:
                    data_row[4] = ambientAirForm.ambienAir_select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table

     print("y",num_rows)
     if num_rows >=18 and num_rows <=23:
          pdf.add_page()
     Table_Data1 = [
          
     ]
     if ambientAirForm.ambientAir_edit_note:
          a=["Note :"+ambientAirForm.ambientAir_edit_note] 
          Table_Data1.append(a)
          
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if ambientAirForm.ambientAir_legend_1:
          a = [ambientAirForm.ambientAir_legend_1]
          Table_data_legend.append(a)
          
     if ambientAirForm.ambientAir_legend_2:
          a = [ambientAirForm.ambientAir_legend_2]
          Table_data_legend.append(a)
          
     if ambientAirForm.ambientAir_legend_3:
          a = [ambientAirForm.ambientAir_legend_3]
          Table_data_legend.append(a)
          
     if ambientAirForm.ambientAir_legend_4:
          a = [ambientAirForm.ambientAir_legend_4]
          Table_data_legend.append(a)
          
     if ambientAirForm.ambientAir_legend_5:
          a = [ambientAirForm.ambientAir_legend_5]
          Table_data_legend.append(a)
          
     if ambientAirForm.ambientAir_legend_6:
          a = [ambientAirForm.ambientAir_legend_6]
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')



     # if ambientAirForm.ambientAir_edit_note:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,210.5,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(208)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=ambientAirForm.ambientAir_edit_note)
     # line_height = 4
     # y = 218
     # if ambientAirForm.ambientAir_legend_1:
     #      pdf.text(10,y,txt=ambientAirForm.ambientAir_legend_1)
     #      y = y+line_height
     # if ambientAirForm.ambientAir_legend_2:
     #      pdf.text(10,y,txt=ambientAirForm.ambientAir_legend_2)
     #      y = y+line_height
     # if ambientAirForm.ambientAir_legend_3:
     #      pdf.text(10,y,txt=ambientAirForm.ambientAir_legend_3)
     #      y = y+line_height
     # if ambientAirForm.ambientAir_legend_4:
     #      pdf.text(10,y,txt=ambientAirForm.ambientAir_legend_4)
     #      y = y+line_height
     # if ambientAirForm.ambientAir_legend_5:
     #      pdf.text(10,y,txt=ambientAirForm.ambientAir_legend_5)
     #      y = y+line_height
     # if ambientAirForm.ambientAir_legend_6:
     #      pdf.text(10,y,txt=ambientAirForm.ambientAir_legend_6)


     pdf.image(ambientAirForm.ambientAir_analyzed_by,30,238,12,12)
     pdf.line(19,250,36+pdf.get_string_width("Analyzed By (Analyst)"),250)
     pdf.text(26,253,"Analyzed By (Analyst)")
     pdf.image(ambientAirForm.ambientAir_reviewd_by,100,238,12,12)
     pdf.line(126,250,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),250)
     pdf.text(87.5,253,"Reviewed By (Assistant Manager)")
     pdf.image(ambientAirForm.ambientAir_approved_by,165,238,12,12)
     pdf.image(ambientAirForm.ambientAir_approved_by1,178,238,12,12)
     pdf.line(155,250,165+pdf.get_string_width("Approved By (Lab Manager)"),250)
     pdf.text(160,253,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,257,-10+pdf.w,257)
     pdf.text(10,262,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,266,txt="• Report is valid for current batch (sample).")
     pdf.text(10,269,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(269.8)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(273)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,259,19,15)
     if ambientAirForm.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if ambientAirForm.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if ambientAirForm.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)         
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,259,19,15)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,276,txt="(Certificate # 20210131)")
     pdf.text(158,276,txt="(Certificate # 20210131)")
     pdf.text(182,276,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,277,25,5)
     pdf.text(132,280,txt=ambientAirForm.ambientAir_doc_con_1)
     pdf.rect(155,277,25,5)
     pdf.text(157,280,txt=ambientAirForm.ambientAir_doc_con_2)
     pdf.rect(180,277,25,5)
     pdf.text(186.5,280,txt=ambientAirForm.ambientAir_doc_con_3)







     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response

@login_required(login_url="/login")
def wasteWaterSludgeList(request):
     wasteWaterForm = WasteWaterSludge.objects.all()
     context = {'data':wasteWaterForm}
     return render(request,'wasteWaterSludgeList.html',context)

@login_required(login_url="/login")
def wasteWaterSludgeDelete(request,pk):
     wastewaterForm = WasteWaterSludge.objects.get(id=pk)
     wastewaterForm.delete()
     return redirect('wasteWaterSludgeList')

@login_required(login_url="/login")
def wastewaterEdit(request,pk):
     wasteWaterForm = WasteWaterSludge.objects.get(id=pk)
     context = {'data':wasteWaterForm}
     return render(request,'wasteWaterEdit.html',context)

@login_required(login_url="/login")
def wasteWaterUpdate(request,pk):
     wasterWaterForm = WasteWaterSludge.objects.get(id=pk)
     if request.method == 'POST':
          wasterWaterForm.location = request.POST['location']
          wasterWaterForm.ww_lab_report_no = request.POST['ww_lab_report_no']
          wasterWaterForm.ww_invoice_no = request.POST['ww_invoice_no']
          wasterWaterForm.ww_report_date = request.POST['ww_report_date']
          wasterWaterForm.ww_report_to = request.POST['ww_report_to']
          wasterWaterForm.ww_address = request.POST['ww_address']
          wasterWaterForm.ww_attention = request.POST['ww_attention']
          wasterWaterForm.ww_email = request.POST['ww_email']
          wasterWaterForm.ww_sampleid = request.POST['ww_sampleid']
          wasterWaterForm.ww_sample_colec_Date = request.POST['ww_sample_colec_Date']
          wasterWaterForm.ww_sample_desc = request.POST['ww_sample_desc']
          wasterWaterForm.ww_sample_type = request.POST['ww_sample_type']
          wasterWaterForm.ww_sample_colec_by = request.POST['ww_sample_colec_by']
          wasterWaterForm.ww_date_of_analy = request.POST['ww_date_of_analy']
          wasterWaterForm.ww_test_desc = request.POST['ww_test_desc']
          wasterWaterForm.ww_sr1 = request.POST['ww_sr1']
          wasterWaterForm.ww_sr2 = request.POST['ww_sr2']
          wasterWaterForm.ww_sr3 = request.POST['ww_sr3']
          wasterWaterForm.ww_sr4 = request.POST['ww_sr4']
          wasterWaterForm.ww_sr5 = request.POST['ww_sr5']
          wasterWaterForm.ww_sr6 = request.POST['ww_sr6']
          wasterWaterForm.ww_sr7 = request.POST['ww_sr7']
          wasterWaterForm.ww_sr8 = request.POST['ww_sr8']
          wasterWaterForm.ww_sr9 = request.POST['ww_sr9']
          wasterWaterForm.ww_sr10 = request.POST['ww_sr10']
          wasterWaterForm.ww_sr11 = request.POST['ww_sr11']
          wasterWaterForm.ww_sr12 = request.POST['ww_sr12']
          wasterWaterForm.ww_sr13 = request.POST['ww_sr13']
          wasterWaterForm.ww_legend_1 = request.POST['ww-legend-1']
          wasterWaterForm.ww_legend_2 = request.POST['ww-legend-2']
          wasterWaterForm.ww_legend_3 = request.POST['ww-legend-3']
          wasterWaterForm.ww_legend_4 = request.POST['ww-legend-4']
          wasterWaterForm.ww_legend_5 = request.POST['ww-legend-5']
          wasterWaterForm.ww_legend_6 = request.POST['ww-legend-6']
          wasterWaterForm.ww_legend_7 = request.POST['ww-legend-7']
          wasterWaterForm.ww_legend_8 = request.POST['ww-legend-8']
          wasterWaterForm.ww_legend_9 = request.POST['ww-legend-9']
          wasterWaterForm.ww_legend_10 = request.POST['ww-legend-10']
          wasterWaterForm.ww_legend_11 = request.POST['ww-legend-11']
          wasterWaterForm.ww_editnote = request.POST['ww_editnote']
          wasterWaterForm.ww_custom_legend = request.POST['ww_custom_legend']
          wasterWaterForm.ww_doc_con_1 = request.POST['ww_doc1']
          wasterWaterForm.ww_doc_con_2 = request.POST['ww_doc2']
          wasterWaterForm.ww_doc_con_3 = request.POST['ww_doc3']
          wasterWaterForm.ww_analyzed_by = request.FILES["ww_analyzedby" ]
          wasterWaterForm.ww_reviewd_by = request.FILES["ww_reviewedby" ]
          wasterWaterForm.ww_approved_by = request.FILES["ww_approvedby" ]
          wasterWaterForm.ww_approved_by1 = request.FILES["ww_approvedby1"]

          wasterWaterForm.save()
          id=(WasteWaterSludge.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f'/wasteWaterSludge-view/{str(id)}/'
               return redirect(to=url)
          else:
               return redirect("wasteWaterSludgeList")
     return render(request,"wasteWaterSludgeList.html")

@login_required(login_url="/login")
def wasteWaterView(request,pk):
     wasteWaterForm =  WasteWaterSludge.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':wasteWaterForm,'qr':'media/qr.png'}

     return render(request,'wasteWaterReport.html',context)



# def ambientAirview(request,pk):
#      ambientAir = AmbientAirForm.objects.get(id=pk)

#      current_url = request.build_absolute_uri()
#      qr = qrcode.QRCode(
#           version=1,
#           error_correction=qrcode.constants.ERROR_CORRECT_L,
#           box_size=10,
#           border=6,
#           )
#      qr.add_data(current_url)
#      qr.make(fit=True)
#      img = qr.make_image(fill_color="black", back_color="white")
#      img.save("media/qr.png")
#      context = {'data':ambientAir,'qr':'media/qr.png'}
#      return render(request,'ambientAirReport.html',context)

@login_required(login_url="/login")
def wasteWaterPdf(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,ww_lab_report_no,ww_invoice_no,ww_report_date,ww_report_to,ww_address,ww_attention,ww_email,ww_sampleid,ww_sample_colec_Date,
                       ww_sample_colec_by,ww_sample_type,ww_sample_desc):
               super().__init__()
               self.ww_lab_report_no = ww_lab_report_no
               self.ww_invoice_no_number = ww_invoice_no
               self.ww_report_date = ww_report_date
               self.ww_report_to = ww_report_to
               self.ww_address = ww_address
               self.ww_attention = ww_attention
               self.ww_email = ww_email
               self.ww_sampleid = ww_sampleid
               self.ww_sample_colec_Date = ww_sample_colec_Date
               self.ww_sample_colec_by = ww_sample_colec_by
               self.ww_sample_type = ww_sample_type
               self.ww_sample_desc = ww_sample_desc



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.ww_lab_report_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.ww_invoice_no_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.ww_report_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.ww_report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.ww_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.ww_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.ww_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(87,82,txt="Sample ID:")
               self.text(110,82,txt=self.ww_sampleid)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(67.7,88,txt="Sample Collection Date:")
               self.text(110,88,txt=self.ww_sample_colec_Date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(73.2,94,txt="Sample Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.ww_sample_desc)

               self.line(105,78,105,108)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(82.8,100,txt="Sample Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.ww_sample_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72,106,txt="Sample Collected By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.ww_sample_colec_by)

               #table header
               self.rect(10,110.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,114.5,txt="Aanalytical Test Report")

               self.set_y(117)




     vem = WasteWaterSludge.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Methods","Unit","Result"],
     ]
     sr_no = 1
     if vem.ww_sr1:
          a = [str(sr_no),"Cadmium (Cd)","*APHA 3111- B","mg/Kg",vem.ww_sr1]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr2:
          a = [str(sr_no),"Copper (Cu)","*APHA 3111- B","mg/Kg",vem.ww_sr2]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr3:
          a = [str(sr_no),"Iron (Fe)","*APHA 3111- B","mg/Kg",vem.ww_sr3]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr4:
          a = [str(sr_no),"Boron (B)","HACH 8015","mg/Kg",vem.ww_sr4]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr5:
          a = [str(sr_no),"Lead (Pb)","APHA 3111- B","mg/Kg",vem.ww_sr5]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr6:
          a = [str(sr_no),"Mercury (Hg)","*APHA 3112- B","mg/Kg",vem.ww_sr6]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr7:
          a = [str(sr_no),"Selenium (Se)","*APHA 3114- B","mg/Kg",vem.ww_sr7]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr8:
          a = [str(sr_no),"Silver (Ag)","*APHA 3111- B","mg/Kg",vem.ww_sr8]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr9:
          a = [str(sr_no),"Nickel (Ni)","*APHA 3111- B","mg/Kg",vem.ww_sr9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr10:
          a = [str(sr_no),"Zinc (Zn)","*APHA 3111- B","mg/Kg",vem.ww_sr10]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr11:
          a = [str(sr_no),"Arsenic (As)","*APHA 3114- B","mg/Kg",vem.ww_sr11]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr12:
          a = [str(sr_no),"Manganese (Mn)","*APHA 3111- B","mg/Kg",vem.ww_sr12]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.ww_sr13:
          a = [str(sr_no),"Chromium","*APHA 3111- B","mg/Kg",vem.ww_sr13]
          sr_no = sr_no+1
          TABLE_DATA.append(a)




     pdf = PDFWithPageNumbers(ww_lab_report_no=vem.ww_lab_report_no,ww_invoice_no=vem.ww_invoice_no,ww_report_date=vem.ww_report_date,ww_report_to=vem.ww_report_to,
                              ww_address=vem.ww_address,ww_attention=vem.ww_attention,ww_email=vem.ww_email,ww_sampleid=vem.ww_sampleid,ww_sample_colec_Date=vem.ww_sample_colec_Date,
                              ww_sample_desc=vem.ww_sample_desc,ww_sample_type=vem.ww_sample_type,ww_sample_colec_by=vem.ww_sample_colec_by,

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)










     num_rows = 0
     #report data table
     with pdf.table(col_widths=(6, 45, 30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               num_rows+=1
               # if k == 0:
               #      data_row[4] = vem.ambienAir_select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table

     # if num_rows >=10 and num_rows <=14:
     #      pdf.add_page()
     Table_Data1 = [
          
     ]
     if vem.ww_editnote:
          a=["Note :"+vem.ww_editnote] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if vem.ww_legend_1:
          a = [vem.ww_legend_1]
          Table_data_legend.append(a)
          
     if vem.ww_legend_2:
          a = [vem.ww_legend_2]
          Table_data_legend.append(a)
          
     if vem.ww_legend_3:
          a = [vem.ww_legend_3]
          Table_data_legend.append(a)
          
     if vem.ww_legend_4:
          a = [vem.ww_legend_4]
          Table_data_legend.append(a)
          
     if vem.ww_legend_5:
          a = [vem.ww_legend_5]
          Table_data_legend.append(a)
          
     if vem.ww_legend_6:
          a = [vem.ww_legend_6]
          Table_data_legend.append(a)
          
     if vem.ww_legend_7:
          a = [vem.ww_legend_7]
          Table_data_legend.append(a)
          
     if vem.ww_legend_8:
          a = [vem.ww_legend_8]
          Table_data_legend.append(a)
          
     if vem.ww_legend_9:
          a = [vem.ww_legend_9]
          Table_data_legend.append(a)
          
     if vem.ww_legend_10:
          a = [vem.ww_legend_10]
          Table_data_legend.append(a)
          
     if vem.ww_legend_11:
          a = [vem.ww_legend_11]
          Table_data_legend.append(a)
          

     if vem.ww_custom_legend:
          a = [vem.ww_custom_legend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L') 


     pdf.image(vem.ww_analyzed_by,30,245,12,12)
     pdf.line(19,256,36+pdf.get_string_width("Analyzed By (Analyst)"),256)
     pdf.text(26,259,"Analyzed By (Analyst)")
     pdf.image(vem.ww_reviewd_by,100,245,12,12)
     pdf.line(126,256,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),256)
     pdf.text(87.5,259,"Reviewed By (Assistant Manager)")
     pdf.image(vem.ww_approved_by,165,245,12,12)
     pdf.image(vem.ww_approved_by1,178,245,12,12)
     pdf.line(155,256,165+pdf.get_string_width("Approved By (Lab Manager)"),256)
     pdf.text(160,259,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,262,-10+pdf.w,262)
     pdf.text(10,266,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,271,txt="• Report is valid for current batch (sample).")
     pdf.text(10,274.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(275.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(279)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,263,19,15)
     if vem.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if vem.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if vem.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,263,19,15)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=vem.ww_doc_con_1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=vem.ww_doc_con_2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=vem.ww_doc_con_3)







     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response




@login_required(login_url="/login")
def vehicularEmissionList(request):
     vel = VehiculEmissionForm.objects.all()
     context = {'data':vel}
     return render(request,'vehicularEmissionList.html',context)

@login_required(login_url="/login")
def vehicularEmissionDelete(request,pk):
     vem =VehiculEmissionForm.objects.get(id=pk)
     vem.delete()
     return redirect(to="vehicularEmissionList")

@login_required(login_url="/login")
def vehicularEmissionEdit(request,pk):
     vem = VehiculEmissionForm.objects.get(id=pk)
     context = {'data':vem}
     return render(request,"vehicularEmissionEdit.html",context)

@login_required(login_url="/login")
def vehicularEmissionUpdate(request,pk):
     vem = VehiculEmissionForm.objects.get(id=pk)
     if request.method == "POST":
          vem.location = request.POST['location']
          vem.vehEm_lab_report_no = request.POST['vehEm_lab_report_no']
          vem.vehEm_invoice_no = request.POST['vehEm_invoice_no']
          vem.vehEm_report_date = request.POST['vehEm_report_date']
          vem.vehEm_report_to = request.POST['vehEm_report_to']
          vem.vehEm_address = request.POST['vehEm_address']
          vem.vehEm_attention = request.POST['vehEm_attention']
          vem.vehEm_email = request.POST['vehEm_email']
          vem.vehEm_testId = request.POST['vehEm_testId']
          vem.vehEm_test_perf_date = request.POST['vehEm_test_perf_date']
          vem.vehEm_test_type = request.POST['vehEm_test_type']
          vem.vehEm_test_perfBy = request.POST['vehEm_test_perfBy']
          vem.vehEm_test_desc = request.POST['vehEm_test_desc']
          vem.select = request.POST['select']
          vem.vehEm_sr1 = request.POST['vehEm_sr1']
          vem.vehEm_sr2 = request.POST['vehEm_sr2']
          vem.vehEm_sr3 = request.POST['vehEm_sr3']
          vem.vehEm_legend_1 = request.POST['vehEm-legend-1']
          vem.vehEm_legend_2 = request.POST['vehEm-legend-2']
          vem.vehEm_legend_3 = request.POST['vehEm-legend-3']
          vem.vehEm_legend_4 = request.POST['vehEm-legend-4']
          vem.vehEm_legend_5 = request.POST['vehEm-legend-5']
          vem.vehEm_legend_6 = request.POST['vehEm-legend-6']
          vem.vehEm_legend_7 = request.POST['vehEm-legend-7']
          vem.vehEm_legend_8 = request.POST['vehEm-legend-8']
          vem.vehEm_legend_9 = request.POST['vehEm-legend-9']
          vem.vehEm_legend_10 = request.POST['vehEm-legend-10']
          vem.vehEm_legend_11 = request.POST['vehEm-legend-11']
          vem.vehEm_edit_note = request.POST['vehEm_edit_note']
          vem.vehEm_custom_legend = request.POST['vehEm_custom_legend']
          vem.vehEm_doc_con1 = request.POST['vehEm_doc-con1']
          vem.vehEm_doc_con2 = request.POST['vehEm_doc-con2']
          vem.vehEm_doc_con3 = request.POST['vehEm_doc-con3']
          vem.vehEm_analyzedby = request.FILES['vehEm-analyzedby']
          vem.vehEm_reviewedby = request.FILES['vehEm-reviewedby']
          vem.vehEm_approvedby = request.FILES['vehEm-approvedby']
          vem.vehEm_approvedby1 = request.FILES['vehEm-approvedby1']

          vem.save()
          id = (VehiculEmissionForm.objects.last()).id
          if "update_and_view" in request.POST:
               url = f'/vehicularEmission-view/{str(id)}/'
               return redirect(to=url)
          else:
               return redirect("vehicularEmissionList")
     return render(request,"vehicularEmissionList.html")

@login_required(login_url="/login")
def vehicularEmissionView(request,pk):
     vem = VehiculEmissionForm.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':vem,'qr':'media/qr.png'}

     return render(request,'vehicularEmissionReport.html',context)

@login_required(login_url="/login")
def vehicularEmissionReport(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,vehEm_lab_report_no,vehEm_invoice_no,vehEm_report_date,vehEm_address,vehEm_attention,vehEm_email,vehEm_testId,vehEm_test_perf_date,
                       vehEm_test_perfBy,vehEm_test_type,vehEm_test_desc,vehEm_report_to):
               super().__init__()
               self.vehEm_lab_report_no = vehEm_lab_report_no
               self.vehEm_invoice_no_number = vehEm_invoice_no
               self.vehEm_report_date = vehEm_report_date
               self.vehEm_address = vehEm_address
               self.vehEm_attention = vehEm_attention
               self.vehEm_email = vehEm_email
               self.vehEm_testId = vehEm_testId
               self.vehEm_test_perf_date = vehEm_test_perf_date
               self.vehEm_test_perfBy = vehEm_test_perfBy
               self.vehEm_test_type = vehEm_test_type
               self.vehEm_test_desc = vehEm_test_desc
               self.vehEm_report_to = vehEm_report_to



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.vehEm_lab_report_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.vehEm_invoice_no_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.vehEm_report_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.vehEm_report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.vehEm_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.vehEm_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.vehEm_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(89,82,txt="Test ID:")
               self.text(110,82,txt=self.vehEm_testId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(68.7,88,txt="Test Performed Date:")
               self.text(110,88,txt=self.vehEm_test_perf_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(75.2,94,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.vehEm_test_desc)

               self.line(105,78,105,108)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(84.8,100,txt="Test Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.vehEm_test_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72,106,txt="Test Performed By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.vehEm_test_perfBy)

               #table header
               self.rect(10,110.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,114.5,txt="Aanalytical Test Report")

               self.set_y(117)




     vem = VehiculEmissionForm.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Unit","Result",""],
     ]
     sr_no = 1
     if vem.vehEm_sr1:
          a = [str(sr_no),"Carbon Monoxide","%",vem.vehEm_sr1,"6"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.vehEm_sr2:
          a = [str(sr_no),"Smoke Ringlemann Scale","-",vem.vehEm_sr2,"2"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if vem.vehEm_sr3:
          a = [str(sr_no),"	Noise","dB",vem.vehEm_sr3,"85"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)





     pdf = PDFWithPageNumbers(vehEm_lab_report_no=vem.vehEm_lab_report_no,vehEm_invoice_no=vem.vehEm_invoice_no,vehEm_report_date=vem.vehEm_report_date,vehEm_report_to=vem.vehEm_report_to,
                              vehEm_address=vem.vehEm_address,vehEm_attention=vem.vehEm_attention,vehEm_email=vem.vehEm_email,vehEm_testId=vem.vehEm_testId,vehEm_test_perf_date=vem.vehEm_test_perf_date,
                              vehEm_test_desc=vem.vehEm_test_desc,vehEm_test_type=vem.vehEm_test_type,vehEm_test_perfBy=vem.vehEm_test_perfBy,

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     with pdf.table(col_widths=(6, 45, 30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               if k == 0:
                    data_row[4] = vem.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table

     if vem.vehEm_edit_note:
          pdf.set_font("Calibri","B", 10)
          pdf.text(10,145,txt="Note:")
          pdf.set_font("Calibri","", 8)
          pdf.set_y(142.5)
          pdf.set_x(20)
          pdf.multi_cell(182,txt=vem.vehEm_edit_note)
     line_height = 4
     y = 153
     if vem.vehEm_legend_1:
          pdf.text(10,y,txt=vem.vehEm_legend_1)
          y = y+line_height
     if vem.vehEm_legend_2:
          pdf.text(10,y,txt=vem.vehEm_legend_2)
          y = y+line_height
     if vem.vehEm_legend_3:
          pdf.text(10,y,txt=vem.vehEm_legend_3)
          y = y+line_height
     if vem.vehEm_legend_4:
          pdf.text(10,y,txt=vem.vehEm_legend_4)
          y = y+line_height
     if vem.vehEm_legend_5:
          pdf.text(10,y,txt=vem.vehEm_legend_5)
          y = y+line_height
     if vem.vehEm_legend_7:
          pdf.text(10,y,txt=vem.vehEm_legend_7)
          y = y+line_height
     if vem.vehEm_legend_6:
          pdf.text(10,y,txt=vem.vehEm_legend_6)
          y = y+line_height
     if vem.vehEm_legend_8:
          pdf.text(10,y,txt=vem.vehEm_legend_8)
          y = y+line_height
     if vem.vehEm_legend_9:
          pdf.text(10,y,txt=vem.vehEm_legend_9)
          y = y+line_height
     if vem.vehEm_legend_10:
          pdf.text(10,y,txt=vem.vehEm_legend_10)
          y = y+line_height
     if vem.vehEm_legend_11:
          pdf.text(10,y,txt=vem.vehEm_legend_11)
          y = y+line_height
     if vem.vehEm_custom_legend:
          pdf.text(10,y,txt=vem.vehEm_custom_legend)
          y = y+line_height


     pdf.image(vem.vehEm_analyzedby,30,245,12,12)
     pdf.line(19,256,36+pdf.get_string_width("Analyzed By (Analyst)"),256)
     pdf.text(26,259,"Analyzed By (Analyst)")
     pdf.image(vem.vehEm_reviewedby,100,245,12,12)
     pdf.line(126,256,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),256)
     pdf.text(87.5,259,"Reviewed By (Assistant Manager)")
     pdf.image(vem.vehEm_approvedby,165,245,12,12)
     pdf.image(vem.vehEm_approvedby1,178,245,12,12)
     pdf.line(155,256,165+pdf.get_string_width("Approved By (Lab Manager)"),256)
     pdf.text(160,259,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,262,-10+pdf.w,262)
     pdf.text(10,266,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,271,txt="• Report is valid for current batch (sample).")
     pdf.text(10,274.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(275.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(279)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,263,19,15)
     if vem.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if vem.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if vem.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,263,19,15)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=vem.vehEm_doc_con1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=vem.vehEm_doc_con2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=vem.vehEm_doc_con3)







     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response

@login_required(login_url="/login")
def luxAnalysisList(request):
     luxAnalysis = LuxAnalysisForm.objects.all()
     context = {'data':luxAnalysis}
     return render(request,"luxAnalysisList.html",context)

@login_required(login_url="/login")
def luxAnalysisDelete(request,pk):
     luxAnalysis = LuxAnalysisForm.objects.get(id=pk)
     luxAnalysis.delete()
     return redirect('luxAnalysisList')

@login_required(login_url="/login")
def luxAnalysisEdit(request,pk):
     luxAnalysis = LuxAnalysisForm.objects.get(id=pk)
     context = {'data':luxAnalysis}
     return render(request,"luxAnalysisEdit.html",context)

@login_required(login_url="/login")
def luxAnalysisUpdate(request,pk):
     luxAnalysis = LuxAnalysisForm.objects.get(id=pk)
     if request.method == 'POST':
          luxAnalysis.location = request.POST['location']
          luxAnalysis.lux_lab_report_no = request.POST['lux_lab_rep_no']
          luxAnalysis.lux_invoice_no = request.POST['lux_invoice_no']
          luxAnalysis.lux_report_date = request.POST['lux_report_date']
          luxAnalysis.lux_report_to = request.POST['lux_report_to']
          luxAnalysis.lux_address = request.POST['lux-address']
          luxAnalysis.lux_attention = request.POST['lux_attention']
          luxAnalysis.lux_email = request.POST['lux_email']
          luxAnalysis.lux_testId = request.POST['lux_testId']
          luxAnalysis.lux_test_perf_date = request.POST['lux_test_perf_date']
          luxAnalysis.lux_test_type = request.POST['lux_test_type']
          luxAnalysis.lux_test_perfBy = request.POST['lux_test_perf_by']
          luxAnalysis.lux_test_desc = request.POST['lux_test_desc']
          luxAnalysis.lux_parameters_1 = request.POST['lux_parameters_1']
          luxAnalysis.lux_result_1 = request.POST['lux_result_1']
          luxAnalysis.lux_parameters_2 = request.POST['lux_parameters_2']
          luxAnalysis.lux_result_2 = request.POST['lux_result_2']
          luxAnalysis.lux_parameters_3 = request.POST['lux_parameters_3']
          luxAnalysis.lux_result_3 = request.POST['lux_result_3']
          luxAnalysis.lux_parameters_4 = request.POST['lux_parameters_4']
          luxAnalysis.lux_result_4 = request.POST['lux_result_4']
          luxAnalysis.lux_parameters_5 = request.POST['lux_parameters_5']
          luxAnalysis.lux_result_5 = request.POST['lux_result_5']
          luxAnalysis.lux_parameters_6 = request.POST['lux_parameters_6']
          luxAnalysis.lux_result_6 = request.POST['lux_result_6']
          luxAnalysis.lux_parameters_7 = request.POST['lux_parameters_7']
          luxAnalysis.lux_result_7 = request.POST['lux_result_7']
          luxAnalysis.lux_parameters_8 = request.POST['lux_parameters_8']
          luxAnalysis.lux_result_8 = request.POST['lux_result_8']
          luxAnalysis.lux_parameters_9 = request.POST['lux_parameters_9']
          luxAnalysis.lux_result_9 = request.POST['lux_result_9']
          luxAnalysis.lux_parameters_10 = request.POST['lux_parameters_10']
          luxAnalysis.lux_result_10 = request.POST['lux_result_10']
          luxAnalysis.lux_parameters_11 = request.POST['lux_parameters_11']
          luxAnalysis.lux_result_11 = request.POST['lux_result_11']
          luxAnalysis.lux_parameters_12 = request.POST['lux_parameters_12']
          luxAnalysis.lux_result_12 = request.POST['lux_result_12']
          luxAnalysis.lux_parameters_13 = request.POST['lux_parameters_13']
          luxAnalysis.lux_result_13 = request.POST['lux_result_13']
          luxAnalysis.lux_legend_1 = request.POST['lux-legend-1']
          luxAnalysis.lux_legend_2 = request.POST['lux-legend-2']
          luxAnalysis.lux_legend_3 = request.POST['lux-legend-3']
          luxAnalysis.lux_legend_4 = request.POST['lux-legend-4']
          luxAnalysis.lux_legend_5 = request.POST['lux-legend-5']
          luxAnalysis.lux_legend_6 = request.POST['lux-legend-6']
          luxAnalysis.lux_legend_7 = request.POST['lux-legend-7']
          luxAnalysis.lux_legend_8 = request.POST['lux-legend-8']
          luxAnalysis.lux_legend_9 = request.POST['lux-legend-9']
          luxAnalysis.lux_legend_10 = request.POST['lux-legend-10']
          luxAnalysis.lux_legend_11 = request.POST['lux-legend-11']
          luxAnalysis.lux_edit_note = request.POST['lux_edit_note']
          luxAnalysis.lux_custom_legend = request.POST['lux_custom_legend']
          luxAnalysis.lux_doc_con1 = request.POST['lux_doc_con1']
          luxAnalysis.lux_doc_con2 = request.POST['lux_doc_con2']
          luxAnalysis.lux_doc_con3 = request.POST['lux_doc_con3']
          luxAnalysis.lux_analyzedby = request.FILES['lux-analyzedby']
          luxAnalysis.lux_reviewedby = request.FILES['lux-reviewedby']
          luxAnalysis.lux_approvedby = request.FILES['lux-approvedby']
          luxAnalysis.lux_approvedby1 = request.FILES['lux-approvedby1']



          id = (LuxAnalysisForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f'/luxAnalysisReport/{str(id)}/'
               return redirect(to=url)
          if "submit" in request.POST:
               return redirect('luxAnalysisList')
     return render(request,"luxAnalysisList.html")


@login_required(login_url="/login")
def luxAnalysisView(request,pk):
     luxAnalysis = LuxAnalysisForm.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':luxAnalysis,'qr':'media/qr.png'}
     print(luxAnalysis.location)

     return render(request,'luxAnalysisReport.html',context)


@login_required(login_url="/login")
def luxAnalysisReportPdf(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,lux_lab_report_no,lux_invoice_no,lux_report_date,lux_address,lux_attention,lux_email,lux_testId,lux_test_perf_date,
                       lux_test_perfBy,lux_test_type,lux_test_desc,lux_report_to):
               super().__init__()
               self.lux_lab_report_no = lux_lab_report_no
               self.lux_invoice_no_number = lux_invoice_no
               self.lux_report_date = lux_report_date
               self.lux_address = lux_address
               self.lux_attention = lux_attention
               self.lux_email = lux_email
               self.lux_testId = lux_testId
               self.lux_test_perf_date = lux_test_perf_date
               self.lux_test_perfBy = lux_test_perfBy
               self.lux_test_type = lux_test_type
               self.lux_test_desc = lux_test_desc
               self.lux_report_to = lux_report_to



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.lux_lab_report_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.lux_invoice_no_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.lux_report_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.lux_report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.lux_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.lux_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.lux_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(89,82,txt="Test ID:")
               self.text(110,82,txt=self.lux_testId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(68.7,88,txt="Test Performed Date:")
               self.text(110,88,txt=self.lux_test_perf_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(75.2,94,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.lux_test_desc)

               self.line(105,78,105,108)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(84.8,100,txt="Test Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.lux_test_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72,106,txt="Test Performed By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.lux_test_perfBy)

               #table header
               self.rect(10,110.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,114.5,txt="Aanalytical Test Report")

               self.set_y(117)




     lux = LuxAnalysisForm.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Unit","Result"],
     ]
     sr_no = 1
     if lux.lux_result_1:
          a = [str(sr_no),lux.lux_parameters_1,"Lux(lx)",lux.lux_result_1]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_2:
          a = [str(sr_no),lux.lux_parameters_2,"Lux(lx)",lux.lux_result_2]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_3:
          a = [str(sr_no),lux.lux_parameters_3,"Lux(lx)",lux.lux_result_3]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_4:
          a = [str(sr_no),lux.lux_parameters_4,"Lux(lx)",lux.lux_result_4]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_5:
          a = [str(sr_no),lux.lux_parameters_5,"Lux(lx)",lux.lux_result_5]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_6:
          a = [str(sr_no),lux.lux_parameters_6,"Lux(lx)",lux.lux_result_6]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_7:
          a = [str(sr_no),lux.lux_parameters_7,"Lux(lx)",lux.lux_result_7]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_8:
          a = [str(sr_no),lux.lux_parameters_8,"Lux(lx)",lux.lux_result_8]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_9:
          a = [str(sr_no),lux.lux_parameters_9,"Lux(lx)",lux.lux_result_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_10:
          a = [str(sr_no),lux.lux_parameters_10,"Lux(lx)",lux.lux_result_10]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_11:
          a = [str(sr_no),lux.lux_parameters_11,"Lux(lx)",lux.lux_result_11]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_12:
          a = [str(sr_no),lux.lux_parameters_12,"Lux(lx)",lux.lux_result_12]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if lux.lux_result_13:
          a = [str(sr_no),lux.lux_parameters_13,"Lux(lx)",lux.lux_result_13]
          sr_no = sr_no+1
          TABLE_DATA.append(a)






     pdf = PDFWithPageNumbers(lux_lab_report_no=lux.lux_lab_report_no,lux_invoice_no=lux.lux_invoice_no,lux_report_date=lux.lux_report_date,lux_report_to=lux.lux_report_to,
                              lux_address=lux.lux_address,lux_attention=lux.lux_attention,lux_email=lux.lux_email,lux_testId=lux.lux_testId,lux_test_perf_date=lux.lux_test_perf_date,
                              lux_test_desc=lux.lux_test_desc,lux_test_type=lux.lux_test_type,lux_test_perfBy=lux.lux_test_perfBy,

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     with pdf.table(col_widths=(10, 50, 30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               # if k == 0:
               #      data_row[4] = lux.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table

     Table_Data1 = [
          
     ]
     if lux.lux_edit_note:
          a=["Note :"+lux.lux_edit_note] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if lux.lux_legend_1:
          a = [lux.lux_legend_1]
          Table_data_legend.append(a)
          
     if lux.lux_legend_2:
          a = [lux.lux_legend_2]
          Table_data_legend.append(a)
          
     if lux.lux_legend_3:
          a = [lux.lux_legend_3]
          Table_data_legend.append(a)
          
     if lux.lux_legend_4:
          a = [lux.lux_legend_4]
          Table_data_legend.append(a)
          
     if lux.lux_legend_5:
          a = [lux.lux_legend_5]
          Table_data_legend.append(a)
          
     if lux.lux_legend_6:
          a = [lux.lux_legend_6]
          Table_data_legend.append(a)
          
     if lux.lux_legend_7:
          a = [lux.lux_legend_7]
          Table_data_legend.append(a)
          
     if lux.lux_legend_8:
          a = [lux.lux_legend_8]
          Table_data_legend.append(a)
          
     if lux.lux_legend_9:
          a = [lux.lux_legend_9]
          Table_data_legend.append(a)
          
     if lux.lux_legend_10:
          a = [lux.lux_legend_10]
          Table_data_legend.append(a)
          
     if lux.lux_legend_11:
          a = [lux.lux_legend_11]
          Table_data_legend.append(a)
          

     if lux.lux_custom_legend:
          a = [lux.lux_custom_legend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')

     # if lux.lux_edit_note:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,205,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(202.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=lux.lux_edit_note)
     # line_height = 4
     # y = 212
     # if lux.lux_legend_1:
     #      pdf.text(10,y,txt=lux.lux_legend_1)
     #      y = y+line_height
     # if lux.lux_legend_2:
     #      pdf.text(10,y,txt=lux.lux_legend_2)
     #      y = y+line_height
     # if lux.lux_legend_3:
     #      pdf.text(10,y,txt=lux.lux_legend_3)
     #      y = y+line_height
     # if lux.lux_legend_4:
     #      pdf.text(10,y,txt=lux.lux_legend_4)
     #      y = y+line_height
     # if lux.lux_legend_5:
     #      pdf.text(10,y,txt=lux.lux_legend_5)
     #      y = y+line_height
     # if lux.lux_legend_7:
     #      pdf.text(10,y,txt=lux.lux_legend_7)
     #      y = y+line_height
     # if lux.lux_legend_6:
     #      pdf.text(10,y,txt=lux.lux_legend_6)
     #      y = y+line_height
     # if lux.lux_legend_8:
     #      pdf.text(10,y,txt=lux.lux_legend_8)
     #      y = y+line_height
     # if lux.lux_legend_9:
     #      pdf.text(10,y,txt=lux.lux_legend_9)
     #      y = y+line_height
     # if lux.lux_legend_10:
     #      pdf.text(10,y,txt=lux.lux_legend_10)
     #      y = y+line_height
     # if lux.lux_legend_11:
     #      pdf.text(10,y,txt=lux.lux_legend_11)
     #      y = y+line_height
     # if lux.lux_custom_legend:
     #      pdf.text(10,y,txt=lux.lux_custom_legend)
     #      y = y+line_height


     pdf.image(lux.lux_analyzedby,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(lux.lux_reviewedby,100,250,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(lux.lux_approvedby,165,250,12,12)
     pdf.image(lux.lux_approvedby1,178,250,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if lux.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if lux.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if lux.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=lux.lux_doc_con1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=lux.lux_doc_con2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=lux.lux_doc_con3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response

@login_required(login_url="/login")
def packingPolyBagList(request):
     ppb = PackingPolyBagForm.objects.all()
     context ={'data':ppb}
     return render(request,"packingPolyBagList.html",context)

@login_required(login_url="/login")
def  packingPolyBagDelete(request,pk):
     ppb = PackingPolyBagForm.objects.get(id=pk)
     ppb.delete()
     return redirect(to="packingPolyBagList")

@login_required(login_url="/login")
def packingPolyBagEdit(request,pk):
     ppb = PackingPolyBagForm.objects.get(id=pk)
     context = {"data":ppb}
     return render(request,"packingPolyBagEdit.html",context)

@login_required(login_url="/login")
def packingPolyBagUpdate(request,pk):
     ppb = PackingPolyBagForm.objects.get(id=pk)
     if request.method == 'POST':
          ppb.location = request.POST['location']
          ppb.pack_lab_rep_no = request.POST['pack_lab_rep_no']
          ppb.pack_invoice = request.POST['pack_invoice']
          ppb.pack_rep_date = request.POST['pack_rep_date']
          ppb.pack_rep_to = request.POST['pack_rep_to']
          ppb.pack_address = request.POST['pack_address']
          ppb.pack_attention = request.POST['pack_attention']
          ppb.pack_email = request.POST['pack_email']
          ppb.pack_sampleId = request.POST['pack_sampleId']
          ppb.pack_sample_colc_date = request.POST['pack_sample_colc_date']
          ppb.pack_sample_desc = request.POST['pack_sample_desc']
          ppb.pack_sample_type = request.POST['pack_sample_type']
          ppb.pack_sample_colc_by = request.POST['pack_sample_colc_by']
          ppb.pack_test_desc = request.POST['pack_test_desc']
          ppb.pack_sr1 = request.POST['pack_sr1']
          ppb.pack_legend_1 = request.POST['pack-legend-1']
          ppb.pack_edit_note = request.POST['pack_edit_note']
          ppb.pack_custom_legend = request.POST['pack_custom_legend']
          ppb.doc_con1 = request.POST['doc_con1']
          ppb.doc_con2 = request.POST['doc_con2']
          ppb.doc_con3 = request.POST['doc_con3']
          ppb.pack_analyzed_by = request.FILES['pack-analyzedby']
          ppb.pack_reviewed_by = request.FILES['pack-reviewedby']
          ppb.pack_approved_by = request.FILES['pack-approvedby']
          ppb.pack_approved_by1 = request.FILES['pack-approvedby1']

          ppb.save()
          id = (PackingPolyBagForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f'/packingpolybag-view/{str(id)}/'
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect('packingPolyBagList')
     return render(request,"packingPolyBagList.html")
     #      if "update_and_view" in request.POST:
     #           url = f'/PackingPoly-view/{str(id)}/'
     #           return redirect(to=url)
     #      else:
     #           return redirect("packingPolyBagList")
     # return render(request,"packingPolyBagList.html")


@login_required(login_url="/login")
def packingPolyBagView(request,pk):
     ppb = PackingPolyBagForm.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':ppb,'qr':'media/qr.png'}

     return render(request,'packingPolyBagReport.html',context)



@login_required(login_url="/login")
def packingPolyBagReport(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,pack_lab_rep_no,pack_invoice,pack_rep_date,pack_address,pack_attention,pack_email,pack_sampleId,pack_sample_colc_date,
                       pack_sample_colc_by,pack_sample_type,pack_test_desc,pack_rep_to):
               super().__init__()
               self.pack_lab_rep_no = pack_lab_rep_no
               self.pack_invoice_number = pack_invoice
               self.pack_rep_date = pack_rep_date
               self.pack_address = pack_address
               self.pack_attention = pack_attention
               self.pack_email = pack_email
               self.pack_sampleId = pack_sampleId
               self.pack_sample_colc_date = pack_sample_colc_date
               self.pack_sample_colc_by = pack_sample_colc_by
               self.pack_sample_type = pack_sample_type
               self.pack_test_desc = pack_test_desc
               self.pack_rep_to = pack_rep_to



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.pack_lab_rep_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.pack_invoice_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.pack_rep_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.pack_rep_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.pack_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.pack_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.pack_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(89,82,txt="Sample ID:")
               self.text(110,82,txt=self.pack_sampleId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(68.7,88,txt="Sample Collected Date:")
               self.text(110,88,txt=self.pack_sample_colc_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(75.2,94,txt="Sample Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.pack_test_desc)

               self.line(105,78,105,114)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(84.8,100,txt="sample Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.pack_sample_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72,106,txt="sample Collected By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.pack_sample_colc_by)


               self.rect(10,108,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72,112,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.pack_sample_colc_by)

               #table header
               self.rect(10,118.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,122,txt="Aanalytical Test Report")

               self.set_y(125.2)




     pack = PackingPolyBagForm.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Methods","Unit","Result"],
     ]
     sr_no = 1
     if pack.pack_sr1:
          a = [str(sr_no),"PVC Content","Beilstein","-",pack.pack_sr1]
          sr_no = sr_no+1
          TABLE_DATA.append(a)



     pdf = PDFWithPageNumbers(pack_lab_rep_no=pack.pack_lab_rep_no,pack_invoice=pack.pack_invoice,pack_rep_date=pack.pack_rep_date,pack_rep_to=pack.pack_rep_to,
                              pack_address=pack.pack_address,pack_attention=pack.pack_attention,pack_email=pack.pack_email,pack_sampleId=pack.pack_sampleId,pack_sample_colc_date=pack.pack_sample_colc_date,
                              pack_test_desc=pack.pack_test_desc,pack_sample_type=pack.pack_sample_type,pack_sample_colc_by=pack.pack_sample_colc_by,

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     with pdf.table(col_widths=(10, 50, 30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               # if k == 0:
               #      data_row[4] = pack.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table

     if pack.pack_edit_note:
          pdf.set_font("Calibri","B", 10)
          pdf.text(10,141,txt="Note:")
          pdf.set_font("Calibri","", 8)
          pdf.set_y(138.5)
          pdf.set_x(20)
          pdf.multi_cell(182,txt=pack.pack_edit_note)
     line_height = 4
     y = 150
     if pack.pack_legend_1:
          pdf.text(10,y,txt=pack.pack_legend_1)
          y = y+line_height
     if pack.pack_custom_legend:
          pdf.text(10,y,txt=pack.pack_custom_legend)
          y = y+line_height


     pdf.image(pack.pack_analyzed_by,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(pack.pack_reviewed_by,100,250,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(pack.pack_approved_by,165,250,12,12)
     pdf.image(pack.pack_approved_by1,178,250,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if pack.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if pack.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if pack.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=pack.doc_con1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=pack.doc_con2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=pack.doc_con3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response


@login_required(login_url="/login")
def noiseAnalysisList(request):
     nA = NoiseAnalysis.objects.all()
     context = {'data':nA}
     return render(request,"noiseAnalysisList.html",context)


@login_required(login_url="/login")
def noiseAnalysisDelete(request,pk):
     nA = NoiseAnalysis.objects.get(id=pk)
     nA.delete()
     return redirect("noiseAnalysisList")


@login_required(login_url="/login")
def noiseAnalysisEdit(request,pk):
     nA = NoiseAnalysis.objects.get(id=pk)
     context = {'data':nA}
     return render(request,"noiseAnalysisEdit.html",context)


@login_required(login_url="/login")
def noiseAnalysisUpdate(request,pk):
     nA = NoiseAnalysis.objects.get(id=pk)
     if request.method == 'POST':
          location = request.POST['location']
          nA.lab_rep_no = request.POST['lab_rep_no']
          nA.invoice_no = request.POST['invoice_no']
          nA.rep_date = request.POST['rep_date']
          nA.report_to = request.POST['report_to']
          nA.address = request.POST['address']
          nA.attention = request.POST['attention']
          nA.email = request.POST['email']
          nA.testId = request.POST['testId']
          nA.test_perf_date = request.POST['test_perf_date']
          nA.test_type = request.POST['test_type']
          nA.test_perf_by = request.POST['test_perf_by']
          nA.test_desc = request.POST['test_desc']
          nA.select = request.POST.get('select')
          nA.select1 = request.POST.get('select1')
          nA.r1 = request.POST['r1']
          nA.r1_1 = request.POST['r1_1']
          nA.r2 = request.POST['r2']
          nA.r2_2 = request.POST['r2_2']
          nA.r3 = request.POST['r3']
          nA.r3_3 = request.POST['r3_3']
          nA.r4 = request.POST['r4']
          nA.r4_4 = request.POST['r4_4']
          nA.r5 = request.POST['r5']
          nA.r5_5 = request.POST['r5_5']
          nA.r6 = request.POST['r6']
          nA.r6_6 = request.POST['r6_6']
          nA.r7 = request.POST['r7']
          nA.r7_7 = request.POST['r7_7']
          nA.r8 = request.POST['r8']
          nA.r8_8 = request.POST['r8_8']
          nA.r9 = request.POST['r9']
          nA.r9_9 = request.POST['r9_9']
          nA.r10 = request.POST['r10']
          nA.r10_10 = request.POST['r10_10']
          nA.r11 = request.POST['r11']
          nA.r11_11 = request.POST['r11_11']
          nA.r12 = request.POST['r12']
          nA.r12_12 = request.POST['r12_12']
          nA.r13 = request.POST['r13']
          nA.r13_13 = request.POST['r13_13']
          nA.legend_1 = request.POST['legend_1']
          nA.legend_2 = request.POST['legend_2']
          nA.legend_3 = request.POST['legend_3']
          nA.legend_4 = request.POST['legend_4']
          nA.legend_5 = request.POST['legend_5']
          nA.legend_6 = request.POST['legend_6']
          nA.legend_7 = request.POST['legend_7']
          nA.legend_8 = request.POST['legend_8']
          nA.legend_9 = request.POST['legend_9']
          nA.legend_10 = request.POST['legend_10']
          nA.legend_11 = request.POST['legend_11']
          nA.editNote = request.POST['editNote']
          nA.customlegend = request.POST['customlegend']
          nA.doc1 = request.POST['doc1']
          nA.doc2 = request.POST['doc2']
          nA.doc3 = request.POST['doc3']
          nA.analyzedby = request.FILES['analyzedby']
          nA.reviewedby = request.FILES['reviewedby']
          nA.approvedby = request.FILES['approvedby']
          nA.approvedby1 = request.FILES['approvedby1']




          nA.save()
          id = (NoiseAnalysis.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/noiseAnalysis-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="noiseAnalysisList")
     return render(request,"noiseAnalysisList.html")


@login_required(login_url="/login")
def noiseAnalysisView(request,pk):
     nA = NoiseAnalysis.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':nA,'qr':'media/qr.png'}

     return render(request,'noiseAnalysisReport.html',context)


@login_required(login_url="/login")
def noiseAnalysisReport(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,lab_rep_no,invoice_no,rep_date,address,attention,email,testId,test_perf_date,
                       test_perf_by,test_type,test_desc,report_to,select1):
               super().__init__()
               self.lab_rep_no = lab_rep_no
               self.invoice_no = invoice_no
               self.rep_date = rep_date
               self.address = address
               self.attention = attention
               self.email = email
               self.testId = testId
               self.test_perf_date = test_perf_date
               self.test_perf_by = test_perf_by
               self.test_type = test_type
               self.test_desc = test_desc
               self.report_to = report_to
               self.select1 = select1



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.lab_rep_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.invoice_no)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.rep_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(89,82,txt="Test ID:")
               self.text(110,82,txt=self.testId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(68.7,88,txt="Test Performed Date:")
               self.text(110,88,txt=self.test_perf_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(92.8,94,txt="Test:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.test_type)

               self.line(105,78,105,108)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72,100,txt="Test Performed By:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.test_perf_by)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(90.5,106,txt="Types:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.select1)

               #table header
               self.rect(10,110.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,114.5,txt="Aanalytical Test Report")

               self.set_y(117)




     nA= NoiseAnalysis.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Methods","Unit","Result",""],
     ]
     sr_no = 1
     if nA.r1 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r1 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r1 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r1 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r1 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r1 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r1 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r1 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r1,"ASTM E1686-16","dB",nA.r1_1,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     if nA.r2 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r2 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r2 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r2 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r2 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r2 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r2 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r2 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r2,"ASTM E1686-16","dB",nA.r2_2,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r3 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r3 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r3 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r3 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r3 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r3 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r3 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r3 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r3,"ASTM E1686-16","dB",nA.r3_3,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r4 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r4 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r4 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r4 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r4 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r4 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r4 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r4 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r4,"ASTM E1686-16","dB",nA.r4_4,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r5 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r5 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r5 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r5 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r5 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r5 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r5 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r5 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r5,"ASTM E1686-16","dB",nA.r5_5,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r6 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r6 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r6 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r6 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r6 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r6 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r6 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r6 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r6,"ASTM E1686-16","dB",nA.r6_6,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r7 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r7 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r7 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r7 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r7 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r7 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r7 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r7 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r7,"ASTM E1686-16","dB",nA.r7_7,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r8 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r8 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r8 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r8 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r8 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r8 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r8 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r8 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r8,"ASTM E1686-16","dB",nA.r8_8,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r9 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r9 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r9 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r9 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r9 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r9 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r9 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r9 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r9,"ASTM E1686-16","dB",nA.r9_9,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r10 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r10 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r10 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r10 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r10 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r10 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r10 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r10 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r10,"ASTM E1686-16","dB",nA.r10_10,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r11 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r11 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r11 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r11 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r11 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r11 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r11 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r11 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r11,"ASTM E1686-16","dB",nA.r11_11,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r12 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r12 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r12 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r12 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r12 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r12 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r12 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r12 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r12,"ASTM E1686-16","dB",nA.r12_12,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if nA.r13 and nA.select1 == "Residential Day":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"65"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r13 and nA.select1 =="Residential Night":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r13 and nA.select1 =="Commercial Day":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"70"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r13 and nA.select1 =="Commercial Night":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"60"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r13 and nA.select1 =="Industrial Day":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r13 and nA.select1 =="Industrial Night":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"75"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r13 and nA.select1 =="Silence Day":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"55"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif nA.r13 and nA.select1 =="Silence Night":
          a = [str(sr_no),nA.r13,"ASTM E1686-16","dB",nA.r13_13,"45"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)








     pdf = PDFWithPageNumbers(lab_rep_no=nA.lab_rep_no,invoice_no=nA.invoice_no,rep_date=nA.rep_date,report_to=nA.report_to,
                              address=nA.address,attention=nA.attention,email=nA.email,testId=nA.testId,test_perf_date=nA.test_perf_date,
                              test_desc=nA.test_desc,test_type=nA.test_type,test_perf_by=nA.test_perf_by,select1=nA.select1

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     with pdf.table(col_widths=(10, 50, 30,30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               if k == 0:
                    data_row[5] = nA.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table
     Table_Data1 = [
          
     ]
     if nA.editNote:
          a=["Note :"+nA.editNote] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if nA.legend_1:
          a = [nA.legend_1]
          Table_data_legend.append(a)
          
     if nA.legend_2:
          a = [nA.legend_2]
          Table_data_legend.append(a)
          
     if nA.legend_3:
          a = [nA.legend_3]
          Table_data_legend.append(a)
          
     if nA.legend_4:
          a = [nA.legend_4]
          Table_data_legend.append(a)
          
     if nA.legend_5:
          a = [nA.legend_5]
          Table_data_legend.append(a)
          
     if nA.legend_6:
          a = [nA.legend_6]
          Table_data_legend.append(a)
          
     if nA.legend_7:
          a = [nA.legend_7]
          Table_data_legend.append(a)
          
     if nA.legend_8:
          a = [nA.legend_8]
          Table_data_legend.append(a)
          
     if nA.legend_9:
          a = [nA.legend_9]
          Table_data_legend.append(a)
          
     if nA.legend_10:
          a = [nA.legend_10]
          Table_data_legend.append(a)
          
     if nA.legend_11:
          a = [nA.legend_11]
          Table_data_legend.append(a)
          

     if nA.customlegend:
          a = [nA.customlegend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')


     # if nA.editNote:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,205,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(202.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=nA.editNote)
     # line_height = 4
     # y = 212
     # if nA.legend_1:
     #      pdf.text(10,y,txt=nA.legend_1)
     #      y = y+line_height
     # if nA.legend_2:
     #      pdf.text(10,y,txt=nA.legend_2)
     #      y = y+line_height
     # if nA.legend_3:
     #      pdf.text(10,y,txt=nA.legend_3)
     #      y = y+line_height
     # if nA.legend_4:
     #      pdf.text(10,y,txt=nA.legend_4)
     #      y = y+line_height
     # if nA.legend_5:
     #      pdf.text(10,y,txt=nA.legend_5)
     #      y = y+line_height
     # if nA.legend_7:
     #      pdf.text(10,y,txt=nA.legend_7)
     #      y = y+line_height
     # if nA.legend_6:
     #      pdf.text(10,y,txt=nA.legend_6)
     #      y = y+line_height
     # if nA.legend_8:
     #      pdf.text(10,y,txt=nA.legend_8)
     #      y = y+line_height
     # if nA.legend_9:
     #      pdf.text(10,y,txt=nA.legend_9)
     #      y = y+line_height
     # if nA.legend_10:
     #      pdf.text(10,y,txt=nA.legend_10)
     #      y = y+line_height
     # if nA.legend_11:
     #      pdf.text(10,y,txt=nA.legend_11)
     #      y = y+line_height
     # if nA.customlegend:
     #      pdf.text(10,y,txt=nA.customlegend)
     #      y = y+line_height


     pdf.image(nA.analyzedby,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(nA.reviewedby,100,250,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(nA.approvedby,165,249,12,12)
     pdf.image(nA.approvedby1,178,249,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if nA.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if nA.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if nA.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=nA.doc1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=nA.doc2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=nA.doc3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response

@login_required(login_url="/login")
def machineOilList(request):
     machineOil = MachineOilForm.objects.all()
     context = {'data':machineOil}
     return render(request,"machineOilList.html",context)

@login_required(login_url="/login")
def machineOilDelete(request,pk):
     machineOil= MachineOilForm.objects.get(id=pk)
     machineOil.delete()
     return redirect("machineOilList")

@login_required(login_url="/login")
def machineOilEdit(request,pk):
     machineOil =  MachineOilForm.objects.get(id=pk)
     context = {'data':machineOil}
     return render(request,"machineOilEdit.html",context)

@login_required(login_url="/login")
def machineOilUpdate(request,pk):
     machineOil = MachineOilForm.objects.get(id=pk)
     if request.method == 'POST':
          location = request.POST['location']
          machineOil.machine_lab_rep_no = request.POST['machine_lab_rep_no']
          machineOil.machine_invoice_no = request.POST['machine_invoice_no']
          machineOil.machine_rep_date = request.POST['machine_rep_date']
          machineOil.machine_report_to = request.POST['machine_report_to']
          machineOil.machine_address = request.POST['machine_address']
          machineOil.machine_attention = request.POST['machine_attention']
          machineOil.machine_email = request.POST['machine_email']
          machineOil.machine_sampleId = request.POST['machine_sampleId']
          machineOil.machine_sample_col_date = request.POST['machine_sample_col_date']
          machineOil.machine_sample_desc = request.POST['machine_sample_desc']
          machineOil.machine_sample_type = request.POST['machine_sample_type']
          machineOil.machine_sample_col_by = request.POST['machine_sample_col_by']
          machineOil.machine_test_desc = request.POST['machine_test_desc']
          machineOil.machine_sr1 = request.POST['machine_sr1']
          machineOil.machine_sr2 = request.POST['machine_sr2']
          machineOil.machine_sr3 = request.POST['machine_sr3']
          machineOil.machine_sr4 = request.POST['machine_sr4']
          machineOil.machine_sr5 = request.POST['machine_sr5']
          machineOil.machine_sr6 = request.POST['machine_sr6']
          machineOil.machine_sr7 = request.POST['machine_sr7']
          machineOil.machine_sr8 = request.POST['machine_sr8']
          machineOil.machine_sr9 = request.POST['machine_sr9']
          machineOil.machine_sr10 = request.POST['machine_sr10']
          machineOil.machine_sr11 = request.POST['machine_sr11']
          machineOil.machine_sr12 = request.POST['machine_sr12']
          machineOil.machine_sr13 = request.POST['machine_sr13']
          machineOil.machine_sr14 = request.POST['machine_sr14']
          machineOil.machine_sr15 = request.POST['machine_sr15']
          machineOil.machine_sr16 = request.POST['machine_sr16']
          machineOil.machine_legend_1 = request.POST['machine_legend-1']
          machineOil.machine_legend_2 = request.POST['machine_legend-2']
          machineOil.custom_legend = request.POST['custom_legend']
          machineOil.machine_edit_note = request.POST['machine_edit_note']
          machineOil.machine_custom_legend = request.POST['machine_custom_legend']
          machineOil.machine_doc1 = request.POST['machine_doc1']
          machineOil.machine_doc2 = request.POST['machine_doc2']
          machineOil.machine_doc3 = request.POST['machine_doc3']
          machineOil.machine_analyzedby = request.FILES['machine_analyzedby']
          machineOil.machine_reviewedby = request.FILES['machine_reviewedby']
          machineOil.machine_approvedby = request.FILES['machine_approvedby']
          machineOil.machine_approvedby1 = request.FILES['machine_approvedby']


          machineOil.save()
          id = (MachineOilForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/machineOil-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="machineOilList")


     return render(request,"machineOil.html")

@login_required(login_url="/login")
def machineOilView(request,pk):
     machineOil = MachineOilForm.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':machineOil,'qr':'media/qr.png'}

     return render(request,'machineOilReport.html',context)

@login_required(login_url="/login")
def machineOilReportPdf(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,machine_lab_rep_no,machine_invoice_no,machine_rep_date,machine_address,machine_attention,machine_email,machine_sampleId,machine_sample_col_date,
                       machine_sample_col_by,machine_sample_type,machine_sample_desc,machine_report_to,machine_test_desc):
               super().__init__()
               self.machine_lab_rep_no = machine_lab_rep_no
               self.machine_invoice_no_number = machine_invoice_no
               self.machine_rep_date = machine_rep_date
               self.machine_address = machine_address
               self.machine_attention = machine_attention
               self.machine_email = machine_email
               self.machine_sampleId = machine_sampleId
               self.machine_sample_col_date = machine_sample_col_date
               self.machine_sample_col_by = machine_sample_col_by
               self.machine_sample_type = machine_sample_type
               self.machine_sample_desc = machine_sample_desc
               self.machine_report_to = machine_report_to
               self.machine_test_desc = machine_test_desc



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.machine_lab_rep_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.machine_invoice_no_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.machine_rep_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.machine_report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.machine_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.machine_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.machine_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(86,82,txt="sample ID:")
               self.text(110,82,txt=self.machine_sampleId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(65.7,88,txt="sample Performed Date:")
               self.text(110,88,txt=self.machine_sample_col_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72.2,94,txt="sample Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.machine_sample_desc)

               self.line(105,78,105,114)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(81.8,100,txt="sample Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.machine_sample_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(70.5,106,txt="Sample Collected By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.machine_sample_col_by)

               self.rect(10,108,190,6)
               self.set_font("Calibri","B", 10)
               self.text(76.5,112,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.machine_test_desc)
               #table header
               self.rect(10,117.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,121.5,txt="Aanalytical Test Report")

               self.set_y(124)




     machine = MachineOilForm.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Methods","Unit","Result","GOAT Limits"],
     ]
     sr_no = 1
     if machine.machine_sr1:
          a = [str(sr_no),"Antimony (Sb)","ASTM D-5185","mg/L",machine.machine_sr1,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr2:
          a = [str(sr_no),"Arsenic (As)","ASTM D-5185","mg/L",machine.machine_sr2,"50"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr3:
          a = [str(sr_no),"Barium (Ba)","ASTM D-5185","mg/L",machine.machine_sr3,"100"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr4:
          a = [str(sr_no),"Cadmium (Cd)","ASTM D-5185","mg/L",machine.machine_sr4,"20"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr5:
          a = [str(sr_no),"Cobalt (Co)","ASTM D-5185","mg/L",machine.machine_sr5,"500"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr6:
          a = [str(sr_no),"Copper (Cu)","ASTM D-5185","mg/L",machine.machine_sr6,"250"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr7:
          a = [str(sr_no),"Chromium (Cr)","ASTM D-5185","mg/L",machine.machine_sr7,"100"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr8:
          a = [str(sr_no),"Iron (Fe)","ASTM D-5185","mg/L",machine.machine_sr8,"2500"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr9:
          a = [str(sr_no),"Lead (Pb)","ASTM D-5185","mg/L",machine.machine_sr9,"100"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr10:
          a = [str(sr_no),"Magnese (Mn)","ASTM D-5185","mg/L",machine.machine_sr10,"1000"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr11:
          a = [str(sr_no),"Nickel (Ni)","ASTM D-5185","mg/L",machine.machine_sr11,"200"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr12:
          a = [str(sr_no),"Mercury (Hg)","ASTM D7622","mg/L",machine.machine_sr12,"04"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr13:
          a = [str(sr_no),"Selenium (Se)","ASTM D-5185","mg/L",machine.machine_sr13,"20"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if machine.machine_sr14:
          a = [str(sr_no),"Silver (Ag)","ASTM D-5185","mg/L",machine.machine_sr14,"100"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)






     pdf = PDFWithPageNumbers(machine_lab_rep_no=machine.machine_lab_rep_no,machine_invoice_no=machine.machine_invoice_no,machine_rep_date=machine.machine_rep_date,machine_report_to=machine.machine_report_to,
                              machine_address=machine.machine_address,machine_attention=machine.machine_attention,machine_email=machine.machine_email,machine_sampleId=machine.machine_sampleId,machine_sample_col_date=machine.machine_sample_col_date,
                              machine_sample_desc=machine.machine_sample_desc,machine_sample_type=machine.machine_sample_type,machine_sample_col_by=machine.machine_sample_col_by,machine_test_desc = machine.machine_test_desc

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     with pdf.table(col_widths=(10, 50, 30,30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               # if k == 0:
               #      data_row[4] = machine.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table


     Table_Data1 = [
          
     ]
     if machine.machine_edit_note:
          a=["Note :"+machine.machine_edit_note] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if machine.machine_legend_1:
          a = [machine.machine_legend_1]
          Table_data_legend.append(a)
          
     if machine.machine_legend_2:
          a = [machine.machine_legend_2]
          Table_data_legend.append(a)

     if machine.custom_legend:
          a = [machine.custom_legend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')
     # if machine.machine_edit_note:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,217,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(214.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=machine.machine_edit_note)
     # line_height = 4
     # y = 224
     # if machine.machine_legend_1:
     #      pdf.text(10,y,txt=machine.machine_legend_1)
     #      y = y+line_height
     # if machine.machine_legend_2:
     #      pdf.text(10,y,txt=machine.machine_legend_2)
     #      y = y+line_height

     # if machine.machine_custom_legend:
     #      pdf.text(10,y,txt=machine.machine_custom_legend)
     #      y = y+line_height


     pdf.image(machine.machine_analyzedby,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(machine.machine_reviewedby,100,250,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(machine.machine_approvedby,165,249,12,12)
     pdf.image(machine.machine_approvedby1,178,249,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if machine.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if machine.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if machine.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=machine.machine_doc1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=machine.machine_doc2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=machine.machine_doc3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response


@login_required(login_url="/login")
def microbialList(request):
     mba = MicrobialAnalysis.objects.all()
     context ={"data":mba}
     return render(request,"microbialAnalysisList.html",context)

@login_required(login_url="/login")
def microbialDelete(request,pk):
     mba = MicrobialAnalysis.objects.get(id=pk)
     mba.delete()
     return redirect("microbialList")

@login_required(login_url="/login")
def microbialEdit(request,pk):
     mba = MicrobialAnalysis.objects.get(id=pk)
     context ={"data":mba}
     return render(request,"microbialEdit.html",context)

@login_required(login_url="/login")
def microbialUpdate(request,pk):
     mba = MicrobialAnalysis.objects.get(id=pk)
     if request.method == 'POST':
          location = request.POST['location']
          mba.micro_lab_report_no = request.POST['micro_lab_report_no']
          mba.micro_invoice_bill = request.POST['micro_invoice_bill']
          mba.micro_rep_date = request.POST['micro_rep_date']
          mba.micro_rep_to = request.POST['micro_rep_to']
          mba.micro_address = request.POST['micro_address']
          mba.micro_attention = request.POST['micro_attention']
          mba.micro_email = request.POST['micro_email']
          mba.micro_sampleId = request.POST['micro_sampleId']
          mba.micro_sample_col_date = request.POST['micro_sample_col_date']
          mba.micro_sample_desc = request.POST['micro_sample_desc']
          mba.micro_sample_type = request.POST['micro_sample_type']
          mba.micro_sample_col_by = request.POST['micro_sample_col_date']
          mba.micro_date_analysis = request.POST['micro_date_analysis']
          mba.micro_test_desc = request.POST['micro_test_desc']
          mba.micro_sr1 = request.POST['micro_sr1']
          mba.micro_sr2 = request.POST['micro_sr2']
          mba.micro_sr3 = request.POST['micro_sr3']
          mba.micro_sr4 = request.POST['micro_sr4']
          mba.micro_sr5 = request.POST['micro_sr5']
          mba.micro_sr6 = request.POST['micro_sr6']
          mba.micro_legend_1 = request.POST['micro_legend_1']
          mba.micro_legend_2 = request.POST['micro_legend_2']
          mba.micro_editnote = request.POST['micro_editnote']
          mba.micro_custom_legend = request.POST['micro_custom_legend']
          mba.micro_doc1 = request.POST['micro_doc1']
          mba.micro_doc2 = request.POST['micro_doc2']
          mba.micro_doc3 = request.POST['micro_doc3']
          mba.micro_analyzedby = request.FILES['micro_analyzedby']
          mba.micro_reviewedby = request.FILES['micro_reviewedby']
          mba.micro_approvedby = request.FILES['micro_approvedby']
          mba.micro_approvedby1 = request.FILES['micro_approvedby1']

          mba.save()
          id = (MachineOilForm.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/microbial-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="microbialList")
     return render(request,"microbialAnalysisList.html")


@login_required(login_url="/login")
def microbialView(request,pk):
     mba = MicrobialAnalysis.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data': mba,'qr':'media/qr.png'}

     return render(request,'microbialReport.html',context)


@login_required(login_url="/login")
def microbialAnalysisPdf(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,micro_lab_report_no,micro_invoice_bill,micro_rep_date,micro_address,micro_attention,micro_email,micro_sampleId,micro_sample_col_date,
                       micro_sample_col_by,micro_sample_type,micro_sample_desc,micro_rep_to,micro_test_desc):
               super().__init__()
               self.micro_lab_report_no = micro_lab_report_no
               self.micro_invoice_bill_number = micro_invoice_bill
               self.micro_rep_date = micro_rep_date
               self.micro_address = micro_address
               self.micro_attention = micro_attention
               self.micro_email = micro_email
               self.micro_sampleId = micro_sampleId
               self.micro_sample_col_date = micro_sample_col_date
               self.micro_sample_col_by = micro_sample_col_by
               self.micro_sample_type = micro_sample_type
               self.micro_sample_desc = micro_sample_desc
               self.micro_rep_to = micro_rep_to
               self.micro_test_desc = micro_test_desc



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.micro_lab_report_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.micro_invoice_bill_number)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.micro_rep_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.micro_rep_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.micro_address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.micro_attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.micro_email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(86,82,txt="sample ID:")
               self.text(110,82,txt=self.micro_sampleId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(65.7,88,txt="sample Performed Date:")
               self.text(110,88,txt=self.micro_sample_col_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72.2,94,txt="sample Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.micro_sample_desc)

               self.line(105,78,105,114)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(81.8,100,txt="sample Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.micro_sample_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(70.5,106,txt="Sample Collected By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.micro_sample_col_by)

               self.rect(10,108,190,6)
               self.set_font("Calibri","B", 10)
               self.text(76.5,112,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.micro_test_desc)
               #table header
               self.rect(10,117.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,121.5,txt="Aanalytical Test Report")

               self.set_y(124)




     micro = MicrobialAnalysis.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Unit","Result"],
     ]
     sr_no = 1
     if micro.micro_sr1:
          a = [str(sr_no),"Total Colony Count","CFU/ml",micro.micro_sr1]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if micro.micro_sr2:
          a = [str(sr_no),"Total Coliform","CFU/ml",micro.micro_sr2]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if micro.micro_sr3:
          a = [str(sr_no),"Faecal E.coli","CFU/ml",micro.micro_sr3]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if micro.micro_sr4:
          a = [str(sr_no),"Faecal Enterococci","CFU/ml",micro.micro_sr4]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if micro.micro_sr5:
          a = [str(sr_no),"Pseudomonas Aeruginosa","CFU/ml",micro.micro_sr5]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if micro.micro_sr6:
          a = [str(sr_no),"Faecal Coliform","CFU/ml",micro.micro_sr6]
          sr_no = sr_no+1
          TABLE_DATA.append(a)







     pdf = PDFWithPageNumbers(micro_lab_report_no=micro.micro_lab_report_no,micro_invoice_bill=micro.micro_invoice_bill,micro_rep_date=micro.micro_rep_date,micro_rep_to=micro.micro_rep_to,
                              micro_address=micro.micro_address,micro_attention=micro.micro_attention,micro_email=micro.micro_email,micro_sampleId=micro.micro_sampleId,micro_sample_col_date=micro.micro_sample_col_date,
                              micro_sample_desc=micro.micro_sample_desc,micro_sample_type=micro.micro_sample_type,micro_sample_col_by=micro.micro_sample_col_by,micro_test_desc = micro.micro_test_desc

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     with pdf.table(col_widths=(10, 50, 30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               # if k == 0:
               #      data_row[4] = micro.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table

     Table_Data1 = [
          
     ]
     if micro.micro_editnote:
          a=["Note :"+micro.micro_editnote] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if micro.micro_legend_1:
          a = [micro.micro_legend_1]
          Table_data_legend.append(a)
          
     if micro.micro_legend_2:
          a = [micro.micro_legend_2]
          Table_data_legend.append(a)

     if micro.micro_custom_legend:
          a = [micro.micro_custom_legend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')

     # if micro.micro_editnote:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,170,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(167.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=micro.micro_editnote)
     # line_height = 4
     # y = 180
     # if micro.micro_legend_1:
     #      pdf.text(10,y,txt=micro.micro_legend_1)
     #      y = y+line_height
     # if micro.micro_legend_2:
     #      pdf.text(10,y,txt=micro.micro_legend_2)
     #      y = y+line_height

     # if micro.micro_custom_legend:
     #      pdf.text(10,y,txt=micro.micro_custom_legend)
     #      y = y+line_height


     pdf.image(micro.micro_analyzedby,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(micro.micro_reviewedby,100,250,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(micro.micro_approvedby,165,249,12,12)
     pdf.image(micro.micro_approvedby1,178,249,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if micro.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if micro.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if micro.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=micro.micro_doc1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=micro.micro_doc2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=micro.micro_doc3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response

@login_required(login_url="/login")
def viscousLiquidList(request):
     vL = ViscousLiquid.objects.all()
     context = {'data':vL}
     return render(request,"viscousLiquidList.html",context)


@login_required(login_url="/login")
def viscousLiquidDelete(request,pk):
     vl = ViscousLiquid.objects.get(id=pk)
     vl.delete()
     return redirect("viscousLiquidList")


@login_required(login_url="/login")
def viscousLiquidEdit(request,pk):
     vL = ViscousLiquid.objects.get(id=pk)
     context = {'data':vL}
     return render(request,"viscousLiquidEdit.html",context)


@login_required(login_url="/login")
def viscousLiquidUpdate(request,pk):
     vL = ViscousLiquid.objects.get(id=pk)
     if request.method == 'POST':
          location = request.POST['location']
          vL.lab_rep_no = request.POST['lab_rep_no']
          vL.invoice_no = request.POST['invoice_no']
          vL.report_date = request.POST['report_date']
          vL.report_to = request.POST['report_to']
          vL.address = request.POST['address']
          vL.Attention = request.POST['Attention']
          vL.Email = request.POST['Email']
          vL.sampleId = request.POST['sampleId']
          vL.sample_Col_date = request.POST['sample_Col_date']
          vL.sample_Desc = request.POST['sample_Desc']
          vL.sample_type = request.POST['sample_type']
          vL.sample_col_by = request.POST['sample_col_by']
          vL.date_of_analysis = request.POST['date_of_analysis']
          vL.test_desc = request.POST['test_desc']
          vL.viscous_select = request.POST.get('select')
          vL.sr1 = request.POST['sr1']
          vL.legend_1 = request.POST['legend_1']
          vL.legend_2 = request.POST['legend_2']
          vL.edit_note = request.POST['edit_note']
          vL.custom_legend = request.POST['custom_legend']
          vL.doc1 = request.POST['doc1']
          vL.doc2 = request.POST['doc2']
          vL.doc3 = request.POST['doc3']
          vL.analyzedby = request.FILES['analyzedby']
          vL.reviewedby = request.FILES['reviewedby']
          vL.approvedby = request.FILES['approvedby']
          vL.approvedby1 = request.FILES['approvedby1']

          vL.save()
          id = (ViscousLiquid.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/viscousLiquid-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="viscousLiquidList")
     return render(request,"viscousLiquidList.html")


@login_required(login_url="/login")
def viscousLiquidview(request,pk):
     vL =ViscousLiquid.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data':vL,'qr':'media/qr.png'}

     return render(request,'viscousLiquidView.html',context)


@login_required(login_url="/login")
def viscousLiquidPdf(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,lab_rep_no,invoice_no,report_date,address,Attention,Email,sampleId,sample_Col_date,
                       sample_col_by,sample_type,sample_Desc,report_to,test_desc):
               super().__init__()
               self.lab_rep_no = lab_rep_no
               self.invoice_no = invoice_no
               self.report_date = report_date
               self.address = address
               self.Attention = Attention
               self.Email = Email
               self.sampleId = sampleId
               self.sample_Col_date = sample_Col_date
               self.sample_col_by = sample_col_by
               self.sample_type = sample_type
               self.sample_Desc = sample_Desc
               self.report_to = report_to
               self.test_desc = test_desc



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.lab_rep_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.invoice_no)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.report_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.Attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.Email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(86,82,txt="sample ID:")
               self.text(110,82,txt=self.sampleId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(65.7,88,txt="sample Performed Date:")
               self.text(110,88,txt=self.sample_Col_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72.2,94,txt="sample Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.sample_Desc)

               self.line(105,78,105,114)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(81.8,100,txt="sample Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.sample_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(70.5,106,txt="Sample Collected By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.sample_col_by)

               self.rect(10,108,190,6)
               self.set_font("Calibri","B", 10)
               self.text(76.5,112,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.test_desc)
               #table header
               self.rect(10,117.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,121.5,txt="Aanalytical Test Report")

               self.set_y(124)




     vL = ViscousLiquid.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Methods","Unit","Result"],
     ]
     sr_no = 1
     if vL.sr1 and vL.viscous_select =="ASTM":
          a = [str(sr_no),"Oil & Grease","ASTM D-3921","mg/L",vL.sr1]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif vL.sr1 and vL.viscous_select =="USEPA":
          a = [str(sr_no),"Oil & Grease","USEPA 1664","mg/L",vL.sr1]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     elif vL.sr1 and vL.viscous_select =="APHA":
          a = [str(sr_no),"Oil & Grease","APHA 5220-B","mg/L",vL.sr1]
          sr_no = sr_no+1
          TABLE_DATA.append(a)








     pdf = PDFWithPageNumbers(lab_rep_no=vL.lab_rep_no,invoice_no=vL.invoice_no,report_date=vL.report_date,report_to=vL.report_to,
                              address=vL.address,Attention=vL.Attention,Email=vL.Email,sampleId=vL.sampleId,sample_Col_date=vL.sample_Col_date,
                              sample_Desc=vL.sample_Desc,sample_type=vL.sample_type,sample_col_by=vL.sample_col_by,test_desc = vL.test_desc

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True)











     #report data table
     with pdf.table(col_widths=(10, 50, 30,30,30),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               # if k == 0:
               #      data_row[4] = vL.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     # data after Table

     Table_Data1 = [
          
     ]
     if vL.edit_note:
          a=["Note :"+vL.edit_note] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if vL.legend_1:
          a = [vL.legend_1]
          Table_data_legend.append(a)
          
     if vL.legend_2:
          a = [vL.legend_2]
          Table_data_legend.append(a)

     if vL.custom_legend:
          a = [vL.custom_legend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')
     # if vL.edit_note:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,140,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(137.8)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=vL.edit_note)
     # line_height = 4
     # y = 150
     # if vL.legend_1:
     #      pdf.text(10,y,txt=vL.legend_1)
     #      y = y+line_height
     # if vL.legend_2:
     #      pdf.text(10,y,txt=vL.legend_2)
     #      y = y+line_height

     # if vL.custom_legend:
     #      pdf.text(10,y,txt=vL.custom_legend)
     #      y = y+line_height


     pdf.image(vL.analyzedby,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(vL.reviewedby,100,250,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(vL.approvedby,165,249,12,12)
     pdf.image(vL.approvedby1,178,249,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if vL.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if vL.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if vL.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=vL.doc1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=vL.doc2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=vL.doc3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response


@login_required(login_url="/login")
def ambientAir2List(request):
     AA = AmbientAir2.objects.all()
     context = {"data":AA}
     return render(request,"ambientAir2List.html",context)

@login_required(login_url="/login")
def ambientAir2Delete(request,pk):
     AA = AmbientAir2.objects.get(id=pk)
     AA.delete()
     return redirect("ambientAir2List")

@login_required(login_url="/login")
def ambientAir2Edit(request,pk):
     AA = AmbientAir2.objects.get(id=pk)
     context = {'data': AA}
     return render(request,"ambientAir2Edit.html",context)

@login_required(login_url="/login")
def ambientAir2Update(request,pk):
     AA = AmbientAir2.objects.get(id=pk)
     if request.method == 'POST':
          AA.location = request.POST['location']
          AA.lab_rep_no = request.POST['lab_rep_no']
          AA.invoice_no = request.POST['invoice_no']
          AA.report_date = request.POST['report_date']
          AA.report_to = request.POST['report_to']
          AA.address = request.POST['address']
          AA.attention = request.POST['attention']
          AA.email = request.POST['email']
          AA.testId = request.POST['testId']
          AA.test_perf_date = request.POST['test_perf_date']
          AA.test_type = request.POST['test_type']
          AA.test_desc = request.POST['test_desc']
          AA.test_test_perf_by = request.POST['test_test_perf_by']
          AA.sr1_1 = request.POST['sr1_1']
          AA.sr1_2 = request.POST['sr1_2']
          AA.sr1_3 = request.POST['sr1_3']
          AA.sr1_4 = request.POST['sr1_4']
          AA.sr1_5 = request.POST['sr1_5']
          AA.sr1_6 = request.POST['sr1_6']
          AA.sr1_7 = request.POST['sr1_7']
          AA.sr1_8 = request.POST['sr1_8']
          AA.sr1_9 = request.POST['sr1_9']
          AA.sr1_10 = request.POST['sr1_10']
          AA.sr2_0 = request.POST['sr2_0']
          AA.sr2_1 = request.POST['sr2_1']
          AA.sr2_2 = request.POST['sr2_2']
          AA.sr2_3 = request.POST['sr2_3']
          AA.sr2_4 = request.POST['sr2_4']
          AA.sr2_5 = request.POST['sr2_5']
          AA.sr2_6 = request.POST['sr2_6']
          AA.sr2_7 = request.POST['sr2_7']
          AA.sr2_8 = request.POST['sr2_8']
          AA.sr2_9 = request.POST['sr2_9']
          AA.sr3_0 = request.POST['sr3_0']
          AA.sr3_1 = request.POST['sr3_1']
          AA.sr3_2 = request.POST['sr3_2']
          AA.sr3_3 = request.POST['sr3_3']
          AA.sr3_4 = request.POST['sr3_4']
          AA.sr3_5 = request.POST['sr3_5']
          AA.sr3_6 = request.POST['sr3_6']
          AA.sr3_7 = request.POST['sr3_7']
          AA.sr3_8 = request.POST['sr3_8']
          AA.sr3_9 = request.POST['sr3_9']
          AA.sr4_0 = request.POST['sr4_0']
          AA.sr4_1 = request.POST['sr4_1']
          AA.sr4_2 = request.POST['sr4_2']
          AA.sr4_3 = request.POST['sr4_3']
          AA.sr4_4 = request.POST['sr4_4']
          AA.sr4_5 = request.POST['sr4_5']
          AA.sr4_6 = request.POST['sr4_6']
          AA.sr4_7 = request.POST['sr4_7']
          AA.sr4_8 = request.POST['sr4_8']
          AA.sr4_9 = request.POST['sr4_9']
          AA.sr5_0 = request.POST['sr5_0']
          AA.sr5_1 = request.POST['sr5_1']
          AA.sr5_2 = request.POST['sr5_2']
          AA.sr5_3 = request.POST['sr5_3']
          AA.sr5_4 = request.POST['sr5_4']
          AA.sr5_5 = request.POST['sr5_5']
          AA.sr5_6 = request.POST['sr5_6']
          AA.sr5_7 = request.POST['sr5_7']
          AA.sr5_8 = request.POST['sr5_8']
          AA.sr5_9 = request.POST['sr5_9']
          AA.sr6_0 = request.POST['sr6_0']
          AA.sr6_1 = request.POST['sr6_1']
          AA.sr6_2 = request.POST['sr6_2']
          AA.sr6_3 = request.POST['sr6_3']
          AA.sr6_4 = request.POST['sr6_4']
          AA.sr6_5 = request.POST['sr6_5']
          AA.sr6_6 = request.POST['sr6_6']
          AA.sr6_7 = request.POST['sr6_7']
          AA.sr6_8 = request.POST['sr6_8']
          AA.sr6_9 = request.POST['sr6_9']
          AA.sr7_0 = request.POST['sr7_0']
          AA.sr7_1 = request.POST['sr7_1']
          AA.sr7_2 = request.POST['sr7_2']
          AA.sr7_3 = request.POST['sr7_3']
          AA.sr7_4 = request.POST['sr7_4']
          AA.sr7_5 = request.POST['sr7_5']
          AA.sr7_6 = request.POST['sr7_6']
          AA.sr7_7 = request.POST['sr7_7']
          AA.sr7_8 = request.POST['sr7_8']
          AA.sr7_9 = request.POST['sr7_9']
          AA.sr8_0 = request.POST['sr8_0']
          AA.sr8_1 = request.POST['sr8_1']
          AA.sr8_2 = request.POST['sr8_2']
          AA.sr8_3 = request.POST['sr8_3']
          AA.sr8_4 = request.POST['sr8_4']
          AA.sr8_5 = request.POST['sr8_5']
          AA.sr8_6 = request.POST['sr8_6']
          AA.sr8_7 = request.POST['sr8_7']
          AA.sr8_8 = request.POST['sr8_8']
          AA.sr8_9 = request.POST['sr8_9']
          AA.sr9_0 = request.POST['sr9_0']
          AA.sr9_1 = request.POST['sr9_1']
          AA.sr9_2 = request.POST['sr9_2']
          AA.sr9_3 = request.POST['sr9_3']
          AA.sr9_4 = request.POST['sr9_4']
          AA.sr9_5 = request.POST['sr9_5']
          AA.sr9_6 = request.POST['sr9_6']
          AA.sr9_7 = request.POST['sr9_7']
          AA.sr9_8 = request.POST['sr9_8']
          AA.sr9_9 = request.POST['sr9_9']
          AA.sr10_0 = request.POST['sr10_0']
          AA.sr10_1 = request.POST['sr10_1']
          AA.sr10_2 = request.POST['sr10_2']
          AA.sr10_3 = request.POST['sr10_3']
          AA.sr10_4 = request.POST['sr10_4']
          AA.sr10_5 = request.POST['sr10_5']
          AA.sr10_6 = request.POST['sr10_6']
          AA.sr10_7 = request.POST['sr10_7']
          AA.sr10_8 = request.POST['sr10_8']
          AA.sr10_9 = request.POST['sr10_9']
          AA.sr11_0 = request.POST['sr11_0']
          AA.sr11_1 = request.POST['sr11_1']
          AA.sr11_2 = request.POST['sr11_2']
          AA.sr11_3 = request.POST['sr11_3']
          AA.sr11_4 = request.POST['sr11_4']
          AA.sr11_5 = request.POST['sr11_5']
          AA.sr11_6 = request.POST['sr11_6']
          AA.sr11_7 = request.POST['sr11_7']
          AA.sr11_8 = request.POST['sr11_8']
          AA.sr11_9 = request.POST['sr11_9']
          AA.sr12_0 = request.POST['sr12_0']
          AA.sr12_1 = request.POST['sr12_1']
          AA.sr12_2 = request.POST['sr12_2']
          AA.sr12_3 = request.POST['sr12_3']
          AA.sr12_4 = request.POST['sr12_4']
          AA.sr12_5 = request.POST['sr12_5']
          AA.sr12_6 = request.POST['sr12_6']
          AA.sr12_7 = request.POST['sr12_7']
          AA.sr12_8 = request.POST['sr12_8']
          AA.sr12_9 = request.POST['sr12_9']
          AA.sr13_0 = request.POST['sr13_0']
          AA.sr13_1 = request.POST['sr13_1']
          AA.sr13_2 = request.POST['sr13_2']
          AA.sr13_3 = request.POST['sr13_3']
          AA.sr13_4 = request.POST['sr13_4']
          AA.sr13_5 = request.POST['sr13_5']
          AA.sr13_6 = request.POST['sr13_6']
          AA.sr13_7 = request.POST['sr13_7']
          AA.sr13_8 = request.POST['sr13_8']
          AA.sr13_9 = request.POST['sr13_9']
          AA.sr14_0 = request.POST['sr14_0']
          AA.sr14_1 = request.POST['sr14_1']
          AA.sr14_2 = request.POST['sr14_2']
          AA.sr14_3 = request.POST['sr14_3']
          AA.sr14_4 = request.POST['sr14_4']
          AA.sr14_5 = request.POST['sr14_5']
          AA.sr14_6 = request.POST['sr14_6']
          AA.sr14_7 = request.POST['sr14_7']
          AA.sr14_8 = request.POST['sr14_8']
          AA.sr14_9 = request.POST['sr14_9']
          AA.sr15_0 = request.POST['sr15_0']
          AA.sr15_1 = request.POST['sr15_1']
          AA.sr15_2 = request.POST['sr15_2']
          AA.sr15_3 = request.POST['sr15_3']
          AA.sr15_4 = request.POST['sr15_4']
          AA.sr15_5 = request.POST['sr15_5']
          AA.sr15_6 = request.POST['sr15_6']
          AA.sr15_7 = request.POST['sr15_7']
          AA.sr15_8 = request.POST['sr15_8']
          AA.sr15_9 = request.POST['sr15_9']
          AA.sr16_0 = request.POST['sr16_0']
          AA.sr16_1 = request.POST['sr16_1']
          AA.sr16_2 = request.POST['sr16_2']
          AA.sr16_3 = request.POST['sr16_3']
          AA.sr16_4 = request.POST['sr16_4']
          AA.sr16_5 = request.POST['sr16_5']
          AA.sr16_6 = request.POST['sr16_6']
          AA.sr16_7 = request.POST['sr16_7']
          AA.sr16_8 = request.POST['sr16_8']
          AA.sr16_9 = request.POST['sr16_9']
          AA.sr17_0 = request.POST['sr17_0']
          AA.sr17_1 = request.POST['sr17_1']
          AA.sr17_2 = request.POST['sr17_2']
          AA.sr17_3 = request.POST['sr17_3']
          AA.sr17_4 = request.POST['sr17_4']
          AA.sr17_5 = request.POST['sr17_5']
          AA.sr17_6 = request.POST['sr17_6']
          AA.sr17_7 = request.POST['sr17_7']
          AA.sr17_8 = request.POST['sr17_8']
          AA.sr17_9 = request.POST['sr17_9']
          AA.sr18_0 = request.POST['sr18_0']
          AA.sr18_1 = request.POST['sr18_1']
          AA.sr18_2 = request.POST['sr18_2']
          AA.sr18_3 = request.POST['sr18_3']
          AA.sr18_4 = request.POST['sr18_4']
          AA.sr18_5 = request.POST['sr18_5']
          AA.sr18_6 = request.POST['sr18_6']
          AA.sr18_7 = request.POST['sr18_7']
          AA.sr18_8 = request.POST['sr18_8']
          AA.sr18_9 = request.POST['sr18_9']
          AA.sr19_0 = request.POST['sr19_0']
          AA.sr19_1 = request.POST['sr19_1']
          AA.sr19_2 = request.POST['sr19_2']
          AA.sr19_3 = request.POST['sr19_3']
          AA.sr19_4 = request.POST['sr19_4']
          AA.sr19_5 = request.POST['sr19_5']
          AA.sr19_6 = request.POST['sr19_6']
          AA.sr19_7 = request.POST['sr19_7']
          AA.sr19_8 = request.POST['sr19_8']
          AA.sr19_9 = request.POST['sr19_9']
          AA.sr20_0 = request.POST['sr20_0']
          AA.sr20_1 = request.POST['sr20_1']
          AA.sr20_2 = request.POST['sr20_2']
          AA.sr20_3 = request.POST['sr20_3']
          AA.sr20_4 = request.POST['sr20_4']
          AA.sr20_5 = request.POST['sr20_5']
          AA.sr20_6 = request.POST['sr20_6']
          AA.sr20_7 = request.POST['sr20_7']
          AA.sr20_8 = request.POST['sr20_8']
          AA.sr20_9 = request.POST['sr20_9']
          AA.sr21_0 = request.POST['sr21_0']
          AA.sr21_1 = request.POST['sr21_1']
          AA.sr21_2 = request.POST['sr21_2']
          AA.sr21_3 = request.POST['sr21_3']
          AA.sr21_4 = request.POST['sr21_4']
          AA.sr21_5 = request.POST['sr21_5']
          AA.sr21_6 = request.POST['sr21_6']
          AA.sr21_7 = request.POST['sr21_7']
          AA.sr21_8 = request.POST['sr21_8']
          AA.sr21_9 = request.POST['sr21_9']
          AA.sr22_0 = request.POST['sr22_0']
          AA.sr22_1 = request.POST['sr22_1']
          AA.sr21_2 = request.POST['sr21_2']
          AA.sr21_3 = request.POST['sr21_3']
          AA.sr21_4 = request.POST['sr21_4']
          AA.sr21_5 = request.POST['sr21_5']
          AA.sr21_6 = request.POST['sr21_6']
          AA.sr21_7 = request.POST['sr21_7']
          AA.sr21_8 = request.POST['sr21_8']
          AA.sr21_9 = request.POST['sr21_9']
          AA.sr22_0 = request.POST['sr22_0']
          AA.sr22_1 = request.POST['sr22_1']
          AA.sr22_2 = request.POST['sr22_2']
          AA.sr22_3 = request.POST['sr22_3']
          AA.sr22_4 = request.POST['sr22_4']
          AA.sr22_5 = request.POST['sr22_5']
          AA.sr22_6 = request.POST['sr22_6']
          AA.sr22_7 = request.POST['sr22_7']
          AA.sr22_8 = request.POST['sr22_8']
          AA.sr22_9 = request.POST['sr22_9']
          AA.sr23_0 = request.POST['sr23_0']
          AA.sr23_1 = request.POST['sr23_1']
          AA.sr23_2 = request.POST['sr23_2']
          AA.sr23_3 = request.POST['sr23_3']
          AA.sr23_4 = request.POST['sr23_4']
          AA.sr23_5 = request.POST['sr23_5']
          AA.sr23_6 = request.POST['sr23_6']
          AA.sr23_7 = request.POST['sr23_7']
          AA.sr23_8 = request.POST['sr23_8']
          AA.sr23_9 = request.POST['sr23_9']
          AA.sr24_0 = request.POST['sr24_0']
          AA.sr24_1 = request.POST['sr24_1']
          AA.sr24_2 = request.POST['sr24_2']
          AA.sr24_3 = request.POST['sr24_3']
          AA.sr24_4 = request.POST['sr24_4']
          AA.sr24_5 = request.POST['sr24_5']
          AA.sr24_6 = request.POST['sr24_6']
          AA.sr24_7 = request.POST['sr24_7']
          AA.sr24_8 = request.POST['sr24_8']
          AA.sr24_9 = request.POST['sr24_9']
          AA.sr25_0 = request.POST['sr25_0']
          AA.sr25_1 = request.POST['sr25_1']
          AA.sr25_2 = request.POST['sr25_2']
          AA.sr25_3 = request.POST['sr25_3']
          AA.sr25_4 = request.POST['sr25_4']
          AA.sr25_5 = request.POST['sr25_5']
          AA.sr25_6 = request.POST['sr25_6']
          AA.sr25_7 = request.POST['sr25_7']
          AA.sr25_8 = request.POST['sr25_8']
          AA.select = request.POST.get('select')
          AA.legend_1 = request.POST['legend_1']
          AA.legend_2 = request.POST['legend_2']
          AA.legend_3 = request.POST['legend_3']
          AA.legend_4 = request.POST['legend_4']
          AA.legend_5 = request.POST['legend_5']
          AA.legend_6 = request.POST['legend_6']
          AA.legend_7 = request.POST['legend_7']
          AA.legend_8 = request.POST['legend_8']
          AA.legend_9 = request.POST['legend_9']
          AA.legend_10 = request.POST['legend_10']
          AA.legend_11 = request.POST['legend_11']
          AA.edit_note = request.POST['edit_note']
          AA.custom_legend = request.POST['custom_legend']
          AA.doc1 = request.POST['doc1']
          AA.doc2 = request.POST['doc2']
          AA.doc3 = request.POST['doc3']
          AA.analyzedby = request.FILES['analyzedby']
          AA.reviewedby = request.FILES['reviewedby']
          AA.approvedby = request.FILES['approvedby']
          AA.approvedby1 = request.FILES['approvedby1']


          AA.save()
          id = (AmbientAir2.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/ambientAir2-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="ambientAir2List")


     return render(request,"ambientAir2List.html")

@login_required(login_url="/login")
def ambientAir2View(request,pk):
     AA = AmbientAir2.objects.get(id=pk)
     print(AA.id)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data': AA,'qr':'media/qr.png'}

     return render(request,'ambientAir2Report.html',context)

@login_required(login_url="/login")
def ambientAir2Pdf(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,lab_rep_no,invoice_no,report_date,address,attention,email,testId,test_perf_date,
                       test_test_perf_by,test_type,report_to,test_desc):
               super().__init__()
               self.lab_rep_no = lab_rep_no
               self.invoice_no = invoice_no
               self.report_date = report_date
               self.address = address
               self.attention = attention
               self.email = email
               self.testId = testId
               self.test_perf_date = test_perf_date
               self.test_test_perf_by = test_test_perf_by
               self.test_type = test_type
               self.report_to = report_to
               self.test_desc = test_desc



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.lab_rep_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.invoice_no)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.report_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(90,82,txt="Test ID:")
               self.text(110,82,txt=self.testId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(69.7,88,txt="Test Performed Date:")
               self.text(110,88,txt=self.test_perf_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(76.2,94,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.test_desc)

               self.line(105,78,105,114)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(85.5,100,txt="Test Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.test_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72.8,106,txt="Test Performed By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.test_test_perf_by)

               self.rect(10,108,190,6)
               self.set_font("Calibri","B", 10)
               self.text(76.5,112,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.test_desc)
               #table header
               self.rect(10,117.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,121.5,txt="Aanalytical Test Report")

               self.set_y(124)




     AA2 = AmbientAir2.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Time","CO mg/m³","NO µg/m3","NO₂ µg/m3","SO₂ µg/m3","O₃ µg/m3","PM10 µg/m3","PM1.0 µg/m3","PM2.5 µg/m3","Lead µg/m3"],
     ]
     sr_no = 1
     if AA2.sr1_1:
          a = [str(sr_no),AA2.sr1_1,AA2.sr1_2,AA2.sr1_3,AA2.sr1_4,AA2.sr1_5,AA2.sr1_6,AA2.sr1_7,AA2.sr1_8,AA2.sr1_9,AA2.sr1_10]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr2_1:
          a = [str(sr_no),AA2.sr2_0,AA2.sr2_1,AA2.sr2_2,AA2.sr2_3,AA2.sr2_4,AA2.sr2_5,AA2.sr2_6,AA2.sr2_7,AA2.sr2_8,AA2.sr2_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr3_1:
          a = [str(sr_no),AA2.sr3_0,AA2.sr3_1,AA2.sr3_2,AA2.sr3_3,AA2.sr3_4,AA2.sr3_5,AA2.sr3_6,AA2.sr3_7,AA2.sr3_8,AA2.sr3_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr4_1:
          a = [str(sr_no),AA2.sr4_0,AA2.sr4_1,AA2.sr4_2,AA2.sr4_3,AA2.sr4_4,AA2.sr4_5,AA2.sr4_6,AA2.sr4_7,AA2.sr4_8,AA2.sr4_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr5_1:
          a = [str(sr_no),AA2.sr5_0,AA2.sr5_1,AA2.sr5_2,AA2.sr5_3,AA2.sr5_4,AA2.sr5_5,AA2.sr5_6,AA2.sr5_7,AA2.sr5_8,AA2.sr5_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr6_1:
          a = [str(sr_no),AA2.sr6_0,AA2.sr6_1,AA2.sr6_2,AA2.sr6_3,AA2.sr6_4,AA2.sr6_5,AA2.sr6_6,AA2.sr6_7,AA2.sr6_8,AA2.sr6_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr7_1:
          a = [str(sr_no),AA2.sr7_0,AA2.sr7_1,AA2.sr7_2,AA2.sr7_3,AA2.sr7_4,AA2.sr7_5,AA2.sr7_6,AA2.sr7_7,AA2.sr7_8,AA2.sr7_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr8_1:
          a = [str(sr_no),AA2.sr8_0,AA2.sr8_1,AA2.sr8_2,AA2.sr8_3,AA2.sr8_4,AA2.sr8_5,AA2.sr8_6,AA2.sr8_7,AA2.sr8_8,AA2.sr8_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr9_1:
          a = [str(sr_no),AA2.sr9_0,AA2.sr9_1,AA2.sr9_2,AA2.sr9_3,AA2.sr9_4,AA2.sr9_5,AA2.sr9_6,AA2.sr9_7,AA2.sr9_8,AA2.sr9_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr10_1:
          a = [str(sr_no),AA2.sr10_0,AA2.sr10_1,AA2.sr10_2,AA2.sr10_3,AA2.sr10_4,AA2.sr10_5,AA2.sr10_6,AA2.sr10_7,AA2.sr10_8,AA2.sr10_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr11_1:
          a = [str(sr_no),AA2.sr11_0,AA2.sr11_1,AA2.sr11_2,AA2.sr11_3,AA2.sr11_4,AA2.sr11_5,AA2.sr11_6,AA2.sr11_7,AA2.sr11_8,AA2.sr11_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr12_1:
          a = [str(sr_no),AA2.sr12_0,AA2.sr12_1,AA2.sr12_2,AA2.sr12_3,AA2.sr12_4,AA2.sr12_5,AA2.sr12_6,AA2.sr12_7,AA2.sr12_8,AA2.sr12_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr13_1:
          a = [str(sr_no),AA2.sr13_0,AA2.sr13_1,AA2.sr13_2,AA2.sr13_3,AA2.sr13_4,AA2.sr13_5,AA2.sr13_6,AA2.sr13_7,AA2.sr13_8,AA2.sr13_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr14_1:
          a = [str(sr_no),AA2.sr14_0,AA2.sr14_1,AA2.sr14_2,AA2.sr14_3,AA2.sr14_4,AA2.sr14_5,AA2.sr14_6,AA2.sr14_7,AA2.sr14_8,AA2.sr14_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr15_1:
          a = [str(sr_no),AA2.sr15_0,AA2.sr15_1,AA2.sr15_2,AA2.sr15_3,AA2.sr15_4,AA2.sr15_5,AA2.sr15_6,AA2.sr15_7,AA2.sr15_8,AA2.sr15_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr16_1:
          a = [str(sr_no),AA2.sr16_0,AA2.sr16_1,AA2.sr16_2,AA2.sr16_3,AA2.sr16_4,AA2.sr16_5,AA2.sr16_6,AA2.sr16_7,AA2.sr16_8,AA2.sr16_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr17_1:
          a = [str(sr_no),AA2.sr17_0,AA2.sr17_1,AA2.sr17_2,AA2.sr17_3,AA2.sr17_4,AA2.sr17_5,AA2.sr17_6,AA2.sr17_7,AA2.sr17_8,AA2.sr17_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr18_1:
          a = [str(sr_no),AA2.sr18_0,AA2.sr18_1,AA2.sr18_2,AA2.sr18_3,AA2.sr18_4,AA2.sr18_5,AA2.sr18_6,AA2.sr18_7,AA2.sr18_8,AA2.sr18_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr19_1:
          a = [str(sr_no),AA2.sr19_0,AA2.sr19_1,AA2.sr19_2,AA2.sr19_3,AA2.sr19_4,AA2.sr19_5,AA2.sr19_6,AA2.sr19_7,AA2.sr19_8,AA2.sr19_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr20_1:
          a = [str(sr_no),AA2.sr20_0,AA2.sr20_1,AA2.sr20_2,AA2.sr20_3,AA2.sr20_4,AA2.sr20_5,AA2.sr20_6,AA2.sr20_7,AA2.sr20_8,AA2.sr20_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr21_1:
          a = [str(sr_no),AA2.sr21_0,AA2.sr21_1,AA2.sr21_2,AA2.sr21_3,AA2.sr21_4,AA2.sr21_5,AA2.sr21_6,AA2.sr21_7,AA2.sr21_8,AA2.sr21_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr22_1:
          a = [str(sr_no),AA2.sr22_0,AA2.sr22_1,AA2.sr22_2,AA2.sr22_3,AA2.sr22_4,AA2.sr22_5,AA2.sr22_6,AA2.sr22_7,AA2.sr22_8,AA2.sr22_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr23_1:
          a = [str(sr_no),AA2.sr23_0,AA2.sr23_1,AA2.sr23_2,AA2.sr23_3,AA2.sr23_4,AA2.sr23_5,AA2.sr23_6,AA2.sr23_7,AA2.sr23_8,AA2.sr23_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr24_1:
          a = [str(sr_no),AA2.sr24_0,AA2.sr24_1,AA2.sr24_2,AA2.sr24_3,AA2.sr24_4,AA2.sr24_5,AA2.sr24_6,AA2.sr24_7,AA2.sr24_8,AA2.sr24_9]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.sr25_0:
          a=[str(sr_no),"Average",AA2.sr25_0,AA2.sr25_1,AA2.sr25_2,AA2.sr25_3,AA2.sr25_4,AA2.sr25_5,AA2.sr25_6,AA2.sr25_7,AA2.sr25_8]
          sr_no = sr_no+1
          TABLE_DATA.append(a)
     if AA2.select == "SEQS":
          a=["SEQS","05","40","80","120","-","150","500","75","1.5","-"]
          TABLE_DATA.append(a)
     if AA2.select == "PEQS":
          a=["PEQS","05","40","80","120","130","150","-","35","1.5","-"]
          TABLE_DATA.append(a)
     if AA2.select == "NEQS":
          a=["NEQS","05","40","80","120","130","150","-","35","1.5","-"]
          TABLE_DATA.append(a)








     pdf = PDFWithPageNumbers(lab_rep_no=AA2.lab_rep_no,invoice_no=AA2.invoice_no,report_date=AA2.report_date,report_to=AA2.report_to,
                              address=AA2.address,attention=AA2.attention,email=AA2.email,testId=AA2.testId,test_perf_date=AA2.test_perf_date,
                              test_desc=AA2.test_desc,test_type=AA2.test_type,test_test_perf_by=AA2.test_test_perf_by

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True, margin=10)










     num_rows=0
     #report data table
     with pdf.table(col_widths=(10, 20, 20,20,20,20,20,20,20,20,20),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER','CENTER','CENTER','CENTER','CENTER','CENTER')) as table:




          for k in range(0,len(TABLE_DATA)):
               data_row = TABLE_DATA[k]
               num_rows = num_rows+1

               # if k == 0:
               #      data_row[4] = AA2.select

               # watwer mark
               # pdf.set_page_background("static/assets/Capture.PNG")
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]

                    row.cell(datum)

     if num_rows >10 and num_rows <27:
          pdf.add_page()   
     Table_Data1 = [
          
     ]
     
     pdf.set_font_size(8)
     if AA2.edit_note:
          a=["Note :"+AA2.edit_note] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')
                    
                              
                    
     
     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if AA2.legend_1:
          a = [AA2.legend_1]
          Table_data_legend.append(a)
          
     if AA2.legend_2:
          a = [AA2.legend_2]
          Table_data_legend.append(a)
          
     if AA2.legend_3:
          a = [AA2.legend_3]
          Table_data_legend.append(a)
          
     if AA2.legend_4:
          a = [AA2.legend_4]
          Table_data_legend.append(a)
          
     if AA2.legend_5:
          a = [AA2.legend_5]
          Table_data_legend.append(a)
          
     if AA2.legend_6:
          a = [AA2.legend_6]
          Table_data_legend.append(a)
          
     if AA2.legend_7:
          a = [AA2.legend_7]
          Table_data_legend.append(a)
          
     if AA2.legend_8:
          a = [AA2.legend_8]
          Table_data_legend.append(a)
          
     if AA2.legend_9:
          a = [AA2.legend_9]
          Table_data_legend.append(a)
          
     if AA2.legend_10:
          a = [AA2.legend_10]
          Table_data_legend.append(a)
          
     if AA2.legend_11:
          a = [AA2.legend_11]
          Table_data_legend.append(a)
          

     if AA2.custom_legend:
          a = [AA2.custom_legend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')  
                    
                    
                      


     # y = 193
     # if num_rows == 19:
     #      pdf.add_page()
     # # data after Table
     # print("Y",pdf.y + num_rows )
     # # data after Table
     # print("ROWS",num_rows)



     # if AA2.edit_note and num_rows == 10:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,y,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(y-2.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=AA2.edit_note)

     # elif AA2.edit_note and num_rows <= 12:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,y+12,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(y+9.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=AA2.edit_note)

     # elif AA2.edit_note and num_rows >= 25:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,y-42,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(148.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=AA2.edit_note)

     # line_height = 4
     # if num_rows == 10:
     #      y=204
     # elif num_rows >= 25:
     #      y=159
     # elif num_rows <= 12:
     #      y=214
     # if AA2.legend_1:
     #      pdf.text(10,y,txt=AA2.legend_1)
     #      y = y+line_height
     # if AA2.legend_2:
     #      pdf.text(10,y,txt=AA2.legend_2)
     #      y = y+line_height
     # if AA2.legend_3:
     #      pdf.text(10,y,txt=AA2.legend_3)
     #      y = y+line_height
     # if AA2.legend_4:
     #      pdf.text(10,y,txt=AA2.legend_4)
     #      y = y+line_height
     # if AA2.legend_5:
     #      pdf.text(10,y,txt=AA2.legend_5)
     #      y = y+line_height
     # if AA2.legend_6:
     #      pdf.text(10,y,txt=AA2.legend_6)
     #      y = y+line_height
     # if AA2.legend_7:
     #      pdf.text(10,y,txt=AA2.legend_7)
     #      y = y+line_height
     # if AA2.legend_8:
     #      pdf.text(10,y,txt=AA2.legend_8)
     #      y = y+line_height
     # if AA2.legend_9:
     #      pdf.text(10,y,txt=AA2.legend_9)
     #      y = y+line_height
     # if AA2.legend_10:
     #      pdf.text(10,y,txt=AA2.legend_10)
     #      y = y+line_height
     # if AA2.legend_11:
     #      pdf.text(10,y,txt=AA2.legend_11)
     #      y = y+line_height

     # if AA2.custom_legend:
     #      pdf.text(10,y,txt=AA2.custom_legend)
     #      y = y+line_height


     pdf.image(AA2.analyzedby,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(AA2.reviewedby,100,249,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(AA2.approvedby,165,249,12,12)
     pdf.image(AA2.approvedby1,178,249,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if AA2.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,268,19,10)
     if AA2.location == 'PEQS':
          pdf.image('/assets/EPA Punjab logo.jpg',158,268,19,10)     
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=AA2.doc1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=AA2.doc2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=AA2.doc3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response


@login_required(login_url="/login")
def wasteWAter2List(request):
     ww = WasteWaterForm2.objects.all()
     context = {'data':ww}
     return render(request,"wasteWater2List.html",context)

@login_required(login_url="/login")
def wasteWAter2Delete(request,pk):
     ww = WasteWaterForm2.objects.get(id=pk)
     ww.delete()
     return redirect("wasteWater2List")

@login_required(login_url="/login")
def wasteWAter2Edit(request,pk):
     ww = WasteWaterForm2.objects.get(id=pk)
     context = {'data':ww}
     return render(request,"wasteWater2Edit.html",context)

@login_required(login_url="/login")
def wasteWAter2Update(request,pk):
     ww = WasteWaterForm2.objects.get(id=pk)
     if request.method == 'POST':
          ww.location = request.POST['location']
          ww.lab_rep_no = request.POST['lab_rep_no']
          ww.invoice_no = request.POST['invoice_no']
          ww.repo_date = request.POST['repo_date']
          ww.report_to = request.POST['report_to']
          ww.address = request.POST['address']
          ww.attention = request.POST['attention']
          ww.email = request.POST['email']
          ww.sampleId = request.POST['sampleId']
          ww.sample_Col_date = request.POST['sample_Col_date']
          ww.sample_desc = request.POST['sample_desc']
          ww.sampling_method = request.POST['sampling_method']
          ww.sample_type = request.POST['sample_type']
          ww.sample_collected_by = request.POST['sample_collected_by']
          ww.date_of_analysis = request.POST['date_of_analysis']
          ww.test_description = request.POST['test_description']
          ww.select = request.POST.get('select')
          ww.result_1 = request.POST['result_1']
          ww.result_1_1 = request.POST['result_1_1']
          ww.result_2 = request.POST['result_2']
          ww.result_2_2 = request.POST['result_2_2']
          ww.result_3 = request.POST['result_3']
          ww.result_3_3 = request.POST['result_3_3']
          ww.result_4 = request.POST['result_4']
          ww.result_4_4 = request.POST['result_4_4']
          ww.result_5 = request.POST['result_5']
          ww.result_5_5 = request.POST['result_5_5']
          ww.result_6 = request.POST['result_6']
          ww.result_6_6 = request.POST['result_6_6']
          ww.result_7 = request.POST['result_7']
          ww.result_7_7 = request.POST['result_7_7']
          ww.metho_select = request.POST.get('metho_select')
          ww.result_8 = request.POST['result_8']
          ww.result_8_8 = request.POST['result_8_8']
          ww.result_9 = request.POST['result_9']
          ww.result_9_9 = request.POST['result_9_9']
          ww.result_10 = request.POST['result_10']
          ww.result_10_10 = request.POST['result_10_10']
          ww.result_11 = request.POST['result_11']
          ww.result_11_11= request.POST['result_11_11']
          ww.result_12 = request.POST['result_12']
          ww.result_12_12 = request.POST['result_12_12']
          ww.result_13 = request.POST['result_13']
          ww.result_13_13 = request.POST['result_13_13']
          ww.result_14 = request.POST['result_14']
          ww.result_14_14 = request.POST['result_14_14']
          ww.result_15 = request.POST['result_15']
          ww.result_15_15 = request.POST['result_15_15']
          ww.result_16 = request.POST['result_16']
          ww.result_16_16 = request.POST['result_16_16']
          ww.result_17 = request.POST['result_17']
          ww.result_17_17 = request.POST['result_17_17']
          ww.result_18 = request.POST['result_18']
          ww.result_18_18 = request.POST['result_18_18']
          ww.result_19 = request.POST['result_19']
          ww.result_19_19 = request.POST['result_19_19']
          ww.result_20 = request.POST['result_20']
          ww.result_20_20 = request.POST['result_20_20']
          ww.result_21 = request.POST['result_21']
          ww.result_21_21 = request.POST['result_21_21']
          ww.result_22 = request.POST['result_22']
          ww.result_22_22 = request.POST['result_22_22']
          ww.result_23 = request.POST['result_23']
          ww.result_23_23 = request.POST['result_23_23']
          ww.result_24 = request.POST['result_24']
          ww.result_24_24 = request.POST['result_24_24']
          ww.result_25 = request.POST['result_25']
          ww.result_25_25 = request.POST['result_25_25']
          ww.result_26 = request.POST['result_26']
          ww.result_26_26 = request.POST['result_26_26']
          ww.result_27 = request.POST['result_27']
          ww.result_27_27 = request.POST['result_27_27']
          ww.result_28 = request.POST['result_28']
          ww.result_28_28 = request.POST['result_28_28']
          ww.result_29 = request.POST['result_29']
          ww.result_29_29 = request.POST['result_29_29']
          ww.result_30 = request.POST['result_30']
          ww.result_30_30 = request.POST['result_30_30']
          ww.result_31 = request.POST['result_31']
          ww.result_31_31 = request.POST['result_31_31']
          ww.result_32 = request.POST['result_32']
          ww.result_32_32 = request.POST['result_32_32']
          ww.legend_1 = request.POST['legend_1']
          ww.legend_2 = request.POST['legend_2']
          ww.legend_3 = request.POST['legend_3']
          ww.legend_4 = request.POST['legend_4']
          ww.legend_5 = request.POST['legend_5']
          ww.legend_6 = request.POST['legend_6']
          ww.legend_7 = request.POST['legend_7']
          ww.legend_8 = request.POST['legend_8']
          ww.legend_9 = request.POST['legend_9']
          ww.legend_10 = request.POST['legend_10']
          ww.legend_11 = request.POST['legend_11']
          ww.editNote = request.POST['editNote']
          ww.customlegend = request.POST['customlegend']
          ww.doc1 = request.POST['doc1']
          ww.doc2 = request.POST['doc2']
          ww.doc3 = request.POST['doc3']
          ww.analyzedby = request.FILES['analyzedby']
          ww.reviewedby = request.FILES['reviewedby']
          ww.approvedby = request.FILES['approvedby']
          ww.approvedby1 = request.FILES['approvedby1']


          ww.save()
          id = (WasteWaterForm2.objects.last()).id
          if "submit_and_view" in request.POST:
               url = f"/wasteWater2-view/{str(id)}/"
               return redirect(to=url)
          if "submit_and_new" in request.POST:
               return redirect(to="wasteWater2List")
     return redirect("wasteWater2List")


@login_required(login_url="/login")
def wasteWAter2View(request,pk):
     ww = WasteWaterForm2.objects.get(id=pk)
     current_url = request.build_absolute_uri()
     qr = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
          border=6,
          )
     qr.add_data(current_url)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     img.save("media/qr.png")
     context = {'data': ww,'qr':'media/qr.png'}

     return render(request,'wasteWater2Report.html',context)


@login_required(login_url="/login")
def wasteWater2Pdf(request,pk):
     from fpdf import FPDF
     class PDFWithPageNumbers(FPDF):
          def __init__(self,lab_rep_no,invoice_no,repo_date,address,attention,email,sampleId,sample_Col_date,
                       sample_collected_by,sample_type,sample_desc,report_to,test_description):
               super().__init__()
               self.lab_rep_no = lab_rep_no
               self.invoice_no = invoice_no
               self.repo_date = repo_date
               self.address = address
               self.attention = attention
               self.email = email
               self.sampleId = sampleId
               self.sample_Col_date = sample_Col_date
               self.sample_collected_by = sample_collected_by
               self.sample_type = sample_type
               self.sample_desc = sample_desc
               self.report_to = report_to
               self.test_description = test_description



          def header(self):
               self.set_y(0)
               self.set_x(0)
               # self.image("static/assets/header.PNG",0,0,self.w,22.5)


               #
               page_number = f" {self.page_no()}"+" of "+ f"{self.page_no()}"

               #header table
               font_path = "static/fonts/calibri.ttf"
               font_path_bold = "static/fonts/calibrib.ttf"
               pdf.add_font("Calibri","",font_path,uni=True)
               pdf.add_font("Calibri","B",font_path_bold,uni=True)
               pdf.set_font("Calibri","", 10)

               self.set_font("Calibri","B", 10)
               self.text(10,36,txt="Lab Report No:")
               self.set_font("Calibri","", 10)
               self.line(34,37,60,37)
               self.text(34,36,txt=self.lab_rep_no)

               self.set_font("Calibri","B", 10)
               self.text(10,43,txt="Invoice Bill No:")
               self.set_font("Calibri","", 10)
               self.line(34,44,60,44)
               self.text(34,43,txt=self.invoice_no)



               self.image("media/qr.png","C",y=28,w=20,h=20)

               self.set_font("Calibri","B", 10)
               self.text(150,43,txt="Reporting Date:")
               self.set_font("Calibri","", 10)
               self.line(175,44,199,44)
               self.text(175,43,txt=self.repo_date)

               self.set_font("Calibri","B", 10)
               self.text(159.5,36,txt="Page No:")
               self.set_font("Calibri","", 10)
               self.line(175,37,178+self.get_string_width(page_number +"of"+ page_number),37)
               self.text(175,36,txt=page_number)


               self.rect(10,48,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,53, txt="Report to:")
               self.line(30,48,30,61)
               self.text(37,53,txt='M/s.')
               self.set_font("Calibri","", 10)
               self.text(46,53,txt=self.report_to)
               self.set_font("Calibri","B", 10)
               self.text(31,58,txt='Address')
               self.set_font("Calibri","", 10)
               self.text(46,58,txt=self.address)

               self.rect(10,63,190,13)
               self.set_font("Calibri","B", 10)
               self.text(12,68, txt="Attention:")
               self.line(30,63,30,76)
               self.text(37,68,txt='Mr.')
               self.set_font("Calibri","", 10)
               self.text(46,68,txt=self.attention)
               self.set_font("Calibri","B", 10)
               self.text(34,73,txt='Email')
               self.set_font("Calibri","", 10)
               self.text(46,73,txt=self.email)


               self.rect(10,78,190,6)
               self.set_font("Calibri","B", 10)
               self.text(86,82,txt="sample ID:")
               self.text(110,82,txt=self.sampleId)

               self.rect(10,84,190,6)
               self.set_font("Calibri","B", 10)
               self.text(65.7,88,txt="sample Performed Date:")
               self.text(110,88,txt=self.sample_Col_date)


               self.rect(10,90.1,190,6)
               self.set_font("Calibri","B", 10)
               self.text(72.2,94,txt="sample Description:")
               self.set_font("Calibri","", 10)
               self.text(110,94,txt=self.sample_desc)

               self.line(105,78,105,114)

               self.rect(10,96,190,6)
               self.set_font("Calibri","B", 10)
               self.text(81.8,100,txt="sample Type:")
               self.set_font("Calibri","", 10)
               self.text(110,100,txt=self.sample_type)

               self.rect(10,102,190,6)
               self.set_font("Calibri","B", 10)
               self.text(70.5,106,txt="Sample Collected By:")
               self.set_font("Calibri","", 10)
               self.text(110,106,txt=self.sample_collected_by)

               self.rect(10,108,190,6)
               self.set_font("Calibri","B", 10)
               self.text(76.5,112,txt="Test Description:")
               self.set_font("Calibri","", 10)
               self.text(110,112,txt=self.test_description)
               #table header
               self.rect(10,117.1,190,7)
               self.set_font("Calibri","B", 12)
               self.text(89,121.5,txt="Aanalytical Test Report")

               self.set_y(124)




     ww = WasteWaterForm2.objects.get(id=pk)


     TABLE_DATA = [
           ["Sr.#","Parameter/Analytics Description","Methods","Unit","Inlet Results","Outlet Results","","",""],
     ]
     sr_no = 1

     if ww.result_1 and ww.select =="SEQS":
          a = [str(sr_no),"Temperature 40°C","*APHA 2550","°C",ww.result_1,ww.result_1_1,"≤ 3C","≤ 3C","≤ 3C"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_1 and ww.select =="PEQS":
          a = [str(sr_no),"Temperature 40°C","*APHA 2550","°C",ww.result_1,ww.result_1_1,"≤ 3C","≤ 3C",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_1 and ww.select =="NEQS":
          a = [str(sr_no),"Temperature 40°C","*APHA 2550","°C",ww.result_1,ww.result_1_1,"≤ 3C","≤ 3C",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_2 and ww.select =="SEQS":
          a = [str(sr_no),"pH","*APHA 4500 H-B","-",ww.result_2,ww.result_2_2,"6.9","6.9","6.9"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_2 and ww.select =="PEQS":
          a = [str(sr_no),"pH","APHA 4500 H-B","-",ww.result_2,ww.result_2_2,"6.9","6.9",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_2 and ww.select =="NEQS":
          a = [str(sr_no),"pH","APHA 4500 H-B","-",ww.result_2,ww.result_2_2,"6.9","6.9",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_3 and ww.select =="SEQS":
          a = [str(sr_no),"Sulphide","*APHA 4500-S2-D","mg/L",ww.result_3,ww.result_3_3,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_3 and ww.select =="PEQS":
          a = [str(sr_no),"Sulphide","*APHA 4500-S2-D","mg/L",ww.result_3,ww.result_3_3,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_3 and ww.select =="NEQS":
          a = [str(sr_no),"Sulphide","*APHA 4500-S2-D","mg/L",ww.result_3,ww.result_3_3,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_4 and ww.select =="SEQS":
          a = [str(sr_no),"Biological Oxygen Demand(BOD)5","HACH 10099","mg/L",ww.result_4,ww.result_4_4,"80","250","80"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_4 and ww.select =="PEQS":
          a = [str(sr_no),"Biological Oxygen Demand(BOD)5","HACH 10099","mg/L",ww.result_4,ww.result_4_4,"80","250",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_4 and ww.select =="NEQS":
          a = [str(sr_no),"Biological Oxygen Demand(BOD)5","HACH 10099","mg/L",ww.result_4,ww.result_4_4,"80","250",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_5 and ww.select =="SEQS":
          a = [str(sr_no),"Chemical Oxygen Demand(COD)","*HACH 8000","mg/L",ww.result_5,ww.result_5_5,"150","400","400"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_5 and ww.select =="PEQS":
          a = [str(sr_no),"Chemical Oxygen Demand(COD)","*HACH 8000","mg/L",ww.result_5,ww.result_5_5,"150","400",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_5 and ww.select =="NEQS":
          a = [str(sr_no),"Chemical Oxygen Demand(COD)","*HACH 8000","mg/L",ww.result_5,ww.result_5_5,"150","400",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_6 and ww.select =="SEQS":
          a = [str(sr_no),"Total Dissolved Solids (TDS)","*APHA 2540-C","mg/L",ww.result_6,ww.result_6_6,"3500","3500","3500"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_6 and ww.select =="PEQS":
          a = [str(sr_no),"Total Dissolved Solids (TDS)","*APHA 2540-C","mg/L",ww.result_6,ww.result_6_6,"3500","3500",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_6 and ww.select =="NEQS":
          a = [str(sr_no),"Total Dissolved Solids (TDS)","*APHA 2540-C","mg/L",ww.result_6,ww.result_6_6,"3500","3500",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_7 and ww.select =="SEQS":
          a = [str(sr_no),"Total Suspended Solids (TSS)","*APHA 2540-D","mg/L",ww.result_7,ww.result_7_7,"200","400","200"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_7 and ww.select =="PEQS":
          a = [str(sr_no),"Total Suspended Solids (TSS)","*APHA 2540-D","mg/L",ww.result_7,ww.result_7_7,"200","400",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_7 and ww.select =="NEQS":
          a = [str(sr_no),"Total Suspended Solids (TSS)","*APHA 2540-D","mg/L",ww.result_7,ww.result_7_7,"200","400",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_8 and ww.select =="SEQS":
          if ww.metho_select =="ASTM":
               a = [str(sr_no),"Oil & Grease","ASTM D-3291","mg/L",ww.result_8,ww.result_8_8,"10","10","10"]
               sr_no = sr_no+1
               TABLE_DATA.append(a)

     elif ww.result_8 and ww.select =="PEQS":
          if ww.metho_select == "ASTM":
               a = [str(sr_no),"Oil & Grease","ASTM D-3291","mg/L",ww.result_8,ww.result_8_8,"10","10",""]
               sr_no = sr_no+1
               TABLE_DATA.append(a)

     elif ww.result_8 and ww.select =="NEQS":
          if ww.metho_select =="ASTM":
               a = [str(sr_no),"Oil & Grease","ASTM D-3291","mg/L",ww.result_8,ww.result_8_8,"10","10",""]
               sr_no = sr_no+1
               TABLE_DATA.append(a)

     if ww.result_8 and ww.select =="SEQS":
          if ww.metho_select =="USEPA":
               a = [str(sr_no),"Oil & Grease","USEPA 1664","mg/L",ww.result_8,ww.result_8_8,"10","10","10"]
               sr_no = sr_no+1
               TABLE_DATA.append(a)

     elif ww.result_8 and ww.select =="PEQS":
          if ww.metho_select == "USEPA":
               a = [str(sr_no),"Oil & Grease","USEPA 1664","mg/L",ww.result_8,ww.result_8_8,"10","10",""]
               sr_no = sr_no+1
               TABLE_DATA.append(a)

     elif ww.result_8 and ww.select =="NEQS":
          if ww.metho_select =="USEPA":
               a = [str(sr_no),"Oil & Grease","USEPA 1664","mg/L",ww.result_8,ww.result_8_8,"10","10",""]
               sr_no = sr_no+1
               TABLE_DATA.append(a)
     if ww.result_8 and ww.select =="SEQS":
          if ww.metho_select =="APHA":
               a = [str(sr_no),"Oil & Grease","APHA 5220-B","mg/L",ww.result_8,ww.result_8_8,"10","10","10"]
               sr_no = sr_no+1
               TABLE_DATA.append(a)

     elif ww.result_8 and ww.select =="PEQS":
          if ww.metho_select == "APHA":
               a = [str(sr_no),"Oil & Grease","APHA 5220-B","mg/L",ww.result_8,ww.result_8_8,"10","10",""]
               sr_no = sr_no+1
               TABLE_DATA.append(a)

     elif ww.result_8 and ww.select =="NEQS":
          if ww.metho_select =="APHA":
               a = [str(sr_no),"Oil & Grease","APHA 5220-B","mg/L",ww.result_8,ww.result_8_8,"10","10",""]
               sr_no = sr_no+1
               TABLE_DATA.append(a)


     if ww.result_9 and ww.select =="SEQS":
          a = [str(sr_no),"Cadmium","*APHA 3111-B","mg/L",ww.result_9,ww.result_9_9,"0.1","0.1","0.1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_9 and ww.select =="PEQS":
          a = [str(sr_no),"Cadmium","*APHA 3111-B","mg/L",ww.result_9,ww.result_9_9,"0.1","0.1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_9 and ww.select =="NEQS":
          a = [str(sr_no),"Cadmium","*APHA 3111-B","mg/L",ww.result_9,ww.result_9_9,"0.1","0.1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_10 and ww.select =="SEQS":
          a = [str(sr_no),"Copper","*APHA 3111-B","mg/L",ww.result_10,ww.result_10_10,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_10 and ww.select =="PEQS":
          a = [str(sr_no),"Copper","*APHA 3111-B","mg/L",ww.result_10,ww.result_10_10,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_10 and ww.select =="NEQS":
          a = [str(sr_no),"Copper","*APHA 3111-B","mg/L",ww.result_10,ww.result_10_10,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_11 and ww.select =="SEQS":
          a = [str(sr_no),"Iron","*APHA 3111-B","mg/L",ww.result_11,ww.result_11_11,"8","8","8"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_11 and ww.select =="PEQS":
          a = [str(sr_no),"Iron","*APHA 3111-B","mg/L",ww.result_11,ww.result_11_11,"8","8",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_11 and ww.select =="NEQS":
          a = [str(sr_no),"Iron","*APHA 3111-B","mg/L",ww.result_11,ww.result_11_11,"8","8",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_12 and ww.select =="SEQS":
          a = [str(sr_no),"Lead","*APHA 3111-B","mg/L",ww.result_12,ww.result_12_12,"0.5","0.5","0.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_12 and ww.select =="PEQS":
          a = [str(sr_no),"Lead","*APHA 3111-B","mg/L",ww.result_12,ww.result_12_12,"0.5","0.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_12 and ww.select =="NEQS":
          a = [str(sr_no),"Lead","*APHA 3111-B","mg/L",ww.result_12,ww.result_12_12,"0.5","0.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_13 and ww.select =="SEQS":
          a = [str(sr_no),"Manganese","*APHA 3111-B","mg/L",ww.result_13,ww.result_13_13,"1.5","1.5","1.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_13 and ww.select =="PEQS":
          a = [str(sr_no),"Manganese","*APHA 3111-B","mg/L",ww.result_13,ww.result_13_13,"1.5","1.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_13 and ww.select =="NEQS":
          a = [str(sr_no),"Manganese","*APHA 3111-B","mg/L",ww.result_13,ww.result_13_13,"1.5","1.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_14 and ww.select =="SEQS":
          a = [str(sr_no),"Mercury","*APHA 3112-B","mg/L",ww.result_14,ww.result_14_14,"0.01","0.01","0.01"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_14 and ww.select =="PEQS":
          a = [str(sr_no),"Mercury","*APHA 3112-B","mg/L",ww.result_14,ww.result_14_14,"0.01","0.01",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_14 and ww.select =="NEQS":
          a = [str(sr_no),"Mercury","*APHA 3112-B","mg/L",ww.result_14,ww.result_14_14,"0.01","0.01",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_15 and ww.select =="SEQS":
          a = [str(sr_no),"Nickel","*APHA 3111-B","mg/L",ww.result_15,ww.result_15_15,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_15 and ww.select =="PEQS":
          a = [str(sr_no),"Nickel","*APHA 3111-B","mg/L",ww.result_15,ww.result_15_15,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_15 and ww.select =="NEQS":
          a = [str(sr_no),"Nickel","*APHA 3111-B","mg/L",ww.result_15,ww.result_15_15,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_16 and ww.select =="SEQS":
          a = [str(sr_no),"Selenium","*APHA 3114-B","mg/L",ww.result_16,ww.result_16_16,"0.5","0.5","0.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_16 and ww.select =="PEQS":
          a = [str(sr_no),"Selenium","*APHA 3114-B","mg/L",ww.result_16,ww.result_16_16,"0.5","0.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_16 and ww.select =="NEQS":
          a = [str(sr_no),"Selenium","*APHA 3114-B","mg/L",ww.result_16,ww.result_16_16,"0.5","0.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_17 and ww.select =="SEQS":
          a = [str(sr_no),"Chromium","*APHA 3111-B","mg/L",ww.result_17,ww.result_17_17,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_17 and ww.select =="PEQS":
          a = [str(sr_no),"Chromium","*APHA 3111-B","mg/L",ww.result_17,ww.result_17_17,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_17 and ww.select =="NEQS":
          a = [str(sr_no),"Chromium","*APHA 3111-B","mg/L",ww.result_17,ww.result_17_17,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_18 and ww.select =="SEQS":
          a = [str(sr_no),"Zinc","*APHA 3111-B","mg/L",ww.result_18,ww.result_18_18,"5","5","5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_18 and ww.select =="PEQS":
          a = [str(sr_no),"Zinc","*APHA 3111-B","mg/L",ww.result_18,ww.result_18_18,"5","5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_18 and ww.select =="NEQS":
          a = [str(sr_no),"Zinc","*APHA 3111-B","mg/L",ww.result_18,ww.result_18_18,"5","5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_19 and ww.select =="SEQS":
          a = [str(sr_no),"Arsenic","*APHA 3114-B","mg/L",ww.result_19,ww.result_19_19,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_19 and ww.select =="PEQS":
          a = [str(sr_no),"Arsenic","*APHA 3114-B","mg/L",ww.result_19,ww.result_19_19,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_19 and ww.select =="NEQS":
          a = [str(sr_no),"Arsenic","*APHA 3114-B","mg/L",ww.result_19,ww.result_19_19,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_20 and ww.select =="SEQS":
          a = [str(sr_no),"Chlorine","HACH 10069","mg/L",ww.result_20,ww.result_20_20,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_20 and ww.select =="PEQS":
          a = [str(sr_no),"Chlorine","HACH 10069","mg/L",ww.result_20,ww.result_20_20,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_20 and ww.select =="NEQS":
          a = [str(sr_no),"Chlorine","HACH 10069","mg/L",ww.result_20,ww.result_20_20,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_21 and ww.select =="SEQS":
          a = [str(sr_no),"Chloride","*APHA 4500 CL-B","mg/L",ww.result_21,ww.result_21_21,"1000","1000","**SC"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_21 and ww.select =="PEQS":
          a = [str(sr_no),"Chloride","*APHA 4500 CL-B","mg/L",ww.result_21,ww.result_21_21,"1000","1000",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_21 and ww.select =="NEQS":
          a = [str(sr_no),"Chloride","*APHA 4500 CL-B","mg/L",ww.result_21,ww.result_21_21,"1000","1000",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_22 and ww.select =="SEQS":
          a = [str(sr_no),"Cyanide","HACH 8027","mg/L",ww.result_22,ww.result_22_22,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_22 and ww.select =="PEQS":
          a = [str(sr_no),"Cyanide","HACH 8027","mg/L",ww.result_22,ww.result_22_22,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_22 and ww.select =="NEQS":
          a = [str(sr_no),"Cyanide","HACH 8027","mg/L",ww.result_22,ww.result_22_22,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_23 and ww.select =="SEQS":
          a = [str(sr_no),"Fluoride","*HACH 8029","mg/L",ww.result_23,ww.result_23_23,"10","10","10"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_23 and ww.select =="PEQS":
          a = [str(sr_no),"Fluoride","*HACH 8029","mg/L",ww.result_23,ww.result_23_23,"10","10",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_23 and ww.select =="NEQS":
          a = [str(sr_no),"Fluoride","*HACH 8029","mg/L",ww.result_23,ww.result_23_23,"10","10",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_24 and ww.select =="SEQS":
          a = [str(sr_no),"Ammonia","*HACH 8038","mg/L",ww.result_24,ww.result_24_24,"40","40","40"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_24 and ww.select =="PEQS":
          a = [str(sr_no),"Ammonia","*HACH 8038","mg/L",ww.result_24,ww.result_24_24,"40","40",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_24 and ww.select =="NEQS":
          a = [str(sr_no),"Ammonia","*HACH 8038","mg/L",ww.result_24,ww.result_24_24,"40","40",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_25 and ww.select =="SEQS":
           a = [str(sr_no),"Total Toxic Metals","APHA 3111","mg/L",ww.result_25,ww.result_25_25,"2","2","2"]
           sr_no = sr_no+1
           TABLE_DATA.append(a)

     elif ww.result_25 and ww.select =="PEQS":
           a = [str(sr_no),"Total Toxic Metals","APHA 3111","mg/L",ww.result_25,ww.result_25_25,"2","2",""]
           sr_no = sr_no+1
           TABLE_DATA.append(a)

     elif ww.result_25 and ww.select =="NEQS":
           a = [str(sr_no),"Total Toxic Metals","APHA 3111","mg/L",ww.result_25,ww.result_25_25,"2","2",""]
           sr_no = sr_no+1
           TABLE_DATA.append(a)


     if ww.result_26 and ww.select =="SEQS":
           a = [str(sr_no),"Sulphate","HACH 8051","mg/L",ww.result_26,ww.result_26_26,"600","1000","**SC"]
           sr_no = sr_no+1
           TABLE_DATA.append(a)

     elif ww.result_26 and ww.select =="PEQS":
           a = [str(sr_no),"Sulphate","HACH 8051","mg/L",ww.result_26,ww.result_26_26,"600","1000",""]
           sr_no = sr_no+1
           TABLE_DATA.append(a)

     elif ww.result_26 and ww.select =="NEQS":
           a = [str(sr_no),"Sulphate","HACH 8051","mg/L",ww.result_26,ww.result_26_26,"600","1000",""]
           sr_no = sr_no+1
           TABLE_DATA.append(a)


     if ww.result_27 and ww.select =="SEQS":
          a = [str(sr_no),"An Ionic Detergent As MBAs","*APHA 5540 C","mg/L",ww.result_27,ww.result_27_27,"20","20","20"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_27 and ww.select =="PEQS":
          a = [str(sr_no),"An Ionic Detergent As MBAs","*APHA 5540 C","mg/L",ww.result_27,ww.result_27_27,"20","20",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_27 and ww.select =="NEQS":
          a = [str(sr_no),"An Ionic Detergent As MBAs","*APHA 5540 C","mg/L",ww.result_27,ww.result_27_27,"20","20",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_28 and ww.select =="SEQS":
          a = [str(sr_no),"Pesticides","USEPA-614.1","mg/L",ww.result_28,ww.result_28_28,"0.15","0.15","0.15"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_28 and ww.select =="PEQS":
          a = [str(sr_no),"Pesticides","USEPA-614.1","mg/L",ww.result_28,ww.result_28_28,"0.15","0.15",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_28 and ww.select =="NEQS":
          a = [str(sr_no),"Pesticides","USEPA-614.1","mg/L",ww.result_28,ww.result_28_28,"0.15","0.15",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_29 and ww.select =="SEQS":
          a = [str(sr_no),"Phenolic Compounds(as Phenol)","HACH 8047","mg/L",ww.result_29,ww.result_29_29,"0.1","0.3","0.3"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_29 and ww.select =="PEQS":
          a = [str(sr_no),"Phenolic Compounds(as Phenol)","HACH 8047","mg/L",ww.result_29,ww.result_29_29,"0.1","0.3",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_29 and ww.select =="NEQS":
          a = [str(sr_no),"Phenolic Compounds(as Phenol)","HACH 8047","mg/L",ww.result_29,ww.result_29_29,"0.1","0.3",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_30 and ww.select =="SEQS":
          a = [str(sr_no),"Boron","HACH 8015","mg/L",ww.result_30,ww.result_30_30,"6","6","6"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_30 and ww.select =="PEQS":
          a = [str(sr_no),"Boron","HACH 8015","mg/L",ww.result_30,ww.result_30_30,"6","6",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_30 and ww.select =="NEQS":
          a = [str(sr_no),"Boron","HACH 8015","mg/L",ww.result_30,ww.result_30_30,"6","6",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_31 and ww.select =="SEQS":
          a = [str(sr_no),"Barium","HACH 8014","mg/L",ww.result_31,ww.result_31_31,"1.5","1.5","1.5"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_31 and ww.select =="PEQS":
          a = [str(sr_no),"Barium","HACH 8014","mg/L",ww.result_31,ww.result_31_31,"1.5","1.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_31 and ww.select =="NEQS":
          a = [str(sr_no),"Barium","HACH 8014","mg/L",ww.result_31,ww.result_31_31,"1.5","1.5",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)


     if ww.result_32 and ww.select =="SEQS":
          a = [str(sr_no),"Silver","*APHA 3111-B","mg/L",ww.result_32,ww.result_32_32,"1","1","1"]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_32 and ww.select =="PEQS":
          a = [str(sr_no),"Silver","*APHA 3111-B","mg/L",ww.result_32,ww.result_32_32,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)

     elif ww.result_32 and ww.select =="NEQS":
          a = [str(sr_no),"Silver","*APHA 3111-B","mg/L",ww.result_32,ww.result_32_32,"1","1",""]
          sr_no = sr_no+1
          TABLE_DATA.append(a)








     pdf = PDFWithPageNumbers(lab_rep_no=ww.lab_rep_no,invoice_no=ww.invoice_no,repo_date=ww.repo_date,report_to=ww.report_to,
                              address=ww.address,attention=ww.attention,email=ww.email,sampleId=ww.sampleId,sample_Col_date=ww.sample_Col_date,
                              sample_desc=ww.sample_desc,sample_type=ww.sample_type,sample_collected_by=ww.sample_collected_by,test_description = ww.test_description

                              )
     pdf.add_page()
     font_path = "static/fonts/calibri.ttf"
     font_path_bold = "static/fonts/calibrib.ttf"
     pdf.add_font("Calibri","",font_path,uni=True)
     pdf.add_font("Calibri","B",font_path_bold,uni=True)
     pdf.set_font("Calibri","", 9)
     pdf.set_auto_page_break(auto=True,margin=5)








     num_rows =0
     with pdf.table(col_widths=(10, 50, 30,30,30,30,10,10,10),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER','CENTER','CENTER','CENTER')) as table:
          # row = table.row()
          # row.cell(7,colspan=2)

           # watwer mark
          # pdf.set_page_background("static/assets/Capture.PNG")

          for k in range(0,1):
               data_row = TABLE_DATA[k]
               num_rows +=1
               if k == 0:
                    data_row[-3] = ww.select


               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    if i>6:
                         pass
                    if k == 0 and i==6:
                         row.cell(datum,colspan=1)
                    else:
                         row.cell(datum)

     
     #report data table
     # col_widths=(10, 50, 30,30,30,30,10)
     with pdf.table(col_widths=(10, 50, 30,30,30,30,10,10,10),width=190,line_height=6,text_align=("CENTER","LEFT","CENTER","CENTER",'CENTER','CENTER','CENTER','CENTER','CENTER')) as table:
          # row = table.row()
          # row.cell(7,colspan=2)

           # watwer mark
          # pdf.set_page_background("static/assets/Capture.PNG")

          for k in range(1,len(TABLE_DATA)):
               num_rows +=1
               data_row = TABLE_DATA[k]


               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]


                    row.cell(datum)

     if num_rows >=10 and num_rows <=32:
          pdf.add_page()
     Table_Data1 = [
          
     ]
     if ww.editNote:
          a=["Note :"+ww.editNote] 
          Table_Data1.append(a)
          print(a)
          
     
     # with pdf.table(col_widths=(190),width=190,line_height=6,text_align=("LEFT")) as table:
         
          for k in range(0,len(Table_Data1)):
               data_row = Table_Data1[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.multi_cell(190, 4, datum, border=0, ln=True, align='L')

     Table_data_legend = [

     ]     
     pdf.set_font_size(8)
     if ww.legend_1:
          a = [ww.legend_1]
          Table_data_legend.append(a)
          
     if ww.legend_2:
          a = [ww.legend_2]
          Table_data_legend.append(a)
          
     if ww.legend_3:
          a = [ww.legend_3]
          Table_data_legend.append(a)
          
     if ww.legend_4:
          a = [ww.legend_4]
          Table_data_legend.append(a)
          
     if ww.legend_5:
          a = [ww.legend_5]
          Table_data_legend.append(a)
          
     if ww.legend_6:
          a = [ww.legend_6]
          Table_data_legend.append(a)
          
     if ww.legend_7:
          a = [ww.legend_7]
          Table_data_legend.append(a)
          
     if ww.legend_8:
          a = [ww.legend_8]
          Table_data_legend.append(a)
          
     if ww.legend_9:
          a = [ww.legend_9]
          Table_data_legend.append(a)
          
     if ww.legend_10:
          a = [ww.legend_10]
          Table_data_legend.append(a)
          
     if ww.legend_11:
          a = [ww.legend_11]
          Table_data_legend.append(a)
          

     if ww.customlegend:
          a = [ww.customlegend]
          Table_data_legend.append(a)
     for k in range(0,len(Table_data_legend)):
               data_row = Table_data_legend[k]
               row = table.row()
               for i in range(0,len(data_row)):
                    datum = data_row[i]
                    row.cell(datum)
                    pdf.cell(190, 4, datum, border=0, ln=True, align='L')       

     # data after Table
     # print(num_rows)
     # if num_rows >= 17 and num_rows <=20:
          # pdf.add_page()
     # elif num_rows == 25:
     #      pdf.add_page()     


     # if ww.editNote and num_rows >= 32:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,169,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(166.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=ww.editNote)
     # elif ww.editNote and num_rows >= 32:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,169,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(166.5)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=ww.editNote)     
     # elif ww.editNote and num_rows >= 17 and num_rows<=20:
     #      pdf.set_font("Calibri","B", 10)
     #      pdf.text(10,130,txt="Note:")
     #      pdf.set_font("Calibri","", 8)
     #      pdf.set_y(127.7)
     #      pdf.set_x(20)
     #      pdf.multi_cell(182,txt=ww.editNote)  

     #      line_height = 4
     #      y = 135
     #      if ww.legend_1:
     #           pdf.text(10,y,txt=ww.legend_1)
     #           y = y+line_height
     #      if ww.legend_2:
     #           pdf.text(10,y,txt=ww.legend_2)
     #           y = y+line_height
     #      if ww.legend_3:
     #           pdf.text(10,y,txt=ww.legend_3)
     #           y = y+line_height
     #      if ww.legend_4:
     #           pdf.text(10,y,txt=ww.legend_4)
     #           y = y+line_height
     #      if ww.legend_5:
     #           pdf.text(10,y,txt=ww.legend_5)
     #           y = y+line_height
     #      if ww.legend_6:
     #           pdf.text(10,y,txt=ww.legend_6)
     #           y = y+line_height
     #      if ww.legend_7:
     #           pdf.text(10,y,txt=ww.legend_7)
     #           y = y+line_height
     #      if ww.legend_8:
     #           pdf.text(10,y,txt=ww.legend_8)
     #           y = y+line_height
     #      if ww.legend_9:
     #           pdf.text(10,y,txt=ww.legend_9)
     #           y = y+line_height
     #      if ww.legend_10:
     #           pdf.text(10,y,txt=ww.legend_10)
     #           y = y+line_height
     #      if ww.legend_11:
     #           pdf.text(10,y,txt=ww.legend_11)
     #           y = y+line_height

     #      if ww.customlegend:
     #           pdf.text(10,y,txt=ww.customlegend)
     #           y = y+line_height  
     # else:
     #      line_height = 4
     #      y = 174
     #      if ww.legend_1:
     #           pdf.text(10,y,txt=ww.legend_1)
     #           y = y+line_height
     #      if ww.legend_2:
     #           pdf.text(10,y,txt=ww.legend_2)
     #           y = y+line_height
     #      if ww.legend_3:
     #           pdf.text(10,y,txt=ww.legend_3)
     #           y = y+line_height
     #      if ww.legend_4:
     #           pdf.text(10,y,txt=ww.legend_4)
     #           y = y+line_height
     #      if ww.legend_5:
     #           pdf.text(10,y,txt=ww.legend_5)
     #           y = y+line_height
     #      if ww.legend_6:
     #           pdf.text(10,y,txt=ww.legend_6)
     #           y = y+line_height
     #      if ww.legend_7:
     #           pdf.text(10,y,txt=ww.legend_7)
     #           y = y+line_height
     #      if ww.legend_8:
     #           pdf.text(10,y,txt=ww.legend_8)
     #           y = y+line_height
     #      if ww.legend_9:
     #           pdf.text(10,y,txt=ww.legend_9)
     #           y = y+line_height
     #      if ww.legend_10:
     #           pdf.text(10,y,txt=ww.legend_10)
     #           y = y+line_height
     #      if ww.legend_11:
     #           pdf.text(10,y,txt=ww.legend_11)
     #           y = y+line_height

     #      if ww.customlegend:
     #           pdf.text(10,y,txt=ww.customlegend)
     #           y = y+line_height
     # line_height = 4
     # y = 174
     # if ww.legend_1:
     #      pdf.text(10,y,txt=ww.legend_1)
     #      y = y+line_height
     # if ww.legend_2:
     #      pdf.text(10,y,txt=ww.legend_2)
     #      y = y+line_height
     # if ww.legend_3:
     #      pdf.text(10,y,txt=ww.legend_3)
     #      y = y+line_height
     # if ww.legend_4:
     #      pdf.text(10,y,txt=ww.legend_4)
     #      y = y+line_height
     # if ww.legend_5:
     #      pdf.text(10,y,txt=ww.legend_5)
     #      y = y+line_height
     # if ww.legend_6:
     #      pdf.text(10,y,txt=ww.legend_6)
     #      y = y+line_height
     # if ww.legend_7:
     #      pdf.text(10,y,txt=ww.legend_7)
     #      y = y+line_height
     # if ww.legend_8:
     #      pdf.text(10,y,txt=ww.legend_8)
     #      y = y+line_height
     # if ww.legend_9:
     #      pdf.text(10,y,txt=ww.legend_9)
     #      y = y+line_height
     # if ww.legend_10:
     #      pdf.text(10,y,txt=ww.legend_10)
     #      y = y+line_height
     # if ww.legend_11:
     #      pdf.text(10,y,txt=ww.legend_11)
     #      y = y+line_height

     # if ww.customlegend:
     #           pdf.text(10,y,txt=ww.customlegend)
     #           y = y+line_height

     pdf.image(ww.analyzedby,30,250,12,12)
     pdf.line(19,261,36+pdf.get_string_width("Analyzed By (Analyst)"),261)
     pdf.text(26,265,"Analyzed By (Analyst)")
     pdf.image(ww.reviewedby,100,250,12,12)
     pdf.line(126,261,47.5+pdf.get_string_width("Reviewed By (Assistant Manager)"),261)
     pdf.text(87.5,265,"Reviewed By (Assistant Manager)")
     pdf.image(ww.approvedby,165,249,12,12)
     pdf.image(ww.approvedby1,178,249,12,12)
     pdf.line(155,261,165+pdf.get_string_width("Approved By (Lab Manager)"),261)
     pdf.text(160,265,"Approved By (Lab Manager)")


     pdf.set_font("Calibri","B", 9)
     pdf.line(10,267,-10+pdf.w,267)
     pdf.text(10,270,txt="Desclaimer:")
     pdf.set_font("Calibri","", 8)
     pdf.text(10,274,txt="• Report is valid for current batch (sample).")
     pdf.text(10,277.5,txt="• This report is not valid for any publication or judical purpose.")
     pdf.set_y(278.4)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• Envi Tech AL is not responsible for the sample identification and data shared by the client.")
     pdf.set_y(282)
     pdf.set_x(9)
     pdf.multi_cell(110,3,txt="• The sample shall be discarded after five working days unless otherwise instructed.")


     pdf.image('static/assets/ISO-9001_2015-LOGO.png',132,268,19,10)
     if ww.location == 'SEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     if ww.location == 'PEQS':
          pdf.image('static/assets/EPA Punjab logo.jpg',158,259,19,15) 
     if ww.location == 'NEQS':
          pdf.image('static/assets/SEPA-Sindh-LOGO.png',158,259,19,15)
     pdf.image('static/assets/ISO-14001_2015-LOGO.png',182,268,19,10)
     pdf.set_font("Calibri","B", 5)
     pdf.text(132.5,280,txt="(Certificate # 20210131)")
     pdf.text(158,280,txt="(Certificate # 20210131)")
     pdf.text(182,280,txt="(Certificate # 20210131)")

     pdf.set_font("Calibri","", 7)
     pdf.rect(130,281,25,5)
     pdf.text(132,284,txt=ww.doc1)
     pdf.rect(155,281,25,5)
     pdf.text(157,284,txt=ww.doc2)
     pdf.rect(180,281,25,5)
     pdf.text(186.5,284,txt=ww.doc3)



     pdf.output('report.pdf')

     pdf = open('report.pdf', 'rb')
     response = FileResponse(pdf)
     return response

@login_required(login_url="/login")
def drinkingWaterClone(request,pk):
     dw = DrinkingWaterForm.objects.get(id=pk)
     context = {'list':dw}
     return render(request,"drinkingWaterFormClone.html",context)

@login_required(login_url="/login")
def drinkingWaterCloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_dw = DrinkingWaterForm.objects.get(id=pk)
     except DrinkingWaterForm.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          # new_dw = deepcopy(existing_dw)
          existing_dw.location = request.POST['location']
          existing_dw.lab_report_no = request.POST['lab_report_no']
          existing_dw.invoice_bill_no = request.POST['invoice_bill_no']
          existing_dw.reporting_date = request.POST['reporting_date']
          existing_dw.report_to = request.POST['reporting_to']
          existing_dw.address = request.POST['address']
          existing_dw.attention = request.POST['attention']
          existing_dw.email = request.POST['email']
          existing_dw.sample_id = request.POST['sample_id']
          existing_dw.sample_collection_date = request.POST['collection_date']
          existing_dw.sample_description = request.POST['sample_description']
          existing_dw.sample_type = request.POST['sample_type']
          existing_dw.sample_collected_by = request.POST['sample_collected_by']
          existing_dw.date_of_analysis_from = request.POST['date_of_analysis_from']
          existing_dw.date_of_analysis_to = request.POST['date_of_analysis_to']
          existing_dw.test_description = request.POST['test_description']
          existing_dw.select = request.POST.get('water-select')
          existing_dw.water_sr1 = request.POST['water_sr1']
          existing_dw.water_sr2 = request.POST['water_sr2']
          existing_dw.water_sr3 = request.POST['water_sr3']
          existing_dw.water_sr4 = request.POST['water_sr4']
          existing_dw.water_sr5 = request.POST['water_sr5']
          existing_dw.water_sr6 = request.POST['water_sr6']
          existing_dw.water_sr7 = request.POST['water_sr7']
          existing_dw.water_sr8 = request.POST['water_sr8']
          existing_dw.water_sr9 = request.POST['water_sr9']
          existing_dw.water_sr10 = request.POST['water_sr10']
          existing_dw.water_sr11 = request.POST['water_sr11']
          existing_dw.water_sr12 = request.POST['water_sr12']
          existing_dw.water_sr13 = request.POST['water_sr13']
          existing_dw.water_sr14 = request.POST['water_sr14']
          existing_dw.water_sr15 = request.POST['water_sr15']
          existing_dw.water_sr16 = request.POST['water_sr16']
          existing_dw.water_sr17 = request.POST['water_sr17']
          existing_dw.water_sr18 = request.POST['water_sr18']
          existing_dw.water_sr19 = request.POST['water_sr19']
          existing_dw.water_sr20 = request.POST['water_sr20']
          existing_dw.water_sr21 = request.POST['water_sr21']
          existing_dw.water_sr22 = request.POST['water_sr22']
          existing_dw.water_sr23 = request.POST['water_sr23']
          existing_dw.water_sr24 = request.POST['water_sr24']
          existing_dw.water_sr25 = request.POST['water_sr25']
          existing_dw.water_sr26 = request.POST['water_sr26']
          existing_dw.water_sr27 = request.POST['water_sr27']
          existing_dw.water_sr28 = request.POST['water_sr28']
          existing_dw.water_sr29 = request.POST['water_sr29']
          existing_dw.water_sr30 = request.POST['water_sr30']
          existing_dw.water_sr31 = request.POST['water_sr31']
          existing_dw.water_sr32 = request.POST['water_sr32']
          existing_dw.legend_1 = request.POST['legend-1']
          existing_dw.legend_2 = request.POST['legend-2']
          existing_dw.legend_3 = request.POST['legend-3']
          existing_dw.legend_4 = request.POST['legend-4']
          existing_dw.legend_5 = request.POST['legend-5']
          existing_dw.legend_6 = request.POST['legend-6']
          existing_dw.legend_7 = request.POST['legend-7']
          existing_dw.legend_8 = request.POST['legend-8']
          existing_dw.legend_9 = request.POST['legend-9']
          existing_dw.legend_10 = request.POST['legend-10']
          existing_dw.legend_11 = request.POST['legend-11']
          existing_dw.edit_note = request.POST['edit-note']
          existing_dw.custom_legend = request.POST['custom-legend']
          existing_dw.doc_controll_1 = request.POST['doc-con-1']
          existing_dw.doc_controll_2 = request.POST['doc-con-2']
          existing_dw.doc_controll_3 = request.POST['doc-con-3']
          existing_dw.analyzed_by = request.FILES["analyzedby" ]
          existing_dw.reviewed_by = request.FILES["reviewedby" ]
          existing_dw.approved_by = request.FILES["approvedby" ]
          existing_dw.approved_by1 = request.FILES["approvedby1" ]

          existing_dw.id = None
          existing_dw.save()
          id = existing_dw.id
          # id = (DrinkingWaterForm.objects.last()).id
          if "submit_and_view" in request.POST:
            url = f"/view-form/{str(id)}/"
            return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
               return redirect(to='drinkWaterList')
          else:
               return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "drinkingWaterFormClone.html")


def ambientAir2Clone(request,pk):
     existing_form = AmbientAir2.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"ambientAir2Clone.html",context)

def ambientAir2cloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = AmbientAir2.objects.get(id=pk)
     except AmbientAir2.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.lab_rep_no = request.POST['lab_rep_no']
          existing_Form.invoice_no = request.POST['invoice_no']
          existing_Form.report_date = request.POST['report_date']
          existing_Form.report_to = request.POST['report_to']
          existing_Form.address = request.POST['address']
          existing_Form.attention = request.POST['attention']
          existing_Form.email = request.POST['email']
          existing_Form.testId = request.POST['testId']
          existing_Form.test_perf_date = request.POST['test_perf_date']
          existing_Form.test_type = request.POST['test_type']
          existing_Form.test_desc = request.POST['test_desc']
          existing_Form.test_test_perf_by = request.POST['test_test_perf_by']
          existing_Form.sr1_1 = request.POST['sr1_1']
          existing_Form.sr1_2 = request.POST['sr1_2']
          existing_Form.sr1_3 = request.POST['sr1_3']
          existing_Form.sr1_4 = request.POST['sr1_4']
          existing_Form.sr1_5 = request.POST['sr1_5']
          existing_Form.sr1_6 = request.POST['sr1_6']
          existing_Form.sr1_7 = request.POST['sr1_7']
          existing_Form.sr1_8 = request.POST['sr1_8']
          existing_Form.sr1_9 = request.POST['sr1_9']
          existing_Form.sr1_10 = request.POST['sr1_10']
          existing_Form.sr2_0 = request.POST['sr2_0']
          existing_Form.sr2_1 = request.POST['sr2_1']
          existing_Form.sr2_2 = request.POST['sr2_2']
          existing_Form.sr2_3 = request.POST['sr2_3']
          existing_Form.sr2_4 = request.POST['sr2_4']
          existing_Form.sr2_5 = request.POST['sr2_5']
          existing_Form.sr2_6 = request.POST['sr2_6']
          existing_Form.sr2_7 = request.POST['sr2_7']
          existing_Form.sr2_8 = request.POST['sr2_8']
          existing_Form.sr2_9 = request.POST['sr2_9']
          existing_Form.sr3_0 = request.POST['sr3_0']
          existing_Form.sr3_1 = request.POST['sr3_1']
          existing_Form.sr3_2 = request.POST['sr3_2']
          existing_Form.sr3_3 = request.POST['sr3_3']
          existing_Form.sr3_4 = request.POST['sr3_4']
          existing_Form.sr3_5 = request.POST['sr3_5']
          existing_Form.sr3_6 = request.POST['sr3_6']
          existing_Form.sr3_7 = request.POST['sr3_7']
          existing_Form.sr3_8 = request.POST['sr3_8']
          existing_Form.sr3_9 = request.POST['sr3_9']
          existing_Form.sr4_0 = request.POST['sr4_0']
          existing_Form.sr4_1 = request.POST['sr4_1']
          existing_Form.sr4_2 = request.POST['sr4_2']
          existing_Form.sr4_3 = request.POST['sr4_3']
          existing_Form.sr4_4 = request.POST['sr4_4']
          existing_Form.sr4_5 = request.POST['sr4_5']
          existing_Form.sr4_6 = request.POST['sr4_6']
          existing_Form.sr4_7 = request.POST['sr4_7']
          existing_Form.sr4_8 = request.POST['sr4_8']
          existing_Form.sr4_9 = request.POST['sr4_9']
          existing_Form.sr5_0 = request.POST['sr5_0']
          existing_Form.sr5_1 = request.POST['sr5_1']
          existing_Form.sr5_2 = request.POST['sr5_2']
          existing_Form.sr5_3 = request.POST['sr5_3']
          existing_Form.sr5_4 = request.POST['sr5_4']
          existing_Form.sr5_5 = request.POST['sr5_5']
          existing_Form.sr5_6 = request.POST['sr5_6']
          existing_Form.sr5_7 = request.POST['sr5_7']
          existing_Form.sr5_8 = request.POST['sr5_8']
          existing_Form.sr5_9 = request.POST['sr5_9']
          existing_Form.sr6_0 = request.POST['sr6_0']
          existing_Form.sr6_1 = request.POST['sr6_1']
          existing_Form.sr6_2 = request.POST['sr6_2']
          existing_Form.sr6_3 = request.POST['sr6_3']
          existing_Form.sr6_4 = request.POST['sr6_4']
          existing_Form.sr6_5 = request.POST['sr6_5']
          existing_Form.sr6_6 = request.POST['sr6_6']
          existing_Form.sr6_7 = request.POST['sr6_7']
          existing_Form.sr6_8 = request.POST['sr6_8']
          existing_Form.sr6_9 = request.POST['sr6_9']
          existing_Form.sr7_0 = request.POST['sr7_0']
          existing_Form.sr7_1 = request.POST['sr7_1']
          existing_Form.sr7_2 = request.POST['sr7_2']
          existing_Form.sr7_3 = request.POST['sr7_3']
          existing_Form.sr7_4 = request.POST['sr7_4']
          existing_Form.sr7_5 = request.POST['sr7_5']
          existing_Form.sr7_6 = request.POST['sr7_6']
          existing_Form.sr7_7 = request.POST['sr7_7']
          existing_Form.sr7_8 = request.POST['sr7_8']
          existing_Form.sr7_9 = request.POST['sr7_9']
          existing_Form.sr8_0 = request.POST['sr8_0']
          existing_Form.sr8_1 = request.POST['sr8_1']
          existing_Form.sr8_2 = request.POST['sr8_2']
          existing_Form.sr8_3 = request.POST['sr8_3']
          existing_Form.sr8_4 = request.POST['sr8_4']
          existing_Form.sr8_5 = request.POST['sr8_5']
          existing_Form.sr8_6 = request.POST['sr8_6']
          existing_Form.sr8_7 = request.POST['sr8_7']
          existing_Form.sr8_8 = request.POST['sr8_8']
          existing_Form.sr8_9 = request.POST['sr8_9']
          existing_Form.sr9_0 = request.POST['sr9_0']
          existing_Form.sr9_1 = request.POST['sr9_1']
          existing_Form.sr9_2 = request.POST['sr9_2']
          existing_Form.sr9_3 = request.POST['sr9_3']
          existing_Form.sr9_4 = request.POST['sr9_4']
          existing_Form.sr9_5 = request.POST['sr9_5']
          existing_Form.sr9_6 = request.POST['sr9_6']
          existing_Form.sr9_7 = request.POST['sr9_7']
          existing_Form.sr9_8 = request.POST['sr9_8']
          existing_Form.sr9_9 = request.POST['sr9_9']
          existing_Form.sr10_0 = request.POST['sr10_0']
          existing_Form.sr10_1 = request.POST['sr10_1']
          existing_Form.sr10_2 = request.POST['sr10_2']
          existing_Form.sr10_3 = request.POST['sr10_3']
          existing_Form.sr10_4 = request.POST['sr10_4']
          existing_Form.sr10_5 = request.POST['sr10_5']
          existing_Form.sr10_6 = request.POST['sr10_6']
          existing_Form.sr10_7 = request.POST['sr10_7']
          existing_Form.sr10_8 = request.POST['sr10_8']
          existing_Form.sr10_9 = request.POST['sr10_9']
          existing_Form.sr11_0 = request.POST['sr11_0']
          existing_Form.sr11_1 = request.POST['sr11_1']
          existing_Form.sr11_2 = request.POST['sr11_2']
          existing_Form.sr11_3 = request.POST['sr11_3']
          existing_Form.sr11_4 = request.POST['sr11_4']
          existing_Form.sr11_5 = request.POST['sr11_5']
          existing_Form.sr11_6 = request.POST['sr11_6']
          existing_Form.sr11_7 = request.POST['sr11_7']
          existing_Form.sr11_8 = request.POST['sr11_8']
          existing_Form.sr11_9 = request.POST['sr11_9']
          existing_Form.sr12_0 = request.POST['sr12_0']
          existing_Form.sr12_1 = request.POST['sr12_1']
          existing_Form.sr12_2 = request.POST['sr12_2']
          existing_Form.sr12_3 = request.POST['sr12_3']
          existing_Form.sr12_4 = request.POST['sr12_4']
          existing_Form.sr12_5 = request.POST['sr12_5']
          existing_Form.sr12_6 = request.POST['sr12_6']
          existing_Form.sr12_7 = request.POST['sr12_7']
          existing_Form.sr12_8 = request.POST['sr12_8']
          existing_Form.sr12_9 = request.POST['sr12_9']
          existing_Form.sr13_0 = request.POST['sr13_0']
          existing_Form.sr13_1 = request.POST['sr13_1']
          existing_Form.sr13_2 = request.POST['sr13_2']
          existing_Form.sr13_3 = request.POST['sr13_3']
          existing_Form.sr13_4 = request.POST['sr13_4']
          existing_Form.sr13_5 = request.POST['sr13_5']
          existing_Form.sr13_6 = request.POST['sr13_6']
          existing_Form.sr13_7 = request.POST['sr13_7']
          existing_Form.sr13_8 = request.POST['sr13_8']
          existing_Form.sr13_9 = request.POST['sr13_9']
          existing_Form.sr14_0 = request.POST['sr14_0']
          existing_Form.sr14_1 = request.POST['sr14_1']
          existing_Form.sr14_2 = request.POST['sr14_2']
          existing_Form.sr14_3 = request.POST['sr14_3']
          existing_Form.sr14_4 = request.POST['sr14_4']
          existing_Form.sr14_5 = request.POST['sr14_5']
          existing_Form.sr14_6 = request.POST['sr14_6']
          existing_Form.sr14_7 = request.POST['sr14_7']
          existing_Form.sr14_8 = request.POST['sr14_8']
          existing_Form.sr14_9 = request.POST['sr14_9']
          existing_Form.sr15_0 = request.POST['sr15_0']
          existing_Form.sr15_1 = request.POST['sr15_1']
          existing_Form.sr15_2 = request.POST['sr15_2']
          existing_Form.sr15_3 = request.POST['sr15_3']
          existing_Form.sr15_4 = request.POST['sr15_4']
          existing_Form.sr15_5 = request.POST['sr15_5']
          existing_Form.sr15_6 = request.POST['sr15_6']
          existing_Form.sr15_7 = request.POST['sr15_7']
          existing_Form.sr15_8 = request.POST['sr15_8']
          existing_Form.sr15_9 = request.POST['sr15_9']
          existing_Form.sr16_0 = request.POST['sr16_0']
          existing_Form.sr16_1 = request.POST['sr16_1']
          existing_Form.sr16_2 = request.POST['sr16_2']
          existing_Form.sr16_3 = request.POST['sr16_3']
          existing_Form.sr16_4 = request.POST['sr16_4']
          existing_Form.sr16_5 = request.POST['sr16_5']
          existing_Form.sr16_6 = request.POST['sr16_6']
          existing_Form.sr16_7 = request.POST['sr16_7']
          existing_Form.sr16_8 = request.POST['sr16_8']
          existing_Form.sr16_9 = request.POST['sr16_9']
          existing_Form.sr17_0 = request.POST['sr17_0']
          existing_Form.sr17_1 = request.POST['sr17_1']
          existing_Form.sr17_2 = request.POST['sr17_2']
          existing_Form.sr17_3 = request.POST['sr17_3']
          existing_Form.sr17_4 = request.POST['sr17_4']
          existing_Form.sr17_5 = request.POST['sr17_5']
          existing_Form.sr17_6 = request.POST['sr17_6']
          existing_Form.sr17_7 = request.POST['sr17_7']
          existing_Form.sr17_8 = request.POST['sr17_8']
          existing_Form.sr17_9 = request.POST['sr17_9']
          existing_Form.sr18_0 = request.POST['sr18_0']
          existing_Form.sr18_1 = request.POST['sr18_1']
          existing_Form.sr18_2 = request.POST['sr18_2']
          existing_Form.sr18_3 = request.POST['sr18_3']
          existing_Form.sr18_4 = request.POST['sr18_4']
          existing_Form.sr18_5 = request.POST['sr18_5']
          existing_Form.sr18_6 = request.POST['sr18_6']
          existing_Form.sr18_7 = request.POST['sr18_7']
          existing_Form.sr18_8 = request.POST['sr18_8']
          existing_Form.sr18_9 = request.POST['sr18_9']
          existing_Form.sr19_0 = request.POST['sr19_0']
          existing_Form.sr19_1 = request.POST['sr19_1']
          existing_Form.sr19_2 = request.POST['sr19_2']
          existing_Form.sr19_3 = request.POST['sr19_3']
          existing_Form.sr19_4 = request.POST['sr19_4']
          existing_Form.sr19_5 = request.POST['sr19_5']
          existing_Form.sr19_6 = request.POST['sr19_6']
          existing_Form.sr19_7 = request.POST['sr19_7']
          existing_Form.sr19_8 = request.POST['sr19_8']
          existing_Form.sr19_9 = request.POST['sr19_9']
          existing_Form.sr20_0 = request.POST['sr20_0']
          existing_Form.sr20_1 = request.POST['sr20_1']
          existing_Form.sr20_2 = request.POST['sr20_2']
          existing_Form.sr20_3 = request.POST['sr20_3']
          existing_Form.sr20_4 = request.POST['sr20_4']
          existing_Form.sr20_5 = request.POST['sr20_5']
          existing_Form.sr20_6 = request.POST['sr20_6']
          existing_Form.sr20_7 = request.POST['sr20_7']
          existing_Form.sr20_8 = request.POST['sr20_8']
          existing_Form.sr20_9 = request.POST['sr20_9']
          existing_Form.sr21_0 = request.POST['sr21_0']
          existing_Form.sr21_1 = request.POST['sr21_1']
          existing_Form.sr21_2 = request.POST['sr21_2']
          existing_Form.sr21_3 = request.POST['sr21_3']
          existing_Form.sr21_4 = request.POST['sr21_4']
          existing_Form.sr21_5 = request.POST['sr21_5']
          existing_Form.sr21_6 = request.POST['sr21_6']
          existing_Form.sr21_7 = request.POST['sr21_7']
          existing_Form.sr21_8 = request.POST['sr21_8']
          existing_Form.sr21_9 = request.POST['sr21_9']
          existing_Form.sr22_0 = request.POST['sr22_0']
          existing_Form.sr22_1 = request.POST['sr22_1']
          existing_Form.sr21_2 = request.POST['sr21_2']
          existing_Form.sr21_3 = request.POST['sr21_3']
          existing_Form.sr21_4 = request.POST['sr21_4']
          existing_Form.sr21_5 = request.POST['sr21_5']
          existing_Form.sr21_6 = request.POST['sr21_6']
          existing_Form.sr21_7 = request.POST['sr21_7']
          existing_Form.sr21_8 = request.POST['sr21_8']
          existing_Form.sr21_9 = request.POST['sr21_9']
          existing_Form.sr22_0 = request.POST['sr22_0']
          existing_Form.sr22_1 = request.POST['sr22_1']
          existing_Form.sr22_2 = request.POST['sr22_2']
          existing_Form.sr22_3 = request.POST['sr22_3']
          existing_Form.sr22_4 = request.POST['sr22_4']
          existing_Form.sr22_5 = request.POST['sr22_5']
          existing_Form.sr22_6 = request.POST['sr22_6']
          existing_Form.sr22_7 = request.POST['sr22_7']
          existing_Form.sr22_8 = request.POST['sr22_8']
          existing_Form.sr22_9 = request.POST['sr22_9']
          existing_Form.sr23_0 = request.POST['sr23_0']
          existing_Form.sr23_1 = request.POST['sr23_1']
          existing_Form.sr23_2 = request.POST['sr23_2']
          existing_Form.sr23_3 = request.POST['sr23_3']
          existing_Form.sr23_4 = request.POST['sr23_4']
          existing_Form.sr23_5 = request.POST['sr23_5']
          existing_Form.sr23_6 = request.POST['sr23_6']
          existing_Form.sr23_7 = request.POST['sr23_7']
          existing_Form.sr23_8 = request.POST['sr23_8']
          existing_Form.sr23_9 = request.POST['sr23_9']
          existing_Form.sr24_0 = request.POST['sr24_0']
          existing_Form.sr24_1 = request.POST['sr24_1']
          existing_Form.sr24_2 = request.POST['sr24_2']
          existing_Form.sr24_3 = request.POST['sr24_3']
          existing_Form.sr24_4 = request.POST['sr24_4']
          existing_Form.sr24_5 = request.POST['sr24_5']
          existing_Form.sr24_6 = request.POST['sr24_6']
          existing_Form.sr24_7 = request.POST['sr24_7']
          existing_Form.sr24_8 = request.POST['sr24_8']
          existing_Form.sr24_9 = request.POST['sr24_9']
          existing_Form.sr25_0 = request.POST['sr25_0']
          existing_Form.sr25_1 = request.POST['sr25_1']
          existing_Form.sr25_2 = request.POST['sr25_2']
          existing_Form.sr25_3 = request.POST['sr25_3']
          existing_Form.sr25_4 = request.POST['sr25_4']
          existing_Form.sr25_5 = request.POST['sr25_5']
          existing_Form.sr25_6 = request.POST['sr25_6']
          existing_Form.sr25_7 = request.POST['sr25_7']
          existing_Form.sr25_8 = request.POST['sr25_8']
          existing_Form.select = request.POST.get('select')
          existing_Form.legend_1 = request.POST['legend_1']
          existing_Form.legend_2 = request.POST['legend_2']
          existing_Form.legend_3 = request.POST['legend_3']
          existing_Form.legend_4 = request.POST['legend_4']
          existing_Form.legend_5 = request.POST['legend_5']
          existing_Form.legend_6 = request.POST['legend_6']
          existing_Form.legend_7 = request.POST['legend_7']
          existing_Form.legend_8 = request.POST['legend_8']
          existing_Form.legend_9 = request.POST['legend_9']
          existing_Form.legend_10 = request.POST['legend_10']
          existing_Form.legend_11 = request.POST['legend_11']
          existing_Form.edit_note = request.POST['edit_note']
          existing_Form.custom_legend = request.POST['custom_legend']
          existing_Form.doc1 = request.POST['doc1']
          existing_Form.doc2 = request.POST['doc2']
          existing_Form.doc3 = request.POST['doc3']
          existing_Form.analyzedby = request.FILES['analyzedby']
          existing_Form.reviewedby = request.FILES['reviewedby']
          existing_Form.approvedby = request.FILES['approvedby']
          existing_Form.approvedby1 = request.FILES['approvedby1']

          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id

          if "submit_and_view" in request.POST:
            url = f"/ambientAir2-view/{str(id)}/"
            return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
               return redirect(to='ambientAir2List')
          else:
               return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "ambientAir2Clone.html")

def ambientAirClone(request,pk):
     existing_form = AmbientAirForm.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"ambientAirClone.html",context)
def ambientAircloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = AmbientAirForm.objects.get(id=pk)
     except AmbientAirForm.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
            existing_Form.location = request.POST['location']
            existing_Form.ambienAir_lab_report_no1 = request.POST['ambient_Air_lab_report_no']
            existing_Form.ambienAir_invoice_bill_no = request.POST['ambientAir_invoice_no']
            existing_Form.ambientAir_reporting_date = request.POST['ambientAir_rep_date']
            existing_Form.ambientAir_reporting_to = request.POST['ambientAir_rep_to']
            existing_Form.ambientAir_address = request.POST['ambientAir_address']
            existing_Form.ambientAir_attention = request.POST['ambientAir_attention']
            existing_Form.ambientAir_email = request.POST['ambientAir_email']
            existing_Form.ambientAir_test_id = request.POST['ambientAir_testid']
            existing_Form.ambientAir_test_perf_date = request.POST['ambientAir_test_perf_date']
            existing_Form.ambientAir_test_type_location = request.POST['ambientAir_testtype_location']
            existing_Form.ambientAir_test_perf_by = request.POST['ambientAir_test_perf_by']
            existing_Form.ambienAir_test_desc = request.POST['ambientAir_test_desc']
            existing_Form.ambienAir_select = request.POST['select']
            existing_Form.ambientAir_sr1 = request.POST['ambientAir_sr1']
            existing_Form.ambientAir_sr2 = request.POST['ambientAir_sr2']
            existing_Form.ambientAir_sr3 = request.POST['ambientAir_sr3']
            existing_Form.ambientAir_sr4 = request.POST['ambientAir_sr4']
            existing_Form.ambientAir_sr5 = request.POST['ambientAir_sr5']
            existing_Form.ambientAir_sr6 = request.POST['ambientAir_sr6']
            existing_Form.ambientAir_sr7 = request.POST['ambientAir_sr7']
            existing_Form.ambientAir_sr8 = request.POST['ambientAir_sr8']
            existing_Form.ambientAir_sr9 = request.POST['ambientAir_sr9']
            existing_Form.ambientAir_sr10 = request.POST['ambientAir_sr10']
            existing_Form.ambientAir_sr11 = request.POST['ambientAir_sr11']
            existing_Form.ambientAir_sr12 = request.POST['ambientAir_sr12']
            existing_Form.ambientAir_sr13 = request.POST['ambientAir_sr13']
            existing_Form.ambientAir_sr14 = request.POST['ambientAir_sr14']
            existing_Form.ambientAir_legend_1 = request.POST['ambientAir-legend-1']
            existing_Form.ambientAir_legend_2 = request.POST['ambientAir-legend-2']
            existing_Form.ambientAir_legend_3 = request.POST['ambientAir-legend-3']
            existing_Form.ambientAir_legend_4 = request.POST['ambientAir-legend-4']
            existing_Form.ambientAir_legend_5 = request.POST['ambientAir-legend-5']
            existing_Form.ambientAir_legend_6 = request.POST['ambientAir-legend-6']
            existing_Form.ambientAir_edit_note = request.POST['ambientAir_editNote']
            existing_Form.ambientAir_custom_legend = request.POST['ambientAir_customlegend']
            existing_Form.ambientAir_doc_con_1 = request.POST['ambientAir_doc1']
            existing_Form.ambientAir_doc_con_2 = request.POST['ambientAir_doc2']
            existing_Form.ambientAir_doc_con_3 = request.POST['ambientAir_doc3']
            existing_Form.ambientAir_analyzed_by = request.FILES["ambientAir_analyzedby" ]
            existing_Form.ambientAir_reviewd_by = request.FILES["ambientAir_reviewedby" ]
            existing_Form.ambientAir_approved_by = request.FILES["ambientAir_approvedby" ]
            existing_Form.ambientAir_approved_by1 = request.FILES["ambientAir_approvedby1" ]

            existing_Form.id = None
            existing_Form.save()
            id = existing_Form.id
            if "update_and_view" in request.POST:
               url = f"/ambientAir-view/{str(id)}/"
               return redirect(to=url)
          
            if "submit" in request.POST:
               # context = {'list': new_dw}
                 return redirect(to='ambientAirList')
            else:
                 return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "ambientAirClone.html")

def GaseousFormclone(request,pk):
     existing_form = GaseousEmissionForm.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"GaseousEmissionClone.html",context) 

def GaseousFormcloneSave(request,pk):         
     try:
        # Fetch the existing form instance by ID
         existing_Form = GaseousEmissionForm.objects.get(id=pk)
     except GaseousEmissionForm.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
        existing_Form.location = request.POST['location']
        existing_Form.GasEm_lab_report_no1 = request.POST['GasEm-lab_report_no']
        existing_Form.GasEm_invoice_bill_no = request.POST['GasEm-invoice-bill-no']
        existing_Form.GaseEm_reporting_date = request.POST['GasEm-reporting-date']
        existing_Form.GaseEm_reporting_to = request.POST['GasEm-report-to']
        existing_Form.GaseEm_address = request.POST['GasEm-address']
        existing_Form.GaseEm_attention = request.POST['GasEm-attention']
        existing_Form.GaseEm_email = request.POST['GasEm-email']
        existing_Form.GaseEm_test_id = request.POST['GasEm-test-id']
        existing_Form.GaseEm_test_perf_date = request.POST['GasEm-test-perf-date']
        existing_Form.GaseEm_test_type = request.POST['GasEm-test-type']
        existing_Form.GaseEm_test_perf_by = request.POST['GasEm-test-perf-by']
        existing_Form.GasEm_test_desc = request.POST['GasEm-test-desc']
        existing_Form.GaseEm_types = request.POST.get('GasEm-type')
        existing_Form.GaseEm_select = request.POST.get('select')
        existing_Form.GaseEm_sr1 = request.POST['GasEm-sr1']
        existing_Form.GaseEm_sr2 = request.POST['GasEm-sr2']
        existing_Form.GaseEm_sr3 = request.POST['GasEm-sr3']
        existing_Form.GaseEm_sr4 = request.POST['GasEm-sr4']
        existing_Form.GaseEm_sr5 = request.POST['GasEm-sr5']
        existing_Form.GaseEm_sr6 = request.POST['GasEm-sr6']
        existing_Form.GaseEm_sr7 = request.POST['GasEm-sr7']
        existing_Form.GaseEm_sr8 = request.POST['GasEm-sr8']
        existing_Form.GaseEm_sr9 = request.POST['GasEm-sr9']
        existing_Form.GaseEm_sr10 = request.POST['GasEm-sr10']
        existing_Form.GaseEm_sr11 = request.POST['GasEm-sr11']
        existing_Form.GaseEm_sr12 = request.POST['GasEm-sr12']
        existing_Form.GaseEm_sr13 = request.POST['GasEm-sr13']
        existing_Form.GaseEm_sr14 = request.POST['GasEm-sr14']
        existing_Form.GaseEm_sr15 = request.POST['GasEm-sr15']
        existing_Form.GaseEm_sr16 = request.POST['GasEm-sr16']
        existing_Form.GaseEm_sr17 = request.POST['GasEm-sr17']
        existing_Form.GaseEm_sr18 = request.POST['GasEm-sr18']
        existing_Form.GaseEm_sr19 = request.POST['GasEm-sr19']
        existing_Form.GaseEm_sr20 = request.POST['GasEm-sr20']
        existing_Form.GaseEm_sr21 = request.POST['GasEm-sr21']
        existing_Form.GaseEm_sr22 = request.POST['GasEm-sr22']
        existing_Form.GaseEm_legend_1 = request.POST['GasEm-legend-1']
        existing_Form.GaseEm_legend_2 = request.POST['GasEm-legend-2']
        existing_Form.GaseEm_legend_3 = request.POST['GasEm-legend-3']
        existing_Form.GaseEm_legend_4 = request.POST['GasEm-legend-4']
        existing_Form.GaseEm_legend_5 = request.POST['GasEm-legend-5']
        existing_Form.GaseEm_legend_6 = request.POST['GasEm-legend-6']
        existing_Form.GaseEm_legend_7 = request.POST['GasEm-legend-7']
        existing_Form.GaseEm_legend_8 = request.POST['GasEm-legend-8']
        existing_Form.GaseEm_legend_9 = request.POST['GasEm-legend-9']
        existing_Form.GaseEm_legend_10 = request.POST['GasEm-legend-10']
        existing_Form.GaseEm_legend_11 = request.POST['GasEm-legend-11']
        existing_Form.GaseEm_edit_note = request.POST['GasEm-editnote']
        existing_Form.GaseEm_custom_legend = request.POST['GasEm-custom-legend']
        existing_Form.GaseEm_doc_con_1 = request.POST['GasEm-doc1']
        existing_Form.GaseEm_doc_con_2 = request.POST['GasEm-doc2']
        existing_Form.GaseEm_doc_con_3 = request.POST['GasEm-doc3']
        existing_Form.GaseEm_analyzed_by = request.FILES["GasEm-analyzedby" ]
        existing_Form.GaseEm_reviewd_by = request.FILES["GasEm-reviewedby" ]
        existing_Form.GaseEm_approved_by = request.FILES["GasEm-approvedby" ]
        existing_Form.GaseEm_approved_by1 = request.FILES["GasEm-approvedby1" ]

        existing_Form.id = None
        existing_Form.save()
        id = existing_Form.id
        if "submit_and_view" in request.POST:
            url = f"/GaseousForm-view-form/{str(id)}/"
            return redirect(to=url)
          
        if "submit" in request.POST:
               # context = {'list': new_dw}
            return redirect(to='gaseousEmissionList')
        else:
            return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "gaseousEmissionClone.html")

def luxFormclone(request,pk):
     existing_form = LuxAnalysisForm.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"luxClone.html",context) 

def luxFormcloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = LuxAnalysisForm.objects.get(id=pk)
     except LuxAnalysisForm.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.lux_lab_report_no = request.POST['lux_lab_rep_no']
          existing_Form.lux_invoice_no = request.POST['lux_invoice_no']
          existing_Form.lux_report_date = request.POST['lux_report_date']
          existing_Form.lux_report_to = request.POST['lux_report_to']
          existing_Form.lux_address = request.POST['lux-address']
          existing_Form.lux_attention = request.POST['lux_attention']
          existing_Form.lux_email = request.POST['lux_email']
          existing_Form.lux_testId = request.POST['lux_testId']
          existing_Form.lux_test_perf_date = request.POST['lux_test_perf_date']
          existing_Form.lux_test_type = request.POST['lux_test_type']
          existing_Form.lux_test_perfBy = request.POST['lux_test_perf_by']
          existing_Form.lux_test_desc = request.POST['lux_test_desc']
          existing_Form.lux_parameters_1 = request.POST['lux_parameters_1']
          existing_Form.lux_result_1 = request.POST['lux_result_1']
          existing_Form.lux_parameters_2 = request.POST['lux_parameters_2']
          existing_Form.lux_result_2 = request.POST['lux_result_2']
          existing_Form.lux_parameters_3 = request.POST['lux_parameters_3']
          existing_Form.lux_result_3 = request.POST['lux_result_3']
          existing_Form.lux_parameters_4 = request.POST['lux_parameters_4']
          existing_Form.lux_result_4 = request.POST['lux_result_4']
          existing_Form.lux_parameters_5 = request.POST['lux_parameters_5']
          existing_Form.lux_result_5 = request.POST['lux_result_5']
          existing_Form.lux_parameters_6 = request.POST['lux_parameters_6']
          existing_Form.lux_result_6 = request.POST['lux_result_6']
          existing_Form.lux_parameters_7 = request.POST['lux_parameters_7']
          existing_Form.lux_result_7 = request.POST['lux_result_7']
          existing_Form.lux_parameters_8 = request.POST['lux_parameters_8']
          existing_Form.lux_result_8 = request.POST['lux_result_8']
          existing_Form.lux_parameters_9 = request.POST['lux_parameters_9']
          existing_Form.lux_result_9 = request.POST['lux_result_9']
          existing_Form.lux_parameters_10 = request.POST['lux_parameters_10']
          existing_Form.lux_result_10 = request.POST['lux_result_10']
          existing_Form.lux_parameters_11 = request.POST['lux_parameters_11']
          existing_Form.lux_result_11 = request.POST['lux_result_11']
          existing_Form.lux_parameters_12 = request.POST['lux_parameters_12']
          existing_Form.lux_result_12 = request.POST['lux_result_12']
          existing_Form.lux_parameters_13 = request.POST['lux_parameters_13']
          existing_Form.lux_result_13 = request.POST['lux_result_13']
          existing_Form.lux_legend_1 = request.POST['lux-legend-1']
          existing_Form.lux_legend_2 = request.POST['lux-legend-2']
          existing_Form.lux_legend_3 = request.POST['lux-legend-3']
          existing_Form.lux_legend_4 = request.POST['lux-legend-4']
          existing_Form.lux_legend_5 = request.POST['lux-legend-5']
          existing_Form.lux_legend_6 = request.POST['lux-legend-6']
          existing_Form.lux_legend_7 = request.POST['lux-legend-7']
          existing_Form.lux_legend_8 = request.POST['lux-legend-8']
          existing_Form.lux_legend_9 = request.POST['lux-legend-9']
          existing_Form.lux_legend_10 = request.POST['lux-legend-10']
          existing_Form.lux_legend_11 = request.POST['lux-legend-11']
          existing_Form.lux_edit_note = request.POST['lux_edit_note']
          existing_Form.lux_custom_legend = request.POST['lux_custom_legend']
          existing_Form.lux_doc_con1 = request.POST['lux_doc_con1']
          existing_Form.lux_doc_con2 = request.POST['lux_doc_con2']
          existing_Form.lux_doc_con3 = request.POST['lux_doc_con3']
          existing_Form.lux_analyzedby = request.FILES['lux-analyzedby']
          existing_Form.lux_reviewedby = request.FILES['lux-reviewedby']
          existing_Form.lux_approvedby = request.FILES['lux-approvedby']
          existing_Form.lux_approvedby1 = request.FILES['lux-approvedby1']

          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/luxAnalysisReport/{str(id)}/"
              return redirect(to=url)
          
          if "submit" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='luxAnalysisList')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "luxClone.html")
          

def machineOilclone(request,pk):
     existing_form = MachineOilForm.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"machineOilClone.html",context)

def machineOilcloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = MachineOilForm.objects.get(id=pk)
     except MachineOilForm.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.machine_lab_rep_no = request.POST['machine_lab_rep_no']
          existing_Form.machine_invoice_no = request.POST['machine_invoice_no']
          existing_Form.machine_rep_date = request.POST['machine_rep_date']
          existing_Form.machine_report_to = request.POST['machine_report_to']
          existing_Form.machine_address = request.POST['machine_address']
          existing_Form.machine_attention = request.POST['machine_attention']
          existing_Form.machine_email = request.POST['machine_email']
          existing_Form.machine_sampleId = request.POST['machine_sampleId']
          existing_Form.machine_sample_col_date = request.POST['machine_sample_col_date']
          existing_Form.machine_sample_desc = request.POST['machine_sample_desc']
          existing_Form.machine_sample_type = request.POST['machine_sample_type']
          existing_Form.machine_sample_col_by = request.POST['machine_sample_col_by']
          existing_Form.machine_test_desc = request.POST['machine_test_desc']
          existing_Form.machine_sr1 = request.POST['machine_sr1']
          existing_Form.machine_sr2 = request.POST['machine_sr2']
          existing_Form.machine_sr3 = request.POST['machine_sr3']
          existing_Form.machine_sr4 = request.POST['machine_sr4']
          existing_Form.machine_sr5 = request.POST['machine_sr5']
          existing_Form.machine_sr6 = request.POST['machine_sr6']
          existing_Form.machine_sr7 = request.POST['machine_sr7']
          existing_Form.machine_sr8 = request.POST['machine_sr8']
          existing_Form.machine_sr9 = request.POST['machine_sr9']
          existing_Form.machine_sr10 = request.POST['machine_sr10']
          existing_Form.machine_sr11 = request.POST['machine_sr11']
          existing_Form.machine_sr12 = request.POST['machine_sr12']
          existing_Form.machine_sr13 = request.POST['machine_sr13']
          existing_Form.machine_sr14 = request.POST['machine_sr14']
          existing_Form.machine_sr15 = request.POST['machine_sr15']
          existing_Form.machine_sr16 = request.POST['machine_sr16']
          existing_Form.machine_legend_1 = request.POST['machine_legend-1']
          existing_Form.machine_legend_2 = request.POST['machine_legend-2']
          existing_Form.custom_legend = request.POST['custom_legend']
          existing_Form.machine_edit_note = request.POST['machine_edit_note']
          existing_Form.machine_custom_legend = request.POST['machine_custom_legend']
          existing_Form.machine_doc1 = request.POST['machine_doc1']
          existing_Form.machine_doc2 = request.POST['machine_doc2']
          existing_Form.machine_doc3 = request.POST['machine_doc3']
          existing_Form.machine_analyzedby = request.FILES['machine_analyzedby']
          existing_Form.machine_reviewedby = request.FILES['machine_reviewedby']
          existing_Form.machine_approvedby = request.FILES['machine_approvedby']
          existing_Form.machine_approvedby1 = request.FILES['machine_approvedby']


          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/machineOil-view/{str(id)}/"
              return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='machineOilList')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "machineOilClone.html")


def microbialclone(request,pk):
     existing_form = MicrobialAnalysis.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"microBialClone.html",context)

def microbialcloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = MicrobialAnalysis.objects.get(id=pk)
     except MicrobialAnalysis.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.micro_lab_report_no = request.POST['micro_lab_report_no']
          existing_Form.micro_invoice_bill = request.POST['micro_invoice_bill']
          existing_Form.micro_rep_date = request.POST['micro_rep_date']
          existing_Form.micro_rep_to = request.POST['micro_rep_to']
          existing_Form.micro_address = request.POST['micro_address']
          existing_Form.micro_attention = request.POST['micro_attention']
          existing_Form.micro_email = request.POST['micro_email']
          existing_Form.micro_sampleId = request.POST['micro_sampleId']
          existing_Form.micro_sample_col_date = request.POST['micro_sample_col_date']
          existing_Form.micro_sample_desc = request.POST['micro_sample_desc']
          existing_Form.micro_sample_type = request.POST['micro_sample_type']
          existing_Form.micro_sample_col_by = request.POST['micro_sample_col_date']
          existing_Form.micro_date_analysis = request.POST['micro_date_analysis']
          existing_Form.micro_test_desc = request.POST['micro_test_desc']
          existing_Form.micro_sr1 = request.POST['micro_sr1']
          existing_Form.micro_sr2 = request.POST['micro_sr2']
          existing_Form.micro_sr3 = request.POST['micro_sr3']
          existing_Form.micro_sr4 = request.POST['micro_sr4']
          existing_Form.micro_sr5 = request.POST['micro_sr5']
          existing_Form.micro_sr6 = request.POST['micro_sr6']
          existing_Form.micro_legend_1 = request.POST['micro_legend_1']
          existing_Form.micro_legend_2 = request.POST['micro_legend_2']
          existing_Form.micro_editnote = request.POST['micro_editnote']
          existing_Form.micro_custom_legend = request.POST['micro_custom_legend']
          existing_Form.micro_doc1 = request.POST['micro_doc1']
          existing_Form.micro_doc2 = request.POST['micro_doc2']
          existing_Form.micro_doc3 = request.POST['micro_doc3']
          existing_Form.micro_analyzedby = request.FILES['micro_analyzedby']
          existing_Form.micro_reviewedby = request.FILES['micro_reviewedby']
          existing_Form.micro_approvedby = request.FILES['micro_approvedby']
          existing_Form.micro_approvedby1 = request.FILES['micro_approvedby1']


          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/microbial-view/{str(id)}/"
              return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='microbialList')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "microBialClone.html")

def noiseAnalysisclone(request,pk):
     existing_form = NoiseAnalysis.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"noiseAnalysisClone.html",context)

def noiseAnalysiscloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = NoiseAnalysis.objects.get(id=pk)
     except NoiseAnalysis.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.lab_rep_no = request.POST['lab_rep_no']
          existing_Form.invoice_no = request.POST['invoice_no']
          existing_Form.rep_date = request.POST['rep_date']
          existing_Form.report_to = request.POST['report_to']
          existing_Form.address = request.POST['address']
          existing_Form.attention = request.POST['attention']
          existing_Form.email = request.POST['email']
          existing_Form.testId = request.POST['testId']
          existing_Form.test_perf_date = request.POST['test_perf_date']
          existing_Form.test_type = request.POST['test_type']
          existing_Form.test_perf_by = request.POST['test_perf_by']
          existing_Form.test_desc = request.POST['test_desc']
          existing_Form.select = request.POST.get('select')
          existing_Form.select1 = request.POST.get('select1')
          existing_Form.r1 = request.POST['r1']
          existing_Form.r1_1 = request.POST['r1_1']
          existing_Form.r2 = request.POST['r2']
          existing_Form.r2_2 = request.POST['r2_2']
          existing_Form.r3 = request.POST['r3']
          existing_Form.r3_3 = request.POST['r3_3']
          existing_Form.r4 = request.POST['r4']
          existing_Form.r4_4 = request.POST['r4_4']
          existing_Form.r5 = request.POST['r5']
          existing_Form.r5_5 = request.POST['r5_5']
          existing_Form.r6 = request.POST['r6']
          existing_Form.r6_6 = request.POST['r6_6']
          existing_Form.r7 = request.POST['r7']
          existing_Form.r7_7 = request.POST['r7_7']
          existing_Form.r8 = request.POST['r8']
          existing_Form.r8_8 = request.POST['r8_8']
          existing_Form.r9 = request.POST['r9']
          existing_Form.r9_9 = request.POST['r9_9']
          existing_Form.r10 = request.POST['r10']
          existing_Form.r10_10 = request.POST['r10_10']
          existing_Form.r11 = request.POST['r11']
          existing_Form.r11_11 = request.POST['r11_11']
          existing_Form.r12 = request.POST['r12']
          existing_Form.r12_12 = request.POST['r12_12']
          existing_Form.r13 = request.POST['r13']
          existing_Form.r13_13 = request.POST['r13_13']
          existing_Form.legend_1 = request.POST['legend_1']
          existing_Form.legend_2 = request.POST['legend_2']
          existing_Form.legend_3 = request.POST['legend_3']
          existing_Form.legend_4 = request.POST['legend_4']
          existing_Form.legend_5 = request.POST['legend_5']
          existing_Form.legend_6 = request.POST['legend_6']
          existing_Form.legend_7 = request.POST['legend_7']
          existing_Form.legend_8 = request.POST['legend_8']
          existing_Form.legend_9 = request.POST['legend_9']
          existing_Form.legend_10 = request.POST['legend_10']
          existing_Form.legend_11 = request.POST['legend_11']
          existing_Form.editNote = request.POST['editNote']
          existing_Form.customlegend = request.POST['customlegend']
          existing_Form.doc1 = request.POST['doc1']
          existing_Form.doc2 = request.POST['doc2']
          existing_Form.doc3 = request.POST['doc3']
          existing_Form.analyzedby = request.FILES['analyzedby']
          existing_Form.reviewedby = request.FILES['reviewedby']
          existing_Form.approvedby = request.FILES['approvedby']
          existing_Form.approvedby1 = request.FILES['approvedby1']


          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/noiseAnalysis-view/{str(id)}/"
              return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='noiseAnalysisList')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "noiseAnalysisClone.html")
          

def packingPolyclone(request,pk):
     existing_form = PackingPolyBagForm.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"packingPolyClone.html",context)

def packingPolycloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = PackingPolyBagForm.objects.get(id=pk)
     except PackingPolyBagForm.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.pack_lab_rep_no = request.POST['pack_lab_rep_no']
          existing_Form.pack_invoice = request.POST['pack_invoice']
          existing_Form.pack_rep_date = request.POST['pack_rep_date']
          existing_Form.pack_rep_to = request.POST['pack_rep_to']
          existing_Form.pack_address = request.POST['pack_address']
          existing_Form.pack_attention = request.POST['pack_attention']
          existing_Form.pack_email = request.POST['pack_email']
          existing_Form.pack_sampleId = request.POST['pack_sampleId']
          existing_Form.pack_sample_colc_date = request.POST['pack_sample_colc_date']
          existing_Form.pack_sample_desc = request.POST['pack_sample_desc']
          existing_Form.pack_sample_type = request.POST['pack_sample_type']
          existing_Form.pack_sample_colc_by = request.POST['pack_sample_colc_by']
          existing_Form.pack_test_desc = request.POST['pack_test_desc']
          existing_Form.pack_sr1 = request.POST['pack_sr1']
          existing_Form.pack_legend_1 = request.POST['pack-legend-1']
          existing_Form.pack_edit_note = request.POST['pack_edit_note']
          existing_Form.pack_custom_legend = request.POST['pack_custom_legend']
          existing_Form.doc_con1 = request.POST['doc_con1']
          existing_Form.doc_con2 = request.POST['doc_con2']
          existing_Form.doc_con3 = request.POST['doc_con3']
          existing_Form.pack_analyzed_by = request.FILES['pack-analyzedby']
          existing_Form.pack_reviewed_by = request.FILES['pack-reviewedby']
          existing_Form.pack_approved_by = request.FILES['pack-approvedby']
          existing_Form.pack_approved_by1 = request.FILES['pack-approvedby1']


          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/packingpolybag-view/{str(id)}/"
              return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='packingPolyBagList')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "packingPolyClone.html")


def vehicularEmissionclone(request,pk):
     existing_form = VehiculEmissionForm.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"vehicularEmissionClone.html",context)

def vehicularEmissioncloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = VehiculEmissionForm.objects.get(id=pk)
     except VehiculEmissionForm.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == "POST":
          existing_Form.location = request.POST['location']
          existing_Form.vehEm_lab_report_no = request.POST['vehEm_lab_report_no']
          existing_Form.vehEm_invoice_no = request.POST['vehEm_invoice_no']
          existing_Form.vehEm_report_date = request.POST['vehEm_report_date']
          existing_Form.vehEm_report_to = request.POST['vehEm_report_to']
          existing_Form.vehEm_address = request.POST['vehEm_address']
          existing_Form.vehEm_attention = request.POST['vehEm_attention']
          existing_Form.vehEm_email = request.POST['vehEm_email']
          existing_Form.vehEm_testId = request.POST['vehEm_testId']
          existing_Form.vehEm_test_perf_date = request.POST['vehEm_test_perf_date']
          existing_Form.vehEm_test_type = request.POST['vehEm_test_type']
          existing_Form.vehEm_test_perfBy = request.POST['vehEm_test_perfBy']
          existing_Form.vehEm_test_desc = request.POST['vehEm_test_desc']
          existing_Form.select = request.POST['select']
          existing_Form.vehEm_sr1 = request.POST['vehEm_sr1']
          existing_Form.vehEm_sr2 = request.POST['vehEm_sr2']
          existing_Form.vehEm_sr3 = request.POST['vehEm_sr3']
          existing_Form.vehEm_legend_1 = request.POST['vehEm-legend-1']
          existing_Form.vehEm_legend_2 = request.POST['vehEm-legend-2']
          existing_Form.vehEm_legend_3 = request.POST['vehEm-legend-3']
          existing_Form.vehEm_legend_4 = request.POST['vehEm-legend-4']
          existing_Form.vehEm_legend_5 = request.POST['vehEm-legend-5']
          existing_Form.vehEm_legend_6 = request.POST['vehEm-legend-6']
          existing_Form.vehEm_legend_7 = request.POST['vehEm-legend-7']
          existing_Form.vehEm_legend_8 = request.POST['vehEm-legend-8']
          existing_Form.vehEm_legend_9 = request.POST['vehEm-legend-9']
          existing_Form.vehEm_legend_10 = request.POST['vehEm-legend-10']
          existing_Form.vehEm_legend_11 = request.POST['vehEm-legend-11']
          existing_Form.vehEm_edit_note = request.POST['vehEm_edit_note']
          existing_Form.vehEm_custom_legend = request.POST['vehEm_custom_legend']
          existing_Form.vehEm_doc_con1 = request.POST['vehEm_doc-con1']
          existing_Form.vehEm_doc_con2 = request.POST['vehEm_doc-con2']
          existing_Form.vehEm_doc_con3 = request.POST['vehEm_doc-con3']
          existing_Form.vehEm_analyzedby = request.FILES['vehEm-analyzedby']
          existing_Form.vehEm_reviewedby = request.FILES['vehEm-reviewedby']
          existing_Form.vehEm_approvedby = request.FILES['vehEm-approvedby']
          existing_Form.vehEm_approvedby1 = request.FILES['vehEm-approvedby1']


          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/vehicularEmission-view/{str(id)}/"
              return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='vehicularEmissionList')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "vehicularEmissionClone.html")


def viscousLiquidclone(request,pk):
     existing_form = ViscousLiquid.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"viscousLiquidClone.html",context)

def viscousLiquidcloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = ViscousLiquid.objects.get(id=pk)
     except ViscousLiquid.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.lab_rep_no = request.POST['lab_rep_no']
          existing_Form.invoice_no = request.POST['invoice_no']
          existing_Form.report_date = request.POST['report_date']
          existing_Form.report_to = request.POST['report_to']
          existing_Form.address = request.POST['address']
          existing_Form.Attention = request.POST['Attention']
          existing_Form.Email = request.POST['Email']
          existing_Form.sampleId = request.POST['sampleId']
          existing_Form.sample_Col_date = request.POST['sample_Col_date']
          existing_Form.sample_Desc = request.POST['sample_Desc']
          existing_Form.sample_type = request.POST['sample_type']
          existing_Form.sample_col_by = request.POST['sample_col_by']
          existing_Form.date_of_analysis = request.POST['date_of_analysis']
          existing_Form.test_desc = request.POST['test_desc']
          existing_Form.viscous_select = request.POST.get('select')
          existing_Form.sr1 = request.POST['sr1']
          existing_Form.legend_1 = request.POST['legend_1']
          existing_Form.legend_2 = request.POST['legend_2']
          existing_Form.edit_note = request.POST['edit_note']
          existing_Form.custom_legend = request.POST['custom_legend']
          existing_Form.doc1 = request.POST['doc1']
          existing_Form.doc2 = request.POST['doc2']
          existing_Form.doc3 = request.POST['doc3']
          existing_Form.analyzedby = request.FILES['analyzedby']
          existing_Form.reviewedby = request.FILES['reviewedby']
          existing_Form.approvedby = request.FILES['approvedby']
          existing_Form.approvedby1 = request.FILES['approvedby1']


          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/viscousLiquid-view/{str(id)}/"
              return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='viscousLiquidList')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "viscousLiquidClone.html")


def wasteWater2clone(request,pk):
     existing_form = WasteWaterForm2.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"WasteWaterForm2Clone.html",context)

def wasteWater2cloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = WasteWaterForm2.objects.get(id=pk)
     except WasteWaterForm2.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
          existing_Form.location = request.POST['location']
          existing_Form.lab_rep_no = request.POST['lab_rep_no']
          existing_Form.invoice_no = request.POST['invoice_no']
          existing_Form.repo_date = request.POST['repo_date']
          existing_Form.report_to = request.POST['report_to']
          existing_Form.address = request.POST['address']
          existing_Form.attention = request.POST['attention']
          existing_Form.email = request.POST['email']
          existing_Form.sampleId = request.POST['sampleId']
          existing_Form.sample_Col_date = request.POST['sample_Col_date']
          existing_Form.sample_desc = request.POST['sample_desc']
          existing_Form.sampling_method = request.POST['sampling_method']
          existing_Form.sample_type = request.POST['sample_type']
          existing_Form.sample_collected_by = request.POST['sample_collected_by']
          existing_Form.date_of_analysis = request.POST['date_of_analysis']
          existing_Form.test_description = request.POST['test_description']
          existing_Form.select = request.POST.get('select')
          existing_Form.result_1 = request.POST['result_1']
          existing_Form.result_1_1 = request.POST['result_1_1']
          existing_Form.result_2 = request.POST['result_2']
          existing_Form.result_2_2 = request.POST['result_2_2']
          existing_Form.result_3 = request.POST['result_3']
          existing_Form.result_3_3 = request.POST['result_3_3']
          existing_Form.result_4 = request.POST['result_4']
          existing_Form.result_4_4 = request.POST['result_4_4']
          existing_Form.result_5 = request.POST['result_5']
          existing_Form.result_5_5 = request.POST['result_5_5']
          existing_Form.result_6 = request.POST['result_6']
          existing_Form.result_6_6 = request.POST['result_6_6']
          existing_Form.result_7 = request.POST['result_7']
          existing_Form.result_7_7 = request.POST['result_7_7']
          existing_Form.metho_select = request.POST.get('metho_select')
          existing_Form.result_8 = request.POST['result_8']
          existing_Form.result_8_8 = request.POST['result_8_8']
          existing_Form.result_9 = request.POST['result_9']
          existing_Form.result_9_9 = request.POST['result_9_9']
          existing_Form.result_10 = request.POST['result_10']
          existing_Form.result_10_10 = request.POST['result_10_10']
          existing_Form.result_11 = request.POST['result_11']
          existing_Form.result_11_11= request.POST['result_11_11']
          existing_Form.result_12 = request.POST['result_12']
          existing_Form.result_12_12 = request.POST['result_12_12']
          existing_Form.result_13 = request.POST['result_13']
          existing_Form.result_13_13 = request.POST['result_13_13']
          existing_Form.result_14 = request.POST['result_14']
          existing_Form.result_14_14 = request.POST['result_14_14']
          existing_Form.result_15 = request.POST['result_15']
          existing_Form.result_15_15 = request.POST['result_15_15']
          existing_Form.result_16 = request.POST['result_16']
          existing_Form.result_16_16 = request.POST['result_16_16']
          existing_Form.result_17 = request.POST['result_17']
          existing_Form.result_17_17 = request.POST['result_17_17']
          existing_Form.result_18 = request.POST['result_18']
          existing_Form.result_18_18 = request.POST['result_18_18']
          existing_Form.result_19 = request.POST['result_19']
          existing_Form.result_19_19 = request.POST['result_19_19']
          existing_Form.result_20 = request.POST['result_20']
          existing_Form.result_20_20 = request.POST['result_20_20']
          existing_Form.result_21 = request.POST['result_21']
          existing_Form.result_21_21 = request.POST['result_21_21']
          existing_Form.result_22 = request.POST['result_22']
          existing_Form.result_22_22 = request.POST['result_22_22']
          existing_Form.result_23 = request.POST['result_23']
          existing_Form.result_23_23 = request.POST['result_23_23']
          existing_Form.result_24 = request.POST['result_24']
          existing_Form.result_24_24 = request.POST['result_24_24']
          existing_Form.result_25 = request.POST['result_25']
          existing_Form.result_25_25 = request.POST['result_25_25']
          existing_Form.result_26 = request.POST['result_26']
          existing_Form.result_26_26 = request.POST['result_26_26']
          existing_Form.result_27 = request.POST['result_27']
          existing_Form.result_27_27 = request.POST['result_27_27']
          existing_Form.result_28 = request.POST['result_28']
          existing_Form.result_28_28 = request.POST['result_28_28']
          existing_Form.result_29 = request.POST['result_29']
          existing_Form.result_29_29 = request.POST['result_29_29']
          existing_Form.result_30 = request.POST['result_30']
          existing_Form.result_30_30 = request.POST['result_30_30']
          existing_Form.result_31 = request.POST['result_31']
          existing_Form.result_31_31 = request.POST['result_31_31']
          existing_Form.result_32 = request.POST['result_32']
          existing_Form.result_32_32 = request.POST['result_32_32']
          existing_Form.legend_1 = request.POST['legend_1']
          existing_Form.legend_2 = request.POST['legend_2']
          existing_Form.legend_3 = request.POST['legend_3']
          existing_Form.legend_4 = request.POST['legend_4']
          existing_Form.legend_5 = request.POST['legend_5']
          existing_Form.legend_6 = request.POST['legend_6']
          existing_Form.legend_7 = request.POST['legend_7']
          existing_Form.legend_8 = request.POST['legend_8']
          existing_Form.legend_9 = request.POST['legend_9']
          existing_Form.legend_10 = request.POST['legend_10']
          existing_Form.legend_11 = request.POST['legend_11']
          existing_Form.editNote = request.POST['editNote']
          existing_Form.customlegend = request.POST['customlegend']
          existing_Form.doc1 = request.POST['doc1']
          existing_Form.doc2 = request.POST['doc2']
          existing_Form.doc3 = request.POST['doc3']
          existing_Form.analyzedby = request.FILES['analyzedby']
          existing_Form.reviewedby = request.FILES['reviewedby']
          existing_Form.approvedby = request.FILES['approvedby']
          existing_Form.approvedby1 = request.FILES['approvedby1']


          existing_Form.id = None
          existing_Form.save()
          id = existing_Form.id
          if "submit_and_view" in request.POST:
              url = f"/wasteWater2-view/{str(id)}/"
              return redirect(to=url)
          
          if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
              return redirect(to='wasteWater2List')
          else:
              return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "WasteWaterForm2Clone.html")

def wasteWaterclone(request,pk):
     existing_form = WasteWaterSludge.objects.get(id=pk)
     context = {'data':existing_form}
     return render(request,"WasteWaterSludgeClone.html",context)

def wasteWatercloneSave(request,pk):
     try:
        # Fetch the existing form instance by ID
         existing_Form = WasteWaterSludge.objects.get(id=pk)
     except WasteWaterSludge.DoesNotExist:
         return HttpResponse("Form not found", status=404)
     if request.method == 'POST':
            existing_Form.location = request.POST['location']
            existing_Form.ww_lab_report_no = request.POST['ww_lab_report_no']
            existing_Form.ww_invoice_no = request.POST['ww_invoice_no']
            existing_Form.ww_report_date = request.POST['ww_report_date']
            existing_Form.ww_report_to = request.POST['ww_report_to']
            existing_Form.ww_address = request.POST['ww_address']
            existing_Form.ww_attention = request.POST['ww_attention']
            existing_Form.ww_email = request.POST['ww_email']
            existing_Form.ww_sampleid = request.POST['ww_sampleid']
            existing_Form.ww_sample_colec_Date = request.POST['ww_sample_colec_Date']
            existing_Form.ww_sample_desc = request.POST['ww_sample_desc']
            existing_Form.ww_sample_type = request.POST['ww_sample_type']
            existing_Form.ww_sample_colec_by = request.POST['ww_sample_colec_by']
            existing_Form.ww_date_of_analy = request.POST['ww_date_of_analy']
            existing_Form.ww_test_desc = request.POST['ww_test_desc']
            existing_Form.ww_sr1 = request.POST['ww_sr1']
            existing_Form.ww_sr2 = request.POST['ww_sr2']
            existing_Form.ww_sr3 = request.POST['ww_sr3']
            existing_Form.ww_sr4 = request.POST['ww_sr4']
            existing_Form.ww_sr5 = request.POST['ww_sr5']
            existing_Form.ww_sr6 = request.POST['ww_sr6']
            existing_Form.ww_sr7 = request.POST['ww_sr7']
            existing_Form.ww_sr8 = request.POST['ww_sr8']
            existing_Form.ww_sr9 = request.POST['ww_sr9']
            existing_Form.ww_sr10 = request.POST['ww_sr10']
            existing_Form.ww_sr11 = request.POST['ww_sr11']
            existing_Form.ww_sr12 = request.POST['ww_sr12']
            existing_Form.ww_sr13 = request.POST['ww_sr13']
            existing_Form.ww_legend_1 = request.POST['ww-legend-1']
            existing_Form.ww_legend_2 = request.POST['ww-legend-2']
            existing_Form.ww_legend_3 = request.POST['ww-legend-3']
            existing_Form.ww_legend_4 = request.POST['ww-legend-4']
            existing_Form.ww_legend_5 = request.POST['ww-legend-5']
            existing_Form.ww_legend_6 = request.POST['ww-legend-6']
            existing_Form.ww_legend_7 = request.POST['ww-legend-7']
            existing_Form.ww_legend_8 = request.POST['ww-legend-8']
            existing_Form.ww_legend_9 = request.POST['ww-legend-9']
            existing_Form.ww_legend_10 = request.POST['ww-legend-10']
            existing_Form.ww_legend_11 = request.POST['ww-legend-11']
            existing_Form.ww_editnote = request.POST['ww_editnote']
            existing_Form.ww_custom_legend = request.POST['ww_custom_legend']
            existing_Form.ww_doc_con_1 = request.POST['ww_doc1']
            existing_Form.ww_doc_con_2 = request.POST['ww_doc2']
            existing_Form.ww_doc_con_3 = request.POST['ww_doc3']
            existing_Form.ww_analyzed_by = request.FILES["ww_analyzedby" ]
            existing_Form.ww_reviewd_by = request.FILES["ww_reviewedby" ]
            existing_Form.ww_approved_by = request.FILES["ww_approvedby" ]
            existing_Form.ww_approved_by1 = request.FILES["ww_approvedby1" ]


            existing_Form.id = None
            existing_Form.save()
            id = existing_Form.id
            if "submit_and_view" in request.POST:
                url = f"/wasteWaterSludge-view/{str(id)}/"
                return redirect(to=url)
          
            if "submit_and_new" in request.POST:
               # context = {'list': new_dw}
                return redirect(to='wasteWaterSludgeList')
            else:
                return HttpResponse("Invalid request method", status=400)
     # context = {'list': existing_dw}
     return render(request, "WasteWaterSludgeClone.html")