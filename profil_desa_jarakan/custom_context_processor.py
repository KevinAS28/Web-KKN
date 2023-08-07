from django.conf import settings

import json, os



def custom_variables(request):
    desa_info = json.loads(open(os.path.join(settings.BASE_DIR, 'info_desa.json')).read())
    return {
        'nama_desa': desa_info['nama_desa'],
        'email_desa': desa_info['email_desa'],
        'telp_desa': desa_info['telp_desa']
        
    }
