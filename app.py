from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import shutil
import subprocess
import record
import run_file

app = FastAPI()

folder_path_rel = "uploads"
audio_save_folder = "sample_audio"



@app.post("/upload_preset/")
async def upload_preset(request: Request):
    # 업로드된 파일을 저장할 경로 설정
    if not os.path.exists(folder_path_rel):
        os.makedirs(folder_path_rel)

    # 파일 데이터를 수신
    file_bytes = await request.body()
    zip_file_path = os.path.join(folder_path_rel, "uploaded_file.zip")

    # 수신한 바이트 데이터를 ZIP 파일로 저장
    with open(zip_file_path, "wb") as file_object:
        file_object.write(file_bytes)

    # ZIP 파일 처리 로직
    subprocess.run(['unzip', '-j', file_location, '-d', folder_path_rel])
    os.remove(file_location)

    run_file.open_vital()
    run_file.preset_move(folder_path_rel)
'''
    run_file.open_preset_play(folder_path_rel)
    run_file.close_vital()

    # sample_audio ZIP 파일 생성
    shutil.make_archive("sample_audio", 'zip', audio_save_folder)

    # 생성된 ZIP 파일 응답으로 반환
    response = FileResponse("sample_audio.zip", media_type='application/zip', filename="sample_audio.zip")

    # 중간 생성된 파일들 삭제 (필요 시)
    shutil.rmtree(folder_path_rel)
    shutil.rmtree(audio_save_folder)

    return response
    
'''
