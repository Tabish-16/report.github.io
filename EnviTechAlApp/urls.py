"""
URL configuration for EnviTechAlApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import include, path
from EnviTechAlApp import settings, views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('', views.home, name = "home"),
    path('drinkingWaterForm', views.drinkingWaterForm),
    path('gaseousEmission',views.gaseousEmission),
    path('ambientAir',views.ambientAirForm),
    path('wasteWaterSludge',views.wasteWaterSludge,name="wasteWaterSludge"),
    path('vehicularEmission',views.vehicularEmission,name="vahicularEmission"),
    path('luxAnalysis',views.luxAnalysis,name="luxAnalysis"),
    path('noiseAnalysis',views.noiseAnalysis,name="noiseAnalysis"),
    path('packingPolyBag',views.packingPoly,name="packingPolyBag"),
    path('machineOil',views.machineOil,name="machineOil"),
    path('microbialAnalysis',views.microbialAnalysis,name="microBialAnalysis"),
    path('viscousLiquid',views.viscousLiquid,name="viscousLiquid"),
    path('ambientAirQuality2',views.ambientAirQuality2,name="ambientAir2"),
    path('wasteWater2',views.wasteWater2,name="wasteWater2"),
    path('drinkingWaterList',views.drinkingWaterList,name="drinkWaterList"),
    path('delete-form/<str:pk>/',views.deleteDrinkingWaterList,name='DriningWaterform-delete'),
    path('edit-form/<str:pk>/',views.editDrinkingWaterList,name='DrinkingWaterform-edit'),
    path('updateRecord<str:pk>/',views.editDrinkingWaterListRecord,name='DrinkingWaterform-editRecord'),
    path('view-form/<str:pk>/',views.drinkWaterReport,name='DrinkingWaterform-view'),
    path('drinkingwaterReport-pdf/<int:pk>/',views.generatePDF,name="drinkingwaterReport-pdf"),
    path('DriningWaterform-clone/<str:pk>/',views.drinkingWaterClone,name="DriningWaterform-clone"),
    path('DriningWaterform-Save/<str:pk>/',views.drinkingWaterCloneSave,name="DriningWaterform-Save"),
    path('gaseousEmissionList',views.gaseousEmissionList,name="gaseousEmissionList"),
    path('GaseousForm-delete/<str:pk>/',views.deleteGaseousList,name='GaseousForm-delete'),
    path('GaseousForm-edit/<str:pk>/',views.editGaseousList,name='GaseousForm-edit'),
    path('GaseousForm-updateRecord<str:pk>/',views.updateGaseousRecord,name='GaseousForm-editRecord'),
    path('GaseousForm-view-form/<str:pk>/',views.gaseousEmissionReport,name='GaseousForm-view'),
    path('GaseousForm-clone/<str:pk>/',views.GaseousFormclone,name="GaseousForm-clone"),
    path('GaseousForm-Save/<str:pk>/',views.GaseousFormcloneSave,name="GaseousForm-Save"),
    path('gaseousEmissionReport-pdf/<int:pk>/',views.gaseousReportgeneratePDF,name="gaseousEmissionReport-pdf"),
    path('ambientAirList',views.ambientAirList,name="ambientAirList"),
    path('ambientAir-delete/<str:pk>/',views.ambientAirDelete,name="ambientAir-delete"),
    path('ambientAir-edit/<str:pk>/',views.ambientAirEdit,name="ambientAir-edit"),
    path('ambientAir-updateRecord/<str:pk>/',views.ambientAirUpdateRecord,name="ambientAir-editRecord"),
    path('ambientAir-view/<str:pk>/',views.ambientAirview,name="ambientAir-view"),
    path('ambientAir-clone/<str:pk>/',views.ambientAirClone,name="ambientAir-clone"),
    path('ambientAir-Save/<str:pk>/',views.ambientAircloneSave,name="ambientAir-Save"),
    path('ambientAirReport-pdf/<int:pk>/',views.ambientAirGeneratePDF,name="AmbientAirReport-pdf"),
    path('wasteWaterSludgeList/',views.wasteWaterSludgeList,name="wasteWaterSludgeList"),
    path('wasteWaterSludge-delete/<str:pk>/',views.wasteWaterSludgeDelete,name="wastewater-delete"),
    path('wasteWaterSludge-edit/<str:pk>/',views.wastewaterEdit,name="wastewater-edit"),
    path('wasteWaterSludge-update/<str:pk>/',views.wasteWaterUpdate,name="wastewater-update"),
    path('wasteWaterSludge-view/<str:pk>/',views.wasteWaterView,name="wastewater-view"),
    path('wastewater-clone/<str:pk>/',views.wasteWaterclone,name="wastewater-clone"),
    path('wasteWater-Save/<str:pk>/',views.wasteWatercloneSave,name="wasteWater-Save"),
    path('wasteWaterSludgeReport-pdf/<str:pk>/',views.wasteWaterPdf,name="wastewaterReport-pdf"),
    path('vehicularEmissionList/',views.vehicularEmissionList,name="vehicularEmissionList"),
    path('vehicularEmission-delete/<str:pk>/',views.vehicularEmissionDelete,name="vehicularEmission-delete"),
    path('vehicularEmission-edit/<str:pk>/',views.vehicularEmissionEdit,name="vehicularEmission-edit"),
    path('vehicularEmission-Update/<str:pk>/',views.vehicularEmissionUpdate,name="vehicularEmission-update"),
    path('vehicularEmission-view/<str:pk>/',views.vehicularEmissionView,name="vehicularEmission-view"),
    path('vehicularEmission-clone/<str:pk>/',views.vehicularEmissionclone,name="vehicularEmission-clone"),
    path('vehicularEmission-Save/<str:pk>/',views.vehicularEmissioncloneSave,name="vehicularEmission-Save"),
    path('vehicularEmissionReport-pdf/<str:pk>/',views.vehicularEmissionReport,name="vehicularEmissionReport-pdf"),
    path('luxAnalysisList/',views.luxAnalysisList,name="luxAnalysisList"),
    path('luxAnalysis-delete/<str:pk>/',views.luxAnalysisDelete,name="luxAnalysis-delete"),
    path('luxAnalysis-edit/<str:pk>/',views.luxAnalysisEdit,name="luxAnalysis-edit"),
    path('luxAnalysis-update/<str:pk>/',views.luxAnalysisUpdate,name="luxAnalysis-update"),
    path('luxAnalysisReport/<str:pk>/',views.luxAnalysisView,name="luxAnalysis-view"),
    path('luxAnalysis-clone/<str:pk>/',views.luxFormclone,name="luxAnalysis-clone"),
    path('luxForm-Save/<str:pk>/',views.luxFormcloneSave,name="luxForm-Save"),
    path('luxAnalysisReport-pdf/<str:pk>/',views.luxAnalysisReportPdf,name="luxAnalysisReport-pdf"),
    path('packingPolyBagList/',views.packingPolyBagList,name="packingPolyBagList"),
    path('packingpolybag-delete/<str:pk>/',views.packingPolyBagDelete,name="packingpolybag-delete"),
    path('packingpolybag-edit/<str:pk>/',views.packingPolyBagEdit,name="packingpolybag-edit"),
    path('packingpolybag-Update/<str:pk>/',views.packingPolyBagUpdate,name="packingpolybag-update"),
    path('packingpolybag-view/<str:pk>/',views.packingPolyBagView,name="packingpolybag-view"),
    path('packingpolybag-clone/<str:pk>/',views.packingPolyclone,name="packingpolybag-clone"),
    path('packingPoly-Save/<str:pk>/',views.packingPolycloneSave,name="packingPoly-Save"),
    path('packingpolybagReport-pdf/<str:pk>/',views.packingPolyBagReport,name="packingpolybagReport-pdf"),
    path('noiseAnalysisList/',views.noiseAnalysisList,name="noiseAnalysisList"),
    path('noiseAnalysis-delete<str:pk>/',views.noiseAnalysisDelete,name="noiseAnalysis-delete"),
    path('noiseAnalysis-edit<str:pk>/',views.noiseAnalysisEdit,name="noiseAnalysis-edit"),
    path('noiseAnalysis-update<str:pk>/',views.noiseAnalysisUpdate,name="noiseAnalysis-update"),
    path('noiseAnalysis-view/<str:pk>/',views.noiseAnalysisView,name="noiseAnalysis-view"),
    path('noiseAnalysis-clone/<str:pk>/',views.noiseAnalysisclone,name="noiseAnalysis-clone"),
    path('noiseAnalysis-Save/<str:pk>/',views.noiseAnalysiscloneSave,name="noiseAnalysis-Save"),
    path('noiseAnalysisReport-pdf/<str:pk>/',views.noiseAnalysisReport,name="noiseAnalysisReport-pdf"),
    path('machineOilList/',views.machineOilList,name="machineOilList"),
    path('machineOil-delete/<str:pk>/',views.machineOilDelete,name="machineOil-delete"),
    path('machineOil-edit/<str:pk>/',views.machineOilEdit,name="machineOil-edit"),
    path('machineOil-update/<str:pk>/',views.machineOilUpdate,name="machineOil-update"),
    path('machineOil-view/<str:pk>/',views.machineOilView,name="machineOil-view"),
    path('machineOil-clone/<str:pk>/',views.machineOilclone,name="machineOil-clone"),
    path('machineOil-Save/<str:pk>/',views.machineOilcloneSave,name="machineOil-Save"),
    path('machineOilReport-Pdf/<str:pk>/',views.machineOilReportPdf,name="machineOilReport-pdf"),
    path('microbialList/',views.microbialList,name="microbialList"),
    path('microbial-delete/<str:pk>/',views.microbialDelete,name="microbial-delete"),
    path('microbial-edit/<str:pk>/',views.microbialEdit,name="microbial-edit"),
    path('microbial-update/<str:pk>/',views.microbialUpdate,name="microbial-update"),
    path('microbial-view/<str:pk>/',views.microbialView,name="microbial-view"),
    path('microbial-clone/<str:pk>/',views.microbialclone,name="microbial-clone"),
    path('microbial-Save/<str:pk>/',views.microbialcloneSave,name="microbial-Save"),
    path('microbialAnalysisReport-pdf/<str:pk>/',views.microbialAnalysisPdf,name="microbialAnalysisReport-pdf"),
    path('viscousLiquidList/',views.viscousLiquidList,name="viscousLiquidList"),
    path('viscousLiquid-delete/<str:pk>/',views.viscousLiquidDelete,name="viscousLiquid-delete"),
    path('viscousLiquid-edit/<str:pk>/',views.viscousLiquidEdit,name="viscousLiquid-edit"),
    path('viscousLiquid-update/<str:pk>/',views.viscousLiquidUpdate,name="viscousLiquid-update"),
    path('viscousLiquid-view/<str:pk>/',views.viscousLiquidview,name="viscousLiquid-view"),
    path('viscousLiquid-clone/<str:pk>/',views.viscousLiquidclone,name="viscousLiquid-clone"),
    path('viscousLiquid-Save/<str:pk>/',views.viscousLiquidcloneSave,name="viscousLiquid-Save"),
    path('viscousLiquid-Pdf/<str:pk>/',views.viscousLiquidPdf,name="viscousLiquid-Pdf"),
    path('ambientAir2List/',views.ambientAir2List,name="ambientAir2List"),
    path('ambientAir2-delete/<str:pk>/',views.ambientAir2Delete,name="ambientAir2-delete"),
    path('ambientAir2-edit/<str:pk>/',views.ambientAir2Edit,name="ambientAir2-edit"),
    path('ambientAir2-update/<str:pk>/',views.ambientAir2Update,name="ambientAir2-update"),
    path('ambientAir2-view/<str:pk>/',views.ambientAir2View,name="ambientAir2-view"),
    path('ambientAir2-clone/<str:pk>/',views.ambientAir2Clone,name="ambientAir2-clone"),
    path('ambientAir2-Save/<str:pk>/',views.ambientAir2cloneSave,name="ambientAir2-Save"),
    path('ambientAir2Report-pdf/<str:pk>/',views.ambientAir2Pdf,name="ambientAir2Report-pdf"),
    path('wasteWater2List/',views.wasteWAter2List,name="wasteWater2List"),
    path('wasteWater2-delete/<str:pk>/',views.wasteWAter2Delete,name="wasteWater2-delete"),
    path('wasteWater2-edit/<str:pk>/',views.wasteWAter2Edit,name="wasteWater2-edit"),
    path('wasteWater2-Update/<str:pk>/',views.wasteWAter2Update,name="wasteWater2-Update"),
    path('wasteWater2-view/<str:pk>/',views.wasteWAter2View,name="wasteWater2-view"),
    path('wasteWater2-clone/<str:pk>/',views.wasteWater2clone,name="wasteWater2-clone"),
    path('wasteWater2-Save/<str:pk>/',views.wasteWater2cloneSave,name="wasteWater2-Save"),
    path('wasteWater2Report-pdf/<str:pk>/',views.wasteWater2Pdf,name="wasteWater2Report-pdf"),
    
   

    #path('', views.drinkWaterForm, name= ""),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
