from django.contrib import admin
from EnviTechAlApp.models import *


admin.site.register(DrinkingWaterForm)
admin.site.register(GaseousEmissionForm)
admin.site.register(AmbientAirForm)
admin.site.register(WasteWaterSludge)
admin.site.register(VehiculEmissionForm)
admin.site.register(LuxAnalysisForm)
admin.site.register(PackingPolyBagForm)
admin.site.register(MachineOilForm)
admin.site.register(MicrobialAnalysis)
admin.site.register(ViscousLiquid)
admin.site.register(AmbientAir2)
admin.site.register(WasteWaterForm2)
admin.site.register(NoiseAnalysis)


admin.site.site_header= 'Envi Tech AL'
admin.site.site_title= 'Envi Tech AL'
admin.site.index_title= 'Administration'




