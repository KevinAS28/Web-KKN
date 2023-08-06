from django.conf import settings

import json, os
desa_info = json.loads(open(os.path.join(settings.BASE_DIR, 'info_desa.json')).read())


def custom_variables(request):
    return {
        'nama_desa': desa_info['nama_desa'],
        'email_desa': desa_info['email_desa'],
        'telp_desa': desa_info['telp_desa']
        
    }
