# pddikti_web/app/routes.py
from flask import Blueprint, render_template, request, flash
from pddiktipy import api
from pddiktipy.exceptions import ValidationError, APIConnectionError

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/search_all', methods=['POST'])
def search_all():
    keyword = request.form.get('keyword')
    result = {}
    error = None
    try:
        with api() as client:
            result = client.search_all(keyword)
    except ValidationError as ve:
        error = f"Validasi error: {ve}"
    except APIConnectionError as ae:
        error = f"Koneksi error: {ae}"
    except Exception as e:
        error = f"Terjadi error: {str(e)}"

    return render_template('search_all.html', result=result, keyword=keyword, error=error)

@main.route('/search_mahasiswa', methods=['GET', 'POST'])
def search_mahasiswa():
    keyword = request.form.get('keyword') if request.method == 'POST' else request.args.get('keyword')
    result = {}
    error = None
    mahasiswa_list = []
    
    if keyword:
        try:
            with api() as client:
                result = client.search_mahasiswa(keyword)
                
                # Handle different response formats
                if isinstance(result, dict) and result.get('data'):
                    data = result['data']
                elif isinstance(result, list):
                    data = result
                else:
                    data = []
                
                # Process student data
                for mhs in data:
                    if isinstance(mhs, dict):
                        mahasiswa_info = {
                            'id': mhs.get('id', ''),
                            'nama': mhs.get('nama', ''),
                            'nim': mhs.get('nim', ''),
                            'nama_pt': mhs.get('nama_pt', ''),
                            'npsn': mhs.get('npsn', ''),  # ID universitas
                            'kode_prodi': mhs.get('kode_prodi', ''),  # ID prodi
                            'kode_pt': mhs.get('kode_pt', mhs.get('kode_pt_singkat', '')),
                            'kode_program_studi': mhs.get('kode_program_studi', '')
                        }
                        mahasiswa_list.append(mahasiswa_info)
                        
        except ValidationError as ve:
            error = f"Validasi error: {ve}"
        except APIConnectionError as ae:
            error = f"Koneksi error: {ae}"
        except Exception as e:
            error = f"Terjadi error: {str(e)}"

    return render_template('search_mahasiswa.html', 
                         result=result, 
                         mahasiswa_list=mahasiswa_list,
                         keyword=keyword, 
                         error=error)

@main.route('/detail_mahasiswa/<mahasiswa_id>')
def detail_mahasiswa(mahasiswa_id):
    detail = {}
    error = None
    
    try:
        with api() as client:
            detail = client.get_detail_mhs(mahasiswa_id)
    except ValidationError as ve:
        error = f"Validasi error: {ve}"
    except APIConnectionError as ae:
        error = f"Koneksi error: {ae}"
    except Exception as e:
        error = f"Terjadi error: {str(e)}"

    return render_template('detail_mahasiswa.html', detail=detail, error=error)

@main.route('/detail_mahasiswa_full/<mahasiswa_id>')
def detail_mahasiswa_full(mahasiswa_id):
    detail = {}
    error = None
    
    try:
        with api() as client:
            # First get the student search result to extract NIM and other details
            search_result = client.search_mahasiswa(mahasiswa_id)
            
            # Debug: Log the search result
            print(f"Search result for ID {mahasiswa_id}: {search_result}")
            
            if search_result is None:
                error = f"API search_mahasiswa returned None for ID: {mahasiswa_id}<br>Mungkin ID mahasiswa tidak valid atau format tidak sesuai."
            elif isinstance(search_result, dict) and search_result.get('data'):
                student_data = search_result['data'][0] if search_result['data'] else {}
                
                # Extract required parameters for the detail API
                nim = student_data.get('nim', '')
                # Use npsn for university ID
                npsn = student_data.get('npsn', '')
                # Use kode_prodi for study program ID
                kode_prodi = student_data.get('kode_prodi', '')
                
                print(f"Extracted data - NIM: {nim}, NPSN: {npsn}, Kode Prodi: {kode_prodi}")
                print(f"Available fields in student_data: {list(student_data.keys())}")
                
                if nim and npsn and kode_prodi:
                    # Use the new detail API endpoint with correct parameters
                    detail = client.get_detail_mhs(nim, npsn, kode_prodi)
                    print(f"Detail API result: {detail}")
                else:
                    error = f"Data mahasiswa tidak lengkap.<br>NIM: {nim}<br>NPSN: {npsn}<br>Kode Prodi: {kode_prodi}<br>Available fields: {list(student_data.keys())}"
            elif isinstance(search_result, list) and search_result:
                # Handle case where search_result is a list
                student_data = search_result[0] if search_result else {}
                nim = student_data.get('nim', '')
                npsn = student_data.get('npsn', '')
                kode_prodi = student_data.get('kode_prodi', '')
                
                if nim and npsn and kode_prodi:
                    detail = client.get_detail_mhs(nim, npsn, kode_prodi)
                else:
                    error = f"Data mahasiswa tidak lengkap dari list response.<br>NIM: {nim}<br>NPSN: {npsn}<br>Kode Prodi: {kode_prodi}<br>Available fields: {list(student_data.keys())}"
            else:
                error = f"Data mahasiswa tidak ditemukan.<br>Search result type: {type(search_result)}<br>Search result: {search_result}"
                
    except ValidationError as ve:
        error = f"Validasi error: {ve}"
    except APIConnectionError as ae:
        error = f"Koneksi error: {ae}"
    except Exception as e:
        error = f"Terjadi error: {str(e)}<br>Error type: {type(e)}"

    return render_template('detail_mahasiswa_full.html', detail=detail, error=error)

@main.route('/detail_mahasiswa_full_direct/<nim>/<npsn>/<kode_prodi>')
def detail_mahasiswa_full_direct(nim, npsn, kode_prodi):
    detail = {}
    error = None
    
    try:
        with api() as client:
            # Use the direct API call with the three required parameters
            detail = client.get_detail_mhs(nim, npsn, kode_prodi)
            print(f"Direct API call result: {detail}")
                
    except ValidationError as ve:
        error = f"Validasi error: {ve}"
    except APIConnectionError as ae:
        error = f"Koneksi error: {ae}"
    except Exception as e:
        error = f"Terjadi error: {str(e)}<br>Error type: {type(e)}"

    return render_template('detail_mahasiswa_full.html', detail=detail, error=error)

@main.route('/search_dosen', methods=['GET', 'POST'])
def search_dosen():
    keyword = request.form.get('keyword') if request.method == 'POST' else request.args.get('keyword')
    result = {}
    error = None
    dosen_list = []
    
    if keyword:
        try:
            with api() as client:
                result = client.search_dosen(keyword)
                
                # Handle different response formats
                if isinstance(result, dict) and result.get('data'):
                    data = result['data']
                elif isinstance(result, list):
                    data = result
                else:
                    data = []
                
                # Process lecturer data
                for dsn in data:
                    if isinstance(dsn, dict):
                        dosen_info = {
                            'id': dsn.get('id', ''),
                            'nama': dsn.get('nama', ''),
                            'nidn': dsn.get('nidn', ''),
                            'nama_pt': dsn.get('nama_pt', ''),
                            'singkatan_pt': dsn.get('singkatan_pt', ''),
                            'nama_prodi': dsn.get('nama_prodi', '')
                        }
                        dosen_list.append(dosen_info)
                        
        except ValidationError as ve:
            error = f"Validasi error: {ve}"
        except APIConnectionError as ae:
            error = f"Koneksi error: {ae}"
        except Exception as e:
            error = f"Terjadi error: {str(e)}"

    return render_template('search_dosen.html', 
                         result=result, 
                         dosen_list=dosen_list,
                         keyword=keyword, 
                         error=error)

@main.route('/detail_dosen/<dosen_id>')
def detail_dosen(dosen_id):
    profile = {}
    penelitian = {}
    pengabdian = {}
    karya = {}
    paten = {}
    study_history = {}
    teaching_history = {}
    error = None
    
    try:
        with api() as client:
            # Get lecturer profile
            profile = client.get_dosen_profile(dosen_id) or {}
            
            # Get lecturer research data
            penelitian = client.get_dosen_penelitian(dosen_id) or {}
            
            # Get lecturer community service data
            pengabdian = client.get_dosen_pengabdian(dosen_id) or {}
            
            # Get lecturer publications
            karya = client.get_dosen_karya(dosen_id) or {}
            
            # Get lecturer patents
            paten = client.get_dosen_paten(dosen_id) or {}
            
            # Get lecturer education history
            study_history = client.get_dosen_study_history(dosen_id) or {}
            
            # Get lecturer teaching history
            teaching_history = client.get_dosen_teaching_history(dosen_id) or {}
            
    except ValidationError as ve:
        error = f"Validasi error: {ve}"
    except APIConnectionError as ae:
        error = f"Koneksi error: {ae}"
    except Exception as e:
        error = f"Terjadi error: {str(e)}"

    return render_template('detail_dosen.html', 
                         profile=profile,
                         penelitian=penelitian,
                         pengabdian=pengabdian,
                         karya=karya,
                         paten=paten,
                         study_history=study_history,
                         teaching_history=teaching_history,
                         error=error)

@main.route('/search_pt', methods=['GET', 'POST'])
def search_pt():
    keyword = request.form.get('keyword') if request.method == 'POST' else request.args.get('keyword')
    result = {}
    error = None
    pt_list = []
    
    if keyword:
        try:
            with api() as client:
                result = client.search_pt(keyword)
                
                # Handle different response formats
                if isinstance(result, dict) and result.get('data'):
                    data = result['data']
                elif isinstance(result, list):
                    data = result
                else:
                    data = []
                
                # Process university data
                for universitas in data:
                    if isinstance(universitas, dict):
                        pt_info = {
                            'nama': universitas.get('nama', ''),
                            'kode': universitas.get('kode', ''),
                            'nama_singkat': universitas.get('nama_singkat', '')
                        }
                        pt_list.append(pt_info)
                        
        except ValidationError as ve:
            error = f"Validasi error: {ve}"
        except APIConnectionError as ae:
            error = f"Koneksi error: {ae}"
        except Exception as e:
            error = f"Terjadi error: {str(e)}"

    return render_template('search_pt.html', 
                         result=result, 
                         pt_list=pt_list,
                         keyword=keyword, 
                         error=error)

@main.route('/search_prodi', methods=['GET', 'POST'])
def search_prodi():
    keyword = request.form.get('keyword') if request.method == 'POST' else request.args.get('keyword')
    result = {}
    error = None
    prodi_list = []
    
    if keyword:
        try:
            with api() as client:
                result = client.search_prodi(keyword)
                
                # Handle different response formats
                if isinstance(result, dict) and result.get('data'):
                    data = result['data']
                elif isinstance(result, list):
                    data = result
                else:
                    data = []
                
                # Process study program data
                for program in data:
                    if isinstance(program, dict):
                        prodi_info = {
                            'nama': program.get('nama', ''),
                            'jenjang': program.get('jenjang', ''),
                            'pt': program.get('pt', ''),
                            'pt_singkat': program.get('pt_singkat', '')
                        }
                        prodi_list.append(prodi_info)
                        
        except ValidationError as ve:
            error = f"Validasi error: {ve}"
        except APIConnectionError as ae:
            error = f"Koneksi error: {ae}"
        except Exception as e:
            error = f"Terjadi error: {str(e)}"

    return render_template('search_prodi.html', 
                         result=result, 
                         prodi_list=prodi_list,
                         keyword=keyword, 
                         error=error)

@main.route('/debug_search/<keyword>')
def debug_search(keyword):
    result = {}
    error = None
    
    try:
        with api() as client:
            result = client.search_mahasiswa(keyword)
    except Exception as e:
        error = f"Error: {str(e)}"
    
    return render_template('debug.html', result=result, error=error, keyword=keyword)

@main.route('/debug_detail/<mahasiswa_id>')
def debug_detail(mahasiswa_id):
    search_result = {}
    detail_result = {}
    error = None
    
    try:
        with api() as client:
            # Test search_mahasiswa
            search_result = client.search_mahasiswa(mahasiswa_id)
            
            # If search works, try to get detail
            if search_result and isinstance(search_result, dict) and search_result.get('data'):
                student_data = search_result['data'][0] if search_result['data'] else {}
                nim = student_data.get('nim', '')
                kode_pt = student_data.get('kode_pt', '')
                kode_prodi = student_data.get('kode_prodi', '')
                
                if nim and kode_pt and kode_prodi:
                    detail_result = client.get_detail_mhs(nim, kode_pt, kode_prodi)
                else:
                    error = f"Missing required fields: NIM={nim}, Kode PT={kode_pt}, Kode Prodi={kode_prodi}"
            else:
                error = f"Search failed: {search_result}"
                
    except Exception as e:
        error = f"Error: {str(e)}"
    
    return render_template('debug_detail.html', 
                         search_result=search_result, 
                         detail_result=detail_result, 
                         error=error, 
                         mahasiswa_id=mahasiswa_id)

