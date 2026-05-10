### $Id: admin.py,v 1.5 2017/12/18 09:12:51 muntaza Exp $

from django.contrib import admin
from umum.models import Provinsi, Kabupaten, LokasiBidang, SKPD, SUBSKPD, KodeBarang, HakTanah, SatuanBarang, KeadaanBarang, SKPenghapusan, MutasiBerkurang, JenisPemanfaatan, AsalUsul, Tahun, GolonganBarang, Tanah, KontrakTanah, PenghapusanTanah, TanahPenghapusan, PemanfaatanTanah, TanahPemanfaatan, HargaTanah, TahunBerkurangUsulHapusTanah, TanahUsulHapus

#### Tanah
from umum.models import TanahDPUPR, KontrakTanahDPUPR, HargaTanahDPUPR, TanahUsulHapusDPUPR, TahunBerkurangUsulHapusTanahDPUPR

from umum.models import TanahPenghapusanDPUPR, TahunBerkurangTanahDPUPR, PenghapusanTanahDPUPR

from umum.models import SKPDAsalTanahDPUPR, SKPDTujuanTanahDPUPR, FotoTanahDPUPR

from umum.admin import HargaTanahInline, TanahAdmin, KontrakTanahAdmin, HargaTanahAdmin, TahunBerkurangUsulHapusTanahInline, TanahUsulHapusAdmin

from umum.admin import TahunBerkurangTanahInline, PenghapusanTanahInline, TanahPenghapusanAdmin
from umum.admin import SKPDAsalTanahInline, SKPDTujuanTanahInline, FotoTanahInline

from umum.admin import GedungBangunanInline



#### Gedung Bangunan
from gedungbangunan.models import StatusTingkat, StatusBeton, KontrakGedungBangunan, HargaGedungBangunan, GedungBangunan, PenghapusanGedungBangunan, PemanfaatanGedungBangunan, TahunBerkurangGedungBangunan, Ruangan, TahunBerkurangUsulHapusGedung

from gedungbangunan.models import GedungBangunanPemanfaatan, GedungBangunanPenghapusan, GedungBangunanRuangan, GedungBangunanUsulHapus

from gedungbangunan.models import GedungBangunanDPUPR, KontrakGedungBangunanDPUPR, HargaGedungBangunanDPUPR, GedungBangunanRuanganDPUPR, GedungBangunanUsulHapusDPUPR, TahunBerkurangUsulHapusGedungDPUPR

from gedungbangunan.models import GedungBangunanPenghapusanDPUPR, TahunBerkurangGedungBangunanDPUPR, PenghapusanGedungBangunanDPUPR

from gedungbangunan.models import SKPDAsalGedungBangunanDPUPR, SKPDTujuanGedungBangunanDPUPR, FotoGedungBangunanDPUPR

from gedungbangunan.admin import HargaGedungBangunanInline, GedungBangunanAdmin, KontrakGedungBangunanAdmin, HargaGedungBangunanAdmin, RuanganInline, GedungBangunanRuanganAdmin, KDPGedungBangunanAdmin, TahunBerkurangUsulHapusGedungInline, GedungBangunanUsulHapusAdmin

from gedungbangunan.admin import TahunBerkurangGedungBangunanInline, PenghapusanGedungBangunanInline, GedungBangunanPenghapusanAdmin
from gedungbangunan.admin import SKPDAsalGedungBangunanInline, SKPDTujuanGedungBangunanInline, FotoGedungBangunanInline


#### Peralatan Mesin
from peralatanmesin.models import KontrakPeralatanMesin, HargaPeralatanMesin, PeralatanMesin, PenghapusanPeralatanMesin, PemanfaatanPeralatanMesin, TahunBerkurangPeralatanMesin, TahunBerkurangUsulHapusPeralatanMesin


#untuk menampung inline
from peralatanmesin.models import PeralatanMesinPemanfaatan, PeralatanMesinPenghapusan, PeralatanMesinUsulHapus

from peralatanmesin.models import PeralatanMesinDPUPR, KontrakPeralatanMesinDPUPR, HargaPeralatanMesinDPUPR, PeralatanMesinUsulHapusDPUPR, TahunBerkurangUsulHapusPeralatanMesinDPUPR

from peralatanmesin.models import PeralatanMesinPenghapusanDPUPR, TahunBerkurangPeralatanMesinDPUPR, PenghapusanPeralatanMesinDPUPR

from peralatanmesin.models import SKPDAsalPeralatanMesinDPUPR, SKPDTujuanPeralatanMesinDPUPR, FotoPeralatanMesinDPUPR

from peralatanmesin.admin import HargaPeralatanMesinInline, PeralatanMesinAdmin, KontrakPeralatanMesinAdmin, HargaPeralatanMesinAdmin, TahunBerkurangUsulHapusPeralatanMesinInline, PeralatanMesinUsulHapusAdmin

from peralatanmesin.admin import TahunBerkurangPeralatanMesinInline, PenghapusanPeralatanMesinInline, PeralatanMesinPenghapusanAdmin
from peralatanmesin.admin import SKPDAsalPeralatanMesinInline, SKPDTujuanPeralatanMesinInline, FotoPeralatanMesinInline



#### Class Tanah
class TahunBerkurangTanahDPUPRInline(TahunBerkurangTanahInline):
    model = TahunBerkurangTanahDPUPR



class PenghapusanTanahDPUPRInline(PenghapusanTanahInline):
    model = PenghapusanTanahDPUPR



class SKPDAsalTanahDPUPRInline(SKPDAsalTanahInline):
    model = SKPDAsalTanahDPUPR



class SKPDTujuanTanahDPUPRInline(SKPDTujuanTanahInline):
    model = SKPDTujuanTanahDPUPR



class FotoTanahDPUPRInline(FotoTanahInline):
    model = FotoTanahDPUPR



class GedungBangunanDPUPRInline(GedungBangunanInline):
    model = GedungBangunanDPUPR



class HargaTanahDPUPRInline(HargaTanahInline):
    model = HargaTanahDPUPR

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak":
            kwargs["queryset"] = KontrakTanah.objects.filter(id_skpd__exact=3)
        return super(HargaTanahDPUPRInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusTanahDPUPRInline(TahunBerkurangUsulHapusTanahInline):
    model = TahunBerkurangUsulHapusTanahDPUPR


class TanahDPUPRAdmin(TanahAdmin):
    inlines = [HargaTanahDPUPRInline,
                SKPDAsalTanahDPUPRInline,
                FotoTanahDPUPRInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=3)
        return super(TanahDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class TanahUsulHapusDPUPRAdmin(TanahUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusTanahDPUPRInline,
                SKPDAsalTanahDPUPRInline,
                FotoTanahDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakTanahDPUPRAdmin(KontrakTanahAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=3)
        return super(KontrakTanahDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=3)



class HargaTanahDPUPRAdmin(HargaTanahAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        tanah_qs = Tanah.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_tanah__in=tanah_qs)



class TanahPenghapusanDPUPRAdmin(TanahPenghapusanAdmin):
    inlines = [PenghapusanTanahDPUPRInline, TahunBerkurangTanahDPUPRInline,
                    SKPDAsalTanahDPUPRInline,
                    SKPDTujuanTanahDPUPRInline,
                    FotoTanahDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



### Register Tanah DPUPR
admin.site.register(TanahDPUPR, TanahDPUPRAdmin)
admin.site.register(TanahUsulHapusDPUPR, TanahUsulHapusDPUPRAdmin)
admin.site.register(KontrakTanahDPUPR, KontrakTanahDPUPRAdmin)
admin.site.register(HargaTanahDPUPR, HargaTanahDPUPRAdmin)
admin.site.register(TanahPenghapusanDPUPR, TanahPenghapusanDPUPRAdmin)



from gedungbangunan.models import KDPGedungBangunanDPUPR


#### Class Gedung dan Bangunan
class TahunBerkurangGedungBangunanDPUPRInline(TahunBerkurangGedungBangunanInline):
    model = TahunBerkurangGedungBangunanDPUPR



class PenghapusanGedungBangunanDPUPRInline(PenghapusanGedungBangunanInline):
    model = PenghapusanGedungBangunanDPUPR



class SKPDAsalGedungBangunanDPUPRInline(SKPDAsalGedungBangunanInline):
    model = SKPDAsalGedungBangunanDPUPR



class SKPDTujuanGedungBangunanDPUPRInline(SKPDTujuanGedungBangunanInline):
    model = SKPDTujuanGedungBangunanDPUPR



class FotoGedungBangunanDPUPRInline(FotoGedungBangunanInline):
    model = FotoGedungBangunanDPUPR



class HargaGedungBangunanDPUPRInline(HargaGedungBangunanInline):
    model = HargaGedungBangunanDPUPR

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_gedung_bangunan":
            kwargs["queryset"] = KontrakGedungBangunan.objects.filter(id_skpd__exact=3)
        return super(HargaGedungBangunanDPUPRInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusGedungDPUPRInline(TahunBerkurangUsulHapusGedungInline):
    model = TahunBerkurangUsulHapusGedungDPUPR


class GedungBangunanDPUPRAdmin(GedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPUPRInline,
                SKPDAsalGedungBangunanDPUPRInline,
                FotoGedungBangunanDPUPRInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=3)
        return super(GedungBangunanDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class KDPGedungBangunanDPUPRAdmin(KDPGedungBangunanAdmin):
    inlines = [HargaGedungBangunanDPUPRInline,
                SKPDAsalGedungBangunanDPUPRInline,
                FotoGedungBangunanDPUPRInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=3)
        return super(KDPGedungBangunanDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanRuanganDPUPRAdmin(GedungBangunanRuanganAdmin):

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=5)



class GedungBangunanUsulHapusDPUPRAdmin(GedungBangunanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusGedungDPUPRInline,
                    SKPDAsalGedungBangunanDPUPRInline,
                    FotoGedungBangunanDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=3).filter(id_mutasi_berkurang__exact=3)



class KontrakGedungBangunanDPUPRAdmin(KontrakGedungBangunanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=3)
        return super(KontrakGedungBangunanDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=3)



class HargaGedungBangunanDPUPRAdmin(HargaGedungBangunanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        gedung_bangunan_qs = GedungBangunan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_gedung_bangunan__in=gedung_bangunan_qs)



class GedungBangunanPenghapusanDPUPRAdmin(GedungBangunanPenghapusanAdmin):
    inlines = [PenghapusanGedungBangunanDPUPRInline, TahunBerkurangGedungBangunanDPUPRInline,
                    SKPDAsalGedungBangunanDPUPRInline,
                    SKPDTujuanGedungBangunanDPUPRInline,
                    FotoGedungBangunanDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register GedungBangunan DPUPR
admin.site.register(GedungBangunanDPUPR, GedungBangunanDPUPRAdmin)
admin.site.register(KDPGedungBangunanDPUPR, KDPGedungBangunanDPUPRAdmin)
admin.site.register(GedungBangunanRuanganDPUPR, GedungBangunanRuanganDPUPRAdmin)
admin.site.register(GedungBangunanUsulHapusDPUPR, GedungBangunanUsulHapusDPUPRAdmin)
admin.site.register(KontrakGedungBangunanDPUPR, KontrakGedungBangunanDPUPRAdmin)
admin.site.register(HargaGedungBangunanDPUPR, HargaGedungBangunanDPUPRAdmin)
admin.site.register(GedungBangunanPenghapusanDPUPR, GedungBangunanPenghapusanDPUPRAdmin)







#### Class Peralatan Mesin
class TahunBerkurangPeralatanMesinDPUPRInline(TahunBerkurangPeralatanMesinInline):
    model = TahunBerkurangPeralatanMesinDPUPR



class PenghapusanPeralatanMesinDPUPRInline(PenghapusanPeralatanMesinInline):
    model = PenghapusanPeralatanMesinDPUPR



class SKPDAsalPeralatanMesinDPUPRInline(SKPDAsalPeralatanMesinInline):
    model = SKPDAsalPeralatanMesinDPUPR



class SKPDTujuanPeralatanMesinDPUPRInline(SKPDTujuanPeralatanMesinInline):
    model = SKPDTujuanPeralatanMesinDPUPR



class FotoPeralatanMesinDPUPRInline(FotoPeralatanMesinInline):
    model = FotoPeralatanMesinDPUPR



class HargaPeralatanMesinDPUPRInline(HargaPeralatanMesinInline):
    model = HargaPeralatanMesinDPUPR

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_peralatan_mesin":
            kwargs["queryset"] = KontrakPeralatanMesin.objects.filter(id_skpd__exact=3)
        return super(HargaPeralatanMesinDPUPRInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusPeralatanMesinDPUPRInline(TahunBerkurangUsulHapusPeralatanMesinInline):
    model = TahunBerkurangUsulHapusPeralatanMesinDPUPR


class PeralatanMesinDPUPRAdmin(PeralatanMesinAdmin):
    inlines = [HargaPeralatanMesinDPUPRInline,
                    SKPDAsalPeralatanMesinDPUPRInline,
                    FotoPeralatanMesinDPUPRInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=3)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=3)
        return super(PeralatanMesinDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class PeralatanMesinUsulHapusDPUPRAdmin(PeralatanMesinUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusPeralatanMesinDPUPRInline,
                    SKPDAsalPeralatanMesinDPUPRInline,
                    FotoPeralatanMesinDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=3)



class KontrakPeralatanMesinDPUPRAdmin(KontrakPeralatanMesinAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=3)
        return super(KontrakPeralatanMesinDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=3)



class HargaPeralatanMesinDPUPRAdmin(HargaPeralatanMesinAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        peralatan_mesin_qs = PeralatanMesin.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_peralatan_mesin__in=peralatan_mesin_qs)



class PeralatanMesinPenghapusanDPUPRAdmin(PeralatanMesinPenghapusanAdmin):
    inlines = [PenghapusanPeralatanMesinDPUPRInline, TahunBerkurangPeralatanMesinDPUPRInline,
                    SKPDAsalPeralatanMesinDPUPRInline,
                    SKPDTujuanPeralatanMesinDPUPRInline,
                    FotoPeralatanMesinDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register PeralatanMesin DPUPR
admin.site.register(PeralatanMesinDPUPR, PeralatanMesinDPUPRAdmin)
admin.site.register(PeralatanMesinUsulHapusDPUPR, PeralatanMesinUsulHapusDPUPRAdmin)
admin.site.register(KontrakPeralatanMesinDPUPR, KontrakPeralatanMesinDPUPRAdmin)
admin.site.register(HargaPeralatanMesinDPUPR, HargaPeralatanMesinDPUPRAdmin)
admin.site.register(PeralatanMesinPenghapusanDPUPR, PeralatanMesinPenghapusanDPUPRAdmin)




#### Jalan, Irigasi, dan Jaringan
from jalanirigasijaringan.models import KontrakJalanIrigasiJaringan, HargaJalanIrigasiJaringan, JalanIrigasiJaringan, PenghapusanJalanIrigasiJaringan, PemanfaatanJalanIrigasiJaringan, TahunBerkurangJalanIrigasiJaringan, TahunBerkurangUsulHapusJalanIrigasiJaringan

from jalanirigasijaringan.models import JalanIrigasiJaringanPemanfaatan, JalanIrigasiJaringanPenghapusan, JalanIrigasiJaringanUsulHapus

from jalanirigasijaringan.models import JalanIrigasiJaringanDPUPR, KontrakJalanIrigasiJaringanDPUPR, HargaJalanIrigasiJaringanDPUPR, KDPJalanIrigasiJaringanDPUPR, JalanIrigasiJaringanUsulHapusDPUPR, TahunBerkurangUsulHapusJalanIrigasiJaringanDPUPR

from jalanirigasijaringan.models import JalanIrigasiJaringanPenghapusanDPUPR, TahunBerkurangJalanIrigasiJaringanDPUPR, PenghapusanJalanIrigasiJaringanDPUPR

from jalanirigasijaringan.models import SKPDAsalJalanIrigasiJaringanDPUPR, SKPDTujuanJalanIrigasiJaringanDPUPR, FotoJalanIrigasiJaringanDPUPR

from jalanirigasijaringan.admin import HargaJalanIrigasiJaringanInline, JalanIrigasiJaringanAdmin, KontrakJalanIrigasiJaringanAdmin, HargaJalanIrigasiJaringanAdmin, KDPJalanIrigasiJaringanAdmin, TahunBerkurangUsulHapusJalanIrigasiJaringanInline, JalanIrigasiJaringanUsulHapusAdmin

from jalanirigasijaringan.admin import TahunBerkurangJalanIrigasiJaringanInline, PenghapusanJalanIrigasiJaringanInline, JalanIrigasiJaringanPenghapusanAdmin
from jalanirigasijaringan.admin import SKPDAsalJalanIrigasiJaringanInline, SKPDTujuanJalanIrigasiJaringanInline, FotoJalanIrigasiJaringanInline



#### Class Jalan, Irigasi dan Jaringan
class TahunBerkurangJalanIrigasiJaringanDPUPRInline(TahunBerkurangJalanIrigasiJaringanInline):
    model = TahunBerkurangJalanIrigasiJaringanDPUPR



class PenghapusanJalanIrigasiJaringanDPUPRInline(PenghapusanJalanIrigasiJaringanInline):
    model = PenghapusanJalanIrigasiJaringanDPUPR



class SKPDAsalJalanIrigasiJaringanDPUPRInline(SKPDAsalJalanIrigasiJaringanInline):
    model = SKPDAsalJalanIrigasiJaringanDPUPR



class SKPDTujuanJalanIrigasiJaringanDPUPRInline(SKPDTujuanJalanIrigasiJaringanInline):
    model = SKPDTujuanJalanIrigasiJaringanDPUPR



class FotoJalanIrigasiJaringanDPUPRInline(FotoJalanIrigasiJaringanInline):
    model = FotoJalanIrigasiJaringanDPUPR





class HargaJalanIrigasiJaringanDPUPRInline(HargaJalanIrigasiJaringanInline):
    model = HargaJalanIrigasiJaringanDPUPR

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_jalan_irigasi_jaringan":
            kwargs["queryset"] = KontrakJalanIrigasiJaringan.objects.filter(id_skpd__exact=3)
        return super(HargaJalanIrigasiJaringanDPUPRInline, self).formfield_for_foreignkey(db_field, request, **kwargs)



class TahunBerkurangUsulHapusJalanIrigasiJaringanDPUPRInline(TahunBerkurangUsulHapusJalanIrigasiJaringanInline):
    model = TahunBerkurangUsulHapusJalanIrigasiJaringanDPUPR


class JalanIrigasiJaringanDPUPRAdmin(JalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPUPRInline,
                    SKPDAsalJalanIrigasiJaringanDPUPRInline,
                    FotoJalanIrigasiJaringanDPUPRInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=3)
        return super(JalanIrigasiJaringanDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=5)



class JalanIrigasiJaringanUsulHapusDPUPRAdmin(JalanIrigasiJaringanUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusJalanIrigasiJaringanDPUPRInline,
                    SKPDAsalJalanIrigasiJaringanDPUPRInline,
                    FotoJalanIrigasiJaringanDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=4).filter(id_mutasi_berkurang__exact=3)



class KDPJalanIrigasiJaringanDPUPRAdmin(KDPJalanIrigasiJaringanAdmin):
    inlines = [HargaJalanIrigasiJaringanDPUPRInline,
                    SKPDAsalJalanIrigasiJaringanDPUPRInline,
                    FotoJalanIrigasiJaringanDPUPRInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=3)
        return super(KDPJalanIrigasiJaringanDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=6).filter(id_mutasi_berkurang__exact=5)



class KontrakJalanIrigasiJaringanDPUPRAdmin(KontrakJalanIrigasiJaringanAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=3)
        return super(KontrakJalanIrigasiJaringanDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=3)



class HargaJalanIrigasiJaringanDPUPRAdmin(HargaJalanIrigasiJaringanAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        jalan_irigasi_jaringan_qs = JalanIrigasiJaringan.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_jalan_irigasi_jaringan__in=jalan_irigasi_jaringan_qs)



class JalanIrigasiJaringanPenghapusanDPUPRAdmin(JalanIrigasiJaringanPenghapusanAdmin):
    inlines = [PenghapusanJalanIrigasiJaringanDPUPRInline, TahunBerkurangJalanIrigasiJaringanDPUPRInline,
                    SKPDAsalJalanIrigasiJaringanDPUPRInline,
                    SKPDTujuanJalanIrigasiJaringanDPUPRInline,
                    FotoJalanIrigasiJaringanDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register JalanIrigasiJaringan DPUPR
admin.site.register(JalanIrigasiJaringanDPUPR, JalanIrigasiJaringanDPUPRAdmin)
admin.site.register(JalanIrigasiJaringanUsulHapusDPUPR, JalanIrigasiJaringanUsulHapusDPUPRAdmin)
admin.site.register(KDPJalanIrigasiJaringanDPUPR, KDPJalanIrigasiJaringanDPUPRAdmin)
admin.site.register(KontrakJalanIrigasiJaringanDPUPR, KontrakJalanIrigasiJaringanDPUPRAdmin)
admin.site.register(HargaJalanIrigasiJaringanDPUPR, HargaJalanIrigasiJaringanDPUPRAdmin)
admin.site.register(JalanIrigasiJaringanPenghapusanDPUPR, JalanIrigasiJaringanPenghapusanDPUPRAdmin)





#### Aset Tetap Lainnya
from atl.models import KontrakATL, HargaATL, ATL, PenghapusanATL, PemanfaatanATL, TahunBerkurangATL, TahunBerkurangUsulHapusATL

from atl.models import ATLPemanfaatan, ATLPenghapusan, ATLUsulHapus

from atl.models import ATLDPUPR, KontrakATLDPUPR, HargaATLDPUPR, ATLUsulHapusDPUPR, TahunBerkurangUsulHapusATLDPUPR

from atl.models import ATLPenghapusanDPUPR, TahunBerkurangATLDPUPR, PenghapusanATLDPUPR

from atl.models import SKPDAsalATLDPUPR, SKPDTujuanATLDPUPR, FotoATLDPUPR

from atl.admin import HargaATLInline, ATLAdmin, KontrakATLAdmin, HargaATLAdmin, TahunBerkurangUsulHapusATLInline, ATLUsulHapusAdmin

from atl.admin import TahunBerkurangATLInline, PenghapusanATLInline, ATLPenghapusanAdmin
from atl.admin import SKPDAsalATLInline, SKPDTujuanATLInline, FotoATLInline




#### Class Aset Tetap Lainnya
class TahunBerkurangATLDPUPRInline(TahunBerkurangATLInline):
    model = TahunBerkurangATLDPUPR



class PenghapusanATLDPUPRInline(PenghapusanATLInline):
    model = PenghapusanATLDPUPR



class SKPDAsalATLDPUPRInline(SKPDAsalATLInline):
    model = SKPDAsalATLDPUPR



class SKPDTujuanATLDPUPRInline(SKPDTujuanATLInline):
    model = SKPDTujuanATLDPUPR



class FotoATLDPUPRInline(FotoATLInline):
    model = FotoATLDPUPR



class HargaATLDPUPRInline(HargaATLInline):
    model = HargaATLDPUPR

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_kontrak_atl":
            kwargs["queryset"] = KontrakATL.objects.filter(id_skpd__exact=3)
        return super(HargaATLDPUPRInline, self).formfield_for_foreignkey(db_field, request, **kwargs)




class TahunBerkurangUsulHapusATLDPUPRInline(TahunBerkurangUsulHapusATLInline):
    model = TahunBerkurangUsulHapusATLDPUPR


class ATLDPUPRAdmin(ATLAdmin):
    inlines = [HargaATLDPUPRInline,
                    SKPDAsalATLDPUPRInline,
                    FotoATLDPUPRInline, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_sub_skpd":
            kwargs["queryset"] = SUBSKPD.objects.filter(id_skpd__exact=3)
        if db_field.name == "id_ruangan":
            kwargs["queryset"] = Ruangan.objects.filter(id_gedung_bangunan__id_sub_skpd__id_skpd__exact=3)
        return super(ATLDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__exact=5)



class ATLUsulHapusDPUPRAdmin(ATLUsulHapusAdmin):
    inlines = [TahunBerkurangUsulHapusATLDPUPRInline,
                    SKPDAsalATLDPUPRInline,
                    FotoATLDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_golongan_barang__exact=5).filter(id_mutasi_berkurang__exact=3)



class KontrakATLDPUPRAdmin(KontrakATLAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_skpd":
            kwargs["queryset"] = SKPD.objects.filter(id__exact=3)
        return super(KontrakATLDPUPRAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        return self.model.objects.filter(id_skpd__exact=3)



class HargaATLDPUPRAdmin(HargaATLAdmin):

    def get_queryset(self, request):
        sub_skpd_qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        atl_qs = ATL.objects.filter(id_sub_skpd__in=sub_skpd_qs)
        return self.model.objects.filter(id_atl__in=atl_qs)



class ATLPenghapusanDPUPRAdmin(ATLPenghapusanAdmin):
    inlines = [PenghapusanATLDPUPRInline, TahunBerkurangATLDPUPRInline,
                    SKPDAsalATLDPUPRInline,
                    SKPDTujuanATLDPUPRInline,
                    FotoATLDPUPRInline, ]

    def get_queryset(self, request):
        qs = SUBSKPD.objects.filter(id_skpd__exact=3)
        return self.model.objects.filter(id_sub_skpd__in=qs).filter(id_mutasi_berkurang__in=[2,4,6,7,10,])



###Register ATL DPUPR
admin.site.register(ATLDPUPR, ATLDPUPRAdmin)
admin.site.register(ATLUsulHapusDPUPR, ATLUsulHapusDPUPRAdmin)
admin.site.register(KontrakATLDPUPR, KontrakATLDPUPRAdmin)
admin.site.register(HargaATLDPUPR, HargaATLDPUPRAdmin)
admin.site.register(ATLPenghapusanDPUPR, ATLPenghapusanDPUPRAdmin)
