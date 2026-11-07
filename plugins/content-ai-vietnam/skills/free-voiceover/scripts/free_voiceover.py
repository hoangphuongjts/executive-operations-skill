"""Local synthesis adapter; imports models only after explicit execution permission."""
import argparse, importlib.util, json, sys, wave, hashlib
from pathlib import Path

def validate(a):
    if a.doctor: return
    if not a.text or not a.output: raise ValueError('Cần --text và --output')
    if not Path(a.text).is_file(): raise ValueError('Không tìm thấy file kịch bản')
    if not Path(a.text).read_text(encoding='utf-8').strip(): raise ValueError('Kịch bản trống')
    if Path(a.output).exists() or Path(str(a.output)+'.json').exists(): raise ValueError('Không ghi đè đầu ra có sẵn')
    if Path(a.output).suffix.lower()!='.wav': raise ValueError('Đầu ra phải là .wav')
    if a.reference:
        if not a.consent: raise ValueError('Clone cần xác nhận quyền từ người nói: --consent')
        if not Path(a.reference).is_file(): raise ValueError('Không tìm thấy file giọng tham chiếu')
        if a.voice: raise ValueError('Chọn preset hoặc reference, không chọn cả hai')
    if not a.allow_model_download: raise ValueError('Chưa cho phép chạy engine/tải model: --allow-model-download')
    if a.engine=='voxcpm' and a.voice: raise ValueError('VoxCPM không dùng tên preset VieNeu')

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--engine',choices=['vieneu','voxcpm'],default='vieneu')
    p.add_argument('--text');p.add_argument('--output');p.add_argument('--voice');p.add_argument('--reference')
    p.add_argument('--consent',action='store_true');p.add_argument('--allow-model-download',action='store_true');p.add_argument('--doctor',action='store_true')
    a=p.parse_args(argv)
    try:
        validate(a)
        if a.doctor:
            print(json.dumps({n:bool(importlib.util.find_spec(n)) for n in ['vieneu','voxcpm','soundfile']},indent=2));return 0
        text=Path(a.text).read_text(encoding='utf-8');out=Path(a.output).resolve();out.parent.mkdir(parents=True,exist_ok=True)
        if a.engine=='vieneu':
            from vieneu import Vieneu
            model=Vieneu(mode='v3turbo',backend='onnx')
            kw={'ref_audio':str(Path(a.reference).resolve()),'denoise':True} if a.reference else ({'voice':a.voice} if a.voice else {})
            if a.voice:
                roster=model.list_preset_voices()
                if a.voice not in {x for pair in roster for x in pair}:raise ValueError('Preset không tồn tại ở phiên bản đã cài; xem list_preset_voices')
            audio=model.infer(text,**kw);model.save(audio,str(out))
        else:
            from voxcpm import VoxCPM
            import soundfile as sf
            model=VoxCPM.from_pretrained('openbmb/VoxCPM2',load_denoiser=False)
            kw={'reference_wav_path':str(Path(a.reference).resolve())} if a.reference else {}
            audio=model.generate(text=text,**kw);sf.write(str(out),audio,model.tts_model.sample_rate)
        import soundfile as sf
        info=sf.info(str(out))
        if info.frames<=0:raise ValueError('Engine tạo âm thanh rỗng')
        record={'engine':a.engine,'voice':a.voice,'reference_used':bool(a.reference),'speaker_permission_confirmed':bool(a.consent),'duration_seconds':info.duration,'sample_rate':info.samplerate,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'listening_review':'not_performed','caption_alignment':'required_after_synthesis','status':'synthesized_not_approved'}
        Path(str(out)+'.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(record,ensure_ascii=False));return 0
    except (ValueError,ImportError,OSError) as e:
        print(str(e),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
